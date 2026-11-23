---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_WebhookEventsSourceConfiguration.html
---

# WebhookEventsSourceConfiguration

Configuration for receiving events from an external provider, such as a SaaS application, that sends them as HTTPS POST requests to a webhook URL. The provider authenticates with an HTTP scheme instead of AWS credentials.

## Contents
<a name="API_WebhookEventsSourceConfiguration_Contents"></a>

 ** AuthConfiguration **   <a name="eventbridgev2-Type-WebhookEventsSourceConfiguration-AuthConfiguration"></a>
How the provider authenticates its requests. Exactly one authentication type must be set, and it can't be changed after the EventSource is created.
Type: [WebhookAuthConfiguration](API_WebhookAuthConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** RoleArn **   <a name="eventbridgev2-Type-WebhookEventsSourceConfiguration-RoleArn"></a>
IAM role the service assumes to put the webhook's events on the event bus. Must belong to the calling account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `arn:aws(-[a-z0-9]+)*:iam::\d{12}:role\/[\w+=,.@/-]+`
Required: Yes

 ** DeduplicationConfiguration **   <a name="eventbridgev2-Type-WebhookEventsSourceConfiguration-DeduplicationConfiguration"></a>
Optional. Deduplicates this EventSource's events on the event bus. Omit it to deduplicate nothing.
Type: [WebhookDeduplicationConfiguration](API_WebhookDeduplicationConfiguration.md) object
Required: No

 ** KmsKeyIdentifier **   <a name="eventbridgev2-Type-WebhookEventsSourceConfiguration-KmsKeyIdentifier"></a>
Optional. The AWS KMS key that encrypts the EventSource's secret in AWS Secrets Manager. Omit it to encrypt the secret with the AWS managed key aws/secretsmanager. A key you supply must be an enabled customer managed key in your account and Region. Changing it re-encrypts the secret under the new key. The previous key can still decrypt the stored versions until the credential is next rotated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9_\-/:]*`
Required: No

 ** LogConfiguration **   <a name="eventbridgev2-Type-WebhookEventsSourceConfiguration-LogConfiguration"></a>
Optional. Controls the log records EventBridge delivers for this EventSource's webhook requests. Omit it to deliver no logs. Logs are delivered to the destinations you configure through Amazon CloudWatch Logs log delivery.
Type: [LogConfiguration](API_LogConfiguration.md) object
Required: No

 ** MetadataHttpHeaders **   <a name="eventbridgev2-Type-WebhookEventsSourceConfiguration-MetadataHttpHeaders"></a>
The HTTP request headers to add to each event's metadata, up to 20. Header names are case-insensitive and can't repeat. Each header is added under its lowercase name. Omit the list to add no headers. Headers that carry credentials or that describe the network path, and the header that carries the static token, can't be listed.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[!#$%&'*+\-.^_`|~0-9A-Za-z]+`
Required: No

## See Also
<a name="API_WebhookEventsSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/WebhookEventsSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/WebhookEventsSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/WebhookEventsSourceConfiguration)
