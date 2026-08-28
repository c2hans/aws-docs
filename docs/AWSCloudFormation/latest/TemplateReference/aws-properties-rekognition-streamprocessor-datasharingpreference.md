---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rekognition-streamprocessor-datasharingpreference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Rekognition::StreamProcessor DataSharingPreference
<a name="aws-properties-rekognition-streamprocessor-datasharingpreference"></a>

Allows you to opt in or opt out to share data with Rekognition to improve model performance. You can choose this option at the account level or on a per-stream basis. Note that if you opt out at the account level, this setting is ignored on individual streams. For more information, see [StreamProcessorDataSharingPreference](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorDataSharingPreference).

## Syntax
<a name="aws-properties-rekognition-streamprocessor-datasharingpreference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rekognition-streamprocessor-datasharingpreference-syntax.json"></a>

```
{
  "[OptIn](#cfn-rekognition-streamprocessor-datasharingpreference-optin)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-rekognition-streamprocessor-datasharingpreference-syntax.yaml"></a>

```
  [OptIn](#cfn-rekognition-streamprocessor-datasharingpreference-optin): {{Boolean}}
```

## Properties
<a name="aws-properties-rekognition-streamprocessor-datasharingpreference-properties"></a>

`OptIn`  <a name="cfn-rekognition-streamprocessor-datasharingpreference-optin"></a>
Describes the opt-in status applied to a stream processor's data sharing policy.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
