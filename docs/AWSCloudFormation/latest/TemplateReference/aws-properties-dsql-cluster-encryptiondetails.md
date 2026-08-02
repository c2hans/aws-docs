---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dsql-cluster-encryptiondetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DSQL::Cluster EncryptionDetails
<a name="aws-properties-dsql-cluster-encryptiondetails"></a>

Configuration details about encryption for the cluster including the AWS KMS key ARN, encryption type, and encryption status.

## Syntax
<a name="aws-properties-dsql-cluster-encryptiondetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dsql-cluster-encryptiondetails-syntax.json"></a>

```
{
  "[EncryptionStatus](#cfn-dsql-cluster-encryptiondetails-encryptionstatus)" : {{String}},
  "[EncryptionType](#cfn-dsql-cluster-encryptiondetails-encryptiontype)" : {{String}},
  "[KmsKeyArn](#cfn-dsql-cluster-encryptiondetails-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-dsql-cluster-encryptiondetails-syntax.yaml"></a>

```
  [EncryptionStatus](#cfn-dsql-cluster-encryptiondetails-encryptionstatus): {{String}}
  [EncryptionType](#cfn-dsql-cluster-encryptiondetails-encryptiontype): {{String}}
  [KmsKeyArn](#cfn-dsql-cluster-encryptiondetails-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-dsql-cluster-encryptiondetails-properties"></a>

`EncryptionStatus`  <a name="cfn-dsql-cluster-encryptiondetails-encryptionstatus"></a>
The status of encryption for the cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionType`  <a name="cfn-dsql-cluster-encryptiondetails-encryptiontype"></a>
The type of encryption that protects the data on your cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-dsql-cluster-encryptiondetails-kmskeyarn"></a>
The ARN of the AWS KMS key that encrypts data in the cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
