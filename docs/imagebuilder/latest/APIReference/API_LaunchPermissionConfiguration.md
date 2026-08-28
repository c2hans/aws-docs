---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LaunchPermissionConfiguration.html
---

# LaunchPermissionConfiguration
<a name="API_LaunchPermissionConfiguration"></a>

Describes the configuration for a launch permission. The launch permission modification request is sent to the [Amazon EC2 ModifyImageAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyImageAttribute.html) API on behalf of the user for each Region they have selected to distribute the AMI. To make an AMI public, set the launch permission authorized accounts to `all`. See the examples for making an AMI public at [Amazon EC2 ModifyImageAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyImageAttribute.html).

## Contents
<a name="API_LaunchPermissionConfiguration_Contents"></a>

 ** organizationalUnitArns **   <a name="imagebuilder-Type-LaunchPermissionConfiguration-organizationalUnitArns"></a>
The ARN for an AWS Organizations organizational unit (OU) that you want to share your AMI with. For more information about key concepts for AWS Organizations, see [AWS Organizations terminology and concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Pattern: `^arn:aws[^:]*:organizations::[0-9]{12}:ou/o-[a-z0-9]{10,32}/ou-[0-9a-z]{4,32}-[0-9a-z]{8,32}`
Required: No

 ** organizationArns **   <a name="imagebuilder-Type-LaunchPermissionConfiguration-organizationArns"></a>
The ARN for an AWS Organization that you want to share your AMI with. For more information, see [What is AWS Organizations?](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Pattern: `^arn:aws[^:]*:organizations::[0-9]{12}:organization/o-[a-z0-9]{10,32}$`
Required: No

 ** userGroups **   <a name="imagebuilder-Type-LaunchPermissionConfiguration-userGroups"></a>
The name of the group.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** userIds **   <a name="imagebuilder-Type-LaunchPermissionConfiguration-userIds"></a>
The AWS account ID.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1536 items.
Pattern: `^[0-9]{12}$`
Required: No

## See Also
<a name="API_LaunchPermissionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/LaunchPermissionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/LaunchPermissionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/LaunchPermissionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
