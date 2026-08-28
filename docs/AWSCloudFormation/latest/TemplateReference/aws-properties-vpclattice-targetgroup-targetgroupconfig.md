---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-targetgroup-targetgroupconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::TargetGroup TargetGroupConfig
<a name="aws-properties-vpclattice-targetgroup-targetgroupconfig"></a>

Describes the configuration of a target group.

For more information, see [Target groups](https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html) in the *Amazon VPC Lattice User Guide*.

## Syntax
<a name="aws-properties-vpclattice-targetgroup-targetgroupconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-targetgroup-targetgroupconfig-syntax.json"></a>

```
{
  "[HealthCheck](#cfn-vpclattice-targetgroup-targetgroupconfig-healthcheck)" : {{HealthCheckConfig}},
  "[IpAddressType](#cfn-vpclattice-targetgroup-targetgroupconfig-ipaddresstype)" : {{String}},
  "[LambdaEventStructureVersion](#cfn-vpclattice-targetgroup-targetgroupconfig-lambdaeventstructureversion)" : {{String}},
  "[Port](#cfn-vpclattice-targetgroup-targetgroupconfig-port)" : {{Integer}},
  "[Protocol](#cfn-vpclattice-targetgroup-targetgroupconfig-protocol)" : {{String}},
  "[ProtocolVersion](#cfn-vpclattice-targetgroup-targetgroupconfig-protocolversion)" : {{String}},
  "[VpcIdentifier](#cfn-vpclattice-targetgroup-targetgroupconfig-vpcidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-vpclattice-targetgroup-targetgroupconfig-syntax.yaml"></a>

```
  [HealthCheck](#cfn-vpclattice-targetgroup-targetgroupconfig-healthcheck): {{
    HealthCheckConfig}}
  [IpAddressType](#cfn-vpclattice-targetgroup-targetgroupconfig-ipaddresstype): {{String}}
  [LambdaEventStructureVersion](#cfn-vpclattice-targetgroup-targetgroupconfig-lambdaeventstructureversion): {{String}}
  [Port](#cfn-vpclattice-targetgroup-targetgroupconfig-port): {{Integer}}
  [Protocol](#cfn-vpclattice-targetgroup-targetgroupconfig-protocol): {{String}}
  [ProtocolVersion](#cfn-vpclattice-targetgroup-targetgroupconfig-protocolversion): {{String}}
  [VpcIdentifier](#cfn-vpclattice-targetgroup-targetgroupconfig-vpcidentifier): {{String}}
```

## Properties
<a name="aws-properties-vpclattice-targetgroup-targetgroupconfig-properties"></a>

`HealthCheck`  <a name="cfn-vpclattice-targetgroup-targetgroupconfig-healthcheck"></a>
The health check configuration. Not supported if the target group type is `LAMBDA` or `ALB`.
*Required*: No
*Type*: [HealthCheckConfig](aws-properties-vpclattice-targetgroup-healthcheckconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpAddressType`  <a name="cfn-vpclattice-targetgroup-targetgroupconfig-ipaddresstype"></a>
The type of IP address used for the target group. Supported only if the target group type is `IP`. The default is `IPV4`.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | IPV6`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LambdaEventStructureVersion`  <a name="cfn-vpclattice-targetgroup-targetgroupconfig-lambdaeventstructureversion"></a>
The version of the event structure that your Lambda function receives. Supported only if the target group type is `LAMBDA`. The default is `V1`.
*Required*: No
*Type*: String
*Allowed values*: `V1 | V2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Port`  <a name="cfn-vpclattice-targetgroup-targetgroupconfig-port"></a>
The port on which the targets are listening. For HTTP, the default is 80. For HTTPS, the default is 443. Not supported if the target group type is `LAMBDA`.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Protocol`  <a name="cfn-vpclattice-targetgroup-targetgroupconfig-protocol"></a>
The protocol to use for routing traffic to the targets. The default is the protocol of the target group. Not supported if the target group type is `LAMBDA`.
*Required*: No
*Type*: String
*Allowed values*: `HTTP | HTTPS | TCP`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProtocolVersion`  <a name="cfn-vpclattice-targetgroup-targetgroupconfig-protocolversion"></a>
The protocol version. The default is `HTTP1`. Not supported if the target group type is `LAMBDA`.
*Required*: No
*Type*: String
*Allowed values*: `HTTP1 | HTTP2 | GRPC`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcIdentifier`  <a name="cfn-vpclattice-targetgroup-targetgroupconfig-vpcidentifier"></a>
The ID of the VPC. Not supported if the target group type is `LAMBDA`.
*Required*: No
*Type*: String
*Pattern*: `^vpc-(([0-9a-z]{8})|([0-9a-z]{17}))$`
*Minimum*: `5`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
