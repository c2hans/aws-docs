---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_WebhookDetails.html
---

# WebhookDetails

Values EventBridge generated for a webhook EventSource.

## Contents
<a name="API_WebhookDetails_Contents"></a>

 ** SecretArn **   <a name="eventbridgev2-Type-WebhookDetails-SecretArn"></a>
The ARN of the AWS Secrets Manager secret, in your account, that holds the secret.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z0-9]+)*:secretsmanager:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):secret:events-webhook(-preprod)?[!/].+`
Required: No

 ** WebhookUrl **   <a name="eventbridgev2-Type-WebhookDetails-WebhookUrl"></a>
The HTTPS URL to configure in the provider. The URL doesn't change for the life of the EventSource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_WebhookDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/WebhookDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/WebhookDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/WebhookDetails)
