---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-srtlistenersettingsrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input SrtListenerSettingsRequest
<a name="aws-properties-medialive-input-srtlistenersettingsrequest"></a>

Configuration for an SRT listener input. Encryption is required for all SRT listener inputs for security reasons. You must provide decryption settings including algorithm and passphrase secret ARN.

The parent of this entity is SrtSettingsRequest.

## Syntax
<a name="aws-properties-medialive-input-srtlistenersettingsrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-srtlistenersettingsrequest-syntax.json"></a>

```
{
  "[Decryption](#cfn-medialive-input-srtlistenersettingsrequest-decryption)" : {{SrtListenerDecryptionRequest}},
  "[MinimumLatency](#cfn-medialive-input-srtlistenersettingsrequest-minimumlatency)" : {{Integer}},
  "[StreamId](#cfn-medialive-input-srtlistenersettingsrequest-streamid)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-input-srtlistenersettingsrequest-syntax.yaml"></a>

```
  [Decryption](#cfn-medialive-input-srtlistenersettingsrequest-decryption): {{
    SrtListenerDecryptionRequest}}
  [MinimumLatency](#cfn-medialive-input-srtlistenersettingsrequest-minimumlatency): {{Integer}}
  [StreamId](#cfn-medialive-input-srtlistenersettingsrequest-streamid): {{String}}
```

## Properties
<a name="aws-properties-medialive-input-srtlistenersettingsrequest-properties"></a>

`Decryption`  <a name="cfn-medialive-input-srtlistenersettingsrequest-decryption"></a>
Required. Decryption settings. If specified, both algorithm and passphrase secret ARN are required.
*Required*: No
*Type*: [SrtListenerDecryptionRequest](aws-properties-medialive-input-srtlistenerdecryptionrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumLatency`  <a name="cfn-medialive-input-srtlistenersettingsrequest-minimumlatency"></a>
Required. The preferred latency in milliseconds for packet loss and recovery. Range 120-15000.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamId`  <a name="cfn-medialive-input-srtlistenersettingsrequest-streamid"></a>
Optional. The stream ID if the upstream system uses this identifier.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
