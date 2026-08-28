---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-healthlake-datatransformationprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::HealthLake::DataTransformationProfile
<a name="aws-resource-healthlake-datatransformationprofile"></a>

Creates a data transformation profile in DRAFT state. Specify a built-in starter profile, an existing profile version, raw profile content, or a sample data file as the source.

## Syntax
<a name="aws-resource-healthlake-datatransformationprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-healthlake-datatransformationprofile-syntax.json"></a>

```
{
  "Type" : "AWS::HealthLake::DataTransformationProfile",
  "Properties" : {
      "[KmsKeyId](#cfn-healthlake-datatransformationprofile-kmskeyid)" : {{String}},
      "[ProfileDescription](#cfn-healthlake-datatransformationprofile-profiledescription)" : {{String}},
      "[ProfileName](#cfn-healthlake-datatransformationprofile-profilename)" : {{String}},
      "[Source](#cfn-healthlake-datatransformationprofile-source)" : {{Source}},
      "[SourceFormat](#cfn-healthlake-datatransformationprofile-sourceformat)" : {{String}},
      "[Tags](#cfn-healthlake-datatransformationprofile-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-healthlake-datatransformationprofile-syntax.yaml"></a>

```
Type: AWS::HealthLake::DataTransformationProfile
Properties:
  [KmsKeyId](#cfn-healthlake-datatransformationprofile-kmskeyid): {{String}}
  [ProfileDescription](#cfn-healthlake-datatransformationprofile-profiledescription): {{String}}
  [ProfileName](#cfn-healthlake-datatransformationprofile-profilename): {{String}}
  [Source](#cfn-healthlake-datatransformationprofile-source): {{
    Source}}
  [SourceFormat](#cfn-healthlake-datatransformationprofile-sourceformat): {{String}}
  [Tags](#cfn-healthlake-datatransformationprofile-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-healthlake-datatransformationprofile-properties"></a>

`KmsKeyId`  <a name="cfn-healthlake-datatransformationprofile-kmskeyid"></a>
The AWS Key Management Service (AWS KMS) key identifier used to encrypt the profile content at rest.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProfileDescription`  <a name="cfn-healthlake-datatransformationprofile-profiledescription"></a>
A human-readable description of the profile's purpose.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProfileName`  <a name="cfn-healthlake-datatransformationprofile-profilename"></a>
A name for the data transformation profile.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Source`  <a name="cfn-healthlake-datatransformationprofile-source"></a>
The source for the initial profile content. Specify a built-in starter profile, an existing profile version to clone, raw profile content for CI/CD workflows, or a sample data file in Amazon S3.
*Required*: No
*Type*: [Source](aws-properties-healthlake-datatransformationprofile-source.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceFormat`  <a name="cfn-healthlake-datatransformationprofile-sourceformat"></a>
The source data format that this profile converts from (Consolidated Clinical Document Architecture (C-CDA) or Comma-separated values (CSV)).
*Required*: Yes
*Type*: String
*Allowed values*: `CCDA | CSV`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-healthlake-datatransformationprofile-tags"></a>
The tags to associate with the profile at creation time.
*Required*: No
*Type*: Array of [Tag](aws-properties-healthlake-datatransformationprofile-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-healthlake-datatransformationprofile-return-values"></a>

### Ref
<a name="aws-resource-healthlake-datatransformationprofile-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-healthlake-datatransformationprofile-return-values-fn--getatt"></a>

####
<a name="aws-resource-healthlake-datatransformationprofile-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`ProfileId`  <a name="ProfileId-fn::getatt"></a>
The unique identifier of the profile.

`TargetFormat`  <a name="TargetFormat-fn::getatt"></a>
The target output format of the profile.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
