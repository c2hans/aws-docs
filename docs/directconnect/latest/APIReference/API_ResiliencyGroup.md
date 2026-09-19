---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ResiliencyGroup.html
---

# ResiliencyGroup
<a name="API_ResiliencyGroup"></a>

Information about a resiliency group.

## Contents
<a name="API_ResiliencyGroup_Contents"></a>

 ** ownerAccount **   <a name="DX-Type-ResiliencyGroup-ownerAccount"></a>
The ID of the AWS account that owns the resiliency group.
Type: String
Required: No

 ** resiliencyGroupArn **   <a name="DX-Type-ResiliencyGroup-resiliencyGroupArn"></a>
The Amazon Resource Name (ARN) of the resiliency group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn:(aws|aws-cn|aws-us-gov):directconnect::[0-9]{12}:dx-resiliency-group/dxrg-[0-9a-z]{17}$`
Required: No

 ** resiliencyGroupId **   <a name="DX-Type-ResiliencyGroup-resiliencyGroupId"></a>
The ID of the resiliency group.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `^(dxrg|DXRG)-[0-9a-zA-Z]{17}$`
Required: No

 ** resiliencyGroupName **   <a name="DX-Type-ResiliencyGroup-resiliencyGroupName"></a>
The name of the resiliency group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_\-]+$`
Required: No

 ** resiliencyGroupType **   <a name="DX-Type-ResiliencyGroup-resiliencyGroupType"></a>
The type of the resiliency group. The valid value is `Managed`.
Type: String
Valid Values: `Managed`
Required: No

 ** state **   <a name="DX-Type-ResiliencyGroup-state"></a>
The state of the resiliency group. The valid values are `pending`, `available`, `deleting`, and `deleted`.
Type: String
Valid Values: `pending | available | deleting | deleted`
Required: No

 ** tags **   <a name="DX-Type-ResiliencyGroup-tags"></a>
The tags associated with the resiliency group.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_ResiliencyGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/ResiliencyGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/ResiliencyGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/ResiliencyGroup)
