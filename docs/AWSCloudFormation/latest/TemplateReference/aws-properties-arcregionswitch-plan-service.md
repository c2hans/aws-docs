---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-service.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan Service
<a name="aws-properties-arcregionswitch-plan-service"></a>

The service for a cross account role.

## Syntax
<a name="aws-properties-arcregionswitch-plan-service-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-service-syntax.json"></a>

```
{
  "[ClusterArn](#cfn-arcregionswitch-plan-service-clusterarn)" : {{String}},
  "[CrossAccountRole](#cfn-arcregionswitch-plan-service-crossaccountrole)" : {{String}},
  "[ExternalId](#cfn-arcregionswitch-plan-service-externalid)" : {{String}},
  "[ServiceArn](#cfn-arcregionswitch-plan-service-servicearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-service-syntax.yaml"></a>

```
  [ClusterArn](#cfn-arcregionswitch-plan-service-clusterarn): {{String}}
  [CrossAccountRole](#cfn-arcregionswitch-plan-service-crossaccountrole): {{String}}
  [ExternalId](#cfn-arcregionswitch-plan-service-externalid): {{String}}
  [ServiceArn](#cfn-arcregionswitch-plan-service-servicearn): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-service-properties"></a>

`ClusterArn`  <a name="cfn-arcregionswitch-plan-service-clusterarn"></a>
The cluster Amazon Resource Name (ARN) for a service.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:ecs:[a-z0-9-]+:\d{12}:cluster/[a-zA-Z0-9_-]{1,255}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CrossAccountRole`  <a name="cfn-arcregionswitch-plan-service-crossaccountrole"></a>
The cross account role for a service.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-arcregionswitch-plan-service-externalid"></a>
The external ID (secret key) for the service.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceArn`  <a name="cfn-arcregionswitch-plan-service-servicearn"></a>
The Amazon Resource Name (ARN) for a service.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:ecs:[a-z0-9-]+:\d{12}:service/[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]{1,255}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
