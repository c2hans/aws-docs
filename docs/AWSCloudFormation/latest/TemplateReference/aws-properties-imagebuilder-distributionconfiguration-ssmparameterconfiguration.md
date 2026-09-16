---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-distributionconfiguration-ssmparameterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::DistributionConfiguration SsmParameterConfiguration
<a name="aws-properties-imagebuilder-distributionconfiguration-ssmparameterconfiguration"></a>

Configuration for a single Parameter in the AWS Systems Manager (SSM) Parameter Store in a given Region.

## Syntax
<a name="aws-properties-imagebuilder-distributionconfiguration-ssmparameterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-distributionconfiguration-ssmparameterconfiguration-syntax.json"></a>

```
{
  "[AmiAccountId](#cfn-imagebuilder-distributionconfiguration-ssmparameterconfiguration-amiaccountid)" : {{String}},
  "[DataType](#cfn-imagebuilder-distributionconfiguration-ssmparameterconfiguration-datatype)" : {{String}},
  "[ParameterName](#cfn-imagebuilder-distributionconfiguration-ssmparameterconfiguration-parametername)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-distributionconfiguration-ssmparameterconfiguration-syntax.yaml"></a>

```
  [AmiAccountId](#cfn-imagebuilder-distributionconfiguration-ssmparameterconfiguration-amiaccountid): {{String}}
  [DataType](#cfn-imagebuilder-distributionconfiguration-ssmparameterconfiguration-datatype): {{String}}
  [ParameterName](#cfn-imagebuilder-distributionconfiguration-ssmparameterconfiguration-parametername): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-distributionconfiguration-ssmparameterconfiguration-properties"></a>

`AmiAccountId`  <a name="cfn-imagebuilder-distributionconfiguration-ssmparameterconfiguration-amiaccountid"></a>
Specify the account that will own the Parameter in a given Region. During distribution, this account must be specified in distribution settings as a target account for the Region.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataType`  <a name="cfn-imagebuilder-distributionconfiguration-ssmparameterconfiguration-datatype"></a>
The type of value the parameter contains. We recommend the `aws:ec2:image` data type.
*Required*: No
*Type*: String
*Allowed values*: `text | aws:ec2:image`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterName`  <a name="cfn-imagebuilder-distributionconfiguration-ssmparameterconfiguration-parametername"></a>
This is the name of the Parameter in the target Region or account. The image distribution creates the Parameter if it doesn't already exist. Otherwise, it updates the parameter.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.\-\/]+$`
*Minimum*: `1`
*Maximum*: `1011`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
