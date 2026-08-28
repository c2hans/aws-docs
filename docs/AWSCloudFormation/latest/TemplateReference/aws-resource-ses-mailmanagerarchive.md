---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-mailmanagerarchive.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerArchive
<a name="aws-resource-ses-mailmanagerarchive"></a>

Creates a new email archive resource for storing and retaining emails.

## Syntax
<a name="aws-resource-ses-mailmanagerarchive-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ses-mailmanagerarchive-syntax.json"></a>

```
{
  "Type" : "AWS::SES::MailManagerArchive",
  "Properties" : {
      "[ArchiveName](#cfn-ses-mailmanagerarchive-archivename)" : {{String}},
      "[KmsKeyArn](#cfn-ses-mailmanagerarchive-kmskeyarn)" : {{String}},
      "[Retention](#cfn-ses-mailmanagerarchive-retention)" : {{ArchiveRetention}},
      "[Tags](#cfn-ses-mailmanagerarchive-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ses-mailmanagerarchive-syntax.yaml"></a>

```
Type: AWS::SES::MailManagerArchive
Properties:
  [ArchiveName](#cfn-ses-mailmanagerarchive-archivename): {{String}}
  [KmsKeyArn](#cfn-ses-mailmanagerarchive-kmskeyarn): {{String}}
  [Retention](#cfn-ses-mailmanagerarchive-retention): {{
    ArchiveRetention}}
  [Tags](#cfn-ses-mailmanagerarchive-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ses-mailmanagerarchive-properties"></a>

`ArchiveName`  <a name="cfn-ses-mailmanagerarchive-archivename"></a>
A unique name for the new archive.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_-]*[a-zA-Z0-9]$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-ses-mailmanagerarchive-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the KMS key for encrypting emails in the archive.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov|-eusc):kms:[a-z0-9-]{1,20}:[0-9]{12}:(key|alias)/.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Retention`  <a name="cfn-ses-mailmanagerarchive-retention"></a>
The period for retaining emails in the archive before automatic deletion.
*Required*: No
*Type*: [ArchiveRetention](aws-properties-ses-mailmanagerarchive-archiveretention.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ses-mailmanagerarchive-tags"></a>
The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-ses-mailmanagerarchive-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ses-mailmanagerarchive-return-values"></a>

### Ref
<a name="aws-resource-ses-mailmanagerarchive-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ses-mailmanagerarchive-return-values-fn--getatt"></a>

####
<a name="aws-resource-ses-mailmanagerarchive-return-values-fn--getatt-fn--getatt"></a>

`ArchiveArn`  <a name="ArchiveArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the archive.

`ArchiveId`  <a name="ArchiveId-fn::getatt"></a>
The unique identifier of the archive.

`ArchiveState`  <a name="ArchiveState-fn::getatt"></a>
The current state of the archive:
+ `ACTIVE` – The archive is ready and available for use.
+ `PENDING_DELETION` – The archive has been marked for deletion and will be permanently deleted in 30 days. No further modifications can be made in this state.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
