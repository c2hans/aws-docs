---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-capacityprovider-capacityproviderpermissionsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::CapacityProvider CapacityProviderPermissionsConfig
<a name="aws-properties-lambda-capacityprovider-capacityproviderpermissionsconfig"></a>

Configuration that specifies the permissions required for the capacity provider to manage compute resources.

## Syntax
<a name="aws-properties-lambda-capacityprovider-capacityproviderpermissionsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-capacityprovider-capacityproviderpermissionsconfig-syntax.json"></a>

```
{
  "[CapacityProviderOperatorRoleArn](#cfn-lambda-capacityprovider-capacityproviderpermissionsconfig-capacityprovideroperatorrolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-capacityprovider-capacityproviderpermissionsconfig-syntax.yaml"></a>

```
  [CapacityProviderOperatorRoleArn](#cfn-lambda-capacityprovider-capacityproviderpermissionsconfig-capacityprovideroperatorrolearn): {{String}}
```

## Properties
<a name="aws-properties-lambda-capacityprovider-capacityproviderpermissionsconfig-properties"></a>

`CapacityProviderOperatorRoleArn`  <a name="cfn-lambda-capacityprovider-capacityproviderpermissionsconfig-capacityprovideroperatorrolearn"></a>
The ARN of the IAM role that the capacity provider uses to manage compute instances and other AWS resources.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `0`
*Maximum*: `10000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
