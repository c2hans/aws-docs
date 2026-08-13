---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-assetbundleimportjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::AssetBundleImportJob
<a name="aws-resource-quicksight-assetbundleimportjob"></a>

<a name="aws-resource-quicksight-assetbundleimportjob-description"></a>The `AWS::QuickSight::AssetBundleImportJob` resource Property description not available. for QuickSight.

## Syntax
<a name="aws-resource-quicksight-assetbundleimportjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-assetbundleimportjob-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::AssetBundleImportJob",
  "Properties" : {
      "[AssetBundleImportJobId](#cfn-quicksight-assetbundleimportjob-assetbundleimportjobid)" : {{String}},
      "[AssetBundleImportSource](#cfn-quicksight-assetbundleimportjob-assetbundleimportsource)" : {{AssetBundleImportSourceDescription}},
      "[AwsAccountId](#cfn-quicksight-assetbundleimportjob-awsaccountid)" : {{String}},
      "[FailureAction](#cfn-quicksight-assetbundleimportjob-failureaction)" : {{String}},
      "[OverrideValidationStrategy](#cfn-quicksight-assetbundleimportjob-overridevalidationstrategy)" : {{AssetBundleImportJobOverrideValidationStrategy}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-assetbundleimportjob-syntax.yaml"></a>

```
Type: AWS::QuickSight::AssetBundleImportJob
Properties:
  [AssetBundleImportJobId](#cfn-quicksight-assetbundleimportjob-assetbundleimportjobid): {{String}}
  [AssetBundleImportSource](#cfn-quicksight-assetbundleimportjob-assetbundleimportsource): {{
    AssetBundleImportSourceDescription}}
  [AwsAccountId](#cfn-quicksight-assetbundleimportjob-awsaccountid): {{String}}
  [FailureAction](#cfn-quicksight-assetbundleimportjob-failureaction): {{String}}
  [OverrideValidationStrategy](#cfn-quicksight-assetbundleimportjob-overridevalidationstrategy): {{
    AssetBundleImportJobOverrideValidationStrategy}}
```

## Properties
<a name="aws-resource-quicksight-assetbundleimportjob-properties"></a>

`AssetBundleImportJobId`  <a name="cfn-quicksight-assetbundleimportjob-assetbundleimportjobid"></a>
The ID of the job. This ID is unique while the job is running. After the job is completed, you can reuse this ID for another job.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AssetBundleImportSource`  <a name="cfn-quicksight-assetbundleimportjob-assetbundleimportsource"></a>
The source of the asset bundle zip file that contains the data that you want to import. The file must be in `QUICKSIGHT_JSON` format.
*Required*: No
*Type*: [AssetBundleImportSourceDescription](aws-properties-quicksight-assetbundleimportjob-assetbundleimportsourcedescription.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AwsAccountId`  <a name="cfn-quicksight-assetbundleimportjob-awsaccountid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FailureAction`  <a name="cfn-quicksight-assetbundleimportjob-failureaction"></a>
The failure action for the import job.
*Required*: No
*Type*: String
*Allowed values*: `DO_NOTHING | ROLLBACK`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OverrideValidationStrategy`  <a name="cfn-quicksight-assetbundleimportjob-overridevalidationstrategy"></a>
The option to relax the validation that is required to create and update analyses, dashboards, and templates with definition objects. When you set this value to `LENIENT`, validation is skipped for specific errors.
*Required*: No
*Type*: [AssetBundleImportJobOverrideValidationStrategy](aws-properties-quicksight-assetbundleimportjob-assetbundleimportjoboverridevalidationstrategy.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-quicksight-assetbundleimportjob-return-values"></a>

### Ref
<a name="aws-resource-quicksight-assetbundleimportjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-assetbundleimportjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-assetbundleimportjob-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the import job.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The time that the import job was created.

`JobStatus`  <a name="JobStatus-fn::getatt"></a>
The current status of the import job.
