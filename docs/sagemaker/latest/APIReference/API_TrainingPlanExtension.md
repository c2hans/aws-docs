---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingPlanExtension.html
---

# TrainingPlanExtension
<a name="API_TrainingPlanExtension"></a>

Details about an extension to a training plan, including the offering ID, dates, status, and cost information.

## Contents
<a name="API_TrainingPlanExtension_Contents"></a>

 ** TrainingPlanExtensionOfferingId **   <a name="sagemaker-Type-TrainingPlanExtension-TrainingPlanExtensionOfferingId"></a>
The unique identifier of the extension offering that was used to create this extension.
Type: String
Required: Yes

 ** AvailabilityZone **   <a name="sagemaker-Type-TrainingPlanExtension-AvailabilityZone"></a>
The Availability Zone of the extension.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** AvailabilityZoneId **   <a name="sagemaker-Type-TrainingPlanExtension-AvailabilityZoneId"></a>
The Availability Zone ID of the extension.
Type: String
Pattern: `[a-z]{3}\d-az\d`
Required: No

 ** CurrencyCode **   <a name="sagemaker-Type-TrainingPlanExtension-CurrencyCode"></a>
The currency code for the upfront fee (e.g., USD).
Type: String
Required: No

 ** DurationHours **   <a name="sagemaker-Type-TrainingPlanExtension-DurationHours"></a>
The duration of the extension in hours.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 4368.
Required: No

 ** PaymentStatus **   <a name="sagemaker-Type-TrainingPlanExtension-PaymentStatus"></a>
The payment processing status of the extension.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** Status **   <a name="sagemaker-Type-TrainingPlanExtension-Status"></a>
The current status of the extension (e.g., Pending, Active, Scheduled, Failed, Expired).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** UpfrontFee **   <a name="sagemaker-Type-TrainingPlanExtension-UpfrontFee"></a>
The upfront fee for the extension.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_TrainingPlanExtension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrainingPlanExtension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrainingPlanExtension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrainingPlanExtension)
