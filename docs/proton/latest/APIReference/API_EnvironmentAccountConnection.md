---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_EnvironmentAccountConnection.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# EnvironmentAccountConnection
<a name="API_EnvironmentAccountConnection"></a>

Detailed data of an AWS Proton environment account connection resource.

## Contents
<a name="API_EnvironmentAccountConnection_Contents"></a>

 ** arn **   <a name="proton-Type-EnvironmentAccountConnection-arn"></a>
The Amazon Resource Name (ARN) of the environment account connection.
Type: String
Required: Yes

 ** environmentAccountId **   <a name="proton-Type-EnvironmentAccountConnection-environmentAccountId"></a>
The environment account that's connected to the environment account connection.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** environmentName **   <a name="proton-Type-EnvironmentAccountConnection-environmentName"></a>
The name of the environment that's associated with the environment account connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** id **   <a name="proton-Type-EnvironmentAccountConnection-id"></a>
The ID of the environment account connection.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** lastModifiedAt **   <a name="proton-Type-EnvironmentAccountConnection-lastModifiedAt"></a>
The time when the environment account connection was last modified.
Type: Timestamp
Required: Yes

 ** managementAccountId **   <a name="proton-Type-EnvironmentAccountConnection-managementAccountId"></a>
The ID of the management account that's connected to the environment account connection.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** requestedAt **   <a name="proton-Type-EnvironmentAccountConnection-requestedAt"></a>
The time when the environment account connection request was made.
Type: Timestamp
Required: Yes

 ** roleArn **   <a name="proton-Type-EnvironmentAccountConnection-roleArn"></a>
The IAM service role that's associated with the environment account connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:([\w+=,.@-]+[/:])*[\w+=,.@-]+`
Required: Yes

 ** status **   <a name="proton-Type-EnvironmentAccountConnection-status"></a>
The status of the environment account connection.
Type: String
Valid Values: `PENDING | CONNECTED | REJECTED`
Required: Yes

 ** codebuildRoleArn **   <a name="proton-Type-EnvironmentAccountConnection-codebuildRoleArn"></a>
The Amazon Resource Name (ARN) of an IAM service role in the environment account. AWS Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})`
Required: No

 ** componentRoleArn **   <a name="proton-Type-EnvironmentAccountConnection-componentRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role that AWS Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.
The environment account connection must have a `componentRoleArn` to allow directly defined components to be associated with any environments running in the account.
For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})`
Required: No

## See Also
<a name="API_EnvironmentAccountConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/EnvironmentAccountConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/EnvironmentAccountConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/EnvironmentAccountConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
