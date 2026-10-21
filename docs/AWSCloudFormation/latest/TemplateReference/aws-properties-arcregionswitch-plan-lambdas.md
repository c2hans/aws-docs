---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-lambdas.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan Lambdas
<a name="aws-properties-arcregionswitch-plan-lambdas"></a>

Configuration for AWS Lambda functions used in a Region switch plan.

## Syntax
<a name="aws-properties-arcregionswitch-plan-lambdas-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-lambdas-syntax.json"></a>

```
{
  "[Arn](#cfn-arcregionswitch-plan-lambdas-arn)" : {{String}},
  "[CrossAccountRole](#cfn-arcregionswitch-plan-lambdas-crossaccountrole)" : {{String}},
  "[ExternalId](#cfn-arcregionswitch-plan-lambdas-externalid)" : {{String}},
  "[Payload](#cfn-arcregionswitch-plan-lambdas-payload)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-lambdas-syntax.yaml"></a>

```
  [Arn](#cfn-arcregionswitch-plan-lambdas-arn): {{String}}
  [CrossAccountRole](#cfn-arcregionswitch-plan-lambdas-crossaccountrole): {{String}}
  [ExternalId](#cfn-arcregionswitch-plan-lambdas-externalid): {{String}}
  [Payload](#cfn-arcregionswitch-plan-lambdas-payload): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-lambdas-properties"></a>

`Arn`  <a name="cfn-arcregionswitch-plan-lambdas-arn"></a>
The Amazon Resource Name (ARN) of the Lambda function.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CrossAccountRole`  <a name="cfn-arcregionswitch-plan-lambdas-crossaccountrole"></a>
The cross account role for the configuration.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-arcregionswitch-plan-lambdas-externalid"></a>
The external ID (secret key) for the configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Payload`  <a name="cfn-arcregionswitch-plan-lambdas-payload"></a>
The JSON payload to send to the Lambda function invocation. If you don't specify a payload, Region switch invokes the function with only the execution metadata.
If you provide a JSON object, Region switch merges execution metadata keys (`InvokedBy`, `PlanArn`, `ExecutionId`, `StepName`) into the top level. If one of your keys has the same name as a metadata key, your key takes precedence.
If you provide any other JSON type (string, number, boolean, or array), Region switch forwards it to the Lambda function unchanged, without adding metadata.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `786432`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
