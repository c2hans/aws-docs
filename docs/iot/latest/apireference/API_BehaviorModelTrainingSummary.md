---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_BehaviorModelTrainingSummary.html
---

# BehaviorModelTrainingSummary
<a name="API_BehaviorModelTrainingSummary"></a>

 The summary of an ML Detect behavior model.

## Contents
<a name="API_BehaviorModelTrainingSummary_Contents"></a>

 ** behaviorName **   <a name="iot-Type-BehaviorModelTrainingSummary-behaviorName"></a>
 The name of the behavior.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** datapointsCollectionPercentage **   <a name="iot-Type-BehaviorModelTrainingSummary-datapointsCollectionPercentage"></a>
 The percentage of datapoints collected.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** lastModelRefreshDate **   <a name="iot-Type-BehaviorModelTrainingSummary-lastModelRefreshDate"></a>
 The date the model was last refreshed.
Type: Timestamp
Required: No

 ** modelStatus **   <a name="iot-Type-BehaviorModelTrainingSummary-modelStatus"></a>
 The status of the behavior model.
Type: String
Valid Values: `PENDING_BUILD | ACTIVE | EXPIRED`
Required: No

 ** securityProfileName **   <a name="iot-Type-BehaviorModelTrainingSummary-securityProfileName"></a>
 The name of the security profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** trainingDataCollectionStartDate **   <a name="iot-Type-BehaviorModelTrainingSummary-trainingDataCollectionStartDate"></a>
 The date a training model started collecting data.
Type: Timestamp
Required: No

## See Also
<a name="API_BehaviorModelTrainingSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/BehaviorModelTrainingSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/BehaviorModelTrainingSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/BehaviorModelTrainingSummary)
