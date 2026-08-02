---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImageUsageResourceType.html
---

# ImageUsageResourceType
<a name="API_ImageUsageResourceType"></a>

A resource type to include in the report. Associated options can also be specified if the resource type is a launch template.

## Contents
<a name="API_ImageUsageResourceType_Contents"></a>

 ** resourceType **
The resource type.
Valid values: `ec2:Instance` \| `ec2:LaunchTemplate`
Type: String
Required: No

 ** ResourceTypeOptionSet.N **
The options that affect the scope of the report. Valid only when `ResourceType` is `ec2:LaunchTemplate`.
Type: Array of [ImageUsageResourceTypeOption](API_ImageUsageResourceTypeOption.md) objects
Required: No

## See Also
<a name="API_ImageUsageResourceType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImageUsageResourceType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImageUsageResourceType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImageUsageResourceType)
