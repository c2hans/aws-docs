---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-customerprofiles-eventstream.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::EventStream
<a name="aws-resource-customerprofiles-eventstream"></a>

An Event Stream resource of Amazon Connect Customer Profiles.

## Syntax
<a name="aws-resource-customerprofiles-eventstream-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-customerprofiles-eventstream-syntax.json"></a>

```
{
  "Type" : "AWS::CustomerProfiles::EventStream",
  "Properties" : {
      "[DomainName](#cfn-customerprofiles-eventstream-domainname)" : {{String}},
      "[EventStreamName](#cfn-customerprofiles-eventstream-eventstreamname)" : {{String}},
      "[Tags](#cfn-customerprofiles-eventstream-tags)" : {{[ Tag, ... ]}},
      "[Uri](#cfn-customerprofiles-eventstream-uri)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-customerprofiles-eventstream-syntax.yaml"></a>

```
Type: AWS::CustomerProfiles::EventStream
Properties:
  [DomainName](#cfn-customerprofiles-eventstream-domainname): {{String}}
  [EventStreamName](#cfn-customerprofiles-eventstream-eventstreamname): {{String}}
  [Tags](#cfn-customerprofiles-eventstream-tags): {{
    - Tag}}
  [Uri](#cfn-customerprofiles-eventstream-uri): {{String}}
```

## Properties
<a name="aws-resource-customerprofiles-eventstream-properties"></a>

`DomainName`  <a name="cfn-customerprofiles-eventstream-domainname"></a>
The unique name of the domain.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EventStreamName`  <a name="cfn-customerprofiles-eventstream-eventstreamname"></a>
The name of the event stream.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-customerprofiles-eventstream-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-customerprofiles-eventstream-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Uri`  <a name="cfn-customerprofiles-eventstream-uri"></a>
The StreamARN of the destination to deliver profile events to. For example, arn:aws:kinesis:region:account-id:stream/stream-name.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-customerprofiles-eventstream-return-values"></a>

### Ref
<a name="aws-resource-customerprofiles-eventstream-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-customerprofiles-eventstream-return-values-fn--getatt"></a>

####
<a name="aws-resource-customerprofiles-eventstream-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp of when the export was created.

`EventStreamArn`  <a name="EventStreamArn-fn::getatt"></a>
A unique identifier for the event stream.

`State`  <a name="State-fn::getatt"></a>
The operational state of destination stream for export.
