---
source_url: https://docs.aws.amazon.com/nova/latest/userguide/modalities-document.html
---

# Document understanding
<a name="modalities-document"></a>

**Note**
This documentation is for Amazon Nova Version 1. For the Amazon Nova 2 document understanding guide, visit [Document understanding](https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-multimodal-models.html#document-understanding).

Amazon Nova’s document understanding capability allows you to include entire documents (PDFs, Word files, spreadsheets, etc.) in your prompt and ask questions or requests about their content. Nova’s multimodal understanding models (Lite, Pro, Premier) can interpret both the text and visual elements (like charts or tables) within these documents. This enables use cases such as question-answering, summarization, and analysis of lengthy reports or scanned documents. Key features include a very large context window (1-2M tokens) for long documents and the ability to handle multiple documents in one query.

Amazon Nova distinguishes between two types of document inputs:
+ **Text-based document types** (e.g. TXT, CSV, Markdown, HTML, DOC): These are processed primarily for their textual content. Nova will focus on understanding and extracting information from the text in these documents.
+ **Media based document types** (e.g. PDF, DOCX): These files may contain complex layouts, images, charts, or embedded graphics. For media-based documents, Nova processes both the visual and textual elements. Nova employs vision-based understanding to interpret visual content—such as charts, tables, diagrams, or screenshots—alongside the document's text.

  JPEG2000 and JBIG2 aren't supported in PDF files in Amazon Nova.

Supported file formats include common document types: plain text and structured text files (CSV, TXT), spreadsheets (XLS/XLSX), HTML/Markdown, Word documents (DOC/DOCX), and PDF files. For images within documents, standard image formats (PNG, JPG, GIF, WebP) are handled, though PDFs containing certain image encodings (CYMK, SVG) are not supported.

**Document Size Limits and Usage Guidelines**

| Constraint | Limit |
| --- | --- |
| Maximum number of documents | Up to 5 documents per request (applies to both direct upload and Amazon S3) |
| Text-based document size | Each text document (e.g., .txt, .csv, .md, .html, .doc) must be ≤ 4.5 MB |
| Media-based document size | For .pdf and .docx files, there is no individual file size limit, but:+  When using direct upload, the combined size of all media documents must be ≤ 25 MB <br />+  When using Amazon S3, the combined size of all media documents must be ≤ 2 GB  |
| Unsupported PDF content | PDFs containing CMYK color profiles or SVG images are not supported |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
