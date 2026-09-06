---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_SnsTopicConfiguration.html
---

# SnsTopicConfiguration
<a name="API_SnsTopicConfiguration"></a>

The proposed access control configuration for an Amazon SNS topic. You can propose a configuration for a new Amazon SNS topic or an existing Amazon SNS topic that you own by specifying the policy. If the configuration is for an existing Amazon SNS topic and you do not specify the Amazon SNS policy, then the access preview uses the existing Amazon SNS policy for the topic. If the access preview is for a new resource and you do not specify the policy, then the access preview assumes an Amazon SNS topic without a policy. To propose deletion of an existing Amazon SNS topic policy, you can specify an empty string for the Amazon SNS policy. For more information, see [Topic](https://docs.aws.amazon.com/sns/latest/api/API_Topic.html).

## Contents
<a name="API_SnsTopicConfiguration_Contents"></a>

 ** topicPolicy **   <a name="accessanalyzer-Type-SnsTopicConfiguration-topicPolicy"></a>
The JSON policy text that defines who can access an Amazon SNS topic. For more information, see [Example cases for Amazon SNS access control](https://docs.aws.amazon.com/sns/latest/dg/sns-access-policy-use-cases.html) in the *Amazon SNS Developer Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 30720.
Required: No

## See Also
<a name="API_SnsTopicConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/SnsTopicConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/SnsTopicConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/SnsTopicConfiguration)
