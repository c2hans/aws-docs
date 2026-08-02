---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ElastiCacheInstanceDetails.html
---

# ElastiCacheInstanceDetails
<a name="API_ElastiCacheInstanceDetails"></a>

Details about the Amazon ElastiCache reservations that AWS recommends that you purchase.

## Contents
<a name="API_ElastiCacheInstanceDetails_Contents"></a>

 ** CurrentGeneration **   <a name="awscostmanagement-Type-ElastiCacheInstanceDetails-CurrentGeneration"></a>
Determines whether the recommendation is for a current generation instance.
Type: Boolean
Required: No

 ** Family **   <a name="awscostmanagement-Type-ElastiCacheInstanceDetails-Family"></a>
The instance family of the recommended reservation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** NodeType **   <a name="awscostmanagement-Type-ElastiCacheInstanceDetails-NodeType"></a>
The type of node that AWS recommends.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** ProductDescription **   <a name="awscostmanagement-Type-ElastiCacheInstanceDetails-ProductDescription"></a>
The description of the recommended reservation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Region **   <a name="awscostmanagement-Type-ElastiCacheInstanceDetails-Region"></a>
The AWS Region of the recommended reservation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** SizeFlexEligible **   <a name="awscostmanagement-Type-ElastiCacheInstanceDetails-SizeFlexEligible"></a>
Determines whether the recommended reservation is size flexible.
Type: Boolean
Required: No

## See Also
<a name="API_ElastiCacheInstanceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/ElastiCacheInstanceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/ElastiCacheInstanceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/ElastiCacheInstanceDetails)
