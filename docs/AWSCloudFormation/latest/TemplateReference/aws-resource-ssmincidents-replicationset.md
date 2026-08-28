---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssmincidents-replicationset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMIncidents::ReplicationSet
<a name="aws-resource-ssmincidents-replicationset"></a>

The `AWS::SSMIncidents::ReplicationSet` resource specifies a set of AWS Regions that Incident Manager data is replicated to and the AWS Key Management Service (AWS KMS key used to encrypt the data.

## Syntax
<a name="aws-resource-ssmincidents-replicationset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ssmincidents-replicationset-syntax.json"></a>

```
{
  "Type" : "AWS::SSMIncidents::ReplicationSet",
  "Properties" : {
      "[DeletionProtected](#cfn-ssmincidents-replicationset-deletionprotected)" : {{Boolean}},
      "[Regions](#cfn-ssmincidents-replicationset-regions)" : {{[ ReplicationRegion, ... ]}},
      "[Tags](#cfn-ssmincidents-replicationset-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ssmincidents-replicationset-syntax.yaml"></a>

```
Type: AWS::SSMIncidents::ReplicationSet
Properties:
  [DeletionProtected](#cfn-ssmincidents-replicationset-deletionprotected): {{Boolean}}
  [Regions](#cfn-ssmincidents-replicationset-regions): {{
    - ReplicationRegion}}
  [Tags](#cfn-ssmincidents-replicationset-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ssmincidents-replicationset-properties"></a>

`DeletionProtected`  <a name="cfn-ssmincidents-replicationset-deletionprotected"></a>
Determines if the replication set deletion protection is enabled or not. If deletion protection is enabled, you can't delete the last Region in the replication set.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Regions`  <a name="cfn-ssmincidents-replicationset-regions"></a>
Specifies the Regions of the replication set.
*Required*: Yes
*Type*: Array of [ReplicationRegion](aws-properties-ssmincidents-replicationset-replicationregion.md)
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ssmincidents-replicationset-tags"></a>
A list of tags to add to the replication set.
*Required*: No
*Type*: Array of [Tag](aws-properties-ssmincidents-replicationset-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-resource-ssmincidents-replicationset--examples"></a>

### Create a replication set
<a name="aws-resource-ssmincidents-replicationset--examples--Create_a_replication_set"></a>

The following example creates a replication set.

**Note**
We recommend creating a replication set and response plan using a single template. For a demonstration, see the examples for [AWS::SSMIncidents::ResponsePlan](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#aws-resource-ssmincidents-responseplan--examples).

#### JSON
<a name="aws-resource-ssmincidents-replicationset--examples--Create_a_replication_set--json"></a>

```
{
   "AWSTemplateFormatVersion": "2010-09-09",
   "Description": "Sample AWS CloudFormation template to create a replication set (JSON).",
   "Resources": {
      "MyReplicationSet": {
         "Type": "AWS::SSMIncidents::ReplicationSet",
         "Properties": {
            "DeletionProtected": true,
            "Regions": [
               {
                  "RegionName": {
                     "Ref": "AWS::Region"
                  }
               }
            ],
            "Tags": [
               {
                  "Key": "MyReplicationSetTagKey",
                  "Value": "MyReplicationSetTagValue"
               }
            ]
         }
      }
   }
}
```

#### YAML
<a name="aws-resource-ssmincidents-replicationset--examples--Create_a_replication_set--yaml"></a>

```
---
AWSTemplateFormatVersion: 2010-09-09
Description: "Sample AWS CloudFormation template to create a replication set (YAML)."
Resources:
  MyReplicationSet:
    Type: AWS::SSMIncidents::ReplicationSet
    Properties:
      DeletionProtected: true
      Regions:
        - RegionName:
            Ref: "AWS::Region"
      Tags:
        - Key: MyReplicationSetTagKey
          Value: MyReplicationSetTagValue
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
