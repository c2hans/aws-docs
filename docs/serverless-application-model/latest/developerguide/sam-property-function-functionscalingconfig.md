---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-functionscalingconfig.html
---

# FunctionScalingConfig
<a name="sam-property-function-functionscalingconfig"></a>

Configures the scaling behavior for Lambda function versions, controlling the number of execution environments (sandboxes) that can be created. This configuration applies to both $LATEST.PUBLISHED and numeric function versions.

## Syntax
<a name="sam-property-function-functionscalingconfig-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-function-functionscalingconfig-syntax.yaml"></a>

```
[MinExecutionEnvironments](#sam-function-functionscalingconfig-minexecutionenvironments): {{Integer}}
[MaxExecutionEnvironments](#sam-function-functionscalingconfig-maxexecutionenvironments): {{Integer}}
```

## Properties
<a name="sam-property-function-functionscalingconfig-properties"></a>

 `MinExecutionEnvironments`   <a name="sam-function-functionscalingconfig-minexecutionenvironments"></a>
The minimum number of execution environments to maintain for the function version.
*Type*: Integer
*Required*: No
*Default*: `3`
*Minimum*: `0`
*CloudFormation compatibility*: This property is passed directly to the `[MinExecutionEnvironments](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-functionscalingconfig-minexecutionenvironments)` property of an `AWS::Lambda::Function` resource.

 `MaxExecutionEnvironments`   <a name="sam-function-functionscalingconfig-maxexecutionenvironments"></a>
The maximum number of execution environments that can be created for the function version.
*Type*: Integer
*Required*: No
*Default*: `3`
*Minimum*: `0`
*CloudFormation compatibility*: This property is passed directly to the `[MaxExecutionEnvironments](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-functionscalingconfig-maxexecutionenvironments)` property of an `AWS::Lambda::Function` resource.

## Examples
<a name="sam-property-function-functionscalingconfig-examples"></a>

### Function scaling configuration
<a name="sam-property-function-functionscalingconfig-examples-basic"></a>

The following example shows a function scaling configuration with minimum and maximum execution environments.

```
FunctionScalingConfig:
  MinExecutionEnvironments: 5
  MaxExecutionEnvironments: 100
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
