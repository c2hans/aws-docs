---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_Tag.html
---

# Tag
<a name="API_route53resolver_Tag"></a>

One tag that you want to add to the specified resource. A tag consists of a `Key` (a name for the tag) and a `Value`.

## Contents
<a name="API_route53resolver_Tag_Contents"></a>

 ** Key **   <a name="Route53Resolver-Type-route53resolver_Tag-Key"></a>
The name for the tag. For example, if you want to associate Resolver resources with the account IDs of your customers for billing purposes, the value of `Key` might be `account-id`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Value **   <a name="Route53Resolver-Type-route53resolver_Tag-Value"></a>
The value for the tag. For example, if `Key` is `account-id`, then `Value` might be the ID of the customer account that you're creating the resource for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## See Also
<a name="API_route53resolver_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/Tag)
