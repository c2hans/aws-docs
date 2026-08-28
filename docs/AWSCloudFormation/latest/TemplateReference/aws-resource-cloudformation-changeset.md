---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-changeset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::ChangeSet
<a name="aws-resource-cloudformation-changeset"></a>

Creates a list of changes that will be applied to a stack so that you can review the changes before executing them. You can create a change set for a stack that doesn't exist or an existing stack. If you create a change set for a stack that doesn't exist, the change set shows all of the resources that CloudFormation will create. If you create a change set for an existing stack, CloudFormation compares the stack's information with the information that you submit in the change set and lists the differences. Use change sets to understand which resources CloudFormation will create or change, and how it will change resources in an existing stack, before you create or update a stack.

To create a change set for a stack that doesn't exist, for the `ChangeSetType` parameter, specify `CREATE`. To create a change set for an existing stack, specify `UPDATE` for the `ChangeSetType` parameter. To create a change set for an import operation, specify `IMPORT` for the `ChangeSetType` parameter. After the `CreateChangeSet` call successfully completes, CloudFormation starts creating the change set. To check the status of the change set or to review it, use the DescribeChangeSet action.

When you are satisfied with the changes the change set will make, execute the change set by using the ExecuteChangeSet action. CloudFormation doesn't make changes until you execute the change set.

To create a change set for the entire stack hierarchy, set `IncludeNestedStacks` to `True`.

## Syntax
<a name="aws-resource-cloudformation-changeset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudformation-changeset-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFormation::ChangeSet",
  "Properties" : {
      "[Capabilities](#cfn-cloudformation-changeset-capabilities)" : {{[ String, ... ]}},
      "[ChangeSetName](#cfn-cloudformation-changeset-changesetname)" : {{String}},
      "[ChangeSetType](#cfn-cloudformation-changeset-changesettype)" : {{String}},
      "[DeploymentMode](#cfn-cloudformation-changeset-deploymentmode)" : {{String}},
      "[Description](#cfn-cloudformation-changeset-description)" : {{String}},
      "[ImportExistingResources](#cfn-cloudformation-changeset-importexistingresources)" : {{Boolean}},
      "[IncludeNestedStacks](#cfn-cloudformation-changeset-includenestedstacks)" : {{Boolean}},
      "[NotificationARNs](#cfn-cloudformation-changeset-notificationarns)" : {{[ String, ... ]}},
      "[OnStackFailure](#cfn-cloudformation-changeset-onstackfailure)" : {{String}},
      "[RoleARN](#cfn-cloudformation-changeset-rolearn)" : {{String}},
      "[StackName](#cfn-cloudformation-changeset-stackname)" : {{String}},
      "[Tags](#cfn-cloudformation-changeset-tags)" : {{[ TagsItems, ... ]}},
      "[TemplateBody](#cfn-cloudformation-changeset-templatebody)" : {{String}},
      "[TemplateURL](#cfn-cloudformation-changeset-templateurl)" : {{String}},
      "[UsePreviousTemplate](#cfn-cloudformation-changeset-useprevioustemplate)" : {{Boolean}}
    }
}
```

### YAML
<a name="aws-resource-cloudformation-changeset-syntax.yaml"></a>

```
Type: AWS::CloudFormation::ChangeSet
Properties:
  [Capabilities](#cfn-cloudformation-changeset-capabilities): {{
    - String}}
  [ChangeSetName](#cfn-cloudformation-changeset-changesetname): {{String}}
  [ChangeSetType](#cfn-cloudformation-changeset-changesettype): {{String}}
  [DeploymentMode](#cfn-cloudformation-changeset-deploymentmode): {{String}}
  [Description](#cfn-cloudformation-changeset-description): {{String}}
  [ImportExistingResources](#cfn-cloudformation-changeset-importexistingresources): {{Boolean}}
  [IncludeNestedStacks](#cfn-cloudformation-changeset-includenestedstacks): {{Boolean}}
  [NotificationARNs](#cfn-cloudformation-changeset-notificationarns): {{
    - String}}
  [OnStackFailure](#cfn-cloudformation-changeset-onstackfailure): {{String}}
  [RoleARN](#cfn-cloudformation-changeset-rolearn): {{String}}
  [StackName](#cfn-cloudformation-changeset-stackname): {{String}}
  [Tags](#cfn-cloudformation-changeset-tags): {{
    - TagsItems}}
  [TemplateBody](#cfn-cloudformation-changeset-templatebody): {{String}}
  [TemplateURL](#cfn-cloudformation-changeset-templateurl): {{String}}
  [UsePreviousTemplate](#cfn-cloudformation-changeset-useprevioustemplate): {{Boolean}}
```

## Properties
<a name="aws-resource-cloudformation-changeset-properties"></a>

`Capabilities`  <a name="cfn-cloudformation-changeset-capabilities"></a>
In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to create the stack.
+ `CAPABILITY_IAM` and `CAPABILITY_NAMED_IAM`

  Some stack templates might include resources that can affect permissions in your AWS account, for example, by creating new IAM users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.

  The following IAM resources require you to specify either the `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM` capability.
  + If you have IAM resources, you can specify either capability.
  + If you have IAM resources with custom names, you *must* specify `CAPABILITY_NAMED_IAM`.
  + If you don't specify either of these capabilities, CloudFormation returns an `InsufficientCapabilities` error.

  If your stack template contains these resources, we suggest that you review all permissions associated with them and edit their permissions if necessary.
  +  [ AWS::IAM::AccessKey](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-accesskey.html)
  +  [ AWS::IAM::Group](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-group.html)
  +  [AWS::IAM::InstanceProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-instanceprofile.html)
  +  [ AWS::IAM::ManagedPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-managedpolicy.html)
  +  [ AWS::IAM::Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-policy.html)
  +  [ AWS::IAM::Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html)
  +  [ AWS::IAM::User](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html)
  +  [AWS::IAM::UserToGroupAddition](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-usertogroupaddition.html)

  For more information, see [Acknowledging IAM resources in CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities).
+  `CAPABILITY_AUTO_EXPAND`

  Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually creating the stack. If your stack template contains one or more macros, and you choose to create a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the [AWS::Include](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-include.html) and [AWS::Serverless](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html) transforms, which are macros hosted by CloudFormation.
**Note**
This capacity doesn't apply to creating change sets, and specifying it when creating change sets has no effect.
If you want to create a stack from a stack template that contains macros *and* nested stacks, you must create or update the stack directly from the template using the CreateStack or UpdateStack action, and specifying this capability.

  For more information about macros, see [Perform custom processing on CloudFormation templates with template macros](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html).
Only one of the `Capabilities` and `ResourceType` parameters can be specified.
*Required*: No
*Type*: Array of String
*Allowed values*: `CAPABILITY_IAM | CAPABILITY_NAMED_IAM | CAPABILITY_AUTO_EXPAND`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ChangeSetName`  <a name="cfn-cloudformation-changeset-changesetname"></a>
The name of the change set. The name must be unique among all change sets that are associated with the specified stack.
A change set name can contain only alphanumeric, case sensitive characters, and hyphens. It must start with an alphabetical character and can't exceed 128 characters.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][-a-zA-Z0-9]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ChangeSetType`  <a name="cfn-cloudformation-changeset-changesettype"></a>
The type of change set operation. To create a change set for a new stack, specify `CREATE`. To create a change set for an existing stack, specify `UPDATE`. To create a change set for an import operation, specify `IMPORT`.
If you create a change set for a new stack, CloudFormation creates a stack with a unique stack ID, but no template or resources. The stack will be in the `REVIEW_IN_PROGRESS` state until you execute the change set.
By default, CloudFormation specifies `UPDATE`. You can't use the `UPDATE` type to create a change set for a new stack or the `CREATE` type to create a change set for an existing stack.
*Required*: No
*Type*: String
*Allowed values*: `CREATE | UPDATE | IMPORT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DeploymentMode`  <a name="cfn-cloudformation-changeset-deploymentmode"></a>
Determines how CloudFormation handles configuration drift during deployment.
+ `REVERT_DRIFT` – Creates a drift-aware change set that brings actual resource states in line with template definitions. Provides a three-way comparison between actual state, previous deployment state, and desired state.
For more information, see [Using drift-aware change sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/drift-aware-change-sets.html) in the *AWS CloudFormation User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `REVERT_DRIFT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-cloudformation-changeset-description"></a>
A description to help you identify this change set.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ImportExistingResources`  <a name="cfn-cloudformation-changeset-importexistingresources"></a>
Indicates if the change set auto-imports resources that already exist. For more information, see [Import AWS resources into a CloudFormation stack automatically](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/import-resources-automatically.html) in the *AWS CloudFormation User Guide*.
This parameter can only import resources that have custom names in templates. For more information, see [name type](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-name.html) in the *AWS CloudFormation User Guide*. To import resources that do not accept custom names, such as EC2 instances, use the `ResourcesToImport` parameter instead.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IncludeNestedStacks`  <a name="cfn-cloudformation-changeset-includenestedstacks"></a>
Creates a change set for the all nested stacks specified in the template. The default behavior of this action is set to `False`. To include nested sets in a change set, specify `True`.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NotificationARNs`  <a name="cfn-cloudformation-changeset-notificationarns"></a>
The Amazon Resource Names (ARNs) of Amazon SNS topics that CloudFormation associates with the stack. To remove all associated notification topics, specify an empty list.
*Required*: No
*Type*: Array of String
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OnStackFailure`  <a name="cfn-cloudformation-changeset-onstackfailure"></a>
Determines what action will be taken if stack creation fails. If this parameter is specified, the `DisableRollback` parameter to the [ExecuteChangeSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html) API operation must not be specified. This must be one of these values:
+ `DELETE` - Deletes the change set if the stack creation fails. This is only valid when the `ChangeSetType` parameter is set to `CREATE`. If the deletion of the stack fails, the status of the stack is `DELETE_FAILED`.
+ `DO_NOTHING` - if the stack creation fails, do nothing. This is equivalent to specifying `true` for the `DisableRollback` parameter to the [ExecuteChangeSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html) API operation.
+ `ROLLBACK` - if the stack creation fails, roll back the stack. This is equivalent to specifying `false` for the `DisableRollback` parameter to the [ExecuteChangeSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html) API operation.
For nested stacks, when the `OnStackFailure` parameter is set to `DELETE` for the change set for the parent stack, any failure in a child stack will cause the parent stack creation to fail and all stacks to be deleted.
*Required*: No
*Type*: String
*Allowed values*: `DO_NOTHING | ROLLBACK | DELETE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleARN`  <a name="cfn-cloudformation-changeset-rolearn"></a>
The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes when executing the change set. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least permission.
If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that is generated from your user credentials.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StackName`  <a name="cfn-cloudformation-changeset-stackname"></a>
The name or the unique ID of the stack for which you are creating a change set. CloudFormation generates the change set by comparing this stack's information with the information that you submit, such as a modified template or different parameter input values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cloudformation-changeset-tags"></a>
Key-value pairs to associate with this stack. CloudFormation also propagates these tags to resources in the stack. You can specify a maximum of 50 tags.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-cloudformation-changeset-tagsitems.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TemplateBody`  <a name="cfn-cloudformation-changeset-templatebody"></a>
A structure that contains the body of the revised template, with a minimum length of 1 byte and a maximum length of 51,200 bytes. CloudFormation generates the change set by comparing this template with the template of the stack that you specified.
Conditional: You must specify only one of the following parameters: `TemplateBody`, `TemplateURL`, or set the `UsePreviousTemplate` to `true`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TemplateURL`  <a name="cfn-cloudformation-changeset-templateurl"></a>
The URL of the file that contains the revised template. The URL must point to a template (max size: 1 MB) that's located in an Amazon S3 bucket or a Systems Manager document. CloudFormation generates the change set by comparing this template with the stack that you specified. The location for an Amazon S3 bucket must start with `https://`. URLs from S3 static websites are not supported.
Conditional: You must specify only one of the following parameters: `TemplateBody`, `TemplateURL`, or set the `UsePreviousTemplate` to `true`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `5120`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UsePreviousTemplate`  <a name="cfn-cloudformation-changeset-useprevioustemplate"></a>
Whether to reuse the template that's associated with the stack to create the change set.
When using templates with the `AWS::LanguageExtensions` transform, provide the template instead of using `UsePreviousTemplate` to ensure new parameter values and Systems Manager parameter updates are applied correctly. For more information, see [AWS::LanguageExtensions transform](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/transform-aws-languageextensions.html).
Conditional: You must specify only one of the following parameters: `TemplateBody`, `TemplateURL`, or set the `UsePreviousTemplate` to `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cloudformation-changeset-return-values"></a>

### Ref
<a name="aws-resource-cloudformation-changeset-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudformation-changeset-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudformation-changeset-return-values-fn--getatt-fn--getatt"></a>

`ChangeSetId`  <a name="ChangeSetId-fn::getatt"></a>
The Amazon Resource Name (ARN) of the change set.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The start time when the change set was created, in UTC.

`StackId`  <a name="StackId-fn::getatt"></a>
The Amazon Resource Name (ARN) of the stack that's associated with the change set.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
