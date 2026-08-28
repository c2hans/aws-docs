---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-ssmassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Instance SsmAssociation
<a name="aws-properties-ec2-instance-ssmassociation"></a>

Specifies the SSM document and parameter values in AWS Systems Manager to associate with an instance.

`SsmAssociations` is a property of the [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) resource.

## Syntax
<a name="aws-properties-ec2-instance-ssmassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instance-ssmassociation-syntax.json"></a>

```
{
  "[AssociationParameters](#cfn-ec2-instance-ssmassociation-associationparameters)" : {{[ AssociationParameter, ... ]}},
  "[DocumentName](#cfn-ec2-instance-ssmassociation-documentname)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-instance-ssmassociation-syntax.yaml"></a>

```
  [AssociationParameters](#cfn-ec2-instance-ssmassociation-associationparameters): {{
    - AssociationParameter}}
  [DocumentName](#cfn-ec2-instance-ssmassociation-documentname): {{String}}
```

## Properties
<a name="aws-properties-ec2-instance-ssmassociation-properties"></a>

`AssociationParameters`  <a name="cfn-ec2-instance-ssmassociation-associationparameters"></a>
The input parameter values to use with the associated SSM document.
*Required*: No
*Type*: Array of [AssociationParameter](aws-properties-ec2-instance-associationparameter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DocumentName`  <a name="cfn-ec2-instance-ssmassociation-documentname"></a>
The name of an SSM document to associate with the instance.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
