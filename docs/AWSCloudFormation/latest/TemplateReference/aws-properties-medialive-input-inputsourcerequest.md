---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-inputsourcerequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input InputSourceRequest
<a name="aws-properties-medialive-input-inputsourcerequest"></a>

Settings that apply only if the input is a pull type of input.

The parent of this entity is Input.

## Syntax
<a name="aws-properties-medialive-input-inputsourcerequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-inputsourcerequest-syntax.json"></a>

```
{
  "[PasswordParam](#cfn-medialive-input-inputsourcerequest-passwordparam)" : {{String}},
  "[Url](#cfn-medialive-input-inputsourcerequest-url)" : {{String}},
  "[Username](#cfn-medialive-input-inputsourcerequest-username)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-input-inputsourcerequest-syntax.yaml"></a>

```
  [PasswordParam](#cfn-medialive-input-inputsourcerequest-passwordparam): {{String}}
  [Url](#cfn-medialive-input-inputsourcerequest-url): {{String}}
  [Username](#cfn-medialive-input-inputsourcerequest-username): {{String}}
```

## Properties
<a name="aws-properties-medialive-input-inputsourcerequest-properties"></a>

`PasswordParam`  <a name="cfn-medialive-input-inputsourcerequest-passwordparam"></a>
The password parameter that holds the password for accessing the upstream system. The password parameter applies only if the upstream system requires credentials.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-medialive-input-inputsourcerequest-url"></a>
For a pull input, the URL where MediaLive pulls the source content from.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-medialive-input-inputsourcerequest-username"></a>
The user name to connect to the upstream system. The user name applies only if the upstream system requires credentials.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
