---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-resourcegroups-tagsynctask.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResourceGroups::TagSyncTask
<a name="aws-resource-resourcegroups-tagsynctask"></a>

Onboards and syncs resources tagged with a specific tag key-value pair to an application.

 **Minimum permissions**

To run this command, you must have the following permissions:
+  `resource-groups:StartTagSyncTask`
+  `resource-groups:CreateGroup`
+ `iam:PassRole` for the role you provide to create a tag-sync task

## Syntax
<a name="aws-resource-resourcegroups-tagsynctask-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-resourcegroups-tagsynctask-syntax.json"></a>

```
{
  "Type" : "AWS::ResourceGroups::TagSyncTask",
  "Properties" : {
      "[Group](#cfn-resourcegroups-tagsynctask-group)" : {{String}},
      "[RoleArn](#cfn-resourcegroups-tagsynctask-rolearn)" : {{String}},
      "[TagKey](#cfn-resourcegroups-tagsynctask-tagkey)" : {{String}},
      "[TagValue](#cfn-resourcegroups-tagsynctask-tagvalue)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-resourcegroups-tagsynctask-syntax.yaml"></a>

```
Type: AWS::ResourceGroups::TagSyncTask
Properties:
  [Group](#cfn-resourcegroups-tagsynctask-group): {{String}}
  [RoleArn](#cfn-resourcegroups-tagsynctask-rolearn): {{String}}
  [TagKey](#cfn-resourcegroups-tagsynctask-tagkey): {{String}}
  [TagValue](#cfn-resourcegroups-tagsynctask-tagvalue): {{String}}
```

## Properties
<a name="aws-resource-resourcegroups-tagsynctask-properties"></a>

`Group`  <a name="cfn-resourcegroups-tagsynctask-group"></a>
The Amazon resource name (ARN) or name of the application group for which you want to create a tag-sync task.
*Required*: Yes
*Type*: String
*Pattern*: `([a-zA-Z0-9_\\.-]{1,150}/[a-z0-9]{26})|(arn:aws(-[a-z]+)*:resource-groups(-(test|beta|gamma))?:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/[a-zA-Z0-9_\\.-]{1,150}/[a-z0-9]{26})`
*Minimum*: `12`
*Maximum*: `1600`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-resourcegroups-tagsynctask-rolearn"></a>
The Amazon resource name (ARN) of the role assumed by the service to tag and untag resources on your behalf.
*Required*: Yes
*Type*: String
*Pattern*: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TagKey`  <a name="cfn-resourcegroups-tagsynctask-tagkey"></a>
The tag key.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TagValue`  <a name="cfn-resourcegroups-tagsynctask-tagvalue"></a>
The tag value.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-resourcegroups-tagsynctask-return-values"></a>

### Ref
<a name="aws-resource-resourcegroups-tagsynctask-return-values-ref"></a>

The `TaskArn`.

### Fn::GetAtt
<a name="aws-resource-resourcegroups-tagsynctask-return-values-fn--getatt"></a>

####
<a name="aws-resource-resourcegroups-tagsynctask-return-values-fn--getatt-fn--getatt"></a>

`GroupArn`  <a name="GroupArn-fn::getatt"></a>
The Amazon resource name (ARN) of the application group.

`GroupName`  <a name="GroupName-fn::getatt"></a>
The name of the application group.

`Status`  <a name="Status-fn::getatt"></a>
The status of the tag-sync task.
Valid values include:
+ `ACTIVE` - The tag-sync task is actively managing resources in the application by adding or removing the `awsApplication` tag from resources when they are tagged or untagged with the specified tag key-value pair.
+ `ERROR` - The tag-sync task is not actively managing resources in the application. Review the `ErrorMessage` for more information about resolving the error.

`TaskArn`  <a name="TaskArn-fn::getatt"></a>
The Amazon resource name (ARN) of the tag-sync task.
