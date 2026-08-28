---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-stack-accessendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::Stack AccessEndpoint
<a name="aws-properties-appstream-stack-accessendpoint"></a>

Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and WorkSpaces Applications. When you specify an interface endpoint for a stack, users of the stack can connect to WorkSpaces Applications only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.

## Syntax
<a name="aws-properties-appstream-stack-accessendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-stack-accessendpoint-syntax.json"></a>

```
{
  "[EndpointType](#cfn-appstream-stack-accessendpoint-endpointtype)" : {{String}},
  "[VpceId](#cfn-appstream-stack-accessendpoint-vpceid)" : {{String}}
}
```

### YAML
<a name="aws-properties-appstream-stack-accessendpoint-syntax.yaml"></a>

```
  [EndpointType](#cfn-appstream-stack-accessendpoint-endpointtype): {{String}}
  [VpceId](#cfn-appstream-stack-accessendpoint-vpceid): {{String}}
```

## Properties
<a name="aws-properties-appstream-stack-accessendpoint-properties"></a>

`EndpointType`  <a name="cfn-appstream-stack-accessendpoint-endpointtype"></a>
The type of interface endpoint.
*Required*: Yes
*Type*: String
*Allowed values*: `STREAMING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpceId`  <a name="cfn-appstream-stack-accessendpoint-vpceid"></a>
The identifier (ID) of the VPC in which the interface endpoint is used.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
