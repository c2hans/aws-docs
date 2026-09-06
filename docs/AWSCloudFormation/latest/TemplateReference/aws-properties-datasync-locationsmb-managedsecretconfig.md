---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationsmb-managedsecretconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationSMB ManagedSecretConfig
<a name="aws-properties-datasync-locationsmb-managedsecretconfig"></a>

Specifies configuration information for a DataSync-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location. DataSync uses the default AWS-managed KMS key to encrypt this secret in AWS Secrets Manager.

## Syntax
<a name="aws-properties-datasync-locationsmb-managedsecretconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationsmb-managedsecretconfig-syntax.json"></a>

```
{
  "[SecretArn](#cfn-datasync-locationsmb-managedsecretconfig-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-locationsmb-managedsecretconfig-syntax.yaml"></a>

```
  [SecretArn](#cfn-datasync-locationsmb-managedsecretconfig-secretarn): {{String}}
```

## Properties
<a name="aws-properties-datasync-locationsmb-managedsecretconfig-properties"></a>

`SecretArn`  <a name="cfn-datasync-locationsmb-managedsecretconfig-secretarn"></a>
Specifies the ARN for an AWS Secrets Manager secret.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):secretsmanager:[a-z-0-9]+:[0-9]{12}:secret:.*|)$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
