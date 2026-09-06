---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedStorageConfiguration.html
---

# ManagedStorageConfiguration
<a name="API_ManagedStorageConfiguration"></a>

The managed storage configuration for the cluster.

## Contents
<a name="API_ManagedStorageConfiguration_Contents"></a>

 ** fargateEphemeralStorageKmsKeyId **   <a name="ECS-Type-ManagedStorageConfiguration-fargateEphemeralStorageKmsKeyId"></a>
Specify the AWS Key Management Service key ID for Fargate ephemeral storage.
When you specify a `fargateEphemeralStorageKmsKeyId`, AWS Fargate uses the key to encrypt data at rest in ephemeral storage. For more information about Fargate ephemeral storage encryption, see [Customer managed keys for AWS Fargate ephemeral storage for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-storage-encryption.html) in the *Amazon Elastic Container Service Developer Guide*.
The key must be a single Region key.
Type: String
Required: No

 ** kmsKeyId **   <a name="ECS-Type-ManagedStorageConfiguration-kmsKeyId"></a>
Specify a AWS Key Management Service key ID to encrypt Amazon ECS managed storage.
 When you specify a `kmsKeyId`, Amazon ECS uses the key to encrypt data volumes managed by Amazon ECS that are attached to tasks in the cluster. The following data volumes are managed by Amazon ECS: Amazon EBS. For more information about encryption of Amazon EBS volumes attached to Amazon ECS tasks, see [Encrypt data stored in Amazon EBS volumes for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-kms-encryption.html) in the *Amazon Elastic Container Service Developer Guide*.
The key must be a single Region key.
Type: String
Required: No

## See Also
<a name="API_ManagedStorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedStorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedStorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedStorageConfiguration)
