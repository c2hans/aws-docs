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
The data type specifies what type of value the Parameter contains. We recommend that you use data type `aws:ec2:image`.
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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
