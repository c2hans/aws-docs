---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_CustomSecretConfig.html
---

# CustomSecretConfig
<a name="API_CustomSecretConfig"></a>

Specifies configuration information for a customer-managed Secrets Manager secret where a storage location credentials is stored in Secrets Manager as plain text (for authentication token, secret key, or password) or as binary (for Kerberos keytab). This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret.

**Note**
You can use either `CmkSecretConfig` or `CustomSecretConfig` to provide credentials for a `CreateLocation` request. Do not provide both parameters for the same request.

## Contents
<a name="API_CustomSecretConfig_Contents"></a>

 ** SecretAccessRoleArn **   <a name="DataSync-Type-CustomSecretConfig-SecretAccessRoleArn"></a>
Specifies the ARN for the AWS Identity and Access Management role that DataSync uses to access the secret specified for `SecretArn`.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^(arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/[a-zA-Z0-9+=,.@_/-]+|)$`
Required: No

 ** SecretArn **   <a name="DataSync-Type-CustomSecretConfig-SecretArn"></a>
Specifies the ARN for an AWS Secrets Manager secret.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^(arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):secretsmanager:[a-z\-0-9]+:[0-9]{12}:secret:.*|)$`
Required: No

## See Also
<a name="API_CustomSecretConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/CustomSecretConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/CustomSecretConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/CustomSecretConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
