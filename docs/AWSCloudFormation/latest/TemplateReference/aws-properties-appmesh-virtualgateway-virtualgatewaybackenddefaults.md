---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualGateway VirtualGatewayBackendDefaults
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults"></a>

An object that represents the default properties for a backend.

## Syntax
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults-syntax.json"></a>

```
{
  "[ClientPolicy](#cfn-appmesh-virtualgateway-virtualgatewaybackenddefaults-clientpolicy)" : {{VirtualGatewayClientPolicy}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults-syntax.yaml"></a>

```
  [ClientPolicy](#cfn-appmesh-virtualgateway-virtualgatewaybackenddefaults-clientpolicy): {{
    VirtualGatewayClientPolicy}}
```

## Properties
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults-properties"></a>

`ClientPolicy`  <a name="cfn-appmesh-virtualgateway-virtualgatewaybackenddefaults-clientpolicy"></a>
A reference to an object that represents a client policy.
*Required*: No
*Type*: [VirtualGatewayClientPolicy](aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
