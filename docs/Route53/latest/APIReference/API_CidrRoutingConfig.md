---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_CidrRoutingConfig.html
---

# CidrRoutingConfig
<a name="API_CidrRoutingConfig"></a>

The object that is specified in resource record set object when you are linking a resource record set to a CIDR location.

A `LocationName` with an asterisk “\*” can be used to create a default CIDR record. `CollectionId` is still required for default record.

## Contents
<a name="API_CidrRoutingConfig_Contents"></a>

 ** CollectionId **   <a name="Route53-Type-CidrRoutingConfig-CollectionId"></a>
The CIDR collection ID.
Type: String
Pattern: `[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}`
Required: Yes

 ** LocationName **   <a name="Route53-Type-CidrRoutingConfig-LocationName"></a>
The CIDR collection location name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Pattern: `[0-9A-Za-z_\-\*]+`
Required: Yes

## See Also
<a name="API_CidrRoutingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/CidrRoutingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/CidrRoutingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/CidrRoutingConfig)
