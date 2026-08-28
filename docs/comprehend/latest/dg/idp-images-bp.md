---
source_url: https://docs.aws.amazon.com/comprehend/latest/dg/idp-images-bp.html
---

# Best practices for images
<a name="idp-images-bp"></a>

When you use image files for custom classification or custom entity recognition, use the following guidelines to achieve the best results:
+ Provide a high quality image, ideally at least 150 DPI.
+ If the image file uses one of the supported formats (TIFF, JPEG, or PNG), don't convert or downsample the file before uploading it to Amazon S3.

For the best results when extracting text from tables in documents, follow these practices:
+ Tables in your document are visually separated from surrounding elements on the page. For example, the table isn't overlaid onto an image or complex pattern.
+ Text within the table is upright. For example, the text isn't rotated relative to other text on the page.

When extracting text from tables, you might see inconsistent results for the following cases:
+ Merged table cells span multiple columns.
+ Tables have cells, rows, or columns that are different than other parts of the same table.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
