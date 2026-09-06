---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_Event.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# Event
<a name="API_Event"></a>

The event details.

## Contents
<a name="API_Event_Contents"></a>

 ** currentLabel **   <a name="FraudDetector-Type-Event-currentLabel"></a>
The label associated with the event.
Type: String
Required: No

 ** entities **   <a name="FraudDetector-Type-Event-entities"></a>
The event entities.
Type: Array of [Entity](API_Entity.md) objects
Required: No

 ** eventId **   <a name="FraudDetector-Type-Event-eventId"></a>
The event ID.
Type: String
Required: No

 ** eventTimestamp **   <a name="FraudDetector-Type-Event-eventTimestamp"></a>
The timestamp that defines when the event under evaluation occurred. The timestamp must be specified using ISO 8601 standard in UTC.
Type: String
Required: No

 ** eventTypeName **   <a name="FraudDetector-Type-Event-eventTypeName"></a>
The event type.
Type: String
Required: No

 ** eventVariables **   <a name="FraudDetector-Type-Event-eventVariables"></a>
Names of the event type's variables you defined in Amazon Fraud Detector to represent data elements and their corresponding values for the event you are sending for evaluation.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** labelTimestamp **   <a name="FraudDetector-Type-Event-labelTimestamp"></a>
The timestamp associated with the label to update. The timestamp must be specified using ISO 8601 standard in UTC.
Type: String
Required: No

## See Also
<a name="API_Event_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/Event)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/Event)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/Event)
