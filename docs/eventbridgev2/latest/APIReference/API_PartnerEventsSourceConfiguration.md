---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_PartnerEventsSourceConfiguration.html
---

# PartnerEventsSourceConfiguration
<a name="API_PartnerEventsSourceConfiguration"></a>

Configuration for forwarding a partner event source's events through a managed partner event bus.

## Contents
<a name="API_PartnerEventsSourceConfiguration_Contents"></a>

 ** PartnerEventSourceArn **   <a name="eventbridgev2-Type-PartnerEventsSourceConfiguration-PartnerEventSourceArn"></a>
ARN of the partner event source to forward. It is a partner-owned resource, so the account segment is empty: arn:aws:events:<region>::event-source/aws.partner/<name>.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `arn:aws(-[a-z0-9]+)*:events:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12})?:event-source\/aws\.partner(\/[\.\-_A-Za-z0-9]+){2,}`
Required: Yes

 ** OnFailureConfiguration **   <a name="eventbridgev2-Type-PartnerEventsSourceConfiguration-OnFailureConfiguration"></a>
The destination for events that could not be forwarded, covering both the forwarding target and the managed partner event bus.
Type: [OnFailureConfiguration](API_OnFailureConfiguration.md) object
Required: No

 ** PartnerBusKmsKeyIdentifier **   <a name="eventbridgev2-Type-PartnerEventsSourceConfiguration-PartnerBusKmsKeyIdentifier"></a>
Identifier of the AWS KMS customer managed key used to encrypt events: a key ID, key ARN, alias name, or alias ARN. When absent, events are encrypted with an AWS owned key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9_\-/:]*`
Required: No

 ** Pattern **   <a name="eventbridgev2-Type-PartnerEventsSourceConfiguration-Pattern"></a>
A filter pattern, as a JSON string, that defines which of the partner event source's events are forwarded to the event bus. If no pattern is specified, all events from the partner event source are forwarded.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3753.
Required: No

## See Also
<a name="API_PartnerEventsSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/PartnerEventsSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/PartnerEventsSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/PartnerEventsSourceConfiguration)
