---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-domain-automatedsnapshotpauseoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Domain AutomatedSnapshotPauseOptions
<a name="aws-properties-opensearchservice-domain-automatedsnapshotpauseoptions"></a>

Specifies the automated snapshot pause options for the domain. These options allow you to temporarily pause automated snapshots for a specified time period.

## Syntax
<a name="aws-properties-opensearchservice-domain-automatedsnapshotpauseoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-domain-automatedsnapshotpauseoptions-syntax.json"></a>

```
{
  "[Enabled](#cfn-opensearchservice-domain-automatedsnapshotpauseoptions-enabled)" : {{Boolean}},
  "[EndTime](#cfn-opensearchservice-domain-automatedsnapshotpauseoptions-endtime)" : {{String}},
  "[StartTime](#cfn-opensearchservice-domain-automatedsnapshotpauseoptions-starttime)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchservice-domain-automatedsnapshotpauseoptions-syntax.yaml"></a>

```
  [Enabled](#cfn-opensearchservice-domain-automatedsnapshotpauseoptions-enabled): {{Boolean}}
  [EndTime](#cfn-opensearchservice-domain-automatedsnapshotpauseoptions-endtime): {{String}}
  [StartTime](#cfn-opensearchservice-domain-automatedsnapshotpauseoptions-starttime): {{String}}
```

## Properties
<a name="aws-properties-opensearchservice-domain-automatedsnapshotpauseoptions-properties"></a>

`Enabled`  <a name="cfn-opensearchservice-domain-automatedsnapshotpauseoptions-enabled"></a>
Whether automated snapshot pause is enabled for the domain.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndTime`  <a name="cfn-opensearchservice-domain-automatedsnapshotpauseoptions-endtime"></a>
The timestamp at which the automated snapshot pause ends.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTime`  <a name="cfn-opensearchservice-domain-automatedsnapshotpauseoptions-starttime"></a>
The timestamp at which the automated snapshot pause begins.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
