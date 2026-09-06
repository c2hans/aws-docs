---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-mailmanagerrelay.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRelay
<a name="aws-resource-ses-mailmanagerrelay"></a>

Resource to create an SMTP relay, which can be used within a Mail Manager rule set to forward incoming emails to defined relay destinations.

## Syntax
<a name="aws-resource-ses-mailmanagerrelay-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ses-mailmanagerrelay-syntax.json"></a>

```
{
  "Type" : "AWS::SES::MailManagerRelay",
  "Properties" : {
      "[Authentication](#cfn-ses-mailmanagerrelay-authentication)" : {{RelayAuthentication}},
      "[RelayName](#cfn-ses-mailmanagerrelay-relayname)" : {{String}},
      "[ServerName](#cfn-ses-mailmanagerrelay-servername)" : {{String}},
      "[ServerPort](#cfn-ses-mailmanagerrelay-serverport)" : {{Number}},
      "[Tags](#cfn-ses-mailmanagerrelay-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ses-mailmanagerrelay-syntax.yaml"></a>

```
Type: AWS::SES::MailManagerRelay
Properties:
  [Authentication](#cfn-ses-mailmanagerrelay-authentication): {{
    RelayAuthentication}}
  [RelayName](#cfn-ses-mailmanagerrelay-relayname): {{String}}
  [ServerName](#cfn-ses-mailmanagerrelay-servername): {{String}}
  [ServerPort](#cfn-ses-mailmanagerrelay-serverport): {{Number}}
  [Tags](#cfn-ses-mailmanagerrelay-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ses-mailmanagerrelay-properties"></a>

`Authentication`  <a name="cfn-ses-mailmanagerrelay-authentication"></a>
Authentication for the relay destination server—specify the secretARN where the SMTP credentials are stored.
*Required*: Yes
*Type*: [RelayAuthentication](aws-properties-ses-mailmanagerrelay-relayauthentication.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RelayName`  <a name="cfn-ses-mailmanagerrelay-relayname"></a>
The unique relay name.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerName`  <a name="cfn-ses-mailmanagerrelay-servername"></a>
The destination relay server address.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-\.]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerPort`  <a name="cfn-ses-mailmanagerrelay-serverport"></a>
The destination relay server port.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ses-mailmanagerrelay-tags"></a>
The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-ses-mailmanagerrelay-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ses-mailmanagerrelay-return-values"></a>

### Ref
<a name="aws-resource-ses-mailmanagerrelay-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ses-mailmanagerrelay-return-values-fn--getatt"></a>

####
<a name="aws-resource-ses-mailmanagerrelay-return-values-fn--getatt-fn--getatt"></a>

`RelayArn`  <a name="RelayArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the relay.

`RelayId`  <a name="RelayId-fn::getatt"></a>
The unique relay identifier.
