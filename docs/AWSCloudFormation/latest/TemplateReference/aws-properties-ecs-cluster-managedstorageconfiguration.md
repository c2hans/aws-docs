---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-cluster-managedstorageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Cluster ManagedStorageConfiguration
<a name="aws-properties-ecs-cluster-managedstorageconfiguration"></a>

The managed storage configuration for the cluster.

## Syntax
<a name="aws-properties-ecs-cluster-managedstorageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-cluster-managedstorageconfiguration-syntax.json"></a>

```
{
  "[FargateEphemeralStorageKmsKeyId](#cfn-ecs-cluster-managedstorageconfiguration-fargateephemeralstoragekmskeyid)" : {{String}},
  "[KmsKeyId](#cfn-ecs-cluster-managedstorageconfiguration-kmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-cluster-managedstorageconfiguration-syntax.yaml"></a>

```
  [FargateEphemeralStorageKmsKeyId](#cfn-ecs-cluster-managedstorageconfiguration-fargateephemeralstoragekmskeyid): {{String}}
  [KmsKeyId](#cfn-ecs-cluster-managedstorageconfiguration-kmskeyid): {{String}}
```

## Properties
<a name="aws-properties-ecs-cluster-managedstorageconfiguration-properties"></a>

`FargateEphemeralStorageKmsKeyId`  <a name="cfn-ecs-cluster-managedstorageconfiguration-fargateephemeralstoragekmskeyid"></a>
Specify the AWS Key Management Service key ID for Fargate ephemeral storage.
When you specify a `fargateEphemeralStorageKmsKeyId`, AWS Fargate uses the key to encrypt data at rest in ephemeral storage. For more information about Fargate ephemeral storage encryption, see [Customer managed keys for AWS Fargate ephemeral storage for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-storage-encryption.html) in the *Amazon Elastic Container Service Developer Guide*.
The key must be a single Region key.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-ecs-cluster-managedstorageconfiguration-kmskeyid"></a>
Specify a AWS Key Management Service key ID to encrypt Amazon ECS managed storage.
 When you specify a `kmsKeyId`, Amazon ECS uses the key to encrypt data volumes managed by Amazon ECS that are attached to tasks in the cluster. The following data volumes are managed by Amazon ECS: Amazon EBS. For more information about encryption of Amazon EBS volumes attached to Amazon ECS tasks, see [Encrypt data stored in Amazon EBS volumes for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-kms-encryption.html) in the *Amazon Elastic Container Service Developer Guide*.
The key must be a single Region key.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
