---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-messagetemplate-messagetemplateattachment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::MessageTemplate MessageTemplateAttachment
<a name="aws-properties-wisdom-messagetemplate-messagetemplateattachment"></a>

Information about the message template attachment.

## Syntax
<a name="aws-properties-wisdom-messagetemplate-messagetemplateattachment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-messagetemplate-messagetemplateattachment-syntax.json"></a>

```
{
  "[AttachmentId](#cfn-wisdom-messagetemplate-messagetemplateattachment-attachmentid)" : {{String}},
  "[AttachmentName](#cfn-wisdom-messagetemplate-messagetemplateattachment-attachmentname)" : {{String}},
  "[S3PresignedUrl](#cfn-wisdom-messagetemplate-messagetemplateattachment-s3presignedurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-messagetemplate-messagetemplateattachment-syntax.yaml"></a>

```
  [AttachmentId](#cfn-wisdom-messagetemplate-messagetemplateattachment-attachmentid): {{String}}
  [AttachmentName](#cfn-wisdom-messagetemplate-messagetemplateattachment-attachmentname): {{String}}
  [S3PresignedUrl](#cfn-wisdom-messagetemplate-messagetemplateattachment-s3presignedurl): {{String}}
```

## Properties
<a name="aws-properties-wisdom-messagetemplate-messagetemplateattachment-properties"></a>

`AttachmentId`  <a name="cfn-wisdom-messagetemplate-messagetemplateattachment-attachmentid"></a>
The identifier of the attachment file.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AttachmentName`  <a name="cfn-wisdom-messagetemplate-messagetemplateattachment-attachmentname"></a>
The name of the attachment file being uploaded. The name should include the file extension.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3PresignedUrl`  <a name="cfn-wisdom-messagetemplate-messagetemplateattachment-s3presignedurl"></a>
The S3 Presigned URL for the attachment file. When generating the PreSignedUrl, please ensure that the expires-in time is set to 30 minutes. The URL can be generated through the AWS Console or through the AWS CLI. For more information, see [Sharing objects with presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
