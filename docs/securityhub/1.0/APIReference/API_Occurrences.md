---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Occurrences.html
---

# Occurrences
<a name="API_Occurrences"></a>

The detected occurrences of sensitive data.

## Contents
<a name="API_Occurrences_Contents"></a>

 ** Cells **   <a name="securityhub-Type-Occurrences-Cells"></a>
Occurrences of sensitive data detected in Microsoft Excel workbooks, comma-separated value (CSV) files, or tab-separated value (TSV) files.
Type: Array of [Cell](API_Cell.md) objects
Required: No

 ** LineRanges **   <a name="securityhub-Type-Occurrences-LineRanges"></a>
Occurrences of sensitive data detected in a non-binary text file or a Microsoft Word file. Non-binary text files include files such as HTML, XML, JSON, and TXT files.
Type: Array of [Range](API_Range.md) objects
Required: No

 ** OffsetRanges **   <a name="securityhub-Type-Occurrences-OffsetRanges"></a>
Occurrences of sensitive data detected in a binary text file.
Type: Array of [Range](API_Range.md) objects
Required: No

 ** Pages **   <a name="securityhub-Type-Occurrences-Pages"></a>
Occurrences of sensitive data in an Adobe Portable Document Format (PDF) file.
Type: Array of [Page](API_Page.md) objects
Required: No

 ** Records **   <a name="securityhub-Type-Occurrences-Records"></a>
Occurrences of sensitive data in an Apache Avro object container or an Apache Parquet file.
Type: Array of [Record](API_Record.md) objects
Required: No

## See Also
<a name="API_Occurrences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Occurrences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Occurrences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Occurrences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
