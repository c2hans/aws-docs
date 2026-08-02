---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_ResourceGroup.html
---

# ResourceGroup
<a name="API_ResourceGroup"></a>

Contains information about a resource group. The resource group defines a set of tags that, when queried, identify the AWS resources that make up the assessment target. This data type is used as the response element in the [DescribeResourceGroups](API_DescribeResourceGroups.md) action.

## Contents
<a name="API_ResourceGroup_Contents"></a>

 ** arn **   <a name="Inspector-Type-ResourceGroup-arn"></a>
The ARN of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** createdAt **   <a name="Inspector-Type-ResourceGroup-createdAt"></a>
The time at which resource group is created.
Type: Timestamp
Required: Yes

 ** tags **   <a name="Inspector-Type-ResourceGroup-tags"></a>
The tags (key and value pairs) of the resource group. This data type property is used in the [CreateResourceGroup](API_CreateResourceGroup.md) action.
Type: Array of [ResourceGroupTag](API_ResourceGroupTag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## See Also
<a name="API_ResourceGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/ResourceGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/ResourceGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/ResourceGroup)
