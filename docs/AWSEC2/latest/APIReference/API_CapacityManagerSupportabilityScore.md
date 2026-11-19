---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityManagerSupportabilityScore.html
---

# CapacityManagerSupportabilityScore

 The supportability score for a single instance type and Availability Zone combination.

## Contents
<a name="API_CapacityManagerSupportabilityScore_Contents"></a>

 ** availabilityZoneId **
 The ID of the Availability Zone.
Type: String
Required: No

 ** instanceType **
 The instance type.
Type: String
Required: No

 ** score **
 How well the combination can support the requested capacity right now. `high` means that the combination holds several times the requested amount. `medium` means that it can cover the request with little to spare. `low` means that it holds less than the requested amount.
Type: String
Valid Values: `high | medium | low`
Required: No

## See Also
<a name="API_CapacityManagerSupportabilityScore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityManagerSupportabilityScore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityManagerSupportabilityScore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityManagerSupportabilityScore)
