---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariantStatus.html
---

# ProductionVariantStatus
<a name="API_ProductionVariantStatus"></a>

Describes the status of the production variant.

## Contents
<a name="API_ProductionVariantStatus_Contents"></a>

 ** Status **   <a name="sagemaker-Type-ProductionVariantStatus-Status"></a>
The endpoint variant status which describes the current deployment stage status or operational status.
+  `Creating`: Creating inference resources for the production variant.
+  `Deleting`: Terminating inference resources for the production variant.
+  `Updating`: Updating capacity for the production variant.
+  `ActivatingTraffic`: Turning on traffic for the production variant.
+  `Baking`: Waiting period to monitor the CloudWatch alarms in the automatic rollback configuration.
Type: String
Valid Values: `Creating | Updating | Deleting | ActivatingTraffic | Baking`
Required: Yes

 ** StatusMessage **   <a name="sagemaker-Type-ProductionVariantStatus-StatusMessage"></a>
A message that describes the status of the production variant.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_ProductionVariantStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProductionVariantStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProductionVariantStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProductionVariantStatus)
