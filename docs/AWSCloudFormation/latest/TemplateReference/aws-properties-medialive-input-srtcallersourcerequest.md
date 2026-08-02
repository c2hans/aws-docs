---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-srtcallersourcerequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input SrtCallerSourceRequest
<a name="aws-properties-medialive-input-srtcallersourcerequest"></a>

Configures the connection for a source that uses SRT as the connection protocol. In terms of establishing the connection, MediaLive is always the caller and the upstream system is always the listener. In terms of transmission of the source content, MediaLive is always the receiver and the upstream system is always the sender.

The parent of this entity is SrtSettingsRequest.

## Syntax
<a name="aws-properties-medialive-input-srtcallersourcerequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-srtcallersourcerequest-syntax.json"></a>

```
{
  "[Decryption](#cfn-medialive-input-srtcallersourcerequest-decryption)" : {{SrtCallerDecryptionRequest}},
  "[MinimumLatency](#cfn-medialive-input-srtcallersourcerequest-minimumlatency)" : {{Integer}},
  "[SrtListenerAddress](#cfn-medialive-input-srtcallersourcerequest-srtlisteneraddress)" : {{String}},
  "[SrtListenerPort](#cfn-medialive-input-srtcallersourcerequest-srtlistenerport)" : {{String}},
  "[StreamId](#cfn-medialive-input-srtcallersourcerequest-streamid)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-input-srtcallersourcerequest-syntax.yaml"></a>

```
  [Decryption](#cfn-medialive-input-srtcallersourcerequest-decryption): {{
    SrtCallerDecryptionRequest}}
  [MinimumLatency](#cfn-medialive-input-srtcallersourcerequest-minimumlatency): {{Integer}}
  [SrtListenerAddress](#cfn-medialive-input-srtcallersourcerequest-srtlisteneraddress): {{String}}
  [SrtListenerPort](#cfn-medialive-input-srtcallersourcerequest-srtlistenerport): {{String}}
  [StreamId](#cfn-medialive-input-srtcallersourcerequest-streamid): {{String}}
```

## Properties
<a name="aws-properties-medialive-input-srtcallersourcerequest-properties"></a>

`Decryption`  <a name="cfn-medialive-input-srtcallersourcerequest-decryption"></a>
Complete these parameters only if the content is encrypted.
*Required*: No
*Type*: [SrtCallerDecryptionRequest](aws-properties-medialive-input-srtcallerdecryptionrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumLatency`  <a name="cfn-medialive-input-srtcallersourcerequest-minimumlatency"></a>
The preferred latency (in milliseconds) for implementing packet loss and recovery. Packet recovery is a key feature of SRT. Obtain this value from the operator at the upstream system.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SrtListenerAddress`  <a name="cfn-medialive-input-srtcallersourcerequest-srtlisteneraddress"></a>
The IP address at the upstream system (the listener) that MediaLive (the caller) will connect to.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SrtListenerPort`  <a name="cfn-medialive-input-srtcallersourcerequest-srtlistenerport"></a>
The port at the upstream system (the listener) that MediaLive (the caller) will connect to.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamId`  <a name="cfn-medialive-input-srtcallersourcerequest-streamid"></a>
This value is required if the upstream system uses this identifier because without it, the SRT handshake between MediaLive (the caller) and the upstream system (the listener) might fail.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
