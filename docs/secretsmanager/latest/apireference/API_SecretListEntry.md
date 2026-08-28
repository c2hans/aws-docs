---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_SecretListEntry.html
---

# SecretListEntry
<a name="API_SecretListEntry"></a>

A structure that contains the details about a secret. It does not include the encrypted `SecretString` and `SecretBinary` values. To get those values, use [GetSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html) .

## Contents
<a name="API_SecretListEntry_Contents"></a>

 ** ARN **   <a name="SecretsManager-Type-SecretListEntry-ARN"></a>
The Amazon Resource Name (ARN) of the secret.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** CreatedDate **   <a name="SecretsManager-Type-SecretListEntry-CreatedDate"></a>
The date and time when a secret was created.
Type: Timestamp
Required: No

 ** DeletedDate **   <a name="SecretsManager-Type-SecretListEntry-DeletedDate"></a>
The date and time the deletion of the secret occurred. Not present on active secrets. The secret can be recovered until the number of days in the recovery window has passed, as specified in the `RecoveryWindowInDays` parameter of the [`DeleteSecret`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DeleteSecret.html) operation.
Type: Timestamp
Required: No

 ** Description **   <a name="SecretsManager-Type-SecretListEntry-Description"></a>
The user-provided description of the secret.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** ExternalSecretRotationMetadata **   <a name="SecretsManager-Type-SecretListEntry-ExternalSecretRotationMetadata"></a>
The metadata needed to successfully rotate a managed external secret. A list of key value pairs in JSON format specified by the partner. For more information about the required information, see [Managed external secrets partners](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html).
Type: Array of [ExternalSecretRotationMetadataItem](API_ExternalSecretRotationMetadataItem.md) objects
Required: No

 ** ExternalSecretRotationRoleArn **   <a name="SecretsManager-Type-SecretListEntry-ExternalSecretRotationRoleArn"></a>
The role that Secrets Manager assumes to call APIs required to perform the rotation. For more information about the required information, see [Managed external secrets partners](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** KmsKeyId **   <a name="SecretsManager-Type-SecretListEntry-KmsKeyId"></a>
The ARN of the AWS KMS key that Secrets Manager uses to encrypt the secret value. If the secret is encrypted with the AWS managed key `aws/secretsmanager`, this field is omitted.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** LastAccessedDate **   <a name="SecretsManager-Type-SecretListEntry-LastAccessedDate"></a>
The date that the secret was last accessed in the Region. This field is omitted if the secret has never been retrieved in the Region.
Type: Timestamp
Required: No

 ** LastChangedDate **   <a name="SecretsManager-Type-SecretListEntry-LastChangedDate"></a>
The last date and time that this secret was modified in any way.
Type: Timestamp
Required: No

 ** LastRotatedDate **   <a name="SecretsManager-Type-SecretListEntry-LastRotatedDate"></a>
The most recent date and time that the Secrets Manager rotation process was successfully completed. This value is null if the secret hasn't ever rotated.
Type: Timestamp
Required: No

 ** Name **   <a name="SecretsManager-Type-SecretListEntry-Name"></a>
The friendly name of the secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** NextRotationDate **   <a name="SecretsManager-Type-SecretListEntry-NextRotationDate"></a>
The next rotation is scheduled to occur on or before this date. If the secret isn't configured for rotation or rotation has been disabled, Secrets Manager returns null.
Type: Timestamp
Required: No

 ** OwningService **   <a name="SecretsManager-Type-SecretListEntry-OwningService"></a>
Returns the name of the service that created the secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** PrimaryRegion **   <a name="SecretsManager-Type-SecretListEntry-PrimaryRegion"></a>
The Region where Secrets Manager originated the secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([a-z]+-)+\d+$`
Required: No

 ** RotationEnabled **   <a name="SecretsManager-Type-SecretListEntry-RotationEnabled"></a>
Indicates whether automatic, scheduled rotation is enabled for this secret.
Type: Boolean
Required: No

 ** RotationLambdaARN **   <a name="SecretsManager-Type-SecretListEntry-RotationLambdaARN"></a>
The ARN of an AWS Lambda function invoked by Secrets Manager to rotate and expire the secret either automatically per the schedule or manually by a call to [`RotateSecret`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** RotationRules **   <a name="SecretsManager-Type-SecretListEntry-RotationRules"></a>
A structure that defines the rotation configuration for the secret.
Type: [RotationRulesType](API_RotationRulesType.md) object
Required: No

 ** SecretVersionsToStages **   <a name="SecretsManager-Type-SecretListEntry-SecretVersionsToStages"></a>
A list of all of the currently assigned `SecretVersionStage` staging labels and the `SecretVersionId` attached to each one. Staging labels are used to keep track of the different versions during the rotation process.
A version that does not have any `SecretVersionStage` is considered deprecated and subject to deletion. Such versions are not included in this list.
Type: String to array of strings map
Key Length Constraints: Minimum length of 32. Maximum length of 64.
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Tags **   <a name="SecretsManager-Type-SecretListEntry-Tags"></a>
The list of user-defined tags associated with the secret. To add tags to a secret, use [`TagResource`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_TagResource.html). To remove tags, use [`UntagResource`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_UntagResource.html).
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** Type **   <a name="SecretsManager-Type-SecretListEntry-Type"></a>
The exact string that identifies the third-party partner that holds the external secret. For more information, see [Managed external secret partners](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_SecretListEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/SecretListEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/SecretListEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/SecretListEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
