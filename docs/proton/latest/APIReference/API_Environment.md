---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_Environment.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# Environment
<a name="API_Environment"></a>

Detailed data of an AWS Proton environment resource. An AWS Proton environment is a set of resources shared across AWS Proton services.

## Contents
<a name="API_Environment_Contents"></a>

 ** arn **   <a name="proton-Type-Environment-arn"></a>
The Amazon Resource Name (ARN) of the environment.
Type: String
Required: Yes

 ** createdAt **   <a name="proton-Type-Environment-createdAt"></a>
The time when the environment was created.
Type: Timestamp
Required: Yes

 ** deploymentStatus **   <a name="proton-Type-Environment-deploymentStatus"></a>
The environment deployment status.
Type: String
Valid Values: `IN_PROGRESS | FAILED | SUCCEEDED | DELETE_IN_PROGRESS | DELETE_FAILED | DELETE_COMPLETE | CANCELLING | CANCELLED`
Required: Yes

 ** lastDeploymentAttemptedAt **   <a name="proton-Type-Environment-lastDeploymentAttemptedAt"></a>
The time when a deployment of the environment was last attempted.
Type: Timestamp
Required: Yes

 ** lastDeploymentSucceededAt **   <a name="proton-Type-Environment-lastDeploymentSucceededAt"></a>
The time when the environment was last deployed successfully.
Type: Timestamp
Required: Yes

 ** name **   <a name="proton-Type-Environment-name"></a>
The name of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** templateMajorVersion **   <a name="proton-Type-Environment-templateMajorVersion"></a>
The major version of the environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** templateMinorVersion **   <a name="proton-Type-Environment-templateMinorVersion"></a>
The minor version of the environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** templateName **   <a name="proton-Type-Environment-templateName"></a>
The Amazon Resource Name (ARN) of the environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** codebuildRoleArn **   <a name="proton-Type-Environment-codebuildRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role that allows AWS Proton to provision infrastructure using CodeBuild-based provisioning on your behalf.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})`
Required: No

 ** componentRoleArn **   <a name="proton-Type-Environment-componentRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role that AWS Proton uses when provisioning directly defined components in this environment. It determines the scope of infrastructure that a component can provision.
The environment must have a `componentRoleArn` to allow directly defined components to be associated with the environment.
For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})`
Required: No

 ** deploymentStatusMessage **   <a name="proton-Type-Environment-deploymentStatusMessage"></a>
An environment deployment status message.
Type: String
Required: No

 ** description **   <a name="proton-Type-Environment-description"></a>
The description of the environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** environmentAccountConnectionId **   <a name="proton-Type-Environment-environmentAccountConnectionId"></a>
The ID of the environment account connection that's used to provision infrastructure resources in an environment account.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** environmentAccountId **   <a name="proton-Type-Environment-environmentAccountId"></a>
The ID of the environment account that the environment infrastructure resources are provisioned in.
Type: String
Pattern: `\d{12}`
Required: No

 ** lastAttemptedDeploymentId **   <a name="proton-Type-Environment-lastAttemptedDeploymentId"></a>
The ID of the last attempted deployment of this environment.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** lastSucceededDeploymentId **   <a name="proton-Type-Environment-lastSucceededDeploymentId"></a>
The ID of the last successful deployment of this environment.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** protonServiceRoleArn **   <a name="proton-Type-Environment-protonServiceRoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Proton service role that allows AWS Proton to make calls to other services on your behalf.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:([\w+=,.@-]+[/:])*[\w+=,.@-]+`
Required: No

 ** provisioning **   <a name="proton-Type-Environment-provisioning"></a>
When included, indicates that the environment template is for customer provisioned and managed infrastructure.
Type: String
Valid Values: `CUSTOMER_MANAGED`
Required: No

 ** provisioningRepository **   <a name="proton-Type-Environment-provisioningRepository"></a>
The linked repository that you use to host your rendered infrastructure templates for self-managed provisioning. A linked repository is a repository that has been registered with AWS Proton. For more information, see [CreateRepository](https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateRepository.html).
Type: [RepositoryBranch](API_RepositoryBranch.md) object
Required: No

 ** spec **   <a name="proton-Type-Environment-spec"></a>
The environment spec.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

## See Also
<a name="API_Environment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/Environment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/Environment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/Environment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
