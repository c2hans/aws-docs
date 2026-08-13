---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-imagebuilder-workflow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::Workflow
<a name="aws-resource-imagebuilder-workflow"></a>

Create a new workflow or a new version of an existing workflow.

## Syntax
<a name="aws-resource-imagebuilder-workflow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-imagebuilder-workflow-syntax.json"></a>

```
{
  "Type" : "AWS::ImageBuilder::Workflow",
  "Properties" : {
      "[ChangeDescription](#cfn-imagebuilder-workflow-changedescription)" : {{String}},
      "[Data](#cfn-imagebuilder-workflow-data)" : {{String}},
      "[Description](#cfn-imagebuilder-workflow-description)" : {{String}},
      "[KmsKeyId](#cfn-imagebuilder-workflow-kmskeyid)" : {{String}},
      "[Name](#cfn-imagebuilder-workflow-name)" : {{String}},
      "[Tags](#cfn-imagebuilder-workflow-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Type](#cfn-imagebuilder-workflow-type)" : {{String}},
      "[Uri](#cfn-imagebuilder-workflow-uri)" : {{String}},
      "[Version](#cfn-imagebuilder-workflow-version)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-imagebuilder-workflow-syntax.yaml"></a>

```
Type: AWS::ImageBuilder::Workflow
Properties:
  [ChangeDescription](#cfn-imagebuilder-workflow-changedescription): {{String}}
  [Data](#cfn-imagebuilder-workflow-data): {{String}}
  [Description](#cfn-imagebuilder-workflow-description): {{String}}
  [KmsKeyId](#cfn-imagebuilder-workflow-kmskeyid): {{String}}
  [Name](#cfn-imagebuilder-workflow-name): {{String}}
  [Tags](#cfn-imagebuilder-workflow-tags): {{
    {{Key}}: {{Value}}}}
  [Type](#cfn-imagebuilder-workflow-type): {{String}}
  [Uri](#cfn-imagebuilder-workflow-uri): {{String}}
  [Version](#cfn-imagebuilder-workflow-version): {{String}}
```

## Properties
<a name="aws-resource-imagebuilder-workflow-properties"></a>

`ChangeDescription`  <a name="cfn-imagebuilder-workflow-changedescription"></a>
Describes what change has been made in this version of the workflow, or what makes this version different from other versions of the workflow.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Data`  <a name="cfn-imagebuilder-workflow-data"></a>
Contains the UTF-8 encoded YAML document content for the workflow. Alternatively, you can specify the `uri` of a YAML document file stored in Amazon S3. However, you cannot specify both properties.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `16000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-imagebuilder-workflow-description"></a>
Describes the workflow.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-imagebuilder-workflow-kmskeyid"></a>
The Amazon Resource Name (ARN) that uniquely identifies the KMS key used to encrypt this workflow resource. This can be either the Key ARN or the Alias ARN. For more information, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) in the *AWS Key Management Service Developer Guide*.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-imagebuilder-workflow-name"></a>
The name of the workflow to create.
*Required*: Yes
*Type*: String
*Pattern*: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-imagebuilder-workflow-tags"></a>
Tags that apply to the workflow resource.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-imagebuilder-workflow-type"></a>
The phase in the image build process for which the workflow resource is responsible.
*Required*: Yes
*Type*: String
*Allowed values*: `BUILD | TEST | DISTRIBUTION`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Uri`  <a name="cfn-imagebuilder-workflow-uri"></a>
The `uri` of a YAML component document file. This must be an S3 URL (`s3://bucket/key`), and the requester must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota.
Alternatively, you can specify the YAML document inline, using the component `data` property. You cannot specify both properties.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Version`  <a name="cfn-imagebuilder-workflow-version"></a>
The semantic version of this workflow resource. The semantic version syntax adheres to the following rules.
The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.
**Assignment:** For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.
**Patterns:** You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]+\.[0-9]+\.[0-9]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-imagebuilder-workflow-return-values"></a>

### Ref
<a name="aws-resource-imagebuilder-workflow-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource ARN, such as `arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/1.0.0/1`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-imagebuilder-workflow-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-imagebuilder-workflow-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the workflow resource.

`LatestVersion.Arn`  <a name="LatestVersion.Arn-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) of the Image Builder resource.

`LatestVersion.Major`  <a name="LatestVersion.Major-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) with the same `major` version of the Image Builder resource.

`LatestVersion.Minor`  <a name="LatestVersion.Minor-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) with the same `minor` version of the Image Builder resource.

`LatestVersion.Patch`  <a name="LatestVersion.Patch-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) with the same `patch` version of the Image Builder resource.

## Examples
<a name="aws-resource-imagebuilder-workflow--examples"></a>

### Create a build workflow using inline Data
<a name="aws-resource-imagebuilder-workflow--examples--Create_a_build_workflow_using_inline_Data"></a>

The following example creates a build workflow with inline YAML content. You can use either the `Data` or `Uri` property to provide the workflow document, but not both.

#### YAML
<a name="aws-resource-imagebuilder-workflow--examples--Create_a_build_workflow_using_inline_Data--yaml"></a>

```
Resources:
  BuildWorkflow:
    Type: AWS::ImageBuilder::Workflow
    Properties:
      Name: my-build-workflow
      Version: '1.0.0'
      Type: BUILD
      Description: Custom build workflow
      ChangeDescription: Initial version
      Data: |
        name: my-build-workflow
        description: Custom build workflow
        schemaVersion: 1.0
        steps:
          - name: LaunchBuildInstance
            action: LaunchInstance
            onFailure: Abort
            inputs:
              waitFor: ssmAgent
          - name: ApplyBuildComponents
            action: ExecuteComponents
            onFailure: Abort
            inputs:
              instanceId.$: $.stepOutputs.LaunchBuildInstance.instanceId
          - name: CreateOutputImage
            action: CreateImage
            onFailure: Abort
            inputs:
              instanceId.$: $.stepOutputs.LaunchBuildInstance.instanceId
          - name: TerminateBuildInstance
            action: TerminateInstance
            onFailure: Continue
            inputs:
              instanceId.$: $.stepOutputs.LaunchBuildInstance.instanceId
      Tags:
        Team: imaging
```

#### JSON
<a name="aws-resource-imagebuilder-workflow--examples--Create_a_build_workflow_using_inline_Data--json"></a>

```
{
    "Resources": {
        "BuildWorkflow": {
            "Type": "AWS::ImageBuilder::Workflow",
            "Properties": {
                "Name": "my-build-workflow",
                "Version": "1.0.0",
                "Type": "BUILD",
                "Description": "Custom build workflow",
                "ChangeDescription": "Initial version",
                "Data": "name: my-build-workflow\ndescription: Custom build workflow\nschemaVersion: 1.0\nsteps:\n  - name: LaunchBuildInstance\n    action: LaunchInstance\n    onFailure: Abort\n    inputs:\n      waitFor: ssmAgent\n  - name: ApplyBuildComponents\n    action: ExecuteComponents\n    onFailure: Abort\n    inputs:\n      instanceId.$: $.stepOutputs.LaunchBuildInstance.instanceId\n  - name: CreateOutputImage\n    action: CreateImage\n    onFailure: Abort\n    inputs:\n      instanceId.$: $.stepOutputs.LaunchBuildInstance.instanceId\n  - name: TerminateBuildInstance\n    action: TerminateInstance\n    onFailure: Continue\n    inputs:\n      instanceId.$: $.stepOutputs.LaunchBuildInstance.instanceId\n",
                "Tags": {
                    "Team": "imaging"
                }
            }
        }
    }
}
```

## See also
<a name="aws-resource-imagebuilder-workflow--seealso"></a>
+ [Manage image workflows](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-image-workflows.html) in the *Image Builder User Guide*.
