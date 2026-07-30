---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-testcase-voicecallentrypointparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::TestCase VoiceCallEntryPointParameters
<a name="aws-properties-connect-testcase-voicecallentrypointparameters"></a>

Parameters for initiating a voice call test.

## Syntax
<a name="aws-properties-connect-testcase-voicecallentrypointparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-testcase-voicecallentrypointparameters-syntax.json"></a>

```
{
  "[DestinationPhoneNumber](#cfn-connect-testcase-voicecallentrypointparameters-destinationphonenumber)" : {{String}},
  "[FlowId](#cfn-connect-testcase-voicecallentrypointparameters-flowid)" : {{String}},
  "[SourcePhoneNumber](#cfn-connect-testcase-voicecallentrypointparameters-sourcephonenumber)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-testcase-voicecallentrypointparameters-syntax.yaml"></a>

```
  [DestinationPhoneNumber](#cfn-connect-testcase-voicecallentrypointparameters-destinationphonenumber): {{String}}
  [FlowId](#cfn-connect-testcase-voicecallentrypointparameters-flowid): {{String}}
  [SourcePhoneNumber](#cfn-connect-testcase-voicecallentrypointparameters-sourcephonenumber): {{String}}
```

## Properties
<a name="aws-properties-connect-testcase-voicecallentrypointparameters-properties"></a>

`DestinationPhoneNumber`  <a name="cfn-connect-testcase-voicecallentrypointparameters-destinationphonenumber"></a>
The destination phone number for the test.
*Required*: No
*Type*: String
*Pattern*: `\\+[1-9]\\d{1,14}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlowId`  <a name="cfn-connect-testcase-voicecallentrypointparameters-flowid"></a>
The flow identifier for the test.
*Required*: No
*Type*: String
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourcePhoneNumber`  <a name="cfn-connect-testcase-voicecallentrypointparameters-sourcephonenumber"></a>
The source phone number for the test.
*Required*: No
*Type*: String
*Pattern*: `\\+[1-9]\\d{1,14}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
