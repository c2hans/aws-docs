---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DefaultWorkspaceCreationProperties.html
---

# DefaultWorkspaceCreationProperties
<a name="API_DefaultWorkspaceCreationProperties"></a>

Describes the default values that are used to create WorkSpaces. For more information, see [Update Directory Details for Your WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/update-directory-details.html).

## Contents
<a name="API_DefaultWorkspaceCreationProperties_Contents"></a>

 ** CustomSecurityGroupId **   <a name="WorkSpaces-Type-DefaultWorkspaceCreationProperties-CustomSecurityGroupId"></a>
The identifier of the default security group to apply to WorkSpaces when they are created. For more information, see [ Security Groups for Your WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-security-groups.html).
Type: String
Length Constraints: Minimum length of 11. Maximum length of 20.
Pattern: `^(sg-([0-9a-f]{8}|[0-9a-f]{17}))$`
Required: No

 ** DefaultOu **   <a name="WorkSpaces-Type-DefaultWorkspaceCreationProperties-DefaultOu"></a>
The organizational unit (OU) in the directory for the WorkSpace machine accounts.
Type: String
Required: No

 ** EnableInternetAccess **   <a name="WorkSpaces-Type-DefaultWorkspaceCreationProperties-EnableInternetAccess"></a>
Specifies whether to automatically assign an Elastic public IP address to WorkSpaces in this directory by default. If enabled, the Elastic public IP address allows outbound internet access from your WorkSpaces when you’re using an internet gateway in the Amazon VPC in which your WorkSpaces are located. If you're using a Network Address Translation (NAT) gateway for outbound internet access from your VPC, or if your WorkSpaces are in public subnets and you manually assign them Elastic IP addresses, you should disable this setting. This setting applies to new WorkSpaces that you launch or to existing WorkSpaces that you rebuild. For more information, see [ Configure a VPC for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-vpc.html).
Type: Boolean
Required: No

 ** EnableMaintenanceMode **   <a name="WorkSpaces-Type-DefaultWorkspaceCreationProperties-EnableMaintenanceMode"></a>
Specifies whether maintenance mode is enabled for WorkSpaces. For more information, see [WorkSpace Maintenance](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html).
Type: Boolean
Required: No

 ** InstanceIamRoleArn **   <a name="WorkSpaces-Type-DefaultWorkspaceCreationProperties-InstanceIamRoleArn"></a>
Indicates the IAM role ARN of the instance.
Type: String
Pattern: `^arn:aws[a-z-]{0,7}:[A-Za-z0-9][A-za-z0-9_/.-]{0,62}:[A-za-z0-9_/.-]{0,63}:[A-za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** UserEnabledAsLocalAdministrator **   <a name="WorkSpaces-Type-DefaultWorkspaceCreationProperties-UserEnabledAsLocalAdministrator"></a>
Specifies whether WorkSpace users are local administrators on their WorkSpaces.
Type: Boolean
Required: No

## See Also
<a name="API_DefaultWorkspaceCreationProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DefaultWorkspaceCreationProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DefaultWorkspaceCreationProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DefaultWorkspaceCreationProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
