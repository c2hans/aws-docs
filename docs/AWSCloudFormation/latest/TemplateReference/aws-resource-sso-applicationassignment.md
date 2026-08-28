---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sso-applicationassignment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSO::ApplicationAssignment
<a name="aws-resource-sso-applicationassignment"></a>

A structure that describes an assignment of a principal to an application.

## Syntax
<a name="aws-resource-sso-applicationassignment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sso-applicationassignment-syntax.json"></a>

```
{
  "Type" : "AWS::SSO::ApplicationAssignment",
  "Properties" : {
      "[ApplicationArn](#cfn-sso-applicationassignment-applicationarn)" : {{String}},
      "[PrincipalId](#cfn-sso-applicationassignment-principalid)" : {{String}},
      "[PrincipalType](#cfn-sso-applicationassignment-principaltype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-sso-applicationassignment-syntax.yaml"></a>

```
Type: AWS::SSO::ApplicationAssignment
Properties:
  [ApplicationArn](#cfn-sso-applicationassignment-applicationarn): {{String}}
  [PrincipalId](#cfn-sso-applicationassignment-principalid): {{String}}
  [PrincipalType](#cfn-sso-applicationassignment-principaltype): {{String}}
```

## Properties
<a name="aws-resource-sso-applicationassignment-properties"></a>

`ApplicationArn`  <a name="cfn-sso-applicationassignment-applicationarn"></a>
The ARN of the application that has principals assigned.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
*Minimum*: `10`
*Maximum*: `1224`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrincipalId`  <a name="cfn-sso-applicationassignment-principalid"></a>
The unique identifier of the principal assigned to the application.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$`
*Minimum*: `1`
*Maximum*: `47`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrincipalType`  <a name="cfn-sso-applicationassignment-principaltype"></a>
The type of the principal assigned to the application.
*Required*: Yes
*Type*: String
*Allowed values*: `USER | GROUP`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sso-applicationassignment-return-values"></a>

### Ref
<a name="aws-resource-sso-applicationassignment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a generated ID, combined by all fields with the delimiter `|`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-sso-applicationassignment--examples"></a>

### Creating a new application assignment for IAM Identity Center
<a name="aws-resource-sso-applicationassignment--examples--Creating_a_new_application_assignment_for"></a>

The following example grants the user permission to access the example application.

#### JSON
<a name="aws-resource-sso-applicationassignment--examples--Creating_a_new_application_assignment_for--json"></a>

```
"ApplicationAssignment": {
    "Type": "AWS::SSO::ApplicationAssignment",
    "Properties": {
        "ApplicationArn": "arn:aws:sso:::application/ssoins-exampleapplicationid",
        "PrincipalID": "user_id",
        "PrincipalType": "USER"
    }
}
```

#### YAML
<a name="aws-resource-sso-applicationassignment--examples--Creating_a_new_application_assignment_for--yaml"></a>

```
ApplicationAssignment:
    Type: AWS::SSO::ApplicationAssignment
    Properties:
        ApplicationArn: 'arn:aws:sso:::application/ssoins-exampleapplicationid'
        PrincipalID: 'user_id'
        PrincipalType: 'USER'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
