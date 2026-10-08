---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ExportOutput.html
---

# ExportOutput
<a name="API_ExportOutput"></a>

Specifies what data to export and how to format it. This is a union: you must specify exactly one member. Currently, the only supported member is `Findings`.

## Contents
<a name="API_ExportOutput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Findings **   <a name="securityhub-Type-ExportOutput-Findings"></a>
Configures an export of Security Hub findings, including the output format and any filters or selected fields.
Type: [FindingsOutput](API_FindingsOutput.md) object
Required: No

## See Also
<a name="API_ExportOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ExportOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ExportOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ExportOutput)
