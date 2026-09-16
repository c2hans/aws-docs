---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fms-applicationslist-app.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FMS::ApplicationsList App
<a name="aws-properties-fms-applicationslist-app"></a>

An individual AWS Firewall Manager application.

## Syntax
<a name="aws-properties-fms-applicationslist-app-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fms-applicationslist-app-syntax.json"></a>

```
{
  "[AppName](#cfn-fms-applicationslist-app-appname)" : {{String}},
  "[Port](#cfn-fms-applicationslist-app-port)" : {{Integer}},
  "[Protocol](#cfn-fms-applicationslist-app-protocol)" : {{String}}
}
```

### YAML
<a name="aws-properties-fms-applicationslist-app-syntax.yaml"></a>

```
  [AppName](#cfn-fms-applicationslist-app-appname): {{String}}
  [Port](#cfn-fms-applicationslist-app-port): {{Integer}}
  [Protocol](#cfn-fms-applicationslist-app-protocol): {{String}}
```

## Properties
<a name="aws-properties-fms-applicationslist-app-properties"></a>

`AppName`  <a name="cfn-fms-applicationslist-app-appname"></a>
The application's name.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-fms-applicationslist-app-port"></a>
The application's port number, for example `80`.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-fms-applicationslist-app-protocol"></a>
The IP protocol name or number. The name can be one of `tcp`, `udp`, or `icmp`. For information on possible numbers, see [Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
