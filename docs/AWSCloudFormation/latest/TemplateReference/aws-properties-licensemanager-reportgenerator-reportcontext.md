---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-licensemanager-reportgenerator-reportcontext.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::ReportGenerator ReportContext
<a name="aws-properties-licensemanager-reportgenerator-reportcontext"></a>

Details of the license configuration that this generator reports on.

## Syntax
<a name="aws-properties-licensemanager-reportgenerator-reportcontext-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-licensemanager-reportgenerator-reportcontext-syntax.json"></a>

```
{
  "[LicenseAssetGroupArns](#cfn-licensemanager-reportgenerator-reportcontext-licenseassetgrouparns)" : {{[ String, ... ]}},
  "[LicenseConfigurationArns](#cfn-licensemanager-reportgenerator-reportcontext-licenseconfigurationarns)" : {{[ String, ... ]}},
  "[ReportEndDate](#cfn-licensemanager-reportgenerator-reportcontext-reportenddate)" : {{String}},
  "[ReportStartDate](#cfn-licensemanager-reportgenerator-reportcontext-reportstartdate)" : {{String}}
}
```

### YAML
<a name="aws-properties-licensemanager-reportgenerator-reportcontext-syntax.yaml"></a>

```
  [LicenseAssetGroupArns](#cfn-licensemanager-reportgenerator-reportcontext-licenseassetgrouparns): {{
    - String}}
  [LicenseConfigurationArns](#cfn-licensemanager-reportgenerator-reportcontext-licenseconfigurationarns): {{
    - String}}
  [ReportEndDate](#cfn-licensemanager-reportgenerator-reportcontext-reportenddate): {{String}}
  [ReportStartDate](#cfn-licensemanager-reportgenerator-reportcontext-reportstartdate): {{String}}
```

## Properties
<a name="aws-properties-licensemanager-reportgenerator-reportcontext-properties"></a>

`LicenseAssetGroupArns`  <a name="cfn-licensemanager-reportgenerator-reportcontext-licenseassetgrouparns"></a>
Amazon Resource Names (ARNs) of the license asset groups to include in the report.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LicenseConfigurationArns`  <a name="cfn-licensemanager-reportgenerator-reportcontext-licenseconfigurationarns"></a>
Amazon Resource Name (ARN) of the license configuration that this generator reports on.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReportEndDate`  <a name="cfn-licensemanager-reportgenerator-reportcontext-reportenddate"></a>
End date for the report data collection period.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReportStartDate`  <a name="cfn-licensemanager-reportgenerator-reportcontext-reportstartdate"></a>
Start date for the report data collection period.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
