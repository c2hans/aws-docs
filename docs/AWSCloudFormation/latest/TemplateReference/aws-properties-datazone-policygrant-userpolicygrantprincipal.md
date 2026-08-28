---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-policygrant-userpolicygrantprincipal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::PolicyGrant UserPolicyGrantPrincipal
<a name="aws-properties-datazone-policygrant-userpolicygrantprincipal"></a>

The user policy grant principal.

## Syntax
<a name="aws-properties-datazone-policygrant-userpolicygrantprincipal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-policygrant-userpolicygrantprincipal-syntax.json"></a>

```
{
  "[AllUsersGrantFilter](#cfn-datazone-policygrant-userpolicygrantprincipal-allusersgrantfilter)" : {{Json}},
  "[UserIdentifier](#cfn-datazone-policygrant-userpolicygrantprincipal-useridentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-policygrant-userpolicygrantprincipal-syntax.yaml"></a>

```
  [AllUsersGrantFilter](#cfn-datazone-policygrant-userpolicygrantprincipal-allusersgrantfilter): {{Json}}
  [UserIdentifier](#cfn-datazone-policygrant-userpolicygrantprincipal-useridentifier): {{String}}
```

## Properties
<a name="aws-properties-datazone-policygrant-userpolicygrantprincipal-properties"></a>

`AllUsersGrantFilter`  <a name="cfn-datazone-policygrant-userpolicygrantprincipal-allusersgrantfilter"></a>
The all users grant filter of the user policy grant principal.
*Required*: No
*Type*: Json
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserIdentifier`  <a name="cfn-datazone-policygrant-userpolicygrantprincipal-useridentifier"></a>
The user ID of the user policy grant principal.
*Required*: No
*Type*: String
*Pattern*: `(^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$|^[a-zA-Z_0-9+=,.@-]+$|^arn:aws[^:]*:iam::\d{12}:.+$)`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
