---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-licensemanager-reportgenerator-s3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::ReportGenerator S3Location
<a name="aws-properties-licensemanager-reportgenerator-s3location"></a>

Details of the S3 bucket that report generator reports are published to.

## Syntax
<a name="aws-properties-licensemanager-reportgenerator-s3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-licensemanager-reportgenerator-s3location-syntax.json"></a>

```
{
  "[Bucket](#cfn-licensemanager-reportgenerator-s3location-bucket)" : {{String}},
  "[KeyPrefix](#cfn-licensemanager-reportgenerator-s3location-keyprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-licensemanager-reportgenerator-s3location-syntax.yaml"></a>

```
  [Bucket](#cfn-licensemanager-reportgenerator-s3location-bucket): {{String}}
  [KeyPrefix](#cfn-licensemanager-reportgenerator-s3location-keyprefix): {{String}}
```

## Properties
<a name="aws-properties-licensemanager-reportgenerator-s3location-properties"></a>

`Bucket`  <a name="cfn-licensemanager-reportgenerator-s3location-bucket"></a>
Name of the S3 bucket reports are published to.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyPrefix`  <a name="cfn-licensemanager-reportgenerator-s3location-keyprefix"></a>
Prefix of the S3 bucket reports are published to.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
