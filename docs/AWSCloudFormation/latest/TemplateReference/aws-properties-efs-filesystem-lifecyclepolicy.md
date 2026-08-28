---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-efs-filesystem-lifecyclepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EFS::FileSystem LifecyclePolicy
<a name="aws-properties-efs-filesystem-lifecyclepolicy"></a>

Describes a policy used by Lifecycle management that specifies when to transition files into and out of the EFS storage classes. For more information, see [Managing file system storage ](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html).

**Note**
Each `LifecyclePolicy` object can have only a single transition. This means that in a request body, `LifecyclePolicies` must be structured as an array of `LifecyclePolicy` objects, one object for each transition, `TransitionToIA`, `TransitionToArchive`, `TransitionToPrimaryStorageClass`.
See the AWS::EFS::FileSystem examples for the correct `LifecyclePolicy` structure. Do not use the syntax shown on this page.

## Syntax
<a name="aws-properties-efs-filesystem-lifecyclepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-efs-filesystem-lifecyclepolicy-syntax.json"></a>

```
{
  "[TransitionToArchive](#cfn-efs-filesystem-lifecyclepolicy-transitiontoarchive)" : {{String}},
  "[TransitionToIA](#cfn-efs-filesystem-lifecyclepolicy-transitiontoia)" : {{String}},
  "[TransitionToPrimaryStorageClass](#cfn-efs-filesystem-lifecyclepolicy-transitiontoprimarystorageclass)" : {{String}}
}
```

### YAML
<a name="aws-properties-efs-filesystem-lifecyclepolicy-syntax.yaml"></a>

```
  [TransitionToArchive](#cfn-efs-filesystem-lifecyclepolicy-transitiontoarchive): {{String}}
  [TransitionToIA](#cfn-efs-filesystem-lifecyclepolicy-transitiontoia): {{String}}
  [TransitionToPrimaryStorageClass](#cfn-efs-filesystem-lifecyclepolicy-transitiontoprimarystorageclass): {{String}}
```

## Properties
<a name="aws-properties-efs-filesystem-lifecyclepolicy-properties"></a>

`TransitionToArchive`  <a name="cfn-efs-filesystem-lifecyclepolicy-transitiontoarchive"></a>
The number of days after files were last accessed in primary storage (the Standard storage class) at which to move them to Archive storage. Metadata operations such as listing the contents of a directory don't count as file access events.
*Required*: No
*Type*: String
*Allowed values*: `AFTER_1_DAY | AFTER_7_DAYS | AFTER_14_DAYS | AFTER_30_DAYS | AFTER_60_DAYS | AFTER_90_DAYS | AFTER_180_DAYS | AFTER_270_DAYS | AFTER_365_DAYS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitionToIA`  <a name="cfn-efs-filesystem-lifecyclepolicy-transitiontoia"></a>
The number of days after files were last accessed in primary storage (the Standard storage class) at which to move them to Infrequent Access (IA) storage. Metadata operations such as listing the contents of a directory don't count as file access events.
*Required*: No
*Type*: String
*Allowed values*: `AFTER_7_DAYS | AFTER_14_DAYS | AFTER_30_DAYS | AFTER_60_DAYS | AFTER_90_DAYS | AFTER_1_DAY | AFTER_180_DAYS | AFTER_270_DAYS | AFTER_365_DAYS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitionToPrimaryStorageClass`  <a name="cfn-efs-filesystem-lifecyclepolicy-transitiontoprimarystorageclass"></a>
Whether to move files back to primary (Standard) storage after they are accessed in IA or Archive storage. Metadata operations such as listing the contents of a directory don't count as file access events.
*Required*: No
*Type*: String
*Allowed values*: `AFTER_1_ACCESS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
