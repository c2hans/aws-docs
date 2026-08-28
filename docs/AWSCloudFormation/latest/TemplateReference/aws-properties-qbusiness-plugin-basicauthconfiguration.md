---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-plugin-basicauthconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Plugin BasicAuthConfiguration
<a name="aws-properties-qbusiness-plugin-basicauthconfiguration"></a>

Information about the basic authentication credentials used to configure a plugin.

## Syntax
<a name="aws-properties-qbusiness-plugin-basicauthconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-plugin-basicauthconfiguration-syntax.json"></a>

```
{
  "[RoleArn](#cfn-qbusiness-plugin-basicauthconfiguration-rolearn)" : {{String}},
  "[SecretArn](#cfn-qbusiness-plugin-basicauthconfiguration-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-plugin-basicauthconfiguration-syntax.yaml"></a>

```
  [RoleArn](#cfn-qbusiness-plugin-basicauthconfiguration-rolearn): {{String}}
  [SecretArn](#cfn-qbusiness-plugin-basicauthconfiguration-secretarn): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-plugin-basicauthconfiguration-properties"></a>

`RoleArn`  <a name="cfn-qbusiness-plugin-basicauthconfiguration-rolearn"></a>
The ARN of an IAM role used by Amazon Q Business to access the basic authentication credentials stored in a Secrets Manager secret.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}$`
*Minimum*: `0`
*Maximum*: `1284`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArn`  <a name="cfn-qbusiness-plugin-basicauthconfiguration-secretarn"></a>
The ARN of the Secrets Manager secret that stores the basic authentication credentials used for plugin configuration..
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}$`
*Minimum*: `0`
*Maximum*: `1284`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
