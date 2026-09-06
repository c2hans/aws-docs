---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-configurationset-archivingoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ConfigurationSet ArchivingOptions
<a name="aws-properties-ses-configurationset-archivingoptions"></a>

Used to associate a configuration set with a MailManager archive.

## Syntax
<a name="aws-properties-ses-configurationset-archivingoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-configurationset-archivingoptions-syntax.json"></a>

```
{
  "[ArchiveArn](#cfn-ses-configurationset-archivingoptions-archivearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-configurationset-archivingoptions-syntax.yaml"></a>

```
  [ArchiveArn](#cfn-ses-configurationset-archivingoptions-archivearn): {{String}}
```

## Properties
<a name="aws-properties-ses-configurationset-archivingoptions-properties"></a>

`ArchiveArn`  <a name="cfn-ses-configurationset-archivingoptions-archivearn"></a>
The Amazon Resource Name (ARN) of the MailManager archive where the Amazon SES API v2 will archive sent emails.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
