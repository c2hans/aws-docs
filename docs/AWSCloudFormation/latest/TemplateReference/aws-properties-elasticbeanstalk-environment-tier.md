---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticbeanstalk-environment-tier.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticBeanstalk::Environment Tier
<a name="aws-properties-elasticbeanstalk-environment-tier"></a>

Describes the environment tier for an [AWS::ElasticBeanstalk::Environment](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html) resource. For more information, see [Environment Tiers](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features-managing-env-tiers.html) in the *AWS Elastic Beanstalk Developer Guide*.

## Syntax
<a name="aws-properties-elasticbeanstalk-environment-tier-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticbeanstalk-environment-tier-syntax.json"></a>

```
{
  "[Name](#cfn-elasticbeanstalk-environment-tier-name)" : {{String}},
  "[Type](#cfn-elasticbeanstalk-environment-tier-type)" : {{String}},
  "[Version](#cfn-elasticbeanstalk-environment-tier-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticbeanstalk-environment-tier-syntax.yaml"></a>

```
  [Name](#cfn-elasticbeanstalk-environment-tier-name): {{String}}
  [Type](#cfn-elasticbeanstalk-environment-tier-type): {{String}}
  [Version](#cfn-elasticbeanstalk-environment-tier-version): {{String}}
```

## Properties
<a name="aws-properties-elasticbeanstalk-environment-tier-properties"></a>

`Name`  <a name="cfn-elasticbeanstalk-environment-tier-name"></a>
The name of this environment tier.
Valid values:
+ For *Web server tier* – `WebServer`
+ For *Worker tier* – `Worker`
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-elasticbeanstalk-environment-tier-type"></a>
The type of this environment tier.
Valid values:
+ For *Web server tier* – `Standard`
+ For *Worker tier* – `SQS/HTTP`
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Version`  <a name="cfn-elasticbeanstalk-environment-tier-version"></a>
The version of this environment tier. When you don't set a value to it, Elastic Beanstalk uses the latest compatible worker tier version.
This member is deprecated. Any specific version that you set may become out of date. We recommend leaving it unspecified.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
