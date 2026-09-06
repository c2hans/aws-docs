---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mwaaserverless-workflow-networkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MWAAServerless::Workflow NetworkConfiguration
<a name="aws-properties-mwaaserverless-workflow-networkconfiguration"></a>

Network configuration for workflow execution. Specifies VPC security groups and subnets for secure network access. When provided, Amazon Managed Workflows for Apache Airflow Serverless deploys ECS worker tasks in your specified VPC configuration, enabling secure access to VPC-only resources. The service uses a proxy API container architecture where one container handles external communication while the worker container connects to your VPC for task execution. This design provides both security isolation and connectivity flexibility.

## Syntax
<a name="aws-properties-mwaaserverless-workflow-networkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mwaaserverless-workflow-networkconfiguration-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-mwaaserverless-workflow-networkconfiguration-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-mwaaserverless-workflow-networkconfiguration-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-mwaaserverless-workflow-networkconfiguration-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-mwaaserverless-workflow-networkconfiguration-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-mwaaserverless-workflow-networkconfiguration-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-mwaaserverless-workflow-networkconfiguration-properties"></a>

`SecurityGroupIds`  <a name="cfn-mwaaserverless-workflow-networkconfiguration-securitygroupids"></a>
A list of VPC security group IDs to associate with the workflow execution environment.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-mwaaserverless-workflow-networkconfiguration-subnetids"></a>
A list of VPC subnet IDs where the workflow execution environment is deployed.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
