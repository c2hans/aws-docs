---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-containerinstance-versioninfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::ContainerInstance VersionInfo
<a name="aws-properties-ecs-containerinstance-versioninfo"></a>

The Docker and Amazon ECS container agent version information about a container instance.

## Syntax
<a name="aws-properties-ecs-containerinstance-versioninfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-containerinstance-versioninfo-syntax.json"></a>

```
{
  "[AgentHash](#cfn-ecs-containerinstance-versioninfo-agenthash)" : {{String}},
  "[AgentVersion](#cfn-ecs-containerinstance-versioninfo-agentversion)" : {{String}},
  "[DockerVersion](#cfn-ecs-containerinstance-versioninfo-dockerversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-containerinstance-versioninfo-syntax.yaml"></a>

```
  [AgentHash](#cfn-ecs-containerinstance-versioninfo-agenthash): {{String}}
  [AgentVersion](#cfn-ecs-containerinstance-versioninfo-agentversion): {{String}}
  [DockerVersion](#cfn-ecs-containerinstance-versioninfo-dockerversion): {{String}}
```

## Properties
<a name="aws-properties-ecs-containerinstance-versioninfo-properties"></a>

`AgentHash`  <a name="cfn-ecs-containerinstance-versioninfo-agenthash"></a>
The Git commit hash for the Amazon ECS container agent build on the [amazon-ecs-agent ](https://github.com/aws/amazon-ecs-agent) GitHub repository.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AgentVersion`  <a name="cfn-ecs-containerinstance-versioninfo-agentversion"></a>
The version number of the Amazon ECS container agent.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DockerVersion`  <a name="cfn-ecs-containerinstance-versioninfo-dockerversion"></a>
The Docker version that's running on the container instance.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
