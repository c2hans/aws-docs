---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rds-dbcluster-masterusersecret.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBCluster MasterUserSecret
<a name="aws-properties-rds-dbcluster-masterusersecret"></a>

The `MasterUserSecret` return value specifies the secret managed by RDS in AWS Secrets Manager for the master user password.

For more information, see [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide* and [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html) in the *Amazon Aurora User Guide.*

## Syntax
<a name="aws-properties-rds-dbcluster-masterusersecret-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rds-dbcluster-masterusersecret-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-rds-dbcluster-masterusersecret-kmskeyid)" : {{String}},
  "[SecretArn](#cfn-rds-dbcluster-masterusersecret-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-rds-dbcluster-masterusersecret-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-rds-dbcluster-masterusersecret-kmskeyid): {{String}}
  [SecretArn](#cfn-rds-dbcluster-masterusersecret-secretarn): {{String}}
```

## Properties
<a name="aws-properties-rds-dbcluster-masterusersecret-properties"></a>

`KmsKeyId`  <a name="cfn-rds-dbcluster-masterusersecret-kmskeyid"></a>
The AWS KMS key identifier that is used to encrypt the secret.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArn`  <a name="cfn-rds-dbcluster-masterusersecret-secretarn"></a>
The Amazon Resource Name (ARN) of the secret. This parameter is a return value that you can retrieve using the `Fn::GetAtt` intrinsic function. For more information, see [Return values](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#aws-resource-rds-dbcluster-return-values).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
