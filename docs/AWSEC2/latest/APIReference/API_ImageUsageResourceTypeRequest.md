---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImageUsageResourceTypeRequest.html
---

# ImageUsageResourceTypeRequest
<a name="API_ImageUsageResourceTypeRequest"></a>

A resource type to include in the report. Associated options can also be specified if the resource type is a launch template.

## Contents
<a name="API_ImageUsageResourceTypeRequest_Contents"></a>

 ** ResourceType **
The resource type.
Valid values: `ec2:Instance` \| `ec2:LaunchTemplate`
Type: String
Required: No

 ** ResourceTypeOption.N **
The options that affect the scope of the report. Valid only when `ResourceType` is `ec2:LaunchTemplate`.
Type: Array of [ImageUsageResourceTypeOptionRequest](API_ImageUsageResourceTypeOptionRequest.md) objects
Required: No

## See Also
<a name="API_ImageUsageResourceTypeRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImageUsageResourceTypeRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImageUsageResourceTypeRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImageUsageResourceTypeRequest)
