---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_CidrCollectionChange.html
---

# CidrCollectionChange
<a name="API_CidrCollectionChange"></a>

A complex type that contains information about the CIDR collection change.

## Contents
<a name="API_CidrCollectionChange_Contents"></a>

 ** Action **   <a name="Route53-Type-CidrCollectionChange-Action"></a>
CIDR collection change action.
Type: String
Valid Values: `PUT | DELETE_IF_EXISTS`
Required: Yes

 ** CidrList **   <a name="Route53-Type-CidrCollectionChange-CidrList"></a>
List of CIDR blocks.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `.*\S.*`
Required: Yes

 ** LocationName **   <a name="Route53-Type-CidrCollectionChange-LocationName"></a>
Name of the location that is associated with the CIDR collection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Pattern: `[0-9A-Za-z_\-]+`
Required: Yes

## See Also
<a name="API_CidrCollectionChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/CidrCollectionChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/CidrCollectionChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/CidrCollectionChange)
