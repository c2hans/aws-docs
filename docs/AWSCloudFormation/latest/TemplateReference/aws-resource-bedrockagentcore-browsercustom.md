---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-browsercustom.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::BrowserCustom
<a name="aws-resource-bedrockagentcore-browsercustom"></a>

AgentCore Browser tool provides a fast, secure, cloud-based browser runtime to enable AI agents to interact with websites at scale.

For more information about using the custom browser, see [Interact with web applications using Amazon Bedrock AgentCore Browser](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html).

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-browsercustom-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-browsercustom-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::BrowserCustom",
  "Properties" : {
      "[BrowserSigning](#cfn-bedrockagentcore-browsercustom-browsersigning)" : {{BrowserSigning}},
      "[Certificates](#cfn-bedrockagentcore-browsercustom-certificates)" : {{[ Certificate, ... ]}},
      "[Description](#cfn-bedrockagentcore-browsercustom-description)" : {{String}},
      "[EnterprisePolicies](#cfn-bedrockagentcore-browsercustom-enterprisepolicies)" : {{[ BrowserEnterprisePolicy, ... ]}},
      "[ExecutionRoleArn](#cfn-bedrockagentcore-browsercustom-executionrolearn)" : {{String}},
      "[Name](#cfn-bedrockagentcore-browsercustom-name)" : {{String}},
      "[NetworkConfiguration](#cfn-bedrockagentcore-browsercustom-networkconfiguration)" : {{BrowserNetworkConfiguration}},
      "[RecordingConfig](#cfn-bedrockagentcore-browsercustom-recordingconfig)" : {{RecordingConfig}},
      "[Tags](#cfn-bedrockagentcore-browsercustom-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-browsercustom-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::BrowserCustom
Properties:
  [BrowserSigning](#cfn-bedrockagentcore-browsercustom-browsersigning): {{
    BrowserSigning}}
  [Certificates](#cfn-bedrockagentcore-browsercustom-certificates): {{
    - Certificate}}
  [Description](#cfn-bedrockagentcore-browsercustom-description): {{String}}
  [EnterprisePolicies](#cfn-bedrockagentcore-browsercustom-enterprisepolicies): {{
    - BrowserEnterprisePolicy}}
  [ExecutionRoleArn](#cfn-bedrockagentcore-browsercustom-executionrolearn): {{String}}
  [Name](#cfn-bedrockagentcore-browsercustom-name): {{String}}
  [NetworkConfiguration](#cfn-bedrockagentcore-browsercustom-networkconfiguration): {{
    BrowserNetworkConfiguration}}
  [RecordingConfig](#cfn-bedrockagentcore-browsercustom-recordingconfig): {{
    RecordingConfig}}
  [Tags](#cfn-bedrockagentcore-browsercustom-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-bedrockagentcore-browsercustom-properties"></a>

`BrowserSigning`  <a name="cfn-bedrockagentcore-browsercustom-browsersigning"></a>
The browser signing configuration that enables cryptographic agent identification using HTTP message signatures for web bot authentication.
*Required*: No
*Type*: [BrowserSigning](aws-properties-bedrockagentcore-browsercustom-browsersigning.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Certificates`  <a name="cfn-bedrockagentcore-browsercustom-certificates"></a>
A list of certificates to install in the browser.
*Required*: No
*Type*: Array of [Certificate](aws-properties-bedrockagentcore-browsercustom-certificate.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-bedrockagentcore-browsercustom-description"></a>
The description of the browser.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnterprisePolicies`  <a name="cfn-bedrockagentcore-browsercustom-enterprisepolicies"></a>
A list of enterprise policy files for the browser.
*Required*: No
*Type*: Array of [BrowserEnterprisePolicy](aws-properties-bedrockagentcore-browsercustom-browserenterprisepolicy.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExecutionRoleArn`  <a name="cfn-bedrockagentcore-browsercustom-executionrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that provides permissions for the browser to access AWS services.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws(?:-cn|-us-gov|-iso(?:-[bef])?)?):iam::[0-9]{12}:role/.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-bedrockagentcore-browsercustom-name"></a>
The name of the browser. The name must be unique within your account.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkConfiguration`  <a name="cfn-bedrockagentcore-browsercustom-networkconfiguration"></a>
The network configuration for the browser. This configuration specifies the network mode for the browser.
*Required*: Yes
*Type*: [BrowserNetworkConfiguration](aws-properties-bedrockagentcore-browsercustom-browsernetworkconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecordingConfig`  <a name="cfn-bedrockagentcore-browsercustom-recordingconfig"></a>
The recording configuration for the browser. When enabled, browser sessions are recorded and stored in the specified Amazon S3 location.
*Required*: No
*Type*: [RecordingConfig](aws-properties-bedrockagentcore-browsercustom-recordingconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrockagentcore-browsercustom-tags"></a>
A map of tag keys and values to assign to the browser. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-browsercustom-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-browsercustom-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the custom browser. For example:

 `arn:aws:bedrock-agentcore:us-east-1:123456789012:browser-custom/MyBrowser-a1b2c3d4e5`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-browsercustom-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-browsercustom-return-values-fn--getatt-fn--getatt"></a>

`BrowserArn`  <a name="BrowserArn-fn::getatt"></a>
The ARN for the custom browser.

`BrowserId`  <a name="BrowserId-fn::getatt"></a>
The ID for the custom browser.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time at which the custom browser was created.

`FailureReason`  <a name="FailureReason-fn::getatt"></a>
The reason for failure if the browser is in a failed state.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The time at which the custom browser was last updated.

`Status`  <a name="Status-fn::getatt"></a>
The status of the custom browser.
