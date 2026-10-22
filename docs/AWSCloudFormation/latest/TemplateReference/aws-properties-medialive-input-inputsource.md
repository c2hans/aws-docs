---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-inputsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input InputSource
<a name="aws-properties-medialive-input-inputsource"></a>

The settings for a PULL type input.

## Syntax
<a name="aws-properties-medialive-input-inputsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-inputsource-syntax.json"></a>

```
{
  "[PasswordParam](#cfn-medialive-input-inputsource-passwordparam)" : {{String}},
  "[Url](#cfn-medialive-input-inputsource-url)" : {{String}},
  "[Username](#cfn-medialive-input-inputsource-username)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-input-inputsource-syntax.yaml"></a>

```
  [PasswordParam](#cfn-medialive-input-inputsource-passwordparam): {{String}}
  [Url](#cfn-medialive-input-inputsource-url): {{String}}
  [Username](#cfn-medialive-input-inputsource-username): {{String}}
```

## Properties
<a name="aws-properties-medialive-input-inputsource-properties"></a>

`PasswordParam`  <a name="cfn-medialive-input-inputsource-passwordparam"></a>
The key used to extract the password from EC2 Parameter store.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-medialive-input-inputsource-url"></a>
This represents the customer's source URL where stream is pulled from.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-medialive-input-inputsource-username"></a>
The username for the input source.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
