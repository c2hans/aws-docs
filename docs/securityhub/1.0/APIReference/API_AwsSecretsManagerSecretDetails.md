---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSecretsManagerSecretDetails.html
---

# AwsSecretsManagerSecretDetails
<a name="API_AwsSecretsManagerSecretDetails"></a>

Details about an AWS Secrets Manager secret.

## Contents
<a name="API_AwsSecretsManagerSecretDetails_Contents"></a>

 ** Deleted **   <a name="securityhub-Type-AwsSecretsManagerSecretDetails-Deleted"></a>
Whether the secret is deleted.
Type: Boolean
Required: No

 ** Description **   <a name="securityhub-Type-AwsSecretsManagerSecretDetails-Description"></a>
The user-provided description of the secret.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KmsKeyId **   <a name="securityhub-Type-AwsSecretsManagerSecretDetails-KmsKeyId"></a>
The ARN, Key ID, or alias of the AWS KMS key used to encrypt the `SecretString` or `SecretBinary` values for versions of this secret.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-AwsSecretsManagerSecretDetails-Name"></a>
The name of the secret.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RotationEnabled **   <a name="securityhub-Type-AwsSecretsManagerSecretDetails-RotationEnabled"></a>
Whether rotation is enabled.
Type: Boolean
Required: No

 ** RotationLambdaArn **   <a name="securityhub-Type-AwsSecretsManagerSecretDetails-RotationLambdaArn"></a>
The ARN of the Lambda function that rotates the secret.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RotationOccurredWithinFrequency **   <a name="securityhub-Type-AwsSecretsManagerSecretDetails-RotationOccurredWithinFrequency"></a>
Whether the rotation occurred within the specified rotation frequency.
Type: Boolean
Required: No

 ** RotationRules **   <a name="securityhub-Type-AwsSecretsManagerSecretDetails-RotationRules"></a>
Defines the rotation schedule for the secret.
Type: [AwsSecretsManagerSecretRotationRules](API_AwsSecretsManagerSecretRotationRules.md) object
Required: No

## See Also
<a name="API_AwsSecretsManagerSecretDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsSecretsManagerSecretDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsSecretsManagerSecretDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsSecretsManagerSecretDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
