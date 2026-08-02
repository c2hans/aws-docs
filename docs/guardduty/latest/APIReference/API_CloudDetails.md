---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CloudDetails.html
---

# CloudDetails
<a name="API_CloudDetails"></a>

Contains details about the cloud environment associated with an investigation.

## Contents
<a name="API_CloudDetails_Contents"></a>

 ** account **   <a name="guardduty-Type-CloudDetails-account"></a>
The AWS account ID of the investigated resource.
Type: String
Required: Yes

 ** provider **   <a name="guardduty-Type-CloudDetails-provider"></a>
The cloud provider. Currently, only `AWS` is supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Valid Values: `AWS`
Required: Yes

 ** region **   <a name="guardduty-Type-CloudDetails-region"></a>
The AWS Region in which the investigated resource resides.
Type: String
Required: Yes

## See Also
<a name="API_CloudDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CloudDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CloudDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CloudDetails)
