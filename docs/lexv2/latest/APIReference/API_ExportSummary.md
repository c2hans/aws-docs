---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ExportSummary.html
---

# ExportSummary
<a name="API_ExportSummary"></a>

Provides summary information about an export in an export list.

## Contents
<a name="API_ExportSummary_Contents"></a>

 ** creationDateTime **   <a name="lexv2-Type-ExportSummary-creationDateTime"></a>
The date and time that the export was created.
Type: Timestamp
Required: No

 ** exportId **   <a name="lexv2-Type-ExportSummary-exportId"></a>
The unique identifier that Amazon Lex assigned to the export.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: No

 ** exportStatus **   <a name="lexv2-Type-ExportSummary-exportStatus"></a>
The status of the export. When the status is `Completed` the export is ready to download.
Type: String
Valid Values: `InProgress | Completed | Failed | Deleting`
Required: No

 ** fileFormat **   <a name="lexv2-Type-ExportSummary-fileFormat"></a>
The file format used in the export files.
Type: String
Valid Values: `LexJson | TSV | CSV`
Required: No

 ** lastUpdatedDateTime **   <a name="lexv2-Type-ExportSummary-lastUpdatedDateTime"></a>
The date and time that the export was last updated.
Type: Timestamp
Required: No

 ** resourceSpecification **   <a name="lexv2-Type-ExportSummary-resourceSpecification"></a>
Information about the bot or bot locale that was exported.
Type: [ExportResourceSpecification](API_ExportResourceSpecification.md) object
Required: No

## See Also
<a name="API_ExportSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ExportSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ExportSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ExportSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
