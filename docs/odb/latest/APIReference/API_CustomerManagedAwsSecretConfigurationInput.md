---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CustomerManagedAwsSecretConfigurationInput.html
---

# CustomerManagedAwsSecretConfigurationInput
<a name="API_CustomerManagedAwsSecretConfigurationInput"></a>

The input configuration for a customer-managed AWS Secrets Manager secret used to supply a password.

## Contents
<a name="API_CustomerManagedAwsSecretConfigurationInput_Contents"></a>

 ** externalIdType **   <a name="odb-Type-CustomerManagedAwsSecretConfigurationInput-externalIdType"></a>
The type of Oracle Cloud Identifier (OCID) used as the external ID when assuming the IAM role.
The valid values depend on the operation. For the `CreateAutonomousDatabase` operation, only `compartment_ocid` and `tenant_ocid` are allowed. For the `UpdateAutonomousDatabase` and `CreateAutonomousDatabaseWallet` operations, `database_ocid`, `compartment_ocid`, and `tenant_ocid` are all allowed.
Type: String
Valid Values: `database_ocid | compartment_ocid | tenant_ocid`
Required: No

 ** iamRoleArn **   <a name="odb-Type-CustomerManagedAwsSecretConfigurationInput-iamRoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that OCI assumes to retrieve the secret value.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{12}:role/.+`
Required: No

 ** secretId **   <a name="odb-Type-CustomerManagedAwsSecretConfigurationInput-secretId"></a>
The identifier or ARN of the AWS Secrets Manager secret that contains the password.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_CustomerManagedAwsSecretConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CustomerManagedAwsSecretConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CustomerManagedAwsSecretConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CustomerManagedAwsSecretConfigurationInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
