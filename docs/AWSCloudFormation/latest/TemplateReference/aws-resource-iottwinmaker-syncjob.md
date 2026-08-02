---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iottwinmaker-syncjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::SyncJob
<a name="aws-resource-iottwinmaker-syncjob"></a>

The SyncJob.

## Syntax
<a name="aws-resource-iottwinmaker-syncjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iottwinmaker-syncjob-syntax.json"></a>

```
{
  "Type" : "AWS::IoTTwinMaker::SyncJob",
  "Properties" : {
      "[SyncRole](#cfn-iottwinmaker-syncjob-syncrole)" : {{String}},
      "[SyncSource](#cfn-iottwinmaker-syncjob-syncsource)" : {{String}},
      "[Tags](#cfn-iottwinmaker-syncjob-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[WorkspaceId](#cfn-iottwinmaker-syncjob-workspaceid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-iottwinmaker-syncjob-syntax.yaml"></a>

```
Type: AWS::IoTTwinMaker::SyncJob
Properties:
  [SyncRole](#cfn-iottwinmaker-syncjob-syncrole): {{String}}
  [SyncSource](#cfn-iottwinmaker-syncjob-syncsource): {{String}}
  [Tags](#cfn-iottwinmaker-syncjob-tags): {{
    {{Key}}: {{Value}}}}
  [WorkspaceId](#cfn-iottwinmaker-syncjob-workspaceid): {{String}}
```

## Properties
<a name="aws-resource-iottwinmaker-syncjob-properties"></a>

`SyncRole`  <a name="cfn-iottwinmaker-syncjob-syncrole"></a>
The SyncJob IAM role. This IAM role is used by the sync job to read from the syncSource, and create, update or delete the corresponding resources.
*Required*: Yes
*Type*: String
*Pattern*: `arn:((aws)|(aws-cn)|(aws-us-gov)):iam::[0-9]{12}:role/.*`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SyncSource`  <a name="cfn-iottwinmaker-syncjob-syncsource"></a>
The sync source.
Currently the only supported syncSoucre is `SITEWISE`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-iottwinmaker-syncjob-tags"></a>
Metadata you can use to manage the SyncJob.
*Required*: No
*Type*: Object of String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkspaceId`  <a name="cfn-iottwinmaker-syncjob-workspaceid"></a>
The ID of the workspace that contains the sync job.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iottwinmaker-syncjob-return-values"></a>

### Ref
<a name="aws-resource-iottwinmaker-syncjob-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the workspace Id and the entity Id.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-iottwinmaker-syncjob-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iottwinmaker-syncjob-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The SyncJob ARN.

`CreationDateTime`  <a name="CreationDateTime-fn::getatt"></a>
The creation date and time of the SyncJob.

`State`  <a name="State-fn::getatt"></a>
The SyncJob's state.

`UpdateDateTime`  <a name="UpdateDateTime-fn::getatt"></a>
The update date and time.
