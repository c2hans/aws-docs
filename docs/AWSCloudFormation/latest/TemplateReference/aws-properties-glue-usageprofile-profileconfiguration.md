---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-usageprofile-profileconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::UsageProfile ProfileConfiguration
<a name="aws-properties-glue-usageprofile-profileconfiguration"></a>

Specifies the job and session values that an admin configures in an AWS Glue usage profile.

## Syntax
<a name="aws-properties-glue-usageprofile-profileconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-usageprofile-profileconfiguration-syntax.json"></a>

```
{
  "[JobConfiguration](#cfn-glue-usageprofile-profileconfiguration-jobconfiguration)" : {{ConfigurationObject}},
  "[SessionConfiguration](#cfn-glue-usageprofile-profileconfiguration-sessionconfiguration)" : {{ConfigurationObject}}
}
```

### YAML
<a name="aws-properties-glue-usageprofile-profileconfiguration-syntax.yaml"></a>

```
  [JobConfiguration](#cfn-glue-usageprofile-profileconfiguration-jobconfiguration): {{
    ConfigurationObject}}
  [SessionConfiguration](#cfn-glue-usageprofile-profileconfiguration-sessionconfiguration): {{
    ConfigurationObject}}
```

## Properties
<a name="aws-properties-glue-usageprofile-profileconfiguration-properties"></a>

`JobConfiguration`  <a name="cfn-glue-usageprofile-profileconfiguration-jobconfiguration"></a>
A key-value map of configuration parameters for AWS Glue jobs.
*Required*: No
*Type*: [ConfigurationObject](aws-properties-glue-usageprofile-configurationobject.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SessionConfiguration`  <a name="cfn-glue-usageprofile-profileconfiguration-sessionconfiguration"></a>
A key-value map of configuration parameters for AWS Glue sessions.
*Required*: No
*Type*: [ConfigurationObject](aws-properties-glue-usageprofile-configurationobject.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
