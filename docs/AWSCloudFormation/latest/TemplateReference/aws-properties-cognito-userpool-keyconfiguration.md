---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-keyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool KeyConfiguration
<a name="aws-properties-cognito-userpool-keyconfiguration"></a>

<a name="aws-properties-cognito-userpool-keyconfiguration-description"></a>The `KeyConfiguration` property type specifies Property description not available. for an [AWS::Cognito::UserPool](aws-resource-cognito-userpool.md).

## Syntax
<a name="aws-properties-cognito-userpool-keyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-keyconfiguration-syntax.json"></a>

```
{
  "[KeyType](#cfn-cognito-userpool-keyconfiguration-keytype)" : {{String}},
  "[KmsKeyArn](#cfn-cognito-userpool-keyconfiguration-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-keyconfiguration-syntax.yaml"></a>

```
  [KeyType](#cfn-cognito-userpool-keyconfiguration-keytype): {{String}}
  [KmsKeyArn](#cfn-cognito-userpool-keyconfiguration-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpool-keyconfiguration-properties"></a>

`KeyType`  <a name="cfn-cognito-userpool-keyconfiguration-keytype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `AWS_OWNED_KEY | CUSTOMER_MANAGED_KEY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-cognito-userpool-keyconfiguration-kmskeyarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
