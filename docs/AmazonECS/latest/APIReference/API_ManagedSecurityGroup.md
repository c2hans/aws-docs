---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedSecurityGroup.html
---

# ManagedSecurityGroup
<a name="API_ManagedSecurityGroup"></a>

A security group associated with the Express service.

## Contents
<a name="API_ManagedSecurityGroup_Contents"></a>

 ** status **   <a name="ECS-Type-ManagedSecurityGroup-status"></a>
The status of the security group.
Type: String
Valid Values: `PROVISIONING | ACTIVE | DEPROVISIONING | DELETED | FAILED`
Required: Yes

 ** updatedAt **   <a name="ECS-Type-ManagedSecurityGroup-updatedAt"></a>
The Unix timestamp for when the security group was last updated.
Type: Timestamp
Required: Yes

 ** arn **   <a name="ECS-Type-ManagedSecurityGroup-arn"></a>
The ARN of the security group.
Type: String
Required: No

 ** statusReason **   <a name="ECS-Type-ManagedSecurityGroup-statusReason"></a>
Information about why the security group is in the current status.
Type: String
Required: No

## See Also
<a name="API_ManagedSecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedSecurityGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedSecurityGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedSecurityGroup)
