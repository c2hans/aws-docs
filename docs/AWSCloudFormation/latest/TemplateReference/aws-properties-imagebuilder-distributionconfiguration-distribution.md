---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-distributionconfiguration-distribution.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::DistributionConfiguration Distribution
<a name="aws-properties-imagebuilder-distributionconfiguration-distribution"></a>

Defines the settings for a specific Region in the distribution configuration. You must specify whether the distribution is for an AMI or a container image. To do so, include exactly one of the following data types for your distribution:
+  `AmiDistributionConfiguration`
+  `ContainerDistributionConfiguration`

## Syntax
<a name="aws-properties-imagebuilder-distributionconfiguration-distribution-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-distributionconfiguration-distribution-syntax.json"></a>

```
{
  "[AmiDistributionConfiguration](#cfn-imagebuilder-distributionconfiguration-distribution-amidistributionconfiguration)" : {{AmiDistributionConfiguration}},
  "[ContainerDistributionConfiguration](#cfn-imagebuilder-distributionconfiguration-distribution-containerdistributionconfiguration)" : {{ContainerDistributionConfiguration}},
  "[FastLaunchConfigurations](#cfn-imagebuilder-distributionconfiguration-distribution-fastlaunchconfigurations)" : {{[ FastLaunchConfiguration, ... ]}},
  "[LaunchTemplateConfigurations](#cfn-imagebuilder-distributionconfiguration-distribution-launchtemplateconfigurations)" : {{[ LaunchTemplateConfiguration, ... ]}},
  "[LicenseConfigurationArns](#cfn-imagebuilder-distributionconfiguration-distribution-licenseconfigurationarns)" : {{[ String, ... ]}},
  "[Region](#cfn-imagebuilder-distributionconfiguration-distribution-region)" : {{String}},
  "[SsmParameterConfigurations](#cfn-imagebuilder-distributionconfiguration-distribution-ssmparameterconfigurations)" : {{[ SsmParameterConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-imagebuilder-distributionconfiguration-distribution-syntax.yaml"></a>

```
  [AmiDistributionConfiguration](#cfn-imagebuilder-distributionconfiguration-distribution-amidistributionconfiguration): {{
    AmiDistributionConfiguration}}
  [ContainerDistributionConfiguration](#cfn-imagebuilder-distributionconfiguration-distribution-containerdistributionconfiguration): {{
    ContainerDistributionConfiguration}}
  [FastLaunchConfigurations](#cfn-imagebuilder-distributionconfiguration-distribution-fastlaunchconfigurations): {{
    - FastLaunchConfiguration}}
  [LaunchTemplateConfigurations](#cfn-imagebuilder-distributionconfiguration-distribution-launchtemplateconfigurations): {{
    - LaunchTemplateConfiguration}}
  [LicenseConfigurationArns](#cfn-imagebuilder-distributionconfiguration-distribution-licenseconfigurationarns): {{
    - String}}
  [Region](#cfn-imagebuilder-distributionconfiguration-distribution-region): {{String}}
  [SsmParameterConfigurations](#cfn-imagebuilder-distributionconfiguration-distribution-ssmparameterconfigurations): {{
    - SsmParameterConfiguration}}
```

## Properties
<a name="aws-properties-imagebuilder-distributionconfiguration-distribution-properties"></a>

`AmiDistributionConfiguration`  <a name="cfn-imagebuilder-distributionconfiguration-distribution-amidistributionconfiguration"></a>
The specific AMI settings; for example, launch permissions or AMI tags.
*Required*: No
*Type*: [AmiDistributionConfiguration](aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainerDistributionConfiguration`  <a name="cfn-imagebuilder-distributionconfiguration-distribution-containerdistributionconfiguration"></a>
Container distribution settings for encryption, licensing, and sharing in a specific Region.
*Required*: No
*Type*: [ContainerDistributionConfiguration](aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FastLaunchConfigurations`  <a name="cfn-imagebuilder-distributionconfiguration-distribution-fastlaunchconfigurations"></a>
The Windows faster-launching configurations to use for AMI distribution.
*Required*: No
*Type*: Array of [FastLaunchConfiguration](aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.md)
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LaunchTemplateConfigurations`  <a name="cfn-imagebuilder-distributionconfiguration-distribution-launchtemplateconfigurations"></a>
A group of launchTemplateConfiguration settings that apply to image distribution for specified accounts.
*Required*: No
*Type*: Array of [LaunchTemplateConfiguration](aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.md)
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LicenseConfigurationArns`  <a name="cfn-imagebuilder-distributionconfiguration-distribution-licenseconfigurationarns"></a>
The License Manager Configuration to associate with the AMI in the specified Region.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-imagebuilder-distributionconfiguration-distribution-region"></a>
The target Region.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SsmParameterConfigurations`  <a name="cfn-imagebuilder-distributionconfiguration-distribution-ssmparameterconfigurations"></a>
Contains settings to update AWS Systems Manager (SSM) Parameter Store Parameters with output AMI IDs from the build by target Region.
*Required*: No
*Type*: Array of [SsmParameterConfiguration](aws-properties-imagebuilder-distributionconfiguration-ssmparameterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-imagebuilder-distributionconfiguration-distribution--examples"></a>

**Topics**
+ [Example 1: AmiDistributionConfiguration with launch permissions](#aws-properties-imagebuilder-distributionconfiguration-distribution--examples--Example_1:_AmiDistributionConfiguration_with_launch_permissions)
+ [Example 2: Create a distribution configuration resource for a copied AMI](#aws-properties-imagebuilder-distributionconfiguration-distribution--examples--Example_2:_Create_a_distribution_configuration_resource_for_a_copied_AMI)
+ [Example 3: ContainerDistributionConfiguration](#aws-properties-imagebuilder-distributionconfiguration-distribution--examples--Example_3:_ContainerDistributionConfiguration)

### Example 1: AmiDistributionConfiguration with launch permissions
<a name="aws-properties-imagebuilder-distributionconfiguration-distribution--examples--Example_1:_AmiDistributionConfiguration_with_launch_permissions"></a>

The following example shows the template for the AmiDistributionConfiguration property in both YAML and JSON format.

**Note**
To make an AMI public, set the launch permission authorized accounts to `all`. See the examples for making an AMI public at [EC2 ModifyImageAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyImageAttribute.html).

#### YAML
<a name="aws-properties-imagebuilder-distributionconfiguration-distribution--examples--Example_1:_AmiDistributionConfiguration_with_launch_permissions--yaml"></a>

```
Distributions:
  - Region: 'us-west-2'
    AmiDistributionConfiguration:
      Name: 'AmiCopyConfiguration - {{ imagebuilder:buildDate }}'
      Description: 'Share an AMI in the distribution Region by granting launch permissions to specified organizations, OUs, user groups, and accounts.'
      AmiTags:
        AmiTagKey: 'AmiTagValue'
      LaunchPermissionConfiguration:
        OrganizationArns:
          - 'arn:aws:organizations::123456789012:organization/o-myorganization123'
        OrganizationalUnitArns:
          - 'arn:aws:organizations::123456789012:ou/o-123example/ou-1234-myorganizationalunit'
        UserGroups:
          - 'GroupName1'
          - 'GroupName2'
        UserIds:
          - '123456789012'
          - '345678901234'
```

#### JSON
<a name="aws-properties-imagebuilder-distributionconfiguration-distribution--examples--Example_1:_AmiDistributionConfiguration_with_launch_permissions--json"></a>

```
{
    "Distributions": [{
        "Region": "us-west-2",
        "AmiDistributionConfiguration": {
            "Name": "AmiCopyConfiguration - {{ imagebuilder:buildDate }}",
            "Description": "Share an AMI in the distribution Region by granting launch permissions to specified organizations, OUs, user groups, and accounts.",
            "AmiTags": {
                "AmiTagKey": "AmiTagValue"
            },
            "LaunchPermissionConfiguration": {
                "OrganizationArns": [
                    "arn:aws:organizations::123456789012:organization/o-myorganization123"
                ],
                "OrganizationalUnitArns": [
                    "arn:aws:organizations::123456789012:ou/o-123example/ou-1234-myorganizationalunit"
                ],
                "UserGroups": [
                    "GroupName1",
                    "GroupName2"
                ],
                "UserIds": [
                    "123456789012",
                    "345678901234"
                ]
            }
        }
    }]
}
```

### Example 2: Create a distribution configuration resource for a copied AMI
<a name="aws-properties-imagebuilder-distributionconfiguration-distribution--examples--Example_2:_Create_a_distribution_configuration_resource_for_a_copied_AMI"></a>

The following example shows the template for the AmiDistributionConfiguration property in both YAML and JSON.

#### YAML
<a name="aws-properties-imagebuilder-distributionconfiguration-distribution--examples--Example_2:_Create_a_distribution_configuration_resource_for_a_copied_AMI--yaml"></a>

```
Distributions:
  - Region: 'us-west-2'
    AmiDistributionConfiguration:
      Name: AmiCopyConfiguration - {{ imagebuilder:buildDate }}
      Description: 'Distribute a copy of the AMI to specific accounts in the destination Region.'
      AmiTags:
        AmiTagKey: 'AmiTagValue'
      TargetAccountIds:
        - '123456789012'
        - '345678901234'
```

#### JSON
<a name="aws-properties-imagebuilder-distributionconfiguration-distribution--examples--Example_2:_Create_a_distribution_configuration_resource_for_a_copied_AMI--json"></a>

```
{
    "Distributions": [{
        "Region": "us-west-2",
        "AmiDistributionConfiguration": {
            "Name": "AmiCopyConfiguration - {{ imagebuilder:buildDate }}",
            "Description": "Distribute a copy of the AMI to specific accounts in the destination Region.",
            "AmiTags": {
                "AmiTagKey": "AmiTagValue"
            },
            "TargetAccountIds": ["123456789012", "345678901234"]
        }
    }]
}
```

### Example 3: ContainerDistributionConfiguration
<a name="aws-properties-imagebuilder-distributionconfiguration-distribution--examples--Example_3:_ContainerDistributionConfiguration"></a>

The following example shows the template for the ContainerDistributionConfiguration property in both YAML and JSON format.

#### YAML
<a name="aws-properties-imagebuilder-distributionconfiguration-distribution--examples--Example_3:_ContainerDistributionConfiguration--yaml"></a>

```
Distributions:
  - Region: 'us-west-2'
    ContainerDistributionConfiguration:
      Description: 'Container distribution for us-west-2'
      TargetRepository:
        Service: ECR
        RepositoryName: 'cfn-test'
      ContainerTags:
        - 'Tag1'
        - 'Tag2'
```

#### JSON
<a name="aws-properties-imagebuilder-distributionconfiguration-distribution--examples--Example_3:_ContainerDistributionConfiguration--json"></a>

```
{
    "Distributions": [{
        "Region": "us-west-2",
        "ContainerDistributionConfiguration": {
            "Description": "Container distribution for us-west-2",
            "TargetRepository": {
                "Service": "ECR",
                "RepositoryName": "cfn-test"
            },
            "ContainerTags": ["Tag1", "Tag2"]
        }
    }]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
