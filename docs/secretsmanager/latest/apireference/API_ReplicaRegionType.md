---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ReplicaRegionType.html
---

# ReplicaRegionType
<a name="API_ReplicaRegionType"></a>

A custom type that specifies a `Region` and the `KmsKeyId` for a replica secret.

## Contents
<a name="API_ReplicaRegionType_Contents"></a>

 ** KmsKeyId **   <a name="SecretsManager-Type-ReplicaRegionType-KmsKeyId"></a>
The ARN, key ID, or alias of the KMS key to encrypt the secret. If you don't include this field, Secrets Manager uses `aws/secretsmanager`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** Region **   <a name="SecretsManager-Type-ReplicaRegionType-Region"></a>
A Region code. For a list of Region codes, see [Name and code of Regions](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([a-z]+-)+\d+$`
Required: No

## See Also
<a name="API_ReplicaRegionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/ReplicaRegionType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/ReplicaRegionType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/ReplicaRegionType)
