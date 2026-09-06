---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appconfig-experimentrun.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppConfig::ExperimentRun
<a name="aws-resource-appconfig-experimentrun"></a>

Describes an experiment run, including its status, exposure settings, and treatment overrides.

## Syntax
<a name="aws-resource-appconfig-experimentrun-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appconfig-experimentrun-syntax.json"></a>

```
{
  "Type" : "AWS::AppConfig::ExperimentRun",
  "Properties" : {
      "[ApplicationIdentifier](#cfn-appconfig-experimentrun-applicationidentifier)" : {{String}},
      "[Description](#cfn-appconfig-experimentrun-description)" : {{String}},
      "[ExperimentDefinitionIdentifier](#cfn-appconfig-experimentrun-experimentdefinitionidentifier)" : {{String}},
      "[ExposurePercentage](#cfn-appconfig-experimentrun-exposurepercentage)" : {{Number}},
      "[Tags](#cfn-appconfig-experimentrun-tags)" : {{[ Tag, ... ]}},
      "[TreatmentOverrides](#cfn-appconfig-experimentrun-treatmentoverrides)" : {{TreatmentOverrides}}
    }
}
```

### YAML
<a name="aws-resource-appconfig-experimentrun-syntax.yaml"></a>

```
Type: AWS::AppConfig::ExperimentRun
Properties:
  [ApplicationIdentifier](#cfn-appconfig-experimentrun-applicationidentifier): {{String}}
  [Description](#cfn-appconfig-experimentrun-description): {{String}}
  [ExperimentDefinitionIdentifier](#cfn-appconfig-experimentrun-experimentdefinitionidentifier): {{String}}
  [ExposurePercentage](#cfn-appconfig-experimentrun-exposurepercentage): {{Number}}
  [Tags](#cfn-appconfig-experimentrun-tags): {{
    - Tag}}
  [TreatmentOverrides](#cfn-appconfig-experimentrun-treatmentoverrides): {{
    TreatmentOverrides}}
```

## Properties
<a name="aws-resource-appconfig-experimentrun-properties"></a>

`ApplicationIdentifier`  <a name="cfn-appconfig-experimentrun-applicationidentifier"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-appconfig-experimentrun-description"></a>
A description of the experiment run.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExperimentDefinitionIdentifier`  <a name="cfn-appconfig-experimentrun-experimentdefinitionidentifier"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExposurePercentage`  <a name="cfn-appconfig-experimentrun-exposurepercentage"></a>
The percentage of the target audience exposed to treatments.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-appconfig-experimentrun-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-appconfig-experimentrun-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TreatmentOverrides`  <a name="cfn-appconfig-experimentrun-treatmentoverrides"></a>
Treatment assignment overrides that assign specific entity IDs to treatments.
*Required*: No
*Type*: [TreatmentOverrides](aws-properties-appconfig-experimentrun-treatmentoverrides.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-appconfig-experimentrun-return-values"></a>

### Ref
<a name="aws-resource-appconfig-experimentrun-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-appconfig-experimentrun-return-values-fn--getatt"></a>

####
<a name="aws-resource-appconfig-experimentrun-return-values-fn--getatt-fn--getatt"></a>

`ApplicationId`  <a name="ApplicationId-fn::getatt"></a>
The application ID.

`ExperimentDefinitionId`  <a name="ExperimentDefinitionId-fn::getatt"></a>
The experiment definition ID.

`Run`  <a name="Run-fn::getatt"></a>
The experiment run number.

`StartedAt`  <a name="StartedAt-fn::getatt"></a>
The date and time the experiment run started, in ISO 8601 format.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the experiment run. Valid values: `RUNNING`, `DONE`.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time the experiment run was last updated, in ISO 8601 format.
