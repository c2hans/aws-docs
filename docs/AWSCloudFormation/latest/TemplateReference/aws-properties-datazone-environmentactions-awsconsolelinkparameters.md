---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-environmentactions-awsconsolelinkparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::EnvironmentActions AwsConsoleLinkParameters
<a name="aws-properties-datazone-environmentactions-awsconsolelinkparameters"></a>

The parameters of the console link specified as part of the environment action.

## Syntax
<a name="aws-properties-datazone-environmentactions-awsconsolelinkparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-environmentactions-awsconsolelinkparameters-syntax.json"></a>

```
{
  "[Uri](#cfn-datazone-environmentactions-awsconsolelinkparameters-uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-environmentactions-awsconsolelinkparameters-syntax.yaml"></a>

```
  [Uri](#cfn-datazone-environmentactions-awsconsolelinkparameters-uri): {{String}}
```

## Properties
<a name="aws-properties-datazone-environmentactions-awsconsolelinkparameters-properties"></a>

`Uri`  <a name="cfn-datazone-environmentactions-awsconsolelinkparameters-uri"></a>
The URI of the console link specified as part of the environment action.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
