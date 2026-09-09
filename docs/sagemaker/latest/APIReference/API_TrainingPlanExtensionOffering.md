---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingPlanExtensionOffering.html
---

# TrainingPlanExtensionOffering
<a name="API_TrainingPlanExtensionOffering"></a>

Details about an available extension offering for a training plan. Use the offering ID with the ` [ExtendTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ExtendTrainingPlan.html) ` API to extend a training plan.

## Contents
<a name="API_TrainingPlanExtensionOffering_Contents"></a>

 ** TrainingPlanExtensionOfferingId **   <a name="sagemaker-Type-TrainingPlanExtensionOffering-TrainingPlanExtensionOfferingId"></a>
The unique identifier for this extension offering.
Type: String
Required: Yes

 ** AvailabilityZone **   <a name="sagemaker-Type-TrainingPlanExtensionOffering-AvailabilityZone"></a>
The Availability Zone for this extension offering.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** CurrencyCode **   <a name="sagemaker-Type-TrainingPlanExtensionOffering-CurrencyCode"></a>
The currency code for the upfront fee (e.g., USD).
Type: String
Required: No

 ** DurationHours **   <a name="sagemaker-Type-TrainingPlanExtensionOffering-DurationHours"></a>
The duration of this extension offering in hours.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 4368.
Required: No

 ** UpfrontFee **   <a name="sagemaker-Type-TrainingPlanExtensionOffering-UpfrontFee"></a>
The upfront fee for this extension offering.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_TrainingPlanExtensionOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrainingPlanExtensionOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrainingPlanExtensionOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrainingPlanExtensionOffering)
