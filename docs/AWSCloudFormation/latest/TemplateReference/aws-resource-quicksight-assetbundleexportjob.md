---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-assetbundleexportjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::AssetBundleExportJob
<a name="aws-resource-quicksight-assetbundleexportjob"></a>

<a name="aws-resource-quicksight-assetbundleexportjob-description"></a>The `AWS::QuickSight::AssetBundleExportJob` resource Property description not available. for QuickSight.

## Syntax
<a name="aws-resource-quicksight-assetbundleexportjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-assetbundleexportjob-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::AssetBundleExportJob",
  "Properties" : {
      "[AssetBundleExportJobId](#cfn-quicksight-assetbundleexportjob-assetbundleexportjobid)" : {{String}},
      "[AwsAccountId](#cfn-quicksight-assetbundleexportjob-awsaccountid)" : {{String}},
      "[ExportFormat](#cfn-quicksight-assetbundleexportjob-exportformat)" : {{String}},
      "[IncludeAllDependencies](#cfn-quicksight-assetbundleexportjob-includealldependencies)" : {{Boolean}},
      "[IncludeFolderMembers](#cfn-quicksight-assetbundleexportjob-includefoldermembers)" : {{String}},
      "[IncludeFolderMemberships](#cfn-quicksight-assetbundleexportjob-includefoldermemberships)" : {{Boolean}},
      "[IncludePermissions](#cfn-quicksight-assetbundleexportjob-includepermissions)" : {{Boolean}},
      "[IncludeTags](#cfn-quicksight-assetbundleexportjob-includetags)" : {{Boolean}},
      "[ResourceArns](#cfn-quicksight-assetbundleexportjob-resourcearns)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-assetbundleexportjob-syntax.yaml"></a>

```
Type: AWS::QuickSight::AssetBundleExportJob
Properties:
  [AssetBundleExportJobId](#cfn-quicksight-assetbundleexportjob-assetbundleexportjobid): {{String}}
  [AwsAccountId](#cfn-quicksight-assetbundleexportjob-awsaccountid): {{String}}
  [ExportFormat](#cfn-quicksight-assetbundleexportjob-exportformat): {{String}}
  [IncludeAllDependencies](#cfn-quicksight-assetbundleexportjob-includealldependencies): {{Boolean}}
  [IncludeFolderMembers](#cfn-quicksight-assetbundleexportjob-includefoldermembers): {{String}}
  [IncludeFolderMemberships](#cfn-quicksight-assetbundleexportjob-includefoldermemberships): {{Boolean}}
  [IncludePermissions](#cfn-quicksight-assetbundleexportjob-includepermissions): {{Boolean}}
  [IncludeTags](#cfn-quicksight-assetbundleexportjob-includetags): {{Boolean}}
  [ResourceArns](#cfn-quicksight-assetbundleexportjob-resourcearns): {{
    - String}}
```

## Properties
<a name="aws-resource-quicksight-assetbundleexportjob-properties"></a>

`AssetBundleExportJobId`  <a name="cfn-quicksight-assetbundleexportjob-assetbundleexportjobid"></a>
The ID of the export job.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AwsAccountId`  <a name="cfn-quicksight-assetbundleexportjob-awsaccountid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExportFormat`  <a name="cfn-quicksight-assetbundleexportjob-exportformat"></a>
The format for the export job.
*Required*: Yes
*Type*: String
*Allowed values*: `CLOUDFORMATION_JSON | QUICKSIGHT_JSON`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IncludeAllDependencies`  <a name="cfn-quicksight-assetbundleexportjob-includealldependencies"></a>
The flag that determines the inclusion of resource dependencies in the returned asset bundle.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IncludeFolderMembers`  <a name="cfn-quicksight-assetbundleexportjob-includefoldermembers"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `RECURSE | ONE_LEVEL | NONE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IncludeFolderMemberships`  <a name="cfn-quicksight-assetbundleexportjob-includefoldermemberships"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IncludePermissions`  <a name="cfn-quicksight-assetbundleexportjob-includepermissions"></a>
The flag that determines the inclusion of permissions associated with each resource ARN.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IncludeTags`  <a name="cfn-quicksight-assetbundleexportjob-includetags"></a>
The flag that determines the inclusion of tags associated with each resource ARN.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceArns`  <a name="cfn-quicksight-assetbundleexportjob-resourcearns"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-quicksight-assetbundleexportjob-return-values"></a>

### Ref
<a name="aws-resource-quicksight-assetbundleexportjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-assetbundleexportjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-assetbundleexportjob-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the export job.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The time that the export job was created.

`JobStatus`  <a name="JobStatus-fn::getatt"></a>
The current status of the export job.
