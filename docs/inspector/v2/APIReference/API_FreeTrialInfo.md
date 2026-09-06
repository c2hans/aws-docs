---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_FreeTrialInfo.html
---

# FreeTrialInfo
<a name="API_FreeTrialInfo"></a>

An object that contains information about the Amazon Inspector free trial for an account.

## Contents
<a name="API_FreeTrialInfo_Contents"></a>

 ** end **   <a name="inspector2-Type-FreeTrialInfo-end"></a>
The date and time that the Amazon Inspector free trail ends for a given account.
Type: Timestamp
Required: Yes

 ** start **   <a name="inspector2-Type-FreeTrialInfo-start"></a>
The date and time that the Amazon Inspector free trail started for a given account.
Type: Timestamp
Required: Yes

 ** status **   <a name="inspector2-Type-FreeTrialInfo-status"></a>
The order to sort results by.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

 ** type **   <a name="inspector2-Type-FreeTrialInfo-type"></a>
The type of scan covered by the Amazon Inspector free trail.
Type: String
Valid Values: `EC2 | ECR | LAMBDA | LAMBDA_CODE | CODE_REPOSITORY | VM | CONTAINER_IMAGE | SERVERLESS_FUNCTION`
Required: Yes

 ** cloudProvider **   <a name="inspector2-Type-FreeTrialInfo-cloudProvider"></a>
The cloud provider associated with the free trial information.
Type: String
Valid Values: `AWS | AZURE | NOT_APPLICABLE`
Required: No

## See Also
<a name="API_FreeTrialInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/FreeTrialInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/FreeTrialInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/FreeTrialInfo)
