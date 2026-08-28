---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-finspace-environment-superuserparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FinSpace::Environment SuperuserParameters
<a name="aws-properties-finspace-environment-superuserparameters"></a>

Configuration information for the superuser.

## Syntax
<a name="aws-properties-finspace-environment-superuserparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-finspace-environment-superuserparameters-syntax.json"></a>

```
{
  "[EmailAddress](#cfn-finspace-environment-superuserparameters-emailaddress)" : {{String}},
  "[FirstName](#cfn-finspace-environment-superuserparameters-firstname)" : {{String}},
  "[LastName](#cfn-finspace-environment-superuserparameters-lastname)" : {{String}}
}
```

### YAML
<a name="aws-properties-finspace-environment-superuserparameters-syntax.yaml"></a>

```
  [EmailAddress](#cfn-finspace-environment-superuserparameters-emailaddress): {{String}}
  [FirstName](#cfn-finspace-environment-superuserparameters-firstname): {{String}}
  [LastName](#cfn-finspace-environment-superuserparameters-lastname): {{String}}
```

## Properties
<a name="aws-properties-finspace-environment-superuserparameters-properties"></a>

`EmailAddress`  <a name="cfn-finspace-environment-superuserparameters-emailaddress"></a>
The email address of the superuser.
*Required*: No
*Type*: String
*Pattern*: `[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+[.]+[A-Za-z]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FirstName`  <a name="cfn-finspace-environment-superuserparameters-firstname"></a>
The first name of the superuser.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]{1,50}$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LastName`  <a name="cfn-finspace-environment-superuserparameters-lastname"></a>
The last name of the superuser.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]{1,50}$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
