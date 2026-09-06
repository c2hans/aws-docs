---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-domain-singlesignon.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Domain SingleSignOn
<a name="aws-properties-datazone-domain-singlesignon"></a>

The single sign-on details in Amazon DataZone.

## Syntax
<a name="aws-properties-datazone-domain-singlesignon-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-domain-singlesignon-syntax.json"></a>

```
{
  "[IdcInstanceArn](#cfn-datazone-domain-singlesignon-idcinstancearn)" : {{String}},
  "[Type](#cfn-datazone-domain-singlesignon-type)" : {{String}},
  "[UserAssignment](#cfn-datazone-domain-singlesignon-userassignment)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-domain-singlesignon-syntax.yaml"></a>

```
  [IdcInstanceArn](#cfn-datazone-domain-singlesignon-idcinstancearn): {{String}}
  [Type](#cfn-datazone-domain-singlesignon-type): {{String}}
  [UserAssignment](#cfn-datazone-domain-singlesignon-userassignment): {{String}}
```

## Properties
<a name="aws-properties-datazone-domain-singlesignon-properties"></a>

`IdcInstanceArn`  <a name="cfn-datazone-domain-singlesignon-idcinstancearn"></a>
The ARN of the IDC instance.
*Required*: No
*Type*: String
*Pattern*: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
*Minimum*: `10`
*Maximum*: `1224`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-datazone-domain-singlesignon-type"></a>
The type of single sign-on in Amazon DataZone.
*Required*: No
*Type*: String
*Allowed values*: `IAM_IDC | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserAssignment`  <a name="cfn-datazone-domain-singlesignon-userassignment"></a>
The single sign-on user assignment in Amazon DataZone.
*Required*: No
*Type*: String
*Allowed values*: `AUTOMATIC | MANUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
