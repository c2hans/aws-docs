---
source_url: https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_ResourceTagMapping.html
---

# ResourceTagMapping
<a name="API_ResourceTagMapping"></a>

A list of resource ARNs and the tags (keys and values) that are associated with each.

## Contents
<a name="API_ResourceTagMapping_Contents"></a>

 ** ComplianceDetails **   <a name="resourcegrouptagging-Type-ResourceTagMapping-ComplianceDetails"></a>
Information that shows whether a resource is compliant with the effective tag policy, including details on any noncompliant tag keys.
Type: [ComplianceDetails](API_ComplianceDetails.md) object
Required: No

 ** ResourceARN **   <a name="resourcegrouptagging-Type-ResourceTagMapping-ResourceARN"></a>
The ARN of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `[\s\S]*`
Required: No

 ** Tags **   <a name="resourcegrouptagging-Type-ResourceTagMapping-Tags"></a>
The tags that have been applied to one or more AWS resources.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_ResourceTagMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/ResourceTagMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/ResourceTagMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/ResourceTagMapping)
