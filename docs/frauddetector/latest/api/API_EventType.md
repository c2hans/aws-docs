---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_EventType.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# EventType
<a name="API_EventType"></a>

The event type details.

## Contents
<a name="API_EventType_Contents"></a>

 ** arn **   <a name="FraudDetector-Type-EventType-arn"></a>
The entity type ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:frauddetector\:[a-z0-9-]{3,20}\:[0-9]{12}\:[^\s]{2,128}$`
Required: No

 ** createdTime **   <a name="FraudDetector-Type-EventType-createdTime"></a>
Timestamp of when the event type was created.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** description **   <a name="FraudDetector-Type-EventType-description"></a>
The event type description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** entityTypes **   <a name="FraudDetector-Type-EventType-entityTypes"></a>
The event type entity types.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

 ** eventIngestion **   <a name="FraudDetector-Type-EventType-eventIngestion"></a>
If `Enabled`, Amazon Fraud Detector stores event data when you generate a prediction and uses that data to update calculated variables in near real-time. Amazon Fraud Detector uses this data, known as `INGESTED_EVENTS`, to train your model and improve fraud predictions.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** eventOrchestration **   <a name="FraudDetector-Type-EventType-eventOrchestration"></a>
The event orchestration status.
Type: [EventOrchestration](API_EventOrchestration.md) object
Required: No

 ** eventVariables **   <a name="FraudDetector-Type-EventType-eventVariables"></a>
The event type event variables.
Type: Array of strings
Required: No

 ** ingestedEventStatistics **   <a name="FraudDetector-Type-EventType-ingestedEventStatistics"></a>
Data about the stored events.
Type: [IngestedEventStatistics](API_IngestedEventStatistics.md) object
Required: No

 ** labels **   <a name="FraudDetector-Type-EventType-labels"></a>
The event type labels.
Type: Array of strings
Required: No

 ** lastUpdatedTime **   <a name="FraudDetector-Type-EventType-lastUpdatedTime"></a>
Timestamp of when the event type was last updated.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** name **   <a name="FraudDetector-Type-EventType-name"></a>
The event type name.
Type: String
Required: No

## See Also
<a name="API_EventType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/EventType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/EventType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/EventType)
