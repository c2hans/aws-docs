---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-application-attachmentsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Application AttachmentsConfiguration
<a name="aws-properties-qbusiness-application-attachmentsconfiguration"></a>

Configuration information for the file upload during chat feature.

## Syntax
<a name="aws-properties-qbusiness-application-attachmentsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-application-attachmentsconfiguration-syntax.json"></a>

```
{
  "[AttachmentsControlMode](#cfn-qbusiness-application-attachmentsconfiguration-attachmentscontrolmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-application-attachmentsconfiguration-syntax.yaml"></a>

```
  [AttachmentsControlMode](#cfn-qbusiness-application-attachmentsconfiguration-attachmentscontrolmode): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-application-attachmentsconfiguration-properties"></a>

`AttachmentsControlMode`  <a name="cfn-qbusiness-application-attachmentsconfiguration-attachmentscontrolmode"></a>
Status information about whether file upload functionality is activated or deactivated for your end user.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
