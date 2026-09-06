---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerrelay-relayauthentication.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRelay RelayAuthentication
<a name="aws-properties-ses-mailmanagerrelay-relayauthentication"></a>

Authentication for the relay destination server—specify the secretARN where the SMTP credentials are stored, or specify an empty NoAuthentication structure if the relay destination server does not require SMTP credential authentication.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

## Syntax
<a name="aws-properties-ses-mailmanagerrelay-relayauthentication-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerrelay-relayauthentication-syntax.json"></a>

```
{
  "[NoAuthentication](#cfn-ses-mailmanagerrelay-relayauthentication-noauthentication)" : {{Json}},
  "[SecretArn](#cfn-ses-mailmanagerrelay-relayauthentication-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerrelay-relayauthentication-syntax.yaml"></a>

```
  [NoAuthentication](#cfn-ses-mailmanagerrelay-relayauthentication-noauthentication): {{Json}}
  [SecretArn](#cfn-ses-mailmanagerrelay-relayauthentication-secretarn): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerrelay-relayauthentication-properties"></a>

`NoAuthentication`  <a name="cfn-ses-mailmanagerrelay-relayauthentication-noauthentication"></a>
Keep an empty structure if the relay destination server does not require SMTP credential authentication.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArn`  <a name="cfn-ses-mailmanagerrelay-relayauthentication-secretarn"></a>
The ARN of the secret created in secrets manager where the relay server's SMTP credentials are stored.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc):secretsmanager:[a-z0-9-]+:\d{12}:secret:[a-zA-Z0-9/_+=,.@-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
