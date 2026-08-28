---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbsubnetgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBSubnetGroup
<a name="aws-resource-rds-dbsubnetgroup"></a>

The `AWS::RDS::DBSubnetGroup` resource creates a database subnet group. Subnet groups must contain at least two subnets in two different Availability Zones in the same region.

For more information, see [ Working with DB subnet groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Subnets) in the *Amazon RDS User Guide*.

## Syntax
<a name="aws-resource-rds-dbsubnetgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rds-dbsubnetgroup-syntax.json"></a>

```
{
  "Type" : "AWS::RDS::DBSubnetGroup",
  "Properties" : {
      "[DBSubnetGroupDescription](#cfn-rds-dbsubnetgroup-dbsubnetgroupdescription)" : {{String}},
      "[DBSubnetGroupName](#cfn-rds-dbsubnetgroup-dbsubnetgroupname)" : {{String}},
      "[SubnetIds](#cfn-rds-dbsubnetgroup-subnetids)" : {{[ String, ... ]}},
      "[Tags](#cfn-rds-dbsubnetgroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rds-dbsubnetgroup-syntax.yaml"></a>

```
Type: AWS::RDS::DBSubnetGroup
Properties:
  [DBSubnetGroupDescription](#cfn-rds-dbsubnetgroup-dbsubnetgroupdescription): {{String}}
  [DBSubnetGroupName](#cfn-rds-dbsubnetgroup-dbsubnetgroupname): {{String}}
  [SubnetIds](#cfn-rds-dbsubnetgroup-subnetids): {{
    - String}}
  [Tags](#cfn-rds-dbsubnetgroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-rds-dbsubnetgroup-properties"></a>

`DBSubnetGroupDescription`  <a name="cfn-rds-dbsubnetgroup-dbsubnetgroupdescription"></a>
The description for the DB subnet group.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DBSubnetGroupName`  <a name="cfn-rds-dbsubnetgroup-dbsubnetgroupname"></a>
The name for the DB subnet group. This value is stored as a lowercase string.
Constraints:
+ Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens.
+ Must not be default.
+ First character must be a letter.
Example: `mydbsubnetgroup`
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-rds-dbsubnetgroup-subnetids"></a>
The EC2 Subnet IDs for the DB subnet group.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-rds-dbsubnetgroup-tags"></a>
Tags to assign to the DB subnet group.
*Required*: No
*Type*: Array of [Tag](aws-properties-rds-dbsubnetgroup-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rds-dbsubnetgroup-return-values"></a>

### Ref
<a name="aws-resource-rds-dbsubnetgroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the DB subnet group.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-rds-dbsubnetgroup-return-values-fn--getatt"></a>

####
<a name="aws-resource-rds-dbsubnetgroup-return-values-fn--getatt-fn--getatt"></a>

`DBSubnetGroupArn`  <a name="DBSubnetGroupArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the DB subnet group.

## Examples
<a name="aws-resource-rds-dbsubnetgroup--examples"></a>

### Create a DB subnet group
<a name="aws-resource-rds-dbsubnetgroup--examples--Create_a_DB_subnet_group"></a>

The following example creates a DB subnet group with two subnet IDs and a set of tags.

#### JSON
<a name="aws-resource-rds-dbsubnetgroup--examples--Create_a_DB_subnet_group--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "myDBSubnetGroup": {
            "Type": "AWS::RDS::DBSubnetGroup",
            "Properties": {
                "DBSubnetGroupDescription": "Description of subnet group",
                "SubnetIds": [
                    "subnet-7b5b4112",
                    "subnet-7b5b4115"
                ],
                "Tags": [
                    {
                        "Key": "mykey",
                        "Value": "myvalue"
                    }
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-dbsubnetgroup--examples--Create_a_DB_subnet_group--yaml"></a>

```
---
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  myDBSubnetGroup:
    Type: AWS::RDS::DBSubnetGroup
    Properties:
      DBSubnetGroupDescription: Description of subnet group
      SubnetIds:
        - subnet-7b5b4112
        - subnet-7b5b4115
      Tags:
        - Key: mykey
          Value: myvalue
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
