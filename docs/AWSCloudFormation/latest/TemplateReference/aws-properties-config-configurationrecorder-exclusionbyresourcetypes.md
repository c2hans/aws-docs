---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-configurationrecorder-exclusionbyresourcetypes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::ConfigurationRecorder ExclusionByResourceTypes
<a name="aws-properties-config-configurationrecorder-exclusionbyresourcetypes"></a>

Specifies whether the configuration recorder excludes certain resource types from being recorded. Use the `ResourceTypes` field to enter a comma-separated list of resource types you want to exclude from recording.

By default, when AWS Config adds support for a new resource type in the Region where you set up the configuration recorder, including global resource types, AWS Config starts recording resources of that type automatically.

**Note**
 **How to use the exclusion recording strategy**
To use this option, you must set the `useOnly` field of [RecordingStrategy](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html) to `EXCLUSION_BY_RESOURCE_TYPES`.
AWS Config will then record configuration changes for all supported resource types, except the resource types that you specify to exclude from being recorded.
 **Global resource types and the exclusion recording strategy **
Unless specifically listed as exclusions, `AWS::RDS::GlobalCluster` will be recorded automatically in all supported AWS Config Regions were the configuration recorder is enabled.
IAM users, groups, roles, and customer managed policies will be recorded in the Region where you set up the configuration recorder if that is a Region where AWS Config was available before February 2022. You cannot be record the global IAM resouce types in Regions supported by AWS Config after February 2022. This list where you cannot record the global IAM resource types includes the following Regions:
Asia Pacific (Hyderabad)
Asia Pacific (Melbourne)
Canada West (Calgary)
Europe (Spain)
Europe (Zurich)
Israel (Tel Aviv)
Middle East (UAE)

## Syntax
<a name="aws-properties-config-configurationrecorder-exclusionbyresourcetypes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-configurationrecorder-exclusionbyresourcetypes-syntax.json"></a>

```
{
  "[ResourceTypes](#cfn-config-configurationrecorder-exclusionbyresourcetypes-resourcetypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-config-configurationrecorder-exclusionbyresourcetypes-syntax.yaml"></a>

```
  [ResourceTypes](#cfn-config-configurationrecorder-exclusionbyresourcetypes-resourcetypes): {{
    - String}}
```

## Properties
<a name="aws-properties-config-configurationrecorder-exclusionbyresourcetypes-properties"></a>

`ResourceTypes`  <a name="cfn-config-configurationrecorder-exclusionbyresourcetypes-resourcetypes"></a>
A comma-separated list of resource types to exclude from recording by the configuration recorder.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-config-configurationrecorder-exclusionbyresourcetypes--examples"></a>

### Record all current and future supported resource types excluding the types you specify
<a name="aws-properties-config-configurationrecorder-exclusionbyresourcetypes--examples--Record_all_current_and_future_supported_resource_types_excluding_the_types_you_specify"></a>

The recordingGroup file specifies which types of resources AWS Config will record.

#### JSON
<a name="aws-properties-config-configurationrecorder-exclusionbyresourcetypes--examples--Record_all_current_and_future_supported_resource_types_excluding_the_types_you_specify--json"></a>

```
{
    "AllSupported": false,
    "ExclusionByResourceTypes": {
        "ResourceTypes": [
            "AWS::Redshift::ClusterSnapshot",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::CloudFront::StreamingDistribution"
        ]
    },
    "IncludeGlobalResourceTypes": false,
    "RecordingStrategy": {
        "UseOnly": "EXCLUSION_BY_RESOURCE_TYPES"
    }
}
```

#### YAML
<a name="aws-properties-config-configurationrecorder-exclusionbyresourcetypes--examples--Record_all_current_and_future_supported_resource_types_excluding_the_types_you_specify--yaml"></a>

```
AllSupported: false
ExclusionByResourceTypes:
    ResourceTypes:
    - AWS::Redshift::ClusterSnapshot
    - AWS::RDS::DBClusterSnapshot
    - AWS::CloudFront::StreamingDistribution
IncludeGlobalResourceTypes: false
RecordingStrategy:
    UseOnly: EXCLUSION_BY_RESOURCE_TYPES
```
