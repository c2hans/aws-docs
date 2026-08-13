---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securitylake-subscribernotification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityLake::SubscriberNotification
<a name="aws-resource-securitylake-subscribernotification"></a>

Notifies the subscriber when new data is written to the data lake for the sources that the subscriber consumes in Security Lake. You can create only one subscriber notification per subscriber.

## Syntax
<a name="aws-resource-securitylake-subscribernotification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securitylake-subscribernotification-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityLake::SubscriberNotification",
  "Properties" : {
      "[NotificationConfiguration](#cfn-securitylake-subscribernotification-notificationconfiguration)" : {{NotificationConfiguration}},
      "[SubscriberArn](#cfn-securitylake-subscribernotification-subscriberarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-securitylake-subscribernotification-syntax.yaml"></a>

```
Type: AWS::SecurityLake::SubscriberNotification
Properties:
  [NotificationConfiguration](#cfn-securitylake-subscribernotification-notificationconfiguration): {{
    NotificationConfiguration}}
  [SubscriberArn](#cfn-securitylake-subscribernotification-subscriberarn): {{String}}
```

## Properties
<a name="aws-resource-securitylake-subscribernotification-properties"></a>

`NotificationConfiguration`  <a name="cfn-securitylake-subscribernotification-notificationconfiguration"></a>
Specify the configurations you want to use for subscriber notification. The subscriber is notified when new data is written to the data lake for sources that the subscriber consumes in Security Lake.
*Required*: Yes
*Type*: [NotificationConfiguration](aws-properties-securitylake-subscribernotification-notificationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubscriberArn`  <a name="cfn-securitylake-subscribernotification-subscriberarn"></a>
The Amazon Resource Name (ARN) of the Security Lake subscriber.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-securitylake-subscribernotification-return-values"></a>

### Ref
<a name="aws-resource-securitylake-subscribernotification-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `ref` function, `ref` returns the type of `SubscriberArn`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-securitylake-subscribernotification-return-values-fn--getatt"></a>

####
<a name="aws-resource-securitylake-subscribernotification-return-values-fn--getatt-fn--getatt"></a>

`SubscriberEndpoint`  <a name="SubscriberEndpoint-fn::getatt"></a>
Property description not available.
