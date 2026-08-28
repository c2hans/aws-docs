---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-events-archive.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Archive
<a name="aws-resource-events-archive"></a>

Creates an archive of events with the specified settings. When you create an archive, incoming events might not immediately start being sent to the archive. Allow a short period of time for changes to take effect. If you do not specify a pattern to filter events sent to the archive, all events are sent to the archive except replayed events. Replayed events are not sent to an archive.

**Important**
If you have specified that EventBridge use a customer managed key for encrypting the source event bus, we strongly recommend you also specify a customer managed key for any archives for the event bus as well.
For more information, see [Encrypting archives](https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-archives.html) in the *Amazon EventBridge User Guide*.

## Syntax
<a name="aws-resource-events-archive-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-events-archive-syntax.json"></a>

```
{
  "Type" : "AWS::Events::Archive",
  "Properties" : {
      "[ArchiveName](#cfn-events-archive-archivename)" : {{String}},
      "[Description](#cfn-events-archive-description)" : {{String}},
      "[EventPattern](#cfn-events-archive-eventpattern)" : {{Json}},
      "[KmsKeyIdentifier](#cfn-events-archive-kmskeyidentifier)" : {{String}},
      "[RetentionDays](#cfn-events-archive-retentiondays)" : {{Integer}},
      "[SourceArn](#cfn-events-archive-sourcearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-events-archive-syntax.yaml"></a>

```
Type: AWS::Events::Archive
Properties:
  [ArchiveName](#cfn-events-archive-archivename): {{String}}
  [Description](#cfn-events-archive-description): {{String}}
  [EventPattern](#cfn-events-archive-eventpattern): {{Json}}
  [KmsKeyIdentifier](#cfn-events-archive-kmskeyidentifier): {{String}}
  [RetentionDays](#cfn-events-archive-retentiondays): {{Integer}}
  [SourceArn](#cfn-events-archive-sourcearn): {{String}}
```

## Properties
<a name="aws-resource-events-archive-properties"></a>

`ArchiveName`  <a name="cfn-events-archive-archivename"></a>
The name for the archive to create.
*Required*: No
*Type*: String
*Pattern*: `[\.\-_A-Za-z0-9]+`
*Minimum*: `1`
*Maximum*: `48`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-events-archive-description"></a>
A description for the archive.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventPattern`  <a name="cfn-events-archive-eventpattern"></a>
An event pattern to use to filter events sent to the archive.
*Required*: No
*Type*: Json
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyIdentifier`  <a name="cfn-events-archive-kmskeyidentifier"></a>
The identifier of the AWS KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt this archive. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.
If you do not specify a customer managed key identifier, EventBridge uses an AWS owned key to encrypt the archive.
For more information, see [Identify and view keys](https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html) in the *AWS Key Management Service Developer Guide*.
If you have specified that EventBridge use a customer managed key for encrypting the source event bus, we strongly recommend you also specify a customer managed key for any archives for the event bus as well.
For more information, see [Encrypting archives](https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-archives.html) in the *Amazon EventBridge User Guide*.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetentionDays`  <a name="cfn-events-archive-retentiondays"></a>
The number of days to retain events for. Default value is 0. If set to 0, events are retained indefinitely
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceArn`  <a name="cfn-events-archive-sourcearn"></a>
The ARN of the event bus that sends events to the archive.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:.+\/.+$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-events-archive-return-values"></a>

### Ref
<a name="aws-resource-events-archive-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the archive name.

### Fn::GetAtt
<a name="aws-resource-events-archive-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-events-archive-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the archive created.

## Examples
<a name="aws-resource-events-archive--examples"></a>

### Create an archive
<a name="aws-resource-events-archive--examples--Create_an_archive"></a>

The following example creates an archive for all EC2 events sent from the default event bus that retains events in the archive for 10 days.

#### JSON
<a name="aws-resource-events-archive--examples--Create_an_archive--json"></a>

```
{
  "SampleArchive":
    "Type" : "AWS::Events::Archive",
    "Properties" : {
        "ArchiveName" : "MyArchive",
        "Description" : "Archive for all EC2 events",
        "EventPattern" : {
              "source": [
                 "aws.ec2"
              ]
           },
        "RetentionDays" : "10",
        "SourceArn" : "arn:aws:events:us-west-2:123456789012:event-bus/default"
      }
}
```

#### YAML
<a name="aws-resource-events-archive--examples--Create_an_archive--yaml"></a>

```
SampleArchive:
  Type: 'AWS::Events::Archive'
  Properties:
    ArchiveName: MyArchive
    Description: Archive for all EC2 events
    EventPattern:
      source:
        - "aws.ec2"
    RetentionDays: 10
    SourceArn: 'arn:aws:events:us-west-2:123456789012:event-bus/default'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
