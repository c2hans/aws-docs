---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-knowledgebase.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::KnowledgeBase
<a name="aws-resource-quicksight-knowledgebase"></a>

Creates a knowledge base from a specified data source. Supported data source connector types include:
+ `S3_KNOWLEDGE_BASE` – Uses an Amazon S3 bucket as the data source.
+ `WEB_CRAWLER` – Uses web pages indexed by the built-in web crawler as the data source.
+ `GOOGLE_DRIVE` – Uses Google Drive as the data source. Supports service account authentication only.
+ `SHAREPOINT` – Uses SharePoint as the data source. Supports two-legged OAuth only.
+ `ONE_DRIVE` – Uses OneDrive as the data source. Supports two-legged OAuth only.

## Syntax
<a name="aws-resource-quicksight-knowledgebase-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-knowledgebase-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::KnowledgeBase",
  "Properties" : {
      "[AccessControlConfiguration](#cfn-quicksight-knowledgebase-accesscontrolconfiguration)" : {{AccessControlConfiguration}},
      "[AwsAccountId](#cfn-quicksight-knowledgebase-awsaccountid)" : {{String}},
      "[DataSourceArn](#cfn-quicksight-knowledgebase-datasourcearn)" : {{String}},
      "[Description](#cfn-quicksight-knowledgebase-description)" : {{String}},
      "[IsEmailNotificationOptedForIngestionFailures](#cfn-quicksight-knowledgebase-isemailnotificationoptedforingestionfailures)" : {{Boolean}},
      "[KnowledgeBaseConfiguration](#cfn-quicksight-knowledgebase-knowledgebaseconfiguration)" : {{KnowledgeBaseConfiguration}},
      "[KnowledgeBaseId](#cfn-quicksight-knowledgebase-knowledgebaseid)" : {{String}},
      "[MediaExtractionConfiguration](#cfn-quicksight-knowledgebase-mediaextractionconfiguration)" : {{MediaExtractionConfiguration}},
      "[Name](#cfn-quicksight-knowledgebase-name)" : {{String}},
      "[Permissions](#cfn-quicksight-knowledgebase-permissions)" : {{[ ResourcePermission, ... ]}},
      "[PrimaryOwnerArn](#cfn-quicksight-knowledgebase-primaryownerarn)" : {{String}},
      "[Tags](#cfn-quicksight-knowledgebase-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-knowledgebase-syntax.yaml"></a>

```
Type: AWS::QuickSight::KnowledgeBase
Properties:
  [AccessControlConfiguration](#cfn-quicksight-knowledgebase-accesscontrolconfiguration): {{
    AccessControlConfiguration}}
  [AwsAccountId](#cfn-quicksight-knowledgebase-awsaccountid): {{String}}
  [DataSourceArn](#cfn-quicksight-knowledgebase-datasourcearn): {{String}}
  [Description](#cfn-quicksight-knowledgebase-description): {{String}}
  [IsEmailNotificationOptedForIngestionFailures](#cfn-quicksight-knowledgebase-isemailnotificationoptedforingestionfailures): {{Boolean}}
  [KnowledgeBaseConfiguration](#cfn-quicksight-knowledgebase-knowledgebaseconfiguration): {{
    KnowledgeBaseConfiguration}}
  [KnowledgeBaseId](#cfn-quicksight-knowledgebase-knowledgebaseid): {{String}}
  [MediaExtractionConfiguration](#cfn-quicksight-knowledgebase-mediaextractionconfiguration): {{
    MediaExtractionConfiguration}}
  [Name](#cfn-quicksight-knowledgebase-name): {{String}}
  [Permissions](#cfn-quicksight-knowledgebase-permissions): {{
    - ResourcePermission}}
  [PrimaryOwnerArn](#cfn-quicksight-knowledgebase-primaryownerarn): {{String}}
  [Tags](#cfn-quicksight-knowledgebase-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-quicksight-knowledgebase-properties"></a>

`AccessControlConfiguration`  <a name="cfn-quicksight-knowledgebase-accesscontrolconfiguration"></a>
The access control configuration for the knowledge base.
*Required*: No
*Type*: [AccessControlConfiguration](aws-properties-quicksight-knowledgebase-accesscontrolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsAccountId`  <a name="cfn-quicksight-knowledgebase-awsaccountid"></a>
The ID of the AWS account that contains the knowledge base.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]*$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataSourceArn`  <a name="cfn-quicksight-knowledgebase-datasourcearn"></a>
The ARN of the data source associated with the knowledge base.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}$`
*Minimum*: `0`
*Maximum*: `1284`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-quicksight-knowledgebase-description"></a>
The description of the knowledge base.
*Required*: No
*Type*: String
*Pattern*: `^\P{C}*$`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsEmailNotificationOptedForIngestionFailures`  <a name="cfn-quicksight-knowledgebase-isemailnotificationoptedforingestionfailures"></a>
Specifies whether email notifications are enabled for ingestion failures.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KnowledgeBaseConfiguration`  <a name="cfn-quicksight-knowledgebase-knowledgebaseconfiguration"></a>
The configuration settings for the knowledge base.
*Required*: Yes
*Type*: [KnowledgeBaseConfiguration](aws-properties-quicksight-knowledgebase-knowledgebaseconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KnowledgeBaseId`  <a name="cfn-quicksight-knowledgebase-knowledgebaseid"></a>
The unique identifier for the knowledge base.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z-_=.+]+$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MediaExtractionConfiguration`  <a name="cfn-quicksight-knowledgebase-mediaextractionconfiguration"></a>
The media extraction configuration for the knowledge base.
*Required*: No
*Type*: [MediaExtractionConfiguration](aws-properties-quicksight-knowledgebase-mediaextractionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-knowledgebase-name"></a>
The name of the knowledge base.
*Required*: Yes
*Type*: String
*Pattern*: `^[\p{L}\p{N}][\p{L}\p{N} _\-\.]*$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Permissions`  <a name="cfn-quicksight-knowledgebase-permissions"></a>
A list of resource permissions on the knowledge base. Each entry grants a specified Amazon QuickSight principal either owner or viewer access. If you don't specify permissions, only the primary owner (if provided) receives owner access.
*Required*: No
*Type*: Array of [ResourcePermission](aws-properties-quicksight-knowledgebase-resourcepermission.md)
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryOwnerArn`  <a name="cfn-quicksight-knowledgebase-primaryownerarn"></a>
The ARN of the primary owner of the knowledge base.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-quicksight-knowledgebase-tags"></a>
The tags to assign to the knowledge base. If you don't specify tags, the knowledge base is created without tags.
*Required*: No
*Type*: Array of [Tag](aws-properties-quicksight-knowledgebase-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-knowledgebase-return-values"></a>

### Ref
<a name="aws-resource-quicksight-knowledgebase-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-knowledgebase-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-knowledgebase-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time that the knowledge base was created.

`DocumentCount`  <a name="DocumentCount-fn::getatt"></a>
The number of documents in the knowledge base.

`KnowledgeBaseArn`  <a name="KnowledgeBaseArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the knowledge base.

`KnowledgeBaseSizeBytes`  <a name="KnowledgeBaseSizeBytes-fn::getatt"></a>
The size of the knowledge base in bytes.

`PrimaryOwnerUsername`  <a name="PrimaryOwnerUsername-fn::getatt"></a>
The username of the primary owner of the knowledge base.

`Status`  <a name="Status-fn::getatt"></a>
The status of the knowledge base.

`Type`  <a name="Type-fn::getatt"></a>
The type of the knowledge base.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time that the knowledge base was last updated.
