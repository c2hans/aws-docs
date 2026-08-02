---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securitylake-subscriber-subscriberidentity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityLake::Subscriber SubscriberIdentity
<a name="aws-properties-securitylake-subscriber-subscriberidentity"></a>

Specify the AWS account ID and external ID that the subscriber will use to access source data.

## Syntax
<a name="aws-properties-securitylake-subscriber-subscriberidentity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securitylake-subscriber-subscriberidentity-syntax.json"></a>

```
{
  "[ExternalId](#cfn-securitylake-subscriber-subscriberidentity-externalid)" : {{String}},
  "[Principal](#cfn-securitylake-subscriber-subscriberidentity-principal)" : {{String}}
}
```

### YAML
<a name="aws-properties-securitylake-subscriber-subscriberidentity-syntax.yaml"></a>

```
  [ExternalId](#cfn-securitylake-subscriber-subscriberidentity-externalid): {{String}}
  [Principal](#cfn-securitylake-subscriber-subscriberidentity-principal): {{String}}
```

## Properties
<a name="aws-properties-securitylake-subscriber-subscriberidentity-properties"></a>

`ExternalId`  <a name="cfn-securitylake-subscriber-subscriberidentity-externalid"></a>
The external ID is a unique identifier that the subscriber provides to you.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w+=,.@:/-]*$`
*Minimum*: `2`
*Maximum*: `1224`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Principal`  <a name="cfn-securitylake-subscriber-subscriberidentity-principal"></a>
Principals can include accounts, users, roles, federated users, or AWS services.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9]{12}|[a-z0-9\.\-]*\.(amazonaws|amazon)\.com)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
