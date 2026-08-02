---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_ExternalEventsDetail.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# ExternalEventsDetail
<a name="API_ExternalEventsDetail"></a>

Details for the external events data used for model version training.

## Contents
<a name="API_ExternalEventsDetail_Contents"></a>

 ** dataAccessRoleArn **   <a name="FraudDetector-Type-ExternalEventsDetail-dataAccessRoleArn"></a>
The ARN of the role that provides Amazon Fraud Detector access to the data location.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:iam\:\:[0-9]{12}\:role\/[^\s]{2,64}$`
Required: Yes

 ** dataLocation **   <a name="FraudDetector-Type-ExternalEventsDetail-dataLocation"></a>
The Amazon S3 bucket location for the data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^s3:\/\/(.+)$`
Required: Yes

## See Also
<a name="API_ExternalEventsDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/ExternalEventsDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/ExternalEventsDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/ExternalEventsDetail)
