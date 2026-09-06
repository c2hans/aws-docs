---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_CollectionSummary.html
---

# CollectionSummary
<a name="API_CollectionSummary"></a>

A complex type that is an entry in an [CidrCollection](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CidrCollection.html) array.

## Contents
<a name="API_CollectionSummary_Contents"></a>

 ** Arn **   <a name="Route53-Type-CollectionSummary-Arn"></a>
The ARN of the collection summary. Can be used to reference the collection in IAM policy or cross-account.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** Id **   <a name="Route53-Type-CollectionSummary-Id"></a>
Unique ID for the CIDR collection.
Type: String
Pattern: `[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}`
Required: No

 ** Name **   <a name="Route53-Type-CollectionSummary-Name"></a>
The name of a CIDR collection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9A-Za-z_\-]+`
Required: No

 ** Version **   <a name="Route53-Type-CollectionSummary-Version"></a>
A sequential counter that Route 53 sets to 1 when you create a CIDR collection and increments by 1 each time you update settings for the CIDR collection.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_CollectionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/CollectionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/CollectionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/CollectionSummary)
