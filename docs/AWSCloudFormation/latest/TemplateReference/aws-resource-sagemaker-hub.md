---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-hub.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Hub
<a name="aws-resource-sagemaker-hub"></a>

Create a hub.

## Syntax
<a name="aws-resource-sagemaker-hub-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-hub-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::Hub",
  "Properties" : {
      "[HubDescription](#cfn-sagemaker-hub-hubdescription)" : {{String}},
      "[HubDisplayName](#cfn-sagemaker-hub-hubdisplayname)" : {{String}},
      "[HubName](#cfn-sagemaker-hub-hubname)" : {{String}},
      "[HubSearchKeywords](#cfn-sagemaker-hub-hubsearchkeywords)" : {{[ String, ... ]}},
      "[S3StorageConfig](#cfn-sagemaker-hub-s3storageconfig)" : {{S3StorageConfig}},
      "[Tags](#cfn-sagemaker-hub-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-hub-syntax.yaml"></a>

```
Type: AWS::SageMaker::Hub
Properties:
  [HubDescription](#cfn-sagemaker-hub-hubdescription): {{String}}
  [HubDisplayName](#cfn-sagemaker-hub-hubdisplayname): {{String}}
  [HubName](#cfn-sagemaker-hub-hubname): {{String}}
  [HubSearchKeywords](#cfn-sagemaker-hub-hubsearchkeywords): {{
    - String}}
  [S3StorageConfig](#cfn-sagemaker-hub-s3storageconfig): {{
    S3StorageConfig}}
  [Tags](#cfn-sagemaker-hub-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sagemaker-hub-properties"></a>

`HubDescription`  <a name="cfn-sagemaker-hub-hubdescription"></a>
A description of the hub.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `1023`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HubDisplayName`  <a name="cfn-sagemaker-hub-hubdisplayname"></a>
The display name of the hub.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HubName`  <a name="cfn-sagemaker-hub-hubname"></a>
The name of the hub.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$`
*Minimum*: `0`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HubSearchKeywords`  <a name="cfn-sagemaker-hub-hubsearchkeywords"></a>
The searchable keywords for the hub.
*Required*: No
*Type*: Array of String
*Minimum*: `0 | 0`
*Maximum*: `255 | 50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3StorageConfig`  <a name="cfn-sagemaker-hub-s3storageconfig"></a>
The Amazon Simple Storage (Amazon S3) location and security configuration for `OfflineStore`.
*Required*: No
*Type*: [S3StorageConfig](aws-properties-sagemaker-hub-s3storageconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-hub-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-hub-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-hub-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-hub-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-hub-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-hub-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The date and time that the hub was created.

`HubArn`  <a name="HubArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the hub.

`HubStatus`  <a name="HubStatus-fn::getatt"></a>
The status of the hub.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The date and time that the hub was last modified.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
