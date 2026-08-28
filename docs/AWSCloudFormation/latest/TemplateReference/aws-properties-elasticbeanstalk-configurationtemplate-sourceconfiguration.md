---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticBeanstalk::ConfigurationTemplate SourceConfiguration
<a name="aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration"></a>

An AWS Elastic Beanstalk configuration template to base a new one on. You can use it to define a [AWS::ElasticBeanstalk::ConfigurationTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-beanstalk-configurationtemplate.html) resource.

## Syntax
<a name="aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration-syntax.json"></a>

```
{
  "[ApplicationName](#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration-applicationname)" : {{String}},
  "[TemplateName](#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration-templatename)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration-syntax.yaml"></a>

```
  [ApplicationName](#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration-applicationname): {{String}}
  [TemplateName](#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration-templatename): {{String}}
```

## Properties
<a name="aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration-properties"></a>

`ApplicationName`  <a name="cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration-applicationname"></a>
The name of the application associated with the configuration.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TemplateName`  <a name="cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration-templatename"></a>
The name of the configuration template.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
