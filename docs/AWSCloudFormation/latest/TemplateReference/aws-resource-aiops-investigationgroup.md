---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-aiops-investigationgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AIOps::InvestigationGroup
<a name="aws-resource-aiops-investigationgroup"></a>

Creates an *investigation group* in your account. Creating an investigation group is a one-time setup task for each Region in your account. It is a necessary task to be able to perform investigations.

Settings in the investigation group help you centrally manage the common properties of your investigations, such as the following:
+ Who can access the investigations
+ Whether investigation data is encrypted with a customer managed AWS Key Management Service key.
+ How long investigations and their data are retained by default.

Currently, you can have one investigation group in each Region in your account. Each investigation in a Region is a part of the investigation group in that Region

To create an investigation group and set up CloudWatch investigations, you must be signed in to an IAM principal that has either the `AIOpsConsoleAdminPolicy` or the `AdministratorAccess` IAM policy attached, or to an account that has similar permissions.

**Important**
You can configure CloudWatch alarms to start investigations and add events to investigations. If you create your investigation group with `CreateInvestigationGroup` and you want to enable alarms to do this, you must use `PutInvestigationGroupPolicy` to create a resource policy that grants this permission to CloudWatch alarms.
For more information about configuring CloudWatch alarms, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

## Syntax
<a name="aws-resource-aiops-investigationgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-aiops-investigationgroup-syntax.json"></a>

```
{
  "Type" : "AWS::AIOps::InvestigationGroup",
  "Properties" : {
      "[ChatbotNotificationChannels](#cfn-aiops-investigationgroup-chatbotnotificationchannels)" : {{[ ChatbotNotificationChannel, ... ]}},
      "[CrossAccountConfigurations](#cfn-aiops-investigationgroup-crossaccountconfigurations)" : {{[ CrossAccountConfiguration, ... ]}},
      "[EncryptionConfig](#cfn-aiops-investigationgroup-encryptionconfig)" : {{EncryptionConfigMap}},
      "[InvestigationGroupPolicy](#cfn-aiops-investigationgroup-investigationgrouppolicy)" : {{String}},
      "[IsCloudTrailEventHistoryEnabled](#cfn-aiops-investigationgroup-iscloudtraileventhistoryenabled)" : {{Boolean}},
      "[Name](#cfn-aiops-investigationgroup-name)" : {{String}},
      "[RetentionInDays](#cfn-aiops-investigationgroup-retentionindays)" : {{Integer}},
      "[RoleArn](#cfn-aiops-investigationgroup-rolearn)" : {{String}},
      "[TagKeyBoundaries](#cfn-aiops-investigationgroup-tagkeyboundaries)" : {{[ String, ... ]}},
      "[Tags](#cfn-aiops-investigationgroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-aiops-investigationgroup-syntax.yaml"></a>

```
Type: AWS::AIOps::InvestigationGroup
Properties:
  [ChatbotNotificationChannels](#cfn-aiops-investigationgroup-chatbotnotificationchannels): {{
    - ChatbotNotificationChannel}}
  [CrossAccountConfigurations](#cfn-aiops-investigationgroup-crossaccountconfigurations): {{
    - CrossAccountConfiguration}}
  [EncryptionConfig](#cfn-aiops-investigationgroup-encryptionconfig): {{
    EncryptionConfigMap}}
  [InvestigationGroupPolicy](#cfn-aiops-investigationgroup-investigationgrouppolicy): {{String}}
  [IsCloudTrailEventHistoryEnabled](#cfn-aiops-investigationgroup-iscloudtraileventhistoryenabled): {{Boolean}}
  [Name](#cfn-aiops-investigationgroup-name): {{String}}
  [RetentionInDays](#cfn-aiops-investigationgroup-retentionindays): {{Integer}}
  [RoleArn](#cfn-aiops-investigationgroup-rolearn): {{String}}
  [TagKeyBoundaries](#cfn-aiops-investigationgroup-tagkeyboundaries): {{
    - String}}
  [Tags](#cfn-aiops-investigationgroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-aiops-investigationgroup-properties"></a>

`ChatbotNotificationChannels`  <a name="cfn-aiops-investigationgroup-chatbotnotificationchannels"></a>
Use this property to integrate CloudWatch investigations with chat applications. This property is an array. For the first string, specify the ARN of an Amazon SNS topic. For the array of strings, specify the ARNs of one or more chat applications configurations that you want to associate with that topic. For more information about these configuration ARNs, see [Getting started with Amazon Q in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-started.html) and [Resource type defined by AWS Chatbot](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awschatbot.html#awschatbot-resources-for-iam-policies).
*Required*: No
*Type*: Array of [ChatbotNotificationChannel](aws-properties-aiops-investigationgroup-chatbotnotificationchannel.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CrossAccountConfigurations`  <a name="cfn-aiops-investigationgroup-crossaccountconfigurations"></a>
List of `sourceRoleArn` values that have been configured for cross-account access.
*Required*: No
*Type*: Array of [CrossAccountConfiguration](aws-properties-aiops-investigationgroup-crossaccountconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionConfig`  <a name="cfn-aiops-investigationgroup-encryptionconfig"></a>
Specifies the customer managed AWS KMS key that the investigation group uses to encrypt data, if there is one. If not, the investigation group uses an AWS key to encrypt the data.
*Required*: No
*Type*: [EncryptionConfigMap](aws-properties-aiops-investigationgroup-encryptionconfigmap.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvestigationGroupPolicy`  <a name="cfn-aiops-investigationgroup-investigationgrouppolicy"></a>
Returns the JSON of the IAM resource policy associated with the specified investigation group in a string. For example, `{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"aiops.alarms.cloudwatch.amazonaws.com\"},\"Action\":[\"aiops:CreateInvestigation\",\"aiops:CreateInvestigationEvent\"],\"Resource\":\"*\",\"Condition\":{\"StringEquals\":{\"aws:SourceAccount\":\"111122223333\"},\"ArnLike\":{\"aws:SourceArn\":\"arn:aws:cloudwatch:us-east-1:111122223333:alarm:*\"}}}]}`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsCloudTrailEventHistoryEnabled`  <a name="cfn-aiops-investigationgroup-iscloudtraileventhistoryenabled"></a>
Specify `true` to enable CloudWatch investigations to have access to change events that are recorded by CloudTrail. The default is `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-aiops-investigationgroup-name"></a>
Specify either the name or the ARN of the investigation group that you want to view. This is used to set the name of the investigation group.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RetentionInDays`  <a name="cfn-aiops-investigationgroup-retentionindays"></a>
Specifies how long that investigation data is kept.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-aiops-investigationgroup-rolearn"></a>
The ARN of the IAM role that the investigation group uses for permissions to gather data.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagKeyBoundaries`  <a name="cfn-aiops-investigationgroup-tagkeyboundaries"></a>
Displays the custom tag keys for custom applications in your system that you have specified in the investigation group. Resource tags help CloudWatch investigations narrow the search space when it is unable to discover definite relationships between resources.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-aiops-investigationgroup-tags"></a>
The list of key-value pairs to associate with the resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-aiops-investigationgroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-aiops-investigationgroup-return-values"></a>

### Ref
<a name="aws-resource-aiops-investigationgroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the investigation group. For example, `arn:aws:aiops:Region:account-id:investigation-group:investigation-group-id`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-aiops-investigationgroup-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-aiops-investigationgroup-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the investigation group.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time that the investigation group was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The name of the user who created the investigation group.

`LastModifiedAt`  <a name="LastModifiedAt-fn::getatt"></a>
The date and time that the investigation group was most recently modified.

`LastModifiedBy`  <a name="LastModifiedBy-fn::getatt"></a>
The name of the user who created the investigation group.
