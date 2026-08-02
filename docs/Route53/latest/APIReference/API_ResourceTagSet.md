---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResourceTagSet.html
---

# ResourceTagSet
<a name="API_ResourceTagSet"></a>

A complex type containing a resource and its associated tags.

## Contents
<a name="API_ResourceTagSet_Contents"></a>

 ** ResourceId **   <a name="Route53-Type-ResourceTagSet-ResourceId"></a>
The ID for the specified resource.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** ResourceType **   <a name="Route53-Type-ResourceTagSet-ResourceType"></a>
The type of the resource.
+ The resource type for health checks is `healthcheck`.
+ The resource type for hosted zones is `hostedzone`.
Type: String
Valid Values: `healthcheck | hostedzone`
Required: No

 ** Tags **   <a name="Route53-Type-ResourceTagSet-Tags"></a>
The tags associated with the specified resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_ResourceTagSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ResourceTagSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ResourceTagSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ResourceTagSet)
