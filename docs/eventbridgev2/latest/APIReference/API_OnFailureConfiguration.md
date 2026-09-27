---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_OnFailureConfiguration.html
---

# OnFailureConfiguration
<a name="API_OnFailureConfiguration"></a>

On-failure configuration: where a failed delivery is sent. Shared by the subscriber and the EventSource.

## Contents
<a name="API_OnFailureConfiguration_Contents"></a>

 ** Arn **   <a name="eventbridgev2-Type-OnFailureConfiguration-Arn"></a>
The ARN of the destination that receives events that could not be delivered. An Amazon SQS queue is the supported destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `arn:aws(-[a-z0-9]+)*:sqs:[a-z][a-z0-9]*(-[a-z0-9]+)*:[0-9]{12}:([A-Za-z0-9_-]{1,80}|[A-Za-z0-9_-]{1,75}\.fifo)(?![\s\S]).*`
Required: No

## See Also
<a name="API_OnFailureConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/OnFailureConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/OnFailureConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/OnFailureConfiguration)
