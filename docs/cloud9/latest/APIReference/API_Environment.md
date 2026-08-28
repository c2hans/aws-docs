---
source_url: https://docs.aws.amazon.com/cloud9/latest/APIReference/API_Environment.html
---

# Environment
<a name="API_Environment"></a>

Information about an AWS Cloud9 development environment.

## Contents
<a name="API_Environment_Contents"></a>

 ** arn **   <a name="cloud9-Type-Environment-arn"></a>
The Amazon Resource Name (ARN) of the environment.
Type: String
Required: Yes

 ** ownerArn **   <a name="cloud9-Type-Environment-ownerArn"></a>
The Amazon Resource Name (ARN) of the environment owner.
Type: String
Required: Yes

 ** type **   <a name="cloud9-Type-Environment-type"></a>
The type of environment. Valid values include the following:
+  `ec2`: An Amazon Elastic Compute Cloud (Amazon EC2) instance connects to the environment.
+  `ssh`: Your own server connects to the environment.
Type: String
Valid Values: `ssh | ec2`
Required: Yes

 ** connectionType **   <a name="cloud9-Type-Environment-connectionType"></a>
The connection type used for connecting to an Amazon EC2 environment. `CONNECT_SSH` is selected by default.
Type: String
Valid Values: `CONNECT_SSH | CONNECT_SSM`
Required: No

 ** description **   <a name="cloud9-Type-Environment-description"></a>
The description for the environment.
Type: String
Length Constraints: Maximum length of 200.
Required: No

 ** id **   <a name="cloud9-Type-Environment-id"></a>
The ID of the environment.
Type: String
Pattern: `^[a-zA-Z0-9]{8,32}$`
Required: No

 ** lifecycle **   <a name="cloud9-Type-Environment-lifecycle"></a>
The state of the environment in its creation or deletion lifecycle.
Type: [EnvironmentLifecycle](API_EnvironmentLifecycle.md) object
Required: No

 ** managedCredentialsStatus **   <a name="cloud9-Type-Environment-managedCredentialsStatus"></a>
Describes the status of AWS managed temporary credentials for the AWS Cloud9 environment. Available values are:
+  `ENABLED_ON_CREATE`
+  `ENABLED_BY_OWNER`
+  `DISABLED_BY_DEFAULT`
+  `DISABLED_BY_OWNER`
+  `DISABLED_BY_COLLABORATOR`
+  `PENDING_REMOVAL_BY_COLLABORATOR`
+  `PENDING_REMOVAL_BY_OWNER`
+  `FAILED_REMOVAL_BY_COLLABORATOR`
+  `ENABLED_BY_OWNER`
+  `DISABLED_BY_DEFAULT`
Type: String
Valid Values: `ENABLED_ON_CREATE | ENABLED_BY_OWNER | DISABLED_BY_DEFAULT | DISABLED_BY_OWNER | DISABLED_BY_COLLABORATOR | PENDING_REMOVAL_BY_COLLABORATOR | PENDING_START_REMOVAL_BY_COLLABORATOR | PENDING_REMOVAL_BY_OWNER | PENDING_START_REMOVAL_BY_OWNER | FAILED_REMOVAL_BY_COLLABORATOR | FAILED_REMOVAL_BY_OWNER`
Required: No

 ** name **   <a name="cloud9-Type-Environment-name"></a>
The name of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Required: No

## See Also
<a name="API_Environment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/Environment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/Environment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/Environment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud9. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud9` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
