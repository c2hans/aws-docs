---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediaconnect-bridgeoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::BridgeOutput
<a name="aws-resource-mediaconnect-bridgeoutput"></a>

 Adds outputs to an existing bridge.

## Syntax
<a name="aws-resource-mediaconnect-bridgeoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediaconnect-bridgeoutput-syntax.json"></a>

```
{
  "Type" : "AWS::MediaConnect::BridgeOutput",
  "Properties" : {
      "[BridgeArn](#cfn-mediaconnect-bridgeoutput-bridgearn)" : {{String}},
      "[Name](#cfn-mediaconnect-bridgeoutput-name)" : {{String}},
      "[NetworkOutput](#cfn-mediaconnect-bridgeoutput-networkoutput)" : {{BridgeNetworkOutput}}
    }
}
```

### YAML
<a name="aws-resource-mediaconnect-bridgeoutput-syntax.yaml"></a>

```
Type: AWS::MediaConnect::BridgeOutput
Properties:
  [BridgeArn](#cfn-mediaconnect-bridgeoutput-bridgearn): {{String}}
  [Name](#cfn-mediaconnect-bridgeoutput-name): {{String}}
  [NetworkOutput](#cfn-mediaconnect-bridgeoutput-networkoutput): {{
    BridgeNetworkOutput}}
```

## Properties
<a name="aws-resource-mediaconnect-bridgeoutput-properties"></a>

`BridgeArn`  <a name="cfn-mediaconnect-bridgeoutput-bridgearn"></a>
 The Amazon Resource Name (ARN) of the bridge that you want to update.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-mediaconnect-bridgeoutput-name"></a>
The network output name. This name is used to reference the output and must be unique among outputs in this bridge.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkOutput`  <a name="cfn-mediaconnect-bridgeoutput-networkoutput"></a>
 The network output of the bridge. A network output is delivered to your premises.
*Required*: Yes
*Type*: [BridgeNetworkOutput](aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediaconnect-bridgeoutput-return-values"></a>

### Ref
<a name="aws-resource-mediaconnect-bridgeoutput-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the bridge ARN and the bridge name. For example:

 `{ "Ref": "arn:aws:mediaconnect:us-east-1:111122223333:bridge:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballArenaIngress|Output:PrimaryOutput1" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
