---
source_url: https://docs.aws.amazon.com/comprehend/latest/dg/idp-set-textract-options.html
---

# Setting text extraction options
<a name="idp-set-textract-options"></a>

 By default, Amazon Comprehend performs the following actions to extract text from a file, based on the input file type:
+ **Word files** – Amazon Comprehend parser extracts the text.
+ **Digital PDF files** – Amazon Comprehend parser extracts the text.
+ **Image files and scanned PDF files** – Amazon Comprehend uses the Amazon Textract `DetectDocumentText` API to extract the text.

For image files and PDF files, you can use the `DocumentReaderConfig` parameter to override these default extraction actions. This parameter is available when you use the Amazon Comprehend console or API for real-time or asynchronous custom analysis.

The `DocumentReaderConfig` parameter contains three fields:
+ **DocumentReadMode** – Set to `SERVICE_DEFAULT` for Amazon Comprehend to perform the default actions.

  Set to `FORCE_DOCUMENT_READ_ACTION` to use Amazon Textract to parse digital PDF files.
+ **DocumentReadAction** – Sets the Amazon Textract API (DetectDocumentText or AnalyzeDocument) to use when Amazon Comprehend uses Amazon Textract for text extraction.
+ **FeatureTypes** – If you set **DocumentReadAction** to use the AnalyzeDocument API operation, you can add one or both of the `FeatureTypes` (TABLES, FORMS). These features provide additional information about the tables and forms in the document. For more information about these features, see [Amazon Textract Document Analysis Response Objects](https://docs.aws.amazon.com/textract/latest/dg/how-it-works-document-layout.html).

The following examples show how to configure `DocumentReaderConfig` for specific use cases:

1. Use Amazon Textract for all PDF files.

   1. **DocumentReadMode** – Set to `FORCE_DOCUMENT_READ_ACTION`.

   1. **DocumentReadAction** – Set to `TEXTRACT_DETECT_DOCUMENT_TEXT`.

   1. **FeatureTypes** – Not required.

1. Use Amazon Textract `AnalyzeDocument` API for all PDF and image files.

   1. **DocumentReadMode** – Set to `FORCE_DOCUMENT_READ_ACTION`.

   1. **DocumentReadAction** – Set to `TEXTRACT_ANALYZE_DOCUMENT`.

   1. **FeatureTypes** – Set to `TABLES`, `FORMS` or both features.

1. Use Amazon Textract `AnalyzeDocument` API for scanned PDF files and all image files.

   1. **DocumentReadMode** – Set to `SERVICE_DEFAULT`.

   1. **DocumentReadAction** – Set to `TEXTRACT_ANALYZE_DOCUMENT`.

   1. **FeatureTypes** – Set to `TABLES`, `FORMS` or both features.

For more information about the Amazon Textract options, see [DocumentReaderConfig](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DocumentReaderConfig.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
