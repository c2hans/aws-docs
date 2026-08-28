---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-healthlake-datatransformationprofile-existingversionedprofilesource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::HealthLake::DataTransformationProfile ExistingVersionedProfileSource
<a name="aws-properties-healthlake-datatransformationprofile-existingversionedprofilesource"></a>

Identifies an existing data transformation profile and version to clone when creating a new profile.

## Syntax
<a name="aws-properties-healthlake-datatransformationprofile-existingversionedprofilesource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-healthlake-datatransformationprofile-existingversionedprofilesource-syntax.json"></a>

```
{
  "[ProfileId](#cfn-healthlake-datatransformationprofile-existingversionedprofilesource-profileid)" : {{String}},
  "[Version](#cfn-healthlake-datatransformationprofile-existingversionedprofilesource-version)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-healthlake-datatransformationprofile-existingversionedprofilesource-syntax.yaml"></a>

```
  [ProfileId](#cfn-healthlake-datatransformationprofile-existingversionedprofilesource-profileid): {{String}}
  [Version](#cfn-healthlake-datatransformationprofile-existingversionedprofilesource-version): {{Integer}}
```

## Properties
<a name="aws-properties-healthlake-datatransformationprofile-existingversionedprofilesource-properties"></a>

`ProfileId`  <a name="cfn-healthlake-datatransformationprofile-existingversionedprofilesource-profileid"></a>
The unique identifier of the existing profile to clone from.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Version`  <a name="cfn-healthlake-datatransformationprofile-existingversionedprofilesource-version"></a>
The version number of the existing profile to clone from.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
