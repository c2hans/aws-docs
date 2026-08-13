---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-internetmonitor-internetevent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InternetMonitor::InternetEvent
<a name="aws-resource-internetmonitor-internetevent"></a>

<a name="aws-resource-internetmonitor-internetevent-description"></a>The `AWS::InternetMonitor::InternetEvent` resource Property description not available. for InternetMonitor.

## Syntax
<a name="aws-resource-internetmonitor-internetevent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-internetmonitor-internetevent-syntax.json"></a>

```
{
  "Type" : "AWS::InternetMonitor::InternetEvent"
}
```

### YAML
<a name="aws-resource-internetmonitor-internetevent-syntax.yaml"></a>

```
Type: AWS::InternetMonitor::InternetEvent
```

## Return values
<a name="aws-resource-internetmonitor-internetevent-return-values"></a>

### Ref
<a name="aws-resource-internetmonitor-internetevent-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-internetmonitor-internetevent-return-values-fn--getatt"></a>

####
<a name="aws-resource-internetmonitor-internetevent-return-values-fn--getatt-fn--getatt"></a>

`EndedAt`  <a name="EndedAt-fn::getatt"></a>
The time when an internet event ended. If the event hasn't ended yet, this value is empty.

`EventArn`  <a name="EventArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the internet event.

`EventId`  <a name="EventId-fn::getatt"></a>
The internally-generated identifier of an internet event.

`EventStatus`  <a name="EventStatus-fn::getatt"></a>
The status of an internet event.

`EventType`  <a name="EventType-fn::getatt"></a>
The type of network impairment.

`StartedAt`  <a name="StartedAt-fn::getatt"></a>
The time when an internet event started.
