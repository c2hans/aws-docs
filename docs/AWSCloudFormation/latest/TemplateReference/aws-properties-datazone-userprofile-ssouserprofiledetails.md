---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-userprofile-ssouserprofiledetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::UserProfile SsoUserProfileDetails
<a name="aws-properties-datazone-userprofile-ssouserprofiledetails"></a>

The SSO user profile detail.

## Syntax
<a name="aws-properties-datazone-userprofile-ssouserprofiledetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-userprofile-ssouserprofiledetails-syntax.json"></a>

```
{
  "[FirstName](#cfn-datazone-userprofile-ssouserprofiledetails-firstname)" : {{String}},
  "[LastName](#cfn-datazone-userprofile-ssouserprofiledetails-lastname)" : {{String}},
  "[Username](#cfn-datazone-userprofile-ssouserprofiledetails-username)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-userprofile-ssouserprofiledetails-syntax.yaml"></a>

```
  [FirstName](#cfn-datazone-userprofile-ssouserprofiledetails-firstname): {{String}}
  [LastName](#cfn-datazone-userprofile-ssouserprofiledetails-lastname): {{String}}
  [Username](#cfn-datazone-userprofile-ssouserprofiledetails-username): {{String}}
```

## Properties
<a name="aws-properties-datazone-userprofile-ssouserprofiledetails-properties"></a>

`FirstName`  <a name="cfn-datazone-userprofile-ssouserprofiledetails-firstname"></a>
The first name as part of the SSO user profile detail.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastName`  <a name="cfn-datazone-userprofile-ssouserprofiledetails-lastname"></a>
The last name as part of the SSO user profile detail.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-datazone-userprofile-ssouserprofiledetails-username"></a>
The username as part of the SSO user profile detail.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z_0-9+=,.@-]+$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
