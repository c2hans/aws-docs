---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-opsitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::OpsItem
<a name="aws-resource-ssm-opsitem"></a>

Operations engineers and IT professionals use AWS Systems Manager OpsCenter to view, investigate, and remediate operational work items (OpsItems) impacting the performance and health of their AWS resources. OpsCenter is integrated with Amazon EventBridge and Amazon CloudWatch. This means you can configure these services to automatically create an OpsItem in OpsCenter when a CloudWatch alarm enters the ALARM state or when EventBridge processes an event from any AWS service that publishes events. Configuring Amazon CloudWatch alarms and EventBridge events to automatically create OpsItems allows you to quickly diagnose and remediate issues with AWS resources from a single console.

To help you diagnose issues, each OpsItem includes contextually relevant information such as the name and ID of the AWS resource that generated the OpsItem, alarm or event details, alarm history, and an alarm timeline graph. For the AWS resource, OpsCenter aggregates information from AWS Config, AWS CloudTrail logs, and EventBridge, so you don't have to navigate across multiple console pages during your investigation. For more information, see [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) in the *AWS Systems Manager User Guide*.

## Syntax
<a name="aws-resource-ssm-opsitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ssm-opsitem-syntax.json"></a>

```
{
  "Type" : "AWS::SSM::OpsItem",
  "Properties" : {
      "[Category](#cfn-ssm-opsitem-category)" : {{String}},
      "[Description](#cfn-ssm-opsitem-description)" : {{String}},
      "[Priority](#cfn-ssm-opsitem-priority)" : {{Integer}},
      "[Severity](#cfn-ssm-opsitem-severity)" : {{String}},
      "[Source](#cfn-ssm-opsitem-source)" : {{String}},
      "[Tags](#cfn-ssm-opsitem-tags)" : {{[ Tag, ... ]}},
      "[Title](#cfn-ssm-opsitem-title)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ssm-opsitem-syntax.yaml"></a>

```
Type: AWS::SSM::OpsItem
Properties:
  [Category](#cfn-ssm-opsitem-category): {{String}}
  [Description](#cfn-ssm-opsitem-description): {{String}}
  [Priority](#cfn-ssm-opsitem-priority): {{Integer}}
  [Severity](#cfn-ssm-opsitem-severity): {{String}}
  [Source](#cfn-ssm-opsitem-source): {{String}}
  [Tags](#cfn-ssm-opsitem-tags): {{
    - Tag}}
  [Title](#cfn-ssm-opsitem-title): {{String}}
```

## Properties
<a name="aws-resource-ssm-opsitem-properties"></a>

`Category`  <a name="cfn-ssm-opsitem-category"></a>
An OpsItem category. Category options include: Availability, Cost, Performance, Recovery, Security.
*Required*: No
*Type*: String
*Pattern*: `^(?!\s*$).+`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-ssm-opsitem-description"></a>
The OpsItem description.
*Required*: Yes
*Type*: String
*Pattern*: `[\s\S]*\S[\s\S]*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Priority`  <a name="cfn-ssm-opsitem-priority"></a>
The importance of this OpsItem in relation to other OpsItems in the system.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Severity`  <a name="cfn-ssm-opsitem-severity"></a>
The severity of the OpsItem. Severity options range from 1 to 4.
*Required*: No
*Type*: String
*Pattern*: `^(?!\s*$).+`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-ssm-opsitem-source"></a>
The origin of the OpsItem, such as Amazon EC2 or Systems Manager. The impacted resource is a subset of source.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s*$).+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ssm-opsitem-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-ssm-opsitem-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-ssm-opsitem-title"></a>
A short heading that describes the nature of the OpsItem and the impacted resource.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s*$).+`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ssm-opsitem-return-values"></a>

### Ref
<a name="aws-resource-ssm-opsitem-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ssm-opsitem-return-values-fn--getatt"></a>

####
<a name="aws-resource-ssm-opsitem-return-values-fn--getatt-fn--getatt"></a>

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The ARN of the AWS account that created the OpsItem.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The date and time the OpsItem was created.

`LastModifiedBy`  <a name="LastModifiedBy-fn::getatt"></a>
The ARN of the AWS account that last updated the OpsItem.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The date and time the OpsItem was last updated.

`OpsItemArn`  <a name="OpsItemArn-fn::getatt"></a>
The OpsItem Amazon Resource Name (ARN).

`OpsItemId`  <a name="OpsItemId-fn::getatt"></a>
The ID of the OpsItem.

`OpsItemType`  <a name="OpsItemType-fn::getatt"></a>
The type of OpsItem. Systems Manager supports the following types of OpsItems:
+  `/aws/issue`

  This type of OpsItem is used for default OpsItems created by OpsCenter.
+  `/aws/changerequest`

  This type of OpsItem is used by Change Manager for reviewing and approving or rejecting change requests.
+  `/aws/insight`

  This type of OpsItem is used by OpsCenter for aggregating and reporting on duplicate OpsItems.

`Status`  <a name="Status-fn::getatt"></a>
The OpsItem status. For more information, see [Editing OpsItem details](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems-editing-details.html) in the *AWS Systems Manager User Guide*.

`Version`  <a name="Version-fn::getatt"></a>
The version of this OpsItem. Each time the OpsItem is edited the version number increments by one.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
