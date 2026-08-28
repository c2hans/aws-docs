---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-docdb-dbsubnetgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DocDB::DBSubnetGroup
<a name="aws-resource-docdb-dbsubnetgroup"></a>

The `AWS::DocDB::DBSubnetGroup`Amazon DocumentDB (with MongoDB compatibility) resource describes a DBSubnetGroup. subnet groups must contain at least one subnet in at least two Availability Zones in the AWS Region. For more information, see [DBSubnetGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBSubnetGroup.html) in the *Amazon DocumentDB Developer Guide*.

## Syntax
<a name="aws-resource-docdb-dbsubnetgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-docdb-dbsubnetgroup-syntax.json"></a>

```
{
  "Type" : "AWS::DocDB::DBSubnetGroup",
  "Properties" : {
      "[DBSubnetGroupDescription](#cfn-docdb-dbsubnetgroup-dbsubnetgroupdescription)" : {{String}},
      "[DBSubnetGroupName](#cfn-docdb-dbsubnetgroup-dbsubnetgroupname)" : {{String}},
      "[SubnetIds](#cfn-docdb-dbsubnetgroup-subnetids)" : {{[ String, ... ]}},
      "[Tags](#cfn-docdb-dbsubnetgroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-docdb-dbsubnetgroup-syntax.yaml"></a>

```
Type: AWS::DocDB::DBSubnetGroup
Properties:
  [DBSubnetGroupDescription](#cfn-docdb-dbsubnetgroup-dbsubnetgroupdescription): {{String}}
  [DBSubnetGroupName](#cfn-docdb-dbsubnetgroup-dbsubnetgroupname): {{String}}
  [SubnetIds](#cfn-docdb-dbsubnetgroup-subnetids): {{
    - String}}
  [Tags](#cfn-docdb-dbsubnetgroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-docdb-dbsubnetgroup-properties"></a>

`DBSubnetGroupDescription`  <a name="cfn-docdb-dbsubnetgroup-dbsubnetgroupdescription"></a>
The description for the subnet group.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DBSubnetGroupName`  <a name="cfn-docdb-dbsubnetgroup-dbsubnetgroupname"></a>
The name for the subnet group. This value is stored as a lowercase string.
Constraints: Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default.
Example: `mySubnetgroup`
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z][0-9a-zA-Z-:._ ]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-docdb-dbsubnetgroup-subnetids"></a>
The Amazon EC2 subnet IDs for the subnet group.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-docdb-dbsubnetgroup-tags"></a>
The tags to be assigned to the subnet group.
*Required*: No
*Type*: Array of [Tag](aws-properties-docdb-dbsubnetgroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-docdb-dbsubnetgroup-return-values"></a>

### Ref
<a name="aws-resource-docdb-dbsubnetgroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the DBSubnetGroup's name, such as `default`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-docdb-dbsubnetgroup--examples"></a>

###
<a name="aws-resource-docdb-dbsubnetgroup--examples--"></a>

#### JSON
<a name="aws-resource-docdb-dbsubnetgroup--examples----json"></a>

```
{
   "AWSTemplateFormatVersion" : "2010-09-09",
   "Resources" : {
      "myDBSubnetGroup" : {
         "Type" : "AWS::DocDB::DBSubnetGroup",
         "Properties" : {
            "DBSubnetGroupDescription" : "description",
            "SubnetIds" : [ "subnet-7b5b4112", "subnet-7b5b4115" ],
            "Tags" : [ {"Key" : "String", "Value" : "String"} ]
         }
      }
   }
}
```

#### YAML
<a name="aws-resource-docdb-dbsubnetgroup--examples----yaml"></a>

```
AWSTemplateFormatVersion: "2010-09-09"
Resources:
   myDBSubnetGroup:
      Type: "AWS::DocDB::DBSubnetGroup"
      Properties:
         DBSubnetGroupDescription: "description"
         SubnetIds:
            - "subnet-7b5b4112"
            - "subnet-7b5b4115"
         Tags:
            -
               Key: "String"
               Value: "String"
```

## See also
<a name="aws-resource-docdb-dbsubnetgroup--seealso"></a>
+  [Subnet](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_Subnet.html)
+  [DBSubnetGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBSubnetGroup.html)
+  [CreateDBSubnetGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CreateDBSubnetGroup.html)
+  [DeleteDBSubnetGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DeleteDBSubnetGroup.html)
+  [DescribeDBSubnetGroups](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeDBSubnetGroups.html)
+  [ModifyDBSubnetGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ModifyDBSubnetGroup.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
