---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/secrets-manager.html
---

# AWS Secrets Manager
<a name="secrets-manager"></a>

[AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically. Secrets Manager integrates with AWS KMS to encrypt every version of every secret value with a unique data key that is protected by an AWS KMS key. This integration protects stored secrets with encryption keys that never leave AWS KMS unencrypted. You can also define custom permissions on the KMS key to audit the operations that generate, encrypt, and decrypt the data keys that protect stored secrets. For more information, see [Secret encryption and decryption in AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html).

Consider the following encryption best practices for this service:
+ For most cases, we recommend using the `aws/secretsmanager` AWS managed key to encrypt secrets. There is no cost for using it.
+ To be able to access a secret from another account or to apply a key policy to the encryption key, use a customer managed key to encrypt the secret.
  + In the key policy, assign the value `secretsmanager.<region>.amazonaws.com` to the [kms:ViaService](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms-via-service) condition key. This limits use of the key to only requests from Secrets Manager.
  + To further limit use of the key to only requests from Secrets Manager with the correct context, use keys or values in the [Secrets Manager encryption context](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html#security-encryption-encryption-context) as a condition for using the KMS key by creating:
    + A [string condition operator](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_String) in an IAM policy or key policy
    + A [grant constraint](https://docs.aws.amazon.com/kms/latest/APIReference/API_GrantConstraints.html) in a grant
