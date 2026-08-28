---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-snowflakevpcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream SnowflakeVpcConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakevpcconfiguration"></a>

Configure a Snowflake VPC

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakevpcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakevpcconfiguration-syntax.json"></a>

```
{
  "[PrivateLinkVpceId](#cfn-kinesisfirehose-deliverystream-snowflakevpcconfiguration-privatelinkvpceid)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakevpcconfiguration-syntax.yaml"></a>

```
  [PrivateLinkVpceId](#cfn-kinesisfirehose-deliverystream-snowflakevpcconfiguration-privatelinkvpceid): {{String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakevpcconfiguration-properties"></a>

`PrivateLinkVpceId`  <a name="cfn-kinesisfirehose-deliverystream-snowflakevpcconfiguration-privatelinkvpceid"></a>
The VPCE ID for Firehose to privately connect with Snowflake. The ID format is com.amazonaws.vpce.[region].vpce-svc-<[id]>. For more information, see [Amazon PrivateLink & Snowflake](https://docs.snowflake.com/en/user-guide/admin-security-privatelink)
*Required*: Yes
*Type*: String
*Pattern*: `([a-zA-Z0-9\-\_]+\.){2,3}vpce\.[a-zA-Z0-9\-]*\.vpce-svc\-[a-zA-Z0-9\-]{17}$`
*Minimum*: `47`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
