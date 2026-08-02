---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CustomerManagedAwsSecretConfiguration.html
---

# CustomerManagedAwsSecretConfiguration
<a name="API_CustomerManagedAwsSecretConfiguration"></a>

The configuration of a customer-managed AWS Secrets Manager secret used to supply a password.

## Contents
<a name="API_CustomerManagedAwsSecretConfiguration_Contents"></a>

 ** externalIdType **   <a name="odb-Type-CustomerManagedAwsSecretConfiguration-externalIdType"></a>
The type of Oracle Cloud Identifier (OCID) used as the external ID when assuming the IAM role.
Type: String
Valid Values: `database_ocid | compartment_ocid | tenant_ocid`
Required: No

 ** iamRoleArn **   <a name="odb-Type-CustomerManagedAwsSecretConfiguration-iamRoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that OCI assumes to retrieve the secret value.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{12}:role/.+`
Required: No

 ** secretId **   <a name="odb-Type-CustomerManagedAwsSecretConfiguration-secretId"></a>
The identifier or ARN of the AWS Secrets Manager secret that contains the password.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_CustomerManagedAwsSecretConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CustomerManagedAwsSecretConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CustomerManagedAwsSecretConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CustomerManagedAwsSecretConfiguration)
