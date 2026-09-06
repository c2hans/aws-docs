---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ESInstanceDetails.html
---

# ESInstanceDetails
<a name="API_ESInstanceDetails"></a>

Details about the Amazon OpenSearch Service reservations that AWS recommends that you purchase.

## Contents
<a name="API_ESInstanceDetails_Contents"></a>

 ** CurrentGeneration **   <a name="awscostmanagement-Type-ESInstanceDetails-CurrentGeneration"></a>
Determines whether the recommendation is for a current-generation instance.
Type: Boolean
Required: No

 ** InstanceClass **   <a name="awscostmanagement-Type-ESInstanceDetails-InstanceClass"></a>
The class of instance that AWS recommends.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** InstanceSize **   <a name="awscostmanagement-Type-ESInstanceDetails-InstanceSize"></a>
The size of instance that AWS recommends.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Region **   <a name="awscostmanagement-Type-ESInstanceDetails-Region"></a>
The AWS Region of the recommended reservation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** SizeFlexEligible **   <a name="awscostmanagement-Type-ESInstanceDetails-SizeFlexEligible"></a>
Determines whether the recommended reservation is size flexible.
Type: Boolean
Required: No

## See Also
<a name="API_ESInstanceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/ESInstanceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/ESInstanceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/ESInstanceDetails)
