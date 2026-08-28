---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/document-content-schema.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# GetDocumentContent Output Schema
<a name="document-content-schema"></a>

When you use the [GetDocumentContent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetDocumentContent.html) API with `outputFormat` set to `EXTRACTED`, the response returns extracted text content in JSON format. The output schema is presented in JSON format:

```
{
   // always V1 for now
   schemaVersionId: string;

   // always JSON for now
   outputFormat: string;

   // content for plain-text documents
   plainTextDocumentContent: string;

   // content for non-plaintext documents such as PDF, DOCX, PPTX, Audio, Video
   nonPlainTextDocumentContent: List<ExtractedDocumentBodyElement>;
}
```

The schema for non-plaintext documents includes the `ExtractedDocumentBodyElement` which includes:

```
{
   text: string;

  // Allowed values: TEXT, ARTICLE, SECTION, DIV, IMAGE_DESCRIPTION, CODE,
  // TABLE, LIST, URL, HEADER, FOOTER, FORM, MENU, AUDIO, VIDEO
   elementType: string;

   horizontalHeaderIndex: integer;
   verticalHeaderIndex: integer;
   htmlDocumentTitle: string;
   sectionTitle: string;
   sectionBody: string;
   tableCaption: string;
   tableFooter: string;
   tableRowHeaders: List<List<string>>;
   tableColumnHeaders: List<List<string>>;
   tableRows: List<List<string>>;
   tableRowsCount: integer;
   tableColumnsCount: integer;
   tableId: string;

   tokens: List<struct>;
   {
        value: string;
        startOffsets: integer;
        endOffsets: integer;
   }

   tableType: string;
   tableSummary: string;

   columnInfoList: List<struct>;
   {
        columnName: string;
        columnSummary: string;
        columnType: string;
        columnRepresentativeValues: List<string>
   }

   // Audio/Video specific fields below
   overallSummary: string;

   audioSummaryList: List<struct>;
   {
        summaryText: string;
        startTimeMilliseconds: string;
        endTimeMilliseconds: string;
   }

   videoSummaryList: List<struct>;
   {
        summaryText: string;
        startTimeMilliseconds: string;
        endTimeMilliseconds: string;
   }

   audioTranscriptList: List<struct>;
   {
        transcriptText: string;
        startTimeMilliseconds: string;
        endTimeMilliseconds: string;
   }

   videoTranscriptList: List<struct>;
   {
        transcriptText: string;
        startTimeMilliseconds: string;
        endTimeMilliseconds: string;
   }
}
```

## Example Output
<a name="document-content-examples"></a>

### Plaintext Document Example
<a name="plaintext-example"></a>

For plaintext documents, the extracted content is returned in the `plainTextDocumentContent` field:

```
{
  "schemaVersionId": "V1",
  "outputFormat": "JSON",
  "plainTextDocumentContent": "This is the extracted text content from a plain text document."
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
