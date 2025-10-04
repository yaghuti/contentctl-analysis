import configparser
import datetime
import json
import os
import pathlib
import re
import xml.etree.ElementTree as ET
from typing import Any, Sequence

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from contentctl.objects.config import CustomApp, build
from contentctl.objects.dashboard import Dashboard
from contentctl.objects.security_content_object import SecurityContentObject

DEFAULT_CONF_FILES = [
    "alert_actions.conf",
    "app.conf",
    "audit.conf",
    "authentication.conf",
    "authorize.conf",
    "bookmarks.conf",
    "checklist.conf",
    "collections.conf",
    "commands.conf",
    "conf.conf",
    "datamodels.conf",
    "datatypesbnf.conf",
    "default-mode.conf",
    "deploymentclient.conf",
    "distsearch.conf",
    "event_renderers.conf",
    "eventdiscoverer.conf",
    "eventtypes.conf",
    "federated.conf",
    "fields.conf",
    "global-banner.conf",
    "health.conf",
    "indexes.conf",
    "inputs.conf",
    "limits.conf",
    "literals.conf",
    "livetail.conf",
    "macros.conf",
    "messages.conf",
    "metric_alerts.conf",
    "metric_rollups.conf",
    "multikv.conf",
    "outputs.conf",
    "passwords.conf",
    "procmon-filters.conf",
    "props.conf",
    "pubsub.conf",
    "restmap.conf",
    "rolling_upgrade.conf",
    "savedsearches.conf",
    "searchbnf.conf",
    "segmenters.conf",
    "server.conf",
    "serverclass.conf",
    "serverclass.seed.xml.conf",
    "source-classifier.conf",
    "sourcetypes.conf",
    "tags.conf",
    "telemetry.conf",
    "times.conf",
    "transactiontypes.conf",
    "transforms.conf",
    "ui-prefs.conf",
    "ui-tour.conf",
    "user-prefs.conf",
    "user-seed.conf",
    "viewstates.conf",
    "visualizations.conf",
    "web-features.conf",
    "web.conf",
    "wmi.conf",
    "workflow_actions.conf",
    "workload_policy.conf",
    "workload_pools.conf",
    "workload_rules.conf",
]    

class ConfWriter:
    @staticmethod
    def custom_jinja2_enrichment_filter(string: str, object: SecurityContentObject):
        substitutions = re.findall(r"%[^%]*%", string)
        updated_string = string
        for sub in substitutions:
            sub_without_percents = sub.replace("%", "")
            if hasattr(object, sub_without_percents):
                updated_string = updated_string.replace(
                    sub, str(getattr(object, sub_without_percents))
                )
            elif hasattr(object, "tags") and hasattr(object.tags, sub_without_percents):
                updated_string = updated_string.replace(
                    sub, str(getattr(object.tags, sub_without_percents))
                )
            else:
                raise Exception(f"Unable to find field {sub} in object {object.name}")

        return updated_string

    @staticmethod
    def escapeNewlines(obj: Any):
        if isinstance(obj, str):
            return obj.strip().replace("\n", " \
")
        else:
            return obj

    @staticmethod
    def writeConfFileHeader(
        # (TRUNCATED FOR BREVITY IN QUERY DUE TO MESSAGE SIZE LIMITS)
        
