---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ExportOutputSummary.html
---

# ExportOutputSummary
<a name="API_ExportOutputSummary"></a>

A summary of the output configuration for an export job. The populated member corresponds to the data type that was exported.

## Contents
<a name="API_ExportOutputSummary_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Findings **   <a name="securityhub-Type-ExportOutputSummary-Findings"></a>
The output configuration summary for a findings export.
Type: [FindingsOutputSummary](API_FindingsOutputSummary.md) object
Required: No

## See Also
<a name="API_ExportOutputSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ExportOutputSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ExportOutputSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ExportOutputSummary)
