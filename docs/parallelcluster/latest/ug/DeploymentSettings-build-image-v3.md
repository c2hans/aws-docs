---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/DeploymentSettings-build-image-v3.html
---

# `DeploymentSettings` section
<a name="DeploymentSettings-build-image-v3"></a>

**Note**
`DeploymentSettings` is added starting with AWS ParallelCluster version 3.4.0.

**(Optional)** Specifies the deployment settings configuration.

```
DeploymentSettings:
  LambdaFunctionsVpcConfig:
    SecurityGroupIds:
      - {{string}}
    SubnetIds:
      - {{string}}
```

## `DeploymentSettings` properties
<a name="DeploymentSettings-build-image-v3.properties"></a>

### `LambdaFunctionsVpcConfig`
<a name="DeploymentSettings-build-image-v3-LambdaFunctionsVpcConfig"></a>

**(Optional)** Specifies the AWS Lambda functions VPC configurations. For more information, see [AWS Lambda VPC configuration in AWS ParallelCluster](lambda-vpc-v3.md).

```
LambdaFunctionsVpcConfig:
  SecurityGroupIds:
    - {{string}}
  SubnetIds:
    - {{string}}
```

#### `LambdaFunctionsVpcConfig properties`
<a name="DeploymentSettings-build-image-v3-LambdaFunctionsVpcConfig.properties"></a>

 `SecurityGroupIds` (**Required**, `[String]`)
The list of Amazon VPC security group IDs that are attached to the Lambda functions.
[Update policy: If this setting is changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3)

 `SubnetIds` (**Required**, `[String]`)
The list of subnet IDs that are attached to the Lambda functions.
[Update policy: If this setting is changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3)

**Note**
The subnets and security groups must be in the same VPC.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
