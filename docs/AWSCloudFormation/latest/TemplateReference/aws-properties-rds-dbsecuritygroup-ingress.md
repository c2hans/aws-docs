---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rds-dbsecuritygroup-ingress.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBSecurityGroup Ingress
<a name="aws-properties-rds-dbsecuritygroup-ingress"></a>

The `Ingress` property type specifies an individual ingress rule within an `AWS::RDS::DBSecurityGroup` resource.

**Note**
EC2-Classic was retired on August 15, 2022. If you haven't migrated from EC2-Classic to a VPC, we recommend that you migrate as soon as possible. For more information, see [Migrate from EC2-Classic to a VPC](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html) in the *Amazon EC2 User Guide*, the blog [EC2-Classic Networking is Retiring – Here’s How to Prepare](https://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/), and [Moving a DB instance not in a VPC into a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Non-VPC2VPC.html) in the *Amazon RDS User Guide*.

## Syntax
<a name="aws-properties-rds-dbsecuritygroup-ingress-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rds-dbsecuritygroup-ingress-syntax.json"></a>

```
{
  "[CIDRIP](#cfn-rds-dbsecuritygroup-ingress-cidrip)" : {{String}},
  "[EC2SecurityGroupId](#cfn-rds-dbsecuritygroup-ingress-ec2securitygroupid)" : {{String}},
  "[EC2SecurityGroupName](#cfn-rds-dbsecuritygroup-ingress-ec2securitygroupname)" : {{String}},
  "[EC2SecurityGroupOwnerId](#cfn-rds-dbsecuritygroup-ingress-ec2securitygroupownerid)" : {{String}}
}
```

### YAML
<a name="aws-properties-rds-dbsecuritygroup-ingress-syntax.yaml"></a>

```
  [CIDRIP](#cfn-rds-dbsecuritygroup-ingress-cidrip): {{String}}
  [EC2SecurityGroupId](#cfn-rds-dbsecuritygroup-ingress-ec2securitygroupid): {{String}}
  [EC2SecurityGroupName](#cfn-rds-dbsecuritygroup-ingress-ec2securitygroupname): {{String}}
  [EC2SecurityGroupOwnerId](#cfn-rds-dbsecuritygroup-ingress-ec2securitygroupownerid): {{String}}
```

## Properties
<a name="aws-properties-rds-dbsecuritygroup-ingress-properties"></a>

`CIDRIP`  <a name="cfn-rds-dbsecuritygroup-ingress-cidrip"></a>
The IP range to authorize.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EC2SecurityGroupId`  <a name="cfn-rds-dbsecuritygroup-ingress-ec2securitygroupid"></a>
Id of the EC2 security group to authorize. For VPC DB security groups, `EC2SecurityGroupId` must be provided. Otherwise, `EC2SecurityGroupOwnerId` and either `EC2SecurityGroupName` or `EC2SecurityGroupId` must be provided.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EC2SecurityGroupName`  <a name="cfn-rds-dbsecuritygroup-ingress-ec2securitygroupname"></a>
Name of the EC2 security group to authorize. For VPC DB security groups, `EC2SecurityGroupId` must be provided. Otherwise, `EC2SecurityGroupOwnerId` and either `EC2SecurityGroupName` or `EC2SecurityGroupId` must be provided.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EC2SecurityGroupOwnerId`  <a name="cfn-rds-dbsecuritygroup-ingress-ec2securitygroupownerid"></a>
AWS account number of the owner of the EC2 security group specified in the `EC2SecurityGroupName` parameter. The AWS access key ID isn't an acceptable value. For VPC DB security groups, `EC2SecurityGroupId` must be provided. Otherwise, `EC2SecurityGroupOwnerId` and either `EC2SecurityGroupName` or `EC2SecurityGroupId` must be provided.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-rds-dbsecuritygroup-ingress--examples"></a>

### Specifying an ingress rule
<a name="aws-properties-rds-dbsecuritygroup-ingress--examples--Specifying_an_ingress_rule"></a>

The following example specifies two security group ingress rules.

#### JSON
<a name="aws-properties-rds-dbsecuritygroup-ingress--examples--Specifying_an_ingress_rule--json"></a>

```
"DBSecurityGroupIngress":[
   {
      "EC2SecurityGroupId":"sg-b0ff1111",
      "EC2SecurityGroupOwnerId":"111122223333"
   },
   {
      "EC2SecurityGroupId":"sg-ffd722222",
      "EC2SecurityGroupOwnerId":"111122223333"
   }
]
```

#### YAML
<a name="aws-properties-rds-dbsecuritygroup-ingress--examples--Specifying_an_ingress_rule--yaml"></a>

```
DBSecurityGroupIngress:
  - EC2SecurityGroupId: sg-b0ff1111
    EC2SecurityGroupOwnerId: '111122223333'
  - EC2SecurityGroupId: sg-ffd722222
    EC2SecurityGroupOwnerId: '111122223333'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
