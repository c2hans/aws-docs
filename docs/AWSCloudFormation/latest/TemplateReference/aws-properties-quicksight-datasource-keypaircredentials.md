---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-keypaircredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource KeyPairCredentials
<a name="aws-properties-quicksight-datasource-keypaircredentials"></a>

The combination of username, private key and passphrase that are used as credentials.

## Syntax
<a name="aws-properties-quicksight-datasource-keypaircredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-keypaircredentials-syntax.json"></a>

```
{
  "[KeyPairUsername](#cfn-quicksight-datasource-keypaircredentials-keypairusername)" : {{String}},
  "[PrivateKey](#cfn-quicksight-datasource-keypaircredentials-privatekey)" : {{String}},
  "[PrivateKeyPassphrase](#cfn-quicksight-datasource-keypaircredentials-privatekeypassphrase)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-keypaircredentials-syntax.yaml"></a>

```
  [KeyPairUsername](#cfn-quicksight-datasource-keypaircredentials-keypairusername): {{String}}
  [PrivateKey](#cfn-quicksight-datasource-keypaircredentials-privatekey): {{String}}
  [PrivateKeyPassphrase](#cfn-quicksight-datasource-keypaircredentials-privatekeypassphrase): {{String}}
```

## Properties
<a name="aws-properties-quicksight-datasource-keypaircredentials-properties"></a>

`KeyPairUsername`  <a name="cfn-quicksight-datasource-keypaircredentials-keypairusername"></a>
Username
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateKey`  <a name="cfn-quicksight-datasource-keypaircredentials-privatekey"></a>
PrivateKey
*Required*: Yes
*Type*: String
*Pattern*: `^-{5}BEGIN (ENCRYPTED )?PRIVATE KEY-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END (ENCRYPTED )?PRIVATE KEY-{5}(\u000D?\u000A)?$`
*Minimum*: `1600`
*Maximum*: `8000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateKeyPassphrase`  <a name="cfn-quicksight-datasource-keypaircredentials-privatekeypassphrase"></a>
PrivateKeyPassphrase
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
