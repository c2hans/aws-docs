---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securitylake-subscriber.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityLake::Subscriber
<a name="aws-resource-securitylake-subscriber"></a>

Creates a subscriber for accounts that are already enabled in Amazon Security Lake. You can create a subscriber with access to data in the current AWS Region.

## Syntax
<a name="aws-resource-securitylake-subscriber-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securitylake-subscriber-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityLake::Subscriber",
  "Properties" : {
      "[AccessTypes](#cfn-securitylake-subscriber-accesstypes)" : {{[ String, ... ]}},
      "[DataLakeArn](#cfn-securitylake-subscriber-datalakearn)" : {{String}},
      "[Sources](#cfn-securitylake-subscriber-sources)" : {{[ Source, ... ]}},
      "[SubscriberDescription](#cfn-securitylake-subscriber-subscriberdescription)" : {{String}},
      "[SubscriberIdentity](#cfn-securitylake-subscriber-subscriberidentity)" : {{SubscriberIdentity}},
      "[SubscriberName](#cfn-securitylake-subscriber-subscribername)" : {{String}},
      "[Tags](#cfn-securitylake-subscriber-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-securitylake-subscriber-syntax.yaml"></a>

```
Type: AWS::SecurityLake::Subscriber
Properties:
  [AccessTypes](#cfn-securitylake-subscriber-accesstypes): {{
    - String}}
  [DataLakeArn](#cfn-securitylake-subscriber-datalakearn): {{String}}
  [Sources](#cfn-securitylake-subscriber-sources): {{
    - Source}}
  [SubscriberDescription](#cfn-securitylake-subscriber-subscriberdescription): {{String}}
  [SubscriberIdentity](#cfn-securitylake-subscriber-subscriberidentity): {{
    SubscriberIdentity}}
  [SubscriberName](#cfn-securitylake-subscriber-subscribername): {{String}}
  [Tags](#cfn-securitylake-subscriber-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-securitylake-subscriber-properties"></a>

`AccessTypes`  <a name="cfn-securitylake-subscriber-accesstypes"></a>
You can choose to notify subscribers of new objects with an Amazon Simple Queue Service (Amazon SQS) queue or through messaging to an HTTPS endpoint provided by the subscriber.
 Subscribers can consume data by directly querying AWS Lake Formation tables in your Amazon S3 bucket through services like Amazon Athena. This subscription type is defined as `LAKEFORMATION`.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `LAKEFORMATION | S3`
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataLakeArn`  <a name="cfn-securitylake-subscriber-datalakearn"></a>
The Amazon Resource Name (ARN) used to create the data lake.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Sources`  <a name="cfn-securitylake-subscriber-sources"></a>
Amazon Security Lake supports log and event collection for natively supported AWS services. For more information, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/source-management.html).
*Required*: Yes
*Type*: Array of [Source](aws-properties-securitylake-subscriber-source.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubscriberDescription`  <a name="cfn-securitylake-subscriber-subscriberdescription"></a>
The subscriber descriptions for a subscriber account. The description for a subscriber includes `subscriberName`, `accountID`, `externalID`, and `subscriberId`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubscriberIdentity`  <a name="cfn-securitylake-subscriber-subscriberidentity"></a>
The AWS identity used to access your data.
*Required*: Yes
*Type*: [SubscriberIdentity](aws-properties-securitylake-subscriber-subscriberidentity.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubscriberName`  <a name="cfn-securitylake-subscriber-subscribername"></a>
The name of your Amazon Security Lake subscriber account.
*Required*: Yes
*Type*: String
*Pattern*: `^[\\\w\s\-_:/,.@=+]*$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-securitylake-subscriber-tags"></a>
An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.
*Required*: No
*Type*: Array of [Tag](aws-properties-securitylake-subscriber-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securitylake-subscriber-return-values"></a>

### Ref
<a name="aws-resource-securitylake-subscriber-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `ref` function, `ref` returns the `Subscriber` name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-securitylake-subscriber-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-securitylake-subscriber-return-values-fn--getatt-fn--getatt"></a>

`ResourceShareArn`  <a name="ResourceShareArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Amazon Security Lake subscriber.

`ResourceShareName`  <a name="ResourceShareName-fn::getatt"></a>
The ARN name of the Amazon Security Lake subscriber.

`S3BucketArn`  <a name="S3BucketArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the S3 bucket.

`SubscriberArn`  <a name="SubscriberArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Security Lake subscriber.

`SubscriberRoleArn`  <a name="SubscriberRoleArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the role used to create the Security Lake subscriber.
