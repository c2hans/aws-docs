---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ErrorDetail.html
---

# ErrorDetail

Describes one cause of a failure of a resource or an update, with an error code, a description, and the IDs of the resources involved.

## Contents
<a name="API_ErrorDetail_Contents"></a>

 ** code **   <a name="rtbfabric-Type-ErrorDetail-code"></a>
The error code for what failed, and what to do about it:
+  `VPC_NOT_FOUND`: the VPC no longer exists. Use an existing VPC.
+  `EC2_SUBNET_NOT_FOUND`: a subnet no longer exists. Use an existing subnet.
+  `EC2_SECURITY_GROUP_NOT_FOUND`: a security group no longer exists. Use an existing security group.
+  `EC2_SUBNET_IP_EXHAUSTION`: a subnet has no free IP addresses. Free IP addresses in the subnet.
+  `IAM_ASSUME_ROLE_ACCESS_DENIED`: RTB Fabric couldn't assume an IAM role in your account. Check that the role exists and that its trust policy allows RTB Fabric to assume it.
+  `INTERNAL_ERROR`: an internal error in RTB Fabric. If it continues, contact AWS Support.
Type: String
Valid Values: `VPC_NOT_FOUND | EC2_SUBNET_NOT_FOUND | EC2_SECURITY_GROUP_NOT_FOUND | EC2_SUBNET_IP_EXHAUSTION | IAM_ASSUME_ROLE_ACCESS_DENIED | INTERNAL_ERROR`
Required: Yes

 ** message **   <a name="rtbfabric-Type-ErrorDetail-message"></a>
A description of the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

 ** resourceIds **   <a name="rtbfabric-Type-ErrorDetail-resourceIds"></a>
The IDs of the resources involved, such as a subnet or security group.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_ErrorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/ErrorDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/ErrorDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/ErrorDetail)
