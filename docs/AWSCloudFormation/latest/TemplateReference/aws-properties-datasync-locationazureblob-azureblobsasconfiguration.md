---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationazureblob-azureblobsasconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationAzureBlob AzureBlobSasConfiguration
<a name="aws-properties-datasync-locationazureblob-azureblobsasconfiguration"></a>

The shared access signature (SAS) configuration that allows AWS DataSync to access your Microsoft Azure Blob Storage.

For more information, see [SAS tokens](https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-sas-tokens) for accessing your Azure Blob Storage.

## Syntax
<a name="aws-properties-datasync-locationazureblob-azureblobsasconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationazureblob-azureblobsasconfiguration-syntax.json"></a>

```
{
  "[AzureBlobSasToken](#cfn-datasync-locationazureblob-azureblobsasconfiguration-azureblobsastoken)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-locationazureblob-azureblobsasconfiguration-syntax.yaml"></a>

```
  [AzureBlobSasToken](#cfn-datasync-locationazureblob-azureblobsasconfiguration-azureblobsastoken): {{String}}
```

## Properties
<a name="aws-properties-datasync-locationazureblob-azureblobsasconfiguration-properties"></a>

`AzureBlobSasToken`  <a name="cfn-datasync-locationazureblob-azureblobsasconfiguration-azureblobsastoken"></a>
Specifies a SAS token that provides permissions to access your Azure Blob Storage.
The token is part of the SAS URI string that comes after the storage resource URI and a question mark. A token looks something like this:
 `sp=r&st=2023-12-20T14:54:52Z&se=2023-12-20T22:54:52Z&spr=https&sv=2021-06-08&sr=c&sig=aBBKDWQvyuVcTPH9EBp%2FXTI9E%2F%2Fmq171%2BZU178wcwqU%3D`
*Required*: Yes
*Type*: String
*Pattern*: `(^.+$)`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
