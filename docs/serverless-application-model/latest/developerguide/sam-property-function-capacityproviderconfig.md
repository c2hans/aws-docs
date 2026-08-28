---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-capacityproviderconfig.html
---

# CapacityProviderConfig
<a name="sam-property-function-capacityproviderconfig"></a>

Configures the capacity provider to which published versions of the function will be attached. This enables the function to run on customer-owned EC2 instances managed by Lambda.

**Note**
This configuration determines the compute type of a function and needs to be specified during the first function deployment. It can't be added or removed after the function resource has been created.

## Syntax
<a name="sam-property-function-capacityproviderconfig-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-function-capacityproviderconfig-syntax.yaml"></a>

```
[Arn](#sam-function-capacityproviderconfig-arn): {{String}}
[ExecutionEnvironmentMemoryGiBPerVCpu](#sam-function-capacityproviderconfig-executionenvironmentmemorygibpervcpu): {{Float}}
[PerExecutionEnvironmentMaxConcurrency](#sam-function-capacityproviderconfig-perexecutionenvironmentmaxconcurrency): {{Integer}}
```

## Properties
<a name="sam-property-function-capacityproviderconfig-properties"></a>

 `Arn`   <a name="sam-function-capacityproviderconfig-arn"></a>
The ARN of the capacity provider to use for this function.
*Type*: String
*Required*: Yes
*CloudFormation compatibility*: This property is unique to SAM.

 `ExecutionEnvironmentMemoryGiBPerVCpu`   <a name="sam-function-capacityproviderconfig-executionenvironmentmemorygibpervcpu"></a>
The ratio of memory (in GiB) to vCPU for each execution environment.
The memory ratio per CPU can't exceed function's total memory of 2048MB. The supported memory-to-CPU ratios are 2GB, 4GB, or 8GB per CPU.
*Type*: Float
*Required*: No
*CloudFormation compatibility*: This property is passed directly to the `[ExecutionEnvironmentMemoryGiBPerVCpu](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-lambdamanagedinstancescapacityproviderconfig)` property of an `AWS::Lambda::Function` resource.

 `PerExecutionEnvironmentMaxConcurrency`   <a name="sam-function-capacityproviderconfig-perexecutionenvironmentmaxconcurrency"></a>
The maximum number of concurrent executions per execution environment (sandbox).
*Type*: Integer
*Required*: No
*CloudFormation compatibility*: This property is passed directly to the `[PerExecutionEnvironmentMaxConcurrency](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-lambdamanagedinstancescapacityproviderconfig)` property of an `AWS::Lambda::Function` resource.

## Examples
<a name="sam-property-function-capacityproviderconfig-examples"></a>

### Capacity provider configuration
<a name="sam-property-function-capacityproviderconfig-examples-basic"></a>

The following example shows a capacity provider configuration that references a capacity provider resource.

```
CapacityProviderConfig:
  Arn: !GetAtt {{MyCapacityProvider}}.Arn
  ExecutionEnvironmentMemoryGiBPerVCpu: 4.0
  PerExecutionEnvironmentMaxConcurrency: 100
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
