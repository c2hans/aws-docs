---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_LogSourceResource.html
---

# LogSourceResource
<a name="API_LogSourceResource"></a>

The supported source types from which logs and events are collected in Amazon Security Lake. For a list of supported AWS services, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html).

## Contents
<a name="API_LogSourceResource_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** awsLogSource **   <a name="securitylake-Type-LogSourceResource-awsLogSource"></a>
Amazon Security Lake supports log and event collection for natively supported AWS services. For more information, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html).
Type: [AwsLogSourceResource](API_AwsLogSourceResource.md) object
Required: No

 ** customLogSource **   <a name="securitylake-Type-LogSourceResource-customLogSource"></a>
Amazon Security Lake supports custom source types. For more information, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/custom-sources.html).
Type: [CustomLogSourceResource](API_CustomLogSourceResource.md) object
Required: No

## See Also
<a name="API_LogSourceResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/LogSourceResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/LogSourceResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/LogSourceResource)
