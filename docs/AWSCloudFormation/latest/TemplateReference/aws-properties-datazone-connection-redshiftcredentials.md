---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-redshiftcredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection RedshiftCredentials
<a name="aws-properties-datazone-connection-redshiftcredentials"></a>

Amazon Redshift credentials of a connection.

## Syntax
<a name="aws-properties-datazone-connection-redshiftcredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-redshiftcredentials-syntax.json"></a>

```
{
  "[SecretArn](#cfn-datazone-connection-redshiftcredentials-secretarn)" : {{String}},
  "[UsernamePassword](#cfn-datazone-connection-redshiftcredentials-usernamepassword)" : {{UsernamePassword}}
}
```

### YAML
<a name="aws-properties-datazone-connection-redshiftcredentials-syntax.yaml"></a>

```
  [SecretArn](#cfn-datazone-connection-redshiftcredentials-secretarn): {{String}}
  [UsernamePassword](#cfn-datazone-connection-redshiftcredentials-usernamepassword): {{
    UsernamePassword}}
```

## Properties
<a name="aws-properties-datazone-connection-redshiftcredentials-properties"></a>

`SecretArn`  <a name="cfn-datazone-connection-redshiftcredentials-secretarn"></a>
The secret ARN of the Amazon Redshift credentials of a connection.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:secretsmanager:[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]:\d{12}:secret:.*$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UsernamePassword`  <a name="cfn-datazone-connection-redshiftcredentials-usernamepassword"></a>
The username and password of the Amazon Redshift credentials of a connection.
*Required*: No
*Type*: [UsernamePassword](aws-properties-datazone-connection-usernamepassword.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
