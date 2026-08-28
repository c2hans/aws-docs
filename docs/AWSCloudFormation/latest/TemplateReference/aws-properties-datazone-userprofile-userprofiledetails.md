---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-userprofile-userprofiledetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::UserProfile UserProfileDetails
<a name="aws-properties-datazone-userprofile-userprofiledetails"></a>

The user profile details.

## Syntax
<a name="aws-properties-datazone-userprofile-userprofiledetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-userprofile-userprofiledetails-syntax.json"></a>

```
{
  "[Iam](#cfn-datazone-userprofile-userprofiledetails-iam)" : {{IamUserProfileDetails}},
  "[Sso](#cfn-datazone-userprofile-userprofiledetails-sso)" : {{SsoUserProfileDetails}}
}
```

### YAML
<a name="aws-properties-datazone-userprofile-userprofiledetails-syntax.yaml"></a>

```
  [Iam](#cfn-datazone-userprofile-userprofiledetails-iam): {{
    IamUserProfileDetails}}
  [Sso](#cfn-datazone-userprofile-userprofiledetails-sso): {{
    SsoUserProfileDetails}}
```

## Properties
<a name="aws-properties-datazone-userprofile-userprofiledetails-properties"></a>

`Iam`  <a name="cfn-datazone-userprofile-userprofiledetails-iam"></a>
The IAM details of the user profile.
*Required*: No
*Type*: [IamUserProfileDetails](aws-properties-datazone-userprofile-iamuserprofiledetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sso`  <a name="cfn-datazone-userprofile-userprofiledetails-sso"></a>
The SSO details of the user profile.
*Required*: No
*Type*: [SsoUserProfileDetails](aws-properties-datazone-userprofile-ssouserprofiledetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
