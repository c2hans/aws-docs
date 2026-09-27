---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-smsvoice-registrationattachment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::RegistrationAttachment
<a name="aws-resource-smsvoice-registrationattachment"></a>

Create a new registration attachment to use for uploading a file or a URL to a file. The maximum file size is 5MB and valid file extensions are PDF, JPEG and PNG. For example, many sender ID registrations require a signed “letter of authorization” (LOA) to be submitted.

Use either `AttachmentUrl` or `AttachmentBody` to upload your attachment. If both are specified then an exception is returned.

## Syntax
<a name="aws-resource-smsvoice-registrationattachment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-smsvoice-registrationattachment-syntax.json"></a>

```
{
  "Type" : "AWS::SMSVOICE::RegistrationAttachment",
  "Properties" : {
      "[AttachmentBody](#cfn-smsvoice-registrationattachment-attachmentbody)" : {{String}},
      "[AttachmentUrl](#cfn-smsvoice-registrationattachment-attachmenturl)" : {{String}},
      "[Tags](#cfn-smsvoice-registrationattachment-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-smsvoice-registrationattachment-syntax.yaml"></a>

```
Type: AWS::SMSVOICE::RegistrationAttachment
Properties:
  [AttachmentBody](#cfn-smsvoice-registrationattachment-attachmentbody): {{String}}
  [AttachmentUrl](#cfn-smsvoice-registrationattachment-attachmenturl): {{String}}
  [Tags](#cfn-smsvoice-registrationattachment-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-smsvoice-registrationattachment-properties"></a>

`AttachmentBody`  <a name="cfn-smsvoice-registrationattachment-attachmentbody"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AttachmentUrl`  <a name="cfn-smsvoice-registrationattachment-attachmenturl"></a>
The URL to the document that's associated with the registration attachment.
*Required*: No
*Type*: String
*Pattern*: `^\S+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-smsvoice-registrationattachment-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-smsvoice-registrationattachment-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-smsvoice-registrationattachment-return-values"></a>

### Ref
<a name="aws-resource-smsvoice-registrationattachment-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-smsvoice-registrationattachment-return-values-fn--getatt"></a>

####
<a name="aws-resource-smsvoice-registrationattachment-return-values-fn--getatt-fn--getatt"></a>

`AttachmentStatus`  <a name="AttachmentStatus-fn::getatt"></a>
The status of the registration attachment.
+ `UPLOAD_IN_PROGRESS` The attachment is being uploaded.
+ `UPLOAD_COMPLETE` The attachment has been uploaded.
+ `UPLOAD_FAILED` The attachment failed to uploaded.
+ `DELETED` The attachment has been deleted..

`CreatedTimestamp`  <a name="CreatedTimestamp-fn::getatt"></a>
The time when the registration attachment was created, in [UNIX epoch time](https://www.epochconverter.com/) format.

`RegistrationAttachmentArn`  <a name="RegistrationAttachmentArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the registration attachment.

`RegistrationAttachmentId`  <a name="RegistrationAttachmentId-fn::getatt"></a>
The unique identifier for the registration attachment.

`UploadedAttachmentUrl`  <a name="UploadedAttachmentUrl-fn::getatt"></a>
Property description not available.
