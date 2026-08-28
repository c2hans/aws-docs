---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-respondergateway-eksendpointsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::ResponderGateway EksEndpointsConfiguration
<a name="aws-properties-rtbfabric-respondergateway-eksendpointsconfiguration"></a>

Describes the configuration of an Amazon Elastic Kubernetes Service endpoint.

## Syntax
<a name="aws-properties-rtbfabric-respondergateway-eksendpointsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-respondergateway-eksendpointsconfiguration-syntax.json"></a>

```
{
  "[ClusterApiServerCaCertificateChain](#cfn-rtbfabric-respondergateway-eksendpointsconfiguration-clusterapiservercacertificatechain)" : {{String}},
  "[ClusterApiServerEndpointUri](#cfn-rtbfabric-respondergateway-eksendpointsconfiguration-clusterapiserverendpointuri)" : {{String}},
  "[ClusterName](#cfn-rtbfabric-respondergateway-eksendpointsconfiguration-clustername)" : {{String}},
  "[EndpointsResourceName](#cfn-rtbfabric-respondergateway-eksendpointsconfiguration-endpointsresourcename)" : {{String}},
  "[EndpointsResourceNamespace](#cfn-rtbfabric-respondergateway-eksendpointsconfiguration-endpointsresourcenamespace)" : {{String}},
  "[RoleArn](#cfn-rtbfabric-respondergateway-eksendpointsconfiguration-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-rtbfabric-respondergateway-eksendpointsconfiguration-syntax.yaml"></a>

```
  [ClusterApiServerCaCertificateChain](#cfn-rtbfabric-respondergateway-eksendpointsconfiguration-clusterapiservercacertificatechain): {{String}}
  [ClusterApiServerEndpointUri](#cfn-rtbfabric-respondergateway-eksendpointsconfiguration-clusterapiserverendpointuri): {{String}}
  [ClusterName](#cfn-rtbfabric-respondergateway-eksendpointsconfiguration-clustername): {{String}}
  [EndpointsResourceName](#cfn-rtbfabric-respondergateway-eksendpointsconfiguration-endpointsresourcename): {{String}}
  [EndpointsResourceNamespace](#cfn-rtbfabric-respondergateway-eksendpointsconfiguration-endpointsresourcenamespace): {{String}}
  [RoleArn](#cfn-rtbfabric-respondergateway-eksendpointsconfiguration-rolearn): {{String}}
```

## Properties
<a name="aws-properties-rtbfabric-respondergateway-eksendpointsconfiguration-properties"></a>

`ClusterApiServerCaCertificateChain`  <a name="cfn-rtbfabric-respondergateway-eksendpointsconfiguration-clusterapiservercacertificatechain"></a>
The CA certificate chain of the cluster API server.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2097152`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ClusterApiServerEndpointUri`  <a name="cfn-rtbfabric-respondergateway-eksendpointsconfiguration-clusterapiserverendpointuri"></a>
The URI of the cluster API server endpoint.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|http)://(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)(?:\.(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?))+$`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ClusterName`  <a name="cfn-rtbfabric-respondergateway-eksendpointsconfiguration-clustername"></a>
The name of the cluster.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9-]{0,61}[A-Za-z0-9]$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`EndpointsResourceName`  <a name="cfn-rtbfabric-respondergateway-eksendpointsconfiguration-endpointsresourcename"></a>
The name of the endpoint resource.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9-]{0,61}[A-Za-z0-9]$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`EndpointsResourceNamespace`  <a name="cfn-rtbfabric-respondergateway-eksendpointsconfiguration-endpointsresourcenamespace"></a>
The namespace of the endpoint resource.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9-]{0,61}[A-Za-z0-9]$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`RoleArn`  <a name="cfn-rtbfabric-respondergateway-eksendpointsconfiguration-rolearn"></a>
The role ARN for the cluster.
*Required*: Yes
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
