# contentctl-analysis

این مخزن شامل خروجی‌های تحلیلی از بررسی کدها و ساختار build ابزار `contentctl` است. هدف فراهم‌کردن مجموعه‌ای ساختار‌یافته از متادیتا، نگاشت‌های ارث‌بری و فایل‌های مرجع است تا برای بررسی‌های انسانی و پردازش‌های خودکار قابل استفاده باشد.

ساختار پیشنهادی:
- analysis/
  - inheritance_mapping.csv       — نگاشت پدر/فرزند برای کلاس‌ها (شامل مسیر فایل‌ها و بازهٔ خطوط)
  - abstract_models_fields.csv    — فیلدها، ولیدیتورها و پیام‌های خطا در مدل‌های abstract
  - build_components.csv          — گام‌ها و فایل‌های کلیدی در جریان build
  - contentctl_conversation_knowledge.json — خلاصهٔ دانش جلسه و منابع
  - inheritance_tree.dot          — Graphviz DOT برای نمایش درخت ارث‌بری
  - metadata.yml                  — توضیحات و متادیتای فایل‌ها (منبع، بازهٔ خطوط، نقش)
- originals/  — کپی کاملِ فایل‌های منبعِ خوانده‌شده برای مرجع و reproducibility

روش استفاده:
1. مخزن را clone کنید: git clone https://github.com/yaghuti/contentctl-analysis.git
2. فایل‌های داخل analysis/ آمادهٔ بررسی یا وارد کردن در پایپ‌لاین‌های داده هستند.
3. برای تولید تصویر از درخت ارث‌بری:
   dot -Tpng analysis/inheritance_tree.dot -o inheritance_tree.png

Snapshot تولید: 2025-10-04T20:05:40Z
License: در صورت تأیید شما، فایل LICENSE (پیشنهاد: MIT) اضافه خواهد شد.