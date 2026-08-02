---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-trigger-notificationproperty.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Trigger NotificationProperty
<a name="aws-properties-glue-trigger-notificationproperty"></a>

Specifies configuration properties of a job run notification.

## Syntax
<a name="aws-properties-glue-trigger-notificationproperty-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-trigger-notificationproperty-syntax.json"></a>

```
{
  "[NotifyDelayAfter](#cfn-glue-trigger-notificationproperty-notifydelayafter)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-glue-trigger-notificationproperty-syntax.yaml"></a>

```
  [NotifyDelayAfter](#cfn-glue-trigger-notificationproperty-notifydelayafter): {{Integer}}
```

## Properties
<a name="aws-properties-glue-trigger-notificationproperty-properties"></a>

`NotifyDelayAfter`  <a name="cfn-glue-trigger-notificationproperty-notifydelayafter"></a>
After a job run starts, the number of minutes to wait before sending a job run delay notification
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
