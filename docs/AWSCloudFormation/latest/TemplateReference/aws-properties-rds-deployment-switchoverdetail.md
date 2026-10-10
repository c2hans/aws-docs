---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rds-deployment-switchoverdetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::Deployment SwitchoverDetail
<a name="aws-properties-rds-deployment-switchoverdetail"></a>

Contains the details about a blue/green deployment.

For more information, see [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html) in the *Amazon RDS User Guide* and [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html) in the *Amazon Aurora User Guide*.

## Syntax
<a name="aws-properties-rds-deployment-switchoverdetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rds-deployment-switchoverdetail-syntax.json"></a>

```
{
  "[SourceMember](#cfn-rds-deployment-switchoverdetail-sourcemember)" : {{String}},
  "[SwitchoverDetailStatus](#cfn-rds-deployment-switchoverdetail-switchoverdetailstatus)" : {{String}},
  "[TargetMember](#cfn-rds-deployment-switchoverdetail-targetmember)" : {{String}}
}
```

### YAML
<a name="aws-properties-rds-deployment-switchoverdetail-syntax.yaml"></a>

```
  [SourceMember](#cfn-rds-deployment-switchoverdetail-sourcemember): {{String}}
  [SwitchoverDetailStatus](#cfn-rds-deployment-switchoverdetail-switchoverdetailstatus): {{String}}
  [TargetMember](#cfn-rds-deployment-switchoverdetail-targetmember): {{String}}
```

## Properties
<a name="aws-properties-rds-deployment-switchoverdetail-properties"></a>

`SourceMember`  <a name="cfn-rds-deployment-switchoverdetail-sourcemember"></a>
The Amazon Resource Name (ARN) of a resource in the blue environment.
*Required*: No
*Type*: String
*Pattern*: `^arn:[A-Za-z][0-9A-Za-z-:._]*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SwitchoverDetailStatus`  <a name="cfn-rds-deployment-switchoverdetail-switchoverdetailstatus"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetMember`  <a name="cfn-rds-deployment-switchoverdetail-targetmember"></a>
The Amazon Resource Name (ARN) of a resource in the green environment.
*Required*: No
*Type*: String
*Pattern*: `^arn:[A-Za-z][0-9A-Za-z-:._]*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
