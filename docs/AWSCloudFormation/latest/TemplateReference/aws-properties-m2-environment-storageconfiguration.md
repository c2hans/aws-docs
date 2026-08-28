---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-m2-environment-storageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::M2::Environment StorageConfiguration
<a name="aws-properties-m2-environment-storageconfiguration"></a>

**Important**
AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Defines the storage configuration for a runtime environment.

## Syntax
<a name="aws-properties-m2-environment-storageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-m2-environment-storageconfiguration-syntax.json"></a>

```
{
  "[Efs](#cfn-m2-environment-storageconfiguration-efs)" : {{EfsStorageConfiguration}},
  "[Fsx](#cfn-m2-environment-storageconfiguration-fsx)" : {{FsxStorageConfiguration}}
}
```

### YAML
<a name="aws-properties-m2-environment-storageconfiguration-syntax.yaml"></a>

```
  [Efs](#cfn-m2-environment-storageconfiguration-efs): {{
    EfsStorageConfiguration}}
  [Fsx](#cfn-m2-environment-storageconfiguration-fsx): {{
    FsxStorageConfiguration}}
```

## Properties
<a name="aws-properties-m2-environment-storageconfiguration-properties"></a>

`Efs`  <a name="cfn-m2-environment-storageconfiguration-efs"></a>
Defines the storage configuration for an Amazon EFS file system.
*Required*: No
*Type*: [EfsStorageConfiguration](aws-properties-m2-environment-efsstorageconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Fsx`  <a name="cfn-m2-environment-storageconfiguration-fsx"></a>
Defines the storage configuration for an Amazon FSx file system.
*Required*: No
*Type*: [FsxStorageConfiguration](aws-properties-m2-environment-fsxstorageconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
