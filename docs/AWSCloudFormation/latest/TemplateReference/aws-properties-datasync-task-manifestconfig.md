---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-task-manifestconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::Task ManifestConfig
<a name="aws-properties-datasync-task-manifestconfig"></a>

Configures a manifest, which is a list of files or objects that you want AWS DataSync to transfer. For more information and configuration examples, see [Specifying what DataSync transfers by using a manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html).

## Syntax
<a name="aws-properties-datasync-task-manifestconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-task-manifestconfig-syntax.json"></a>

```
{
  "[Action](#cfn-datasync-task-manifestconfig-action)" : {{String}},
  "[Format](#cfn-datasync-task-manifestconfig-format)" : {{String}},
  "[Source](#cfn-datasync-task-manifestconfig-source)" : {{Source}}
}
```

### YAML
<a name="aws-properties-datasync-task-manifestconfig-syntax.yaml"></a>

```
  [Action](#cfn-datasync-task-manifestconfig-action): {{String}}
  [Format](#cfn-datasync-task-manifestconfig-format): {{String}}
  [Source](#cfn-datasync-task-manifestconfig-source): {{
    Source}}
```

## Properties
<a name="aws-properties-datasync-task-manifestconfig-properties"></a>

`Action`  <a name="cfn-datasync-task-manifestconfig-action"></a>
Specifies what DataSync uses the manifest for.
*Required*: No
*Type*: String
*Allowed values*: `TRANSFER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Format`  <a name="cfn-datasync-task-manifestconfig-format"></a>
Specifies the file format of your manifest. For more information, see [Creating a manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html#transferring-with-manifest-create).
*Required*: No
*Type*: String
*Allowed values*: `CSV`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-datasync-task-manifestconfig-source"></a>
Specifies the manifest that you want DataSync to use and where it's hosted.
You must specify this parameter if you're configuring a new manifest on or after February 7, 2024.
If you don't, you'll get a 400 status code and `ValidationException` error stating that you're missing the IAM role for DataSync to access the S3 bucket where you're hosting your manifest. For more information, see [Providing DataSync access to your manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html#transferring-with-manifest-access).
*Required*: Yes
*Type*: [Source](aws-properties-datasync-task-source.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
