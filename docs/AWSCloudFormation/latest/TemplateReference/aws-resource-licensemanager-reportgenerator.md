---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-licensemanager-reportgenerator.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::ReportGenerator
<a name="aws-resource-licensemanager-reportgenerator"></a>

Describe the details of a report generator.

## Syntax
<a name="aws-resource-licensemanager-reportgenerator-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-licensemanager-reportgenerator-syntax.json"></a>

```
{
  "Type" : "AWS::LicenseManager::ReportGenerator",
  "Properties" : {
      "[Description](#cfn-licensemanager-reportgenerator-description)" : {{String}},
      "[ReportContext](#cfn-licensemanager-reportgenerator-reportcontext)" : {{ReportContext}},
      "[ReportFrequency](#cfn-licensemanager-reportgenerator-reportfrequency)" : {{ReportFrequency}},
      "[ReportGeneratorName](#cfn-licensemanager-reportgenerator-reportgeneratorname)" : {{String}},
      "[ReportType](#cfn-licensemanager-reportgenerator-reporttype)" : {{[ String, ... ]}},
      "[Tags](#cfn-licensemanager-reportgenerator-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-licensemanager-reportgenerator-syntax.yaml"></a>

```
Type: AWS::LicenseManager::ReportGenerator
Properties:
  [Description](#cfn-licensemanager-reportgenerator-description): {{String}}
  [ReportContext](#cfn-licensemanager-reportgenerator-reportcontext): {{
    ReportContext}}
  [ReportFrequency](#cfn-licensemanager-reportgenerator-reportfrequency): {{
    ReportFrequency}}
  [ReportGeneratorName](#cfn-licensemanager-reportgenerator-reportgeneratorname): {{String}}
  [ReportType](#cfn-licensemanager-reportgenerator-reporttype): {{
    - String}}
  [Tags](#cfn-licensemanager-reportgenerator-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-licensemanager-reportgenerator-properties"></a>

`Description`  <a name="cfn-licensemanager-reportgenerator-description"></a>
Description of the report generator.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReportContext`  <a name="cfn-licensemanager-reportgenerator-reportcontext"></a>
License configuration type for this generator.
*Required*: Yes
*Type*: [ReportContext](aws-properties-licensemanager-reportgenerator-reportcontext.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReportFrequency`  <a name="cfn-licensemanager-reportgenerator-reportfrequency"></a>
Details about how frequently reports are generated.
*Required*: Yes
*Type*: [ReportFrequency](aws-properties-licensemanager-reportgenerator-reportfrequency.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReportGeneratorName`  <a name="cfn-licensemanager-reportgenerator-reportgeneratorname"></a>
Name of the report generator.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReportType`  <a name="cfn-licensemanager-reportgenerator-reporttype"></a>
Type of reports that are generated.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `LicenseConfigurationSummaryReport | LicenseConfigurationUsageReport | LicenseAssetGroupUsageReport`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-licensemanager-reportgenerator-tags"></a>
Tags associated with the report generator.
*Required*: No
*Type*: Array of [Tag](aws-properties-licensemanager-reportgenerator-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-licensemanager-reportgenerator-return-values"></a>

### Ref
<a name="aws-resource-licensemanager-reportgenerator-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-licensemanager-reportgenerator-return-values-fn--getatt"></a>

####
<a name="aws-resource-licensemanager-reportgenerator-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreateTime`  <a name="CreateTime-fn::getatt"></a>
Time the report was created.

`ReportCreatorAccount`  <a name="ReportCreatorAccount-fn::getatt"></a>
The AWS account ID used to create the report generator.
