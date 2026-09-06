---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-workflow-efsinputfilelocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Workflow EfsInputFileLocation
<a name="aws-properties-transfer-workflow-efsinputfilelocation"></a>

Specifies the Amazon EFS identifier and the path for the file being used.

## Syntax
<a name="aws-properties-transfer-workflow-efsinputfilelocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-workflow-efsinputfilelocation-syntax.json"></a>

```
{
  "[FileSystemId](#cfn-transfer-workflow-efsinputfilelocation-filesystemid)" : {{String}},
  "[Path](#cfn-transfer-workflow-efsinputfilelocation-path)" : {{String}}
}
```

### YAML
<a name="aws-properties-transfer-workflow-efsinputfilelocation-syntax.yaml"></a>

```
  [FileSystemId](#cfn-transfer-workflow-efsinputfilelocation-filesystemid): {{String}}
  [Path](#cfn-transfer-workflow-efsinputfilelocation-path): {{String}}
```

## Properties
<a name="aws-properties-transfer-workflow-efsinputfilelocation-properties"></a>

`FileSystemId`  <a name="cfn-transfer-workflow-efsinputfilelocation-filesystemid"></a>
The identifier of the file system, assigned by Amazon EFS.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:(access-point/fsap|file-system/fs)-[0-9a-f]{8,40}|fs(ap)?-[0-9a-f]{8,40})$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Path`  <a name="cfn-transfer-workflow-efsinputfilelocation-path"></a>
The pathname for the folder being used by a workflow.
*Required*: No
*Type*: String
*Pattern*: `^[^\x00]+$`
*Minimum*: `1`
*Maximum*: `65536`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
