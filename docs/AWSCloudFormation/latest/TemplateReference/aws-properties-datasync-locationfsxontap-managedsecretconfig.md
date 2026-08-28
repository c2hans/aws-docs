---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationfsxontap-managedsecretconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationFSxONTAP ManagedSecretConfig
<a name="aws-properties-datasync-locationfsxontap-managedsecretconfig"></a>

Specifies configuration information for a DataSync-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location. DataSync uses the default AWS-managed KMS key to encrypt this secret in AWS Secrets Manager.

## Syntax
<a name="aws-properties-datasync-locationfsxontap-managedsecretconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationfsxontap-managedsecretconfig-syntax.json"></a>

```
{
  "[SecretArn](#cfn-datasync-locationfsxontap-managedsecretconfig-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-locationfsxontap-managedsecretconfig-syntax.yaml"></a>

```
  [SecretArn](#cfn-datasync-locationfsxontap-managedsecretconfig-secretarn): {{String}}
```

## Properties
<a name="aws-properties-datasync-locationfsxontap-managedsecretconfig-properties"></a>

`SecretArn`  <a name="cfn-datasync-locationfsxontap-managedsecretconfig-secretarn"></a>
Specifies the ARN for an AWS Secrets Manager secret.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):secretsmanager:[a-z-0-9]+:[0-9]{12}:secret:.*|)$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
