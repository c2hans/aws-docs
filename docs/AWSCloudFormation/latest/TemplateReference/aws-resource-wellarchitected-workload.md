---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wellarchitected-workload.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WellArchitected::Workload
<a name="aws-resource-wellarchitected-workload"></a>

Input for workload creation.

## Syntax
<a name="aws-resource-wellarchitected-workload-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wellarchitected-workload-syntax.json"></a>

```
{
  "Type" : "AWS::WellArchitected::Workload",
  "Properties" : {
      "[AccountIds](#cfn-wellarchitected-workload-accountids)" : {{[ String, ... ]}},
      "[ArchitecturalDesign](#cfn-wellarchitected-workload-architecturaldesign)" : {{String}},
      "[AwsRegions](#cfn-wellarchitected-workload-awsregions)" : {{[ String, ... ]}},
      "[Description](#cfn-wellarchitected-workload-description)" : {{String}},
      "[DiscoveryConfig](#cfn-wellarchitected-workload-discoveryconfig)" : {{DiscoveryConfig}},
      "[Environment](#cfn-wellarchitected-workload-environment)" : {{String}},
      "[Industry](#cfn-wellarchitected-workload-industry)" : {{String}},
      "[IndustryType](#cfn-wellarchitected-workload-industrytype)" : {{String}},
      "[Lenses](#cfn-wellarchitected-workload-lenses)" : {{[ String, ... ]}},
      "[NonAwsRegions](#cfn-wellarchitected-workload-nonawsregions)" : {{[ String, ... ]}},
      "[Notes](#cfn-wellarchitected-workload-notes)" : {{String}},
      "[ReviewOwner](#cfn-wellarchitected-workload-reviewowner)" : {{String}},
      "[Tags](#cfn-wellarchitected-workload-tags)" : {{[ TagsItems, ... ]}},
      "[WorkloadName](#cfn-wellarchitected-workload-workloadname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-wellarchitected-workload-syntax.yaml"></a>

```
Type: AWS::WellArchitected::Workload
Properties:
  [AccountIds](#cfn-wellarchitected-workload-accountids): {{
    - String}}
  [ArchitecturalDesign](#cfn-wellarchitected-workload-architecturaldesign): {{String}}
  [AwsRegions](#cfn-wellarchitected-workload-awsregions): {{
    - String}}
  [Description](#cfn-wellarchitected-workload-description): {{String}}
  [DiscoveryConfig](#cfn-wellarchitected-workload-discoveryconfig): {{
    DiscoveryConfig}}
  [Environment](#cfn-wellarchitected-workload-environment): {{String}}
  [Industry](#cfn-wellarchitected-workload-industry): {{String}}
  [IndustryType](#cfn-wellarchitected-workload-industrytype): {{String}}
  [Lenses](#cfn-wellarchitected-workload-lenses): {{
    - String}}
  [NonAwsRegions](#cfn-wellarchitected-workload-nonawsregions): {{
    - String}}
  [Notes](#cfn-wellarchitected-workload-notes): {{String}}
  [ReviewOwner](#cfn-wellarchitected-workload-reviewowner): {{String}}
  [Tags](#cfn-wellarchitected-workload-tags): {{
    - TagsItems}}
  [WorkloadName](#cfn-wellarchitected-workload-workloadname): {{String}}
```

## Properties
<a name="aws-resource-wellarchitected-workload-properties"></a>

`AccountIds`  <a name="cfn-wellarchitected-workload-accountids"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `12 | 0`
*Maximum*: `12 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ArchitecturalDesign`  <a name="cfn-wellarchitected-workload-architecturaldesign"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^(|(https?|ftp):\/\/[^\s/$.?#].[^\s]*)$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsRegions`  <a name="cfn-wellarchitected-workload-awsregions"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `100 | 50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-wellarchitected-workload-description"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DiscoveryConfig`  <a name="cfn-wellarchitected-workload-discoveryconfig"></a>
Well-Architected discovery configuration settings associated to the workload.
*Required*: No
*Type*: [DiscoveryConfig](aws-properties-wellarchitected-workload-discoveryconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Environment`  <a name="cfn-wellarchitected-workload-environment"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `PRODUCTION | PREPRODUCTION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Industry`  <a name="cfn-wellarchitected-workload-industry"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IndustryType`  <a name="cfn-wellarchitected-workload-industrytype"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Lenses`  <a name="cfn-wellarchitected-workload-lenses"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NonAwsRegions`  <a name="cfn-wellarchitected-workload-nonawsregions"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `3 | 0`
*Maximum*: `25 | 5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Notes`  <a name="cfn-wellarchitected-workload-notes"></a>
The notes associated with the workload.
For a review template, these are the notes that will be associated with the workload when the template is applied.
*Required*: No
*Type*: String
*Maximum*: `2084`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReviewOwner`  <a name="cfn-wellarchitected-workload-reviewowner"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-wellarchitected-workload-tags"></a>
The tags to be associated with the workload.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-wellarchitected-workload-tagsitems.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkloadName`  <a name="cfn-wellarchitected-workload-workloadname"></a>
The name of the workload.
The name must be unique within an account within an AWS Region. Spaces and capitalization are ignored when checking for uniqueness.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-wellarchitected-workload-return-values"></a>

### Ref
<a name="aws-resource-wellarchitected-workload-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-wellarchitected-workload-return-values-fn--getatt"></a>

####
<a name="aws-resource-wellarchitected-workload-return-values-fn--getatt-fn--getatt"></a>

`ImprovementStatus`  <a name="ImprovementStatus-fn::getatt"></a>
Property description not available.

`WorkloadArn`  <a name="WorkloadArn-fn::getatt"></a>
The ARN for the workload.

`WorkloadId`  <a name="WorkloadId-fn::getatt"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
