---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceCreationProperties.html
---

# WorkspaceCreationProperties
<a name="API_WorkspaceCreationProperties"></a>

Describes the default properties that are used for creating WorkSpaces. For more information, see [Update Directory Details for Your WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/update-directory-details.html).

## Contents
<a name="API_WorkspaceCreationProperties_Contents"></a>

 ** CustomSecurityGroupId **   <a name="WorkSpaces-Type-WorkspaceCreationProperties-CustomSecurityGroupId"></a>
The identifier of your custom security group.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 20.
Pattern: `^(sg-([0-9a-f]{8}|[0-9a-f]{17}))$`
Required: No

 ** DefaultOu **   <a name="WorkSpaces-Type-WorkspaceCreationProperties-DefaultOu"></a>
The default organizational unit (OU) for your WorkSpaces directories. This string must be the full Lightweight Directory Access Protocol (LDAP) distinguished name for the target domain and OU. It must be in the form `"OU=value,DC=value,DC=value"`, where *value* is any string of characters, and the number of domain components (DCs) is two or more. For example, `OU=WorkSpaces_machines,DC=machines,DC=example,DC=com`.
+ To avoid errors, certain characters in the distinguished name must be escaped. For more information, see [ Distinguished Names](https://docs.microsoft.com/previous-versions/windows/desktop/ldap/distinguished-names) in the Microsoft documentation.
+ The API doesn't validate whether the OU exists.
Type: String
Required: No

 ** EnableInternetAccess **   <a name="WorkSpaces-Type-WorkspaceCreationProperties-EnableInternetAccess"></a>
Indicates whether internet access is enabled for your WorkSpaces.
Type: Boolean
Required: No

 ** EnableMaintenanceMode **   <a name="WorkSpaces-Type-WorkspaceCreationProperties-EnableMaintenanceMode"></a>
Indicates whether maintenance mode is enabled for your WorkSpaces. For more information, see [WorkSpace Maintenance](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html).
Type: Boolean
Required: No

 ** InstanceIamRoleArn **   <a name="WorkSpaces-Type-WorkspaceCreationProperties-InstanceIamRoleArn"></a>
Indicates the IAM role ARN of the instance.
Type: String
Pattern: `^arn:aws[a-z-]{0,7}:[A-Za-z0-9][A-za-z0-9_/.-]{0,62}:[A-za-z0-9_/.-]{0,63}:[A-za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** UserEnabledAsLocalAdministrator **   <a name="WorkSpaces-Type-WorkspaceCreationProperties-UserEnabledAsLocalAdministrator"></a>
Indicates whether users are local administrators of their WorkSpaces.
Type: Boolean
Required: No

## See Also
<a name="API_WorkspaceCreationProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/WorkspaceCreationProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/WorkspaceCreationProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/WorkspaceCreationProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
