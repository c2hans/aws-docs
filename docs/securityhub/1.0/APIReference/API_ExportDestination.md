---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ExportDestination.html
---

# ExportDestination
<a name="API_ExportDestination"></a>

Specifies where Security Hub writes the export output. This is a union: you must specify exactly one member. Currently, the only supported member is `S3`.

## Contents
<a name="API_ExportDestination_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** S3 **   <a name="securityhub-Type-ExportDestination-S3"></a>
The Amazon Simple Storage Service (Amazon S3) bucket and AWS Key Management Service (AWS KMS) key that Security Hub uses to write the export.
Type: [S3ExportDestination](API_S3ExportDestination.md) object
Required: No

## See Also
<a name="API_ExportDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ExportDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ExportDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ExportDestination)
