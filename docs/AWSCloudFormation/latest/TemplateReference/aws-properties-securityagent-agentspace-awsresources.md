---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityagent-agentspace-awsresources.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::AgentSpace AWSResources
<a name="aws-properties-securityagent-agentspace-awsresources"></a>

The Amazon Web Services resources associated with an agent space, including VPCs, log groups, S3 buckets, secrets, Lambda functions, and IAM roles.

## Syntax
<a name="aws-properties-securityagent-agentspace-awsresources-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityagent-agentspace-awsresources-syntax.json"></a>

```
{
  "[IamRoles](#cfn-securityagent-agentspace-awsresources-iamroles)" : {{[ String, ... ]}},
  "[LambdaFunctionArns](#cfn-securityagent-agentspace-awsresources-lambdafunctionarns)" : {{[ String, ... ]}},
  "[LogGroups](#cfn-securityagent-agentspace-awsresources-loggroups)" : {{[ String, ... ]}},
  "[S3Buckets](#cfn-securityagent-agentspace-awsresources-s3buckets)" : {{[ String, ... ]}},
  "[SecretArns](#cfn-securityagent-agentspace-awsresources-secretarns)" : {{[ String, ... ]}},
  "[Vpcs](#cfn-securityagent-agentspace-awsresources-vpcs)" : {{[ VpcConfig, ... ]}}
}
```

### YAML
<a name="aws-properties-securityagent-agentspace-awsresources-syntax.yaml"></a>

```
  [IamRoles](#cfn-securityagent-agentspace-awsresources-iamroles): {{
    - String}}
  [LambdaFunctionArns](#cfn-securityagent-agentspace-awsresources-lambdafunctionarns): {{
    - String}}
  [LogGroups](#cfn-securityagent-agentspace-awsresources-loggroups): {{
    - String}}
  [S3Buckets](#cfn-securityagent-agentspace-awsresources-s3buckets): {{
    - String}}
  [SecretArns](#cfn-securityagent-agentspace-awsresources-secretarns): {{
    - String}}
  [Vpcs](#cfn-securityagent-agentspace-awsresources-vpcs): {{
    - VpcConfig}}
```

## Properties
<a name="aws-properties-securityagent-agentspace-awsresources-properties"></a>

`IamRoles`  <a name="cfn-securityagent-agentspace-awsresources-iamroles"></a>
The IAM roles associated with the agent space.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LambdaFunctionArns`  <a name="cfn-securityagent-agentspace-awsresources-lambdafunctionarns"></a>
The Amazon Resource Names (ARNs) of the Lambda functions associated with the agent space.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroups`  <a name="cfn-securityagent-agentspace-awsresources-loggroups"></a>
The Amazon Resource Names (ARNs) of the CloudWatch log groups associated with the agent space.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Buckets`  <a name="cfn-securityagent-agentspace-awsresources-s3buckets"></a>
The Amazon Resource Names (ARNs) of the S3 buckets associated with the agent space.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArns`  <a name="cfn-securityagent-agentspace-awsresources-secretarns"></a>
The Amazon Resource Names (ARNs) of the Secrets Manager secrets associated with the agent space.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Vpcs`  <a name="cfn-securityagent-agentspace-awsresources-vpcs"></a>
The VPC configurations associated with the agent space.
*Required*: No
*Type*: Array of [VpcConfig](aws-properties-securityagent-agentspace-vpcconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
