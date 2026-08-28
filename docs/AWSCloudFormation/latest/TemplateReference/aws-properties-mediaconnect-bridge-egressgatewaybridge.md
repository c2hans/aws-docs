---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-bridge-egressgatewaybridge.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Bridge EgressGatewayBridge
<a name="aws-properties-mediaconnect-bridge-egressgatewaybridge"></a>

Create a bridge with the egress bridge type. An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises.

## Syntax
<a name="aws-properties-mediaconnect-bridge-egressgatewaybridge-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-bridge-egressgatewaybridge-syntax.json"></a>

```
{
  "[MaxBitrate](#cfn-mediaconnect-bridge-egressgatewaybridge-maxbitrate)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-bridge-egressgatewaybridge-syntax.yaml"></a>

```
  [MaxBitrate](#cfn-mediaconnect-bridge-egressgatewaybridge-maxbitrate): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-bridge-egressgatewaybridge-properties"></a>

`MaxBitrate`  <a name="cfn-mediaconnect-bridge-egressgatewaybridge-maxbitrate"></a>
 The maximum expected bitrate (in bps) of the egress bridge.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
