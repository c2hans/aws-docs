---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ResiliencyGroupSummary.html
---

# ResiliencyGroupSummary
<a name="API_ResiliencyGroupSummary"></a>

Summary information about a resiliency group.

## Contents
<a name="API_ResiliencyGroupSummary_Contents"></a>

 ** ownerAccount **   <a name="DX-Type-ResiliencyGroupSummary-ownerAccount"></a>
The ID of the AWS account that owns the resiliency group.
Type: String
Required: No

 ** resiliencyGroupArn **   <a name="DX-Type-ResiliencyGroupSummary-resiliencyGroupArn"></a>
The Amazon Resource Name (ARN) of the resiliency group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn:(aws|aws-cn|aws-us-gov):directconnect::[0-9]{12}:dx-resiliency-group/dxrg-[0-9a-z]{17}$`
Required: No

 ** resiliencyGroupId **   <a name="DX-Type-ResiliencyGroupSummary-resiliencyGroupId"></a>
The ID of the resiliency group.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `^(dxrg|DXRG)-[0-9a-zA-Z]{17}$`
Required: No

 ** resiliencyGroupName **   <a name="DX-Type-ResiliencyGroupSummary-resiliencyGroupName"></a>
The name of the resiliency group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_\-]+$`
Required: No

 ** resiliencyGroupType **   <a name="DX-Type-ResiliencyGroupSummary-resiliencyGroupType"></a>
The type of the resiliency group. The valid value is `Managed`.
Type: String
Valid Values: `Managed`
Required: No

 ** state **   <a name="DX-Type-ResiliencyGroupSummary-state"></a>
The state of the resiliency group.
Type: String
Valid Values: `pending | available | deleting | deleted`
Required: No

## See Also
<a name="API_ResiliencyGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/ResiliencyGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/ResiliencyGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/ResiliencyGroupSummary)
