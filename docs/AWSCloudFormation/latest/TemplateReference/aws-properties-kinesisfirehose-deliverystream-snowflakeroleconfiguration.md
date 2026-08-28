---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-snowflakeroleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream SnowflakeRoleConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakeroleconfiguration"></a>

Optionally configure a Snowflake role. Otherwise the default user role will be used.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakeroleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakeroleconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-kinesisfirehose-deliverystream-snowflakeroleconfiguration-enabled)" : {{Boolean}},
  "[SnowflakeRole](#cfn-kinesisfirehose-deliverystream-snowflakeroleconfiguration-snowflakerole)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakeroleconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-kinesisfirehose-deliverystream-snowflakeroleconfiguration-enabled): {{Boolean}}
  [SnowflakeRole](#cfn-kinesisfirehose-deliverystream-snowflakeroleconfiguration-snowflakerole): {{String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakeroleconfiguration-properties"></a>

`Enabled`  <a name="cfn-kinesisfirehose-deliverystream-snowflakeroleconfiguration-enabled"></a>
Enable Snowflake role
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnowflakeRole`  <a name="cfn-kinesisfirehose-deliverystream-snowflakeroleconfiguration-snowflakerole"></a>
The Snowflake role you wish to configure
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
