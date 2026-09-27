---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_AwsServiceEventsSourceConfiguration.html
---

# AwsServiceEventsSourceConfiguration
<a name="API_AwsServiceEventsSourceConfiguration"></a>

Configuration for forwarding a single AWS service's events from the account's default event bus.

## Contents
<a name="API_AwsServiceEventsSourceConfiguration_Contents"></a>

 ** AwsService **   <a name="eventbridgev2-Type-AwsServiceEventsSourceConfiguration-AwsService"></a>
A single AWS service source identifier, e.g. "aws.s3". Wildcards and lists are rejected.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `aws\.[a-z0-9\-]+`
Required: Yes

 ** OnFailureConfiguration **   <a name="eventbridgev2-Type-AwsServiceEventsSourceConfiguration-OnFailureConfiguration"></a>
The destination for events that could not be forwarded.
Type: [OnFailureConfiguration](API_OnFailureConfiguration.md) object
Required: No

 ** Pattern **   <a name="eventbridgev2-Type-AwsServiceEventsSourceConfiguration-Pattern"></a>
A filter pattern, as a JSON string, that defines which of the service's events are forwarded to the event bus. Do not include source, account, or region as top-level fields. If no pattern is specified, all events from the service are forwarded.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3753.
Required: No

## See Also
<a name="API_AwsServiceEventsSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/AwsServiceEventsSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/AwsServiceEventsSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/AwsServiceEventsSourceConfiguration)
