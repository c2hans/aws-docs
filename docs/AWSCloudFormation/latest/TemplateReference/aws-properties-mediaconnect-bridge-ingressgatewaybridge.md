---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-bridge-ingressgatewaybridge.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Bridge IngressGatewayBridge
<a name="aws-properties-mediaconnect-bridge-ingressgatewaybridge"></a>

Create a bridge with the ingress bridge type. An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud.

## Syntax
<a name="aws-properties-mediaconnect-bridge-ingressgatewaybridge-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-bridge-ingressgatewaybridge-syntax.json"></a>

```
{
  "[MaxBitrate](#cfn-mediaconnect-bridge-ingressgatewaybridge-maxbitrate)" : {{Integer}},
  "[MaxOutputs](#cfn-mediaconnect-bridge-ingressgatewaybridge-maxoutputs)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-bridge-ingressgatewaybridge-syntax.yaml"></a>

```
  [MaxBitrate](#cfn-mediaconnect-bridge-ingressgatewaybridge-maxbitrate): {{Integer}}
  [MaxOutputs](#cfn-mediaconnect-bridge-ingressgatewaybridge-maxoutputs): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-bridge-ingressgatewaybridge-properties"></a>

`MaxBitrate`  <a name="cfn-mediaconnect-bridge-ingressgatewaybridge-maxbitrate"></a>
The maximum expected bitrate (in bps) of the ingress bridge.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxOutputs`  <a name="cfn-mediaconnect-bridge-ingressgatewaybridge-maxoutputs"></a>
The maximum number of outputs on the ingress bridge.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
