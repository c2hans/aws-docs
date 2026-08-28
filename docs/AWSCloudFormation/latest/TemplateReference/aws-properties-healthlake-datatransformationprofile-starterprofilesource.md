---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-healthlake-datatransformationprofile-starterprofilesource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::HealthLake::DataTransformationProfile StarterProfileSource
<a name="aws-properties-healthlake-datatransformationprofile-starterprofilesource"></a>

Identifies a built-in starter profile to use as the source when creating a data transformation profile. Valid only when the source format is Consolidated Clinical Document Architecture (C-CDA).

## Syntax
<a name="aws-properties-healthlake-datatransformationprofile-starterprofilesource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-healthlake-datatransformationprofile-starterprofilesource-syntax.json"></a>

```
{
  "[StarterProfileName](#cfn-healthlake-datatransformationprofile-starterprofilesource-starterprofilename)" : {{String}}
}
```

### YAML
<a name="aws-properties-healthlake-datatransformationprofile-starterprofilesource-syntax.yaml"></a>

```
  [StarterProfileName](#cfn-healthlake-datatransformationprofile-starterprofilesource-starterprofilename): {{String}}
```

## Properties
<a name="aws-properties-healthlake-datatransformationprofile-starterprofilesource-properties"></a>

`StarterProfileName`  <a name="cfn-healthlake-datatransformationprofile-starterprofilesource-starterprofilename"></a>
The name of the built-in starter profile.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
