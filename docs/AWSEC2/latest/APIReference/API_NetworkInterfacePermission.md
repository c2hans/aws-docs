---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_NetworkInterfacePermission.html
---

# NetworkInterfacePermission
<a name="API_NetworkInterfacePermission"></a>

Describes a permission for a network interface.

## Contents
<a name="API_NetworkInterfacePermission_Contents"></a>

 ** awsAccountId **
The AWS account ID.
Type: String
Required: No

 ** awsService **
The AWS service.
Type: String
Required: No

 ** networkInterfaceId **
The ID of the network interface.
Type: String
Required: No

 ** networkInterfacePermissionId **
The ID of the network interface permission.
Type: String
Required: No

 ** permission **
The type of permission.
Type: String
Valid Values: `INSTANCE-ATTACH | EIP-ASSOCIATE`
Required: No

 ** permissionState **
Information about the state of the permission.
Type: [NetworkInterfacePermissionState](API_NetworkInterfacePermissionState.md) object
Required: No

## See Also
<a name="API_NetworkInterfacePermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/NetworkInterfacePermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/NetworkInterfacePermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/NetworkInterfacePermission)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
