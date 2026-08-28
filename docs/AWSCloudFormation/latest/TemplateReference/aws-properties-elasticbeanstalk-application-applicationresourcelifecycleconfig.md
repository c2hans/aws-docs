---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticBeanstalk::Application ApplicationResourceLifecycleConfig
<a name="aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig"></a>

The resource lifecycle configuration for an application. Defines lifecycle settings for resources that belong to the application, and the service role that Elastic Beanstalk assumes in order to apply lifecycle settings. The version lifecycle configuration defines lifecycle settings for application versions.

`ApplicationResourceLifecycleConfig` is a property of the [AWS::ElasticBeanstalk::Application](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html) resource.

## Syntax
<a name="aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig-syntax.json"></a>

```
{
  "[ServiceRole](#cfn-elasticbeanstalk-application-applicationresourcelifecycleconfig-servicerole)" : {{String}},
  "[VersionLifecycleConfig](#cfn-elasticbeanstalk-application-applicationresourcelifecycleconfig-versionlifecycleconfig)" : {{ApplicationVersionLifecycleConfig}}
}
```

### YAML
<a name="aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig-syntax.yaml"></a>

```
  [ServiceRole](#cfn-elasticbeanstalk-application-applicationresourcelifecycleconfig-servicerole): {{String}}
  [VersionLifecycleConfig](#cfn-elasticbeanstalk-application-applicationresourcelifecycleconfig-versionlifecycleconfig): {{
    ApplicationVersionLifecycleConfig}}
```

## Properties
<a name="aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig-properties"></a>

`ServiceRole`  <a name="cfn-elasticbeanstalk-application-applicationresourcelifecycleconfig-servicerole"></a>
The ARN of an IAM service role that Elastic Beanstalk has permission to assume.
The `ServiceRole` property is required the first time that you provide a `ResourceLifecycleConfig` for the application. After you provide it once, Elastic Beanstalk persists the Service Role with the application, and you don't need to specify it again. You can, however, specify it in subsequent updates to change the Service Role to another value.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionLifecycleConfig`  <a name="cfn-elasticbeanstalk-application-applicationresourcelifecycleconfig-versionlifecycleconfig"></a>
Defines lifecycle settings for application versions.
*Required*: No
*Type*: [ApplicationVersionLifecycleConfig](aws-properties-elasticbeanstalk-application-applicationversionlifecycleconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
