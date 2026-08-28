---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-projectprofile-environmentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::ProjectProfile EnvironmentConfiguration
<a name="aws-properties-datazone-projectprofile-environmentconfiguration"></a>

The configuration of an environment.

## Syntax
<a name="aws-properties-datazone-projectprofile-environmentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-projectprofile-environmentconfiguration-syntax.json"></a>

```
{
  "[AwsAccount](#cfn-datazone-projectprofile-environmentconfiguration-awsaccount)" : {{AwsAccount}},
  "[AwsRegion](#cfn-datazone-projectprofile-environmentconfiguration-awsregion)" : {{Region}},
  "[ConfigurationParameters](#cfn-datazone-projectprofile-environmentconfiguration-configurationparameters)" : {{EnvironmentConfigurationParametersDetails}},
  "[DeploymentMode](#cfn-datazone-projectprofile-environmentconfiguration-deploymentmode)" : {{String}},
  "[DeploymentOrder](#cfn-datazone-projectprofile-environmentconfiguration-deploymentorder)" : {{Number}},
  "[Description](#cfn-datazone-projectprofile-environmentconfiguration-description)" : {{String}},
  "[EnvironmentBlueprintId](#cfn-datazone-projectprofile-environmentconfiguration-environmentblueprintid)" : {{String}},
  "[EnvironmentConfigurationId](#cfn-datazone-projectprofile-environmentconfiguration-environmentconfigurationid)" : {{String}},
  "[Name](#cfn-datazone-projectprofile-environmentconfiguration-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-projectprofile-environmentconfiguration-syntax.yaml"></a>

```
  [AwsAccount](#cfn-datazone-projectprofile-environmentconfiguration-awsaccount): {{
    AwsAccount}}
  [AwsRegion](#cfn-datazone-projectprofile-environmentconfiguration-awsregion): {{
    Region}}
  [ConfigurationParameters](#cfn-datazone-projectprofile-environmentconfiguration-configurationparameters): {{
    EnvironmentConfigurationParametersDetails}}
  [DeploymentMode](#cfn-datazone-projectprofile-environmentconfiguration-deploymentmode): {{String}}
  [DeploymentOrder](#cfn-datazone-projectprofile-environmentconfiguration-deploymentorder): {{Number}}
  [Description](#cfn-datazone-projectprofile-environmentconfiguration-description): {{String}}
  [EnvironmentBlueprintId](#cfn-datazone-projectprofile-environmentconfiguration-environmentblueprintid): {{String}}
  [EnvironmentConfigurationId](#cfn-datazone-projectprofile-environmentconfiguration-environmentconfigurationid): {{String}}
  [Name](#cfn-datazone-projectprofile-environmentconfiguration-name): {{String}}
```

## Properties
<a name="aws-properties-datazone-projectprofile-environmentconfiguration-properties"></a>

`AwsAccount`  <a name="cfn-datazone-projectprofile-environmentconfiguration-awsaccount"></a>
The AWS account of the environment.
*Required*: No
*Type*: [AwsAccount](aws-properties-datazone-projectprofile-awsaccount.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsRegion`  <a name="cfn-datazone-projectprofile-environmentconfiguration-awsregion"></a>
The AWS Region of the environment.
*Required*: Yes
*Type*: [Region](aws-properties-datazone-projectprofile-region.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfigurationParameters`  <a name="cfn-datazone-projectprofile-environmentconfiguration-configurationparameters"></a>
The configuration parameters of the environment.
*Required*: No
*Type*: [EnvironmentConfigurationParametersDetails](aws-properties-datazone-projectprofile-environmentconfigurationparametersdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeploymentMode`  <a name="cfn-datazone-projectprofile-environmentconfiguration-deploymentmode"></a>
The deployment mode of the environment.
*Required*: No
*Type*: String
*Allowed values*: `ON_CREATE | ON_DEMAND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeploymentOrder`  <a name="cfn-datazone-projectprofile-environmentconfiguration-deploymentorder"></a>
The deployment order of the environment.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-datazone-projectprofile-environmentconfiguration-description"></a>
The environment description.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentBlueprintId`  <a name="cfn-datazone-projectprofile-environmentconfiguration-environmentblueprintid"></a>
The environment blueprint ID.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,36}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentConfigurationId`  <a name="cfn-datazone-projectprofile-environmentconfiguration-environmentconfigurationid"></a>
The configuration ID with which the environment is created.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,36}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-datazone-projectprofile-environmentconfiguration-name"></a>
The environment name.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w -]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
