---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/authoring-lambda-managed-instances.html
---

# Run functions on Lambda Managed Instances with AWS SAM

This topic describes how AWS SAM supports Lambda Managed Instances, how function versions work for these functions, and how to plan for capacity when you deploy them.

## What is Lambda Managed Instances?
<a name="authoring-lambda-managed-instances-intro"></a>

Lambda Managed Instances is a Lambda compute type. With Lambda Managed Instances, you can run your functions on current-generation Amazon EC2 instances in your account, including instances with graphics processing units (GPUs). You choose instance types based on your performance and cost requirements. You also benefit from Amazon EC2 pricing options such as Amazon EC2 Savings Plans and Reserved Instances.

You define a capacity provider that specifies the instance types and subnets to use. Lambda launches the instances, manages their lifecycle, and scales execution environments on them. Each execution environment can process several invocations at the same time.

To learn more, see [Lambda Managed Instances](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html) in the *AWS Lambda Developer Guide*.

**Topics**
+ [What is Lambda Managed Instances?](#authoring-lambda-managed-instances-intro)
+ [Lambda Managed Instances support in AWS SAM](#authoring-lambda-managed-instances-sam-support)
+ [How AWS SAM deployments publish the `$LATEST.PUBLISHED` version](#authoring-lambda-managed-instances-versions)
+ [Use numbered versions and aliases](#authoring-lambda-managed-instances-aliases)
+ [Plan for instance capacity during deployment](#authoring-lambda-managed-instances-capacity)
+ [Learn more](#authoring-lambda-managed-instances-learn)

## Lambda Managed Instances support in AWS SAM
<a name="authoring-lambda-managed-instances-sam-support"></a>

AWS SAM provides the [AWS::Serverless::CapacityProvider](sam-resource-capacityprovider.md) resource for Lambda Managed Instances. This resource defines the capacity provider, which includes the instance types, subnets, and scaling settings for the instances that run your functions.

The following `AWS::Serverless::Function` properties configure a function that runs on a capacity provider:

| **Property** | **Description** |
| --- | --- |
| [CapacityProviderConfig](sam-resource-function.md#sam-function-capacityproviderconfig) | Attaches the function to a capacity provider. For when you can set it, see [CapacityProviderConfig](sam-property-function-capacityproviderconfig.md). |
| [FunctionScalingConfig](sam-resource-function.md#sam-function-functionscalingconfig) | Sets the minimum and maximum number of execution environments. |
| [AcceleratorConfig](sam-resource-function.md#sam-function-acceleratorconfig) | Sets the accelerator memory for a GPU function. |
| [PublishToLatestPublished](sam-resource-function.md#sam-function-publishtolatestpublished) | Controls whether Lambda publishes updates to the `$LATEST.PUBLISHED` version. |

AWS SAM validates these properties when it transforms the template. `FunctionScalingConfig` and `AcceleratorConfig` require `CapacityProviderConfig`. A function that sets `CapacityProviderConfig` can't also set [ProvisionedConcurrencyConfig](sam-resource-function.md#sam-function-provisionedconcurrencyconfig) or [VpcConfig](sam-resource-function.md#sam-function-vpcconfig). Set the network configuration in the capacity provider's [VpcConfig](sam-resource-capacityprovider.md#sam-capacityprovider-vpcconfig) instead.

## How AWS SAM deployments publish the `$LATEST.PUBLISHED` version
<a name="authoring-lambda-managed-instances-versions"></a>

An unqualified invocation of a Lambda Managed Instances function runs the `$LATEST.PUBLISHED` version, and only published versions can serve invocations. So when CloudFormation creates a function that uses a capacity provider, Lambda creates the `$LATEST.PUBLISHED` version regardless of the value of `PublishToLatestPublished`, and you can invoke the function by name as soon as stack creation completes.

`PublishToLatestPublished` applies to later updates of the function. Setting it to `false` doesn't delete a `$LATEST.PUBLISHED` version that already exists.

## Use numbered versions and aliases
<a name="authoring-lambda-managed-instances-aliases"></a>

To publish numbered versions and point an alias at the latest one, use [AutoPublishAlias](sam-resource-function.md#sam-function-autopublishalias).

AWS SAM sets the `DeletionPolicy` of the generated `AWS::Lambda::Version` resource to `Delete` for a function that uses a capacity provider, and to `Retain` for other functions. To use a different policy, set [VersionDeletionPolicy](sam-resource-function.md#sam-function-versiondeletionpolicy).

**Important**
When a function that sets `FunctionScalingConfig` also has `CapacityProviderConfig` and `AutoPublishAlias`, AWS SAM applies `FunctionScalingConfig` to the generated `AWS::Lambda::Version` and to the `AWS::Lambda::Function`. The function-level setting applies to `$LATEST.PUBLISHED`. As a result, the version that the alias points to and `$LATEST.PUBLISHED` each keep at least [MinExecutionEnvironments](sam-property-function-functionscalingconfig.md#sam-function-functionscalingconfig-minexecutionenvironments) execution environments running.
If all invocations go through the alias, set `PublishToLatestPublished` to `false` so that later updates don't publish to `$LATEST.PUBLISHED`. This setting doesn't remove the `$LATEST.PUBLISHED` version created with the function.
To remove the `$LATEST.PUBLISHED` version:
Deploy the template with `PublishToLatestPublished` set to `false`. Otherwise, the next update publishes to `$LATEST.PUBLISHED` again.
Run the following AWS CLI command to delete the `$LATEST.PUBLISHED` version. Use single quotes so that your shell doesn't expand `$LATEST`. Replace {{my-function}} with the name of your function:

   ```
   $ aws lambda delete-function --function-name {{my-function}} --qualifier '$LATEST.PUBLISHED'
   ```
After you remove it, invoke the function only through the alias or a version number, because unqualified invocations use `$LATEST.PUBLISHED`. For more information, see [DeleteFunction](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteFunction.html) in the *AWS Lambda API Reference*.

The following template defines a capacity provider and a function that publishes updates only through the `live` alias. Every function in this template uses the capacity provider, so the template sets `PublishToLatestPublished` in the [Globals section of the AWS SAM template](sam-specification-template-anatomy-globals.md). If a template also has functions that don't use a capacity provider, set `PublishToLatestPublished` on each function that uses one instead. Each `...` line marks where other properties or sections can go:

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Parameters:
  SubnetIds:
    Type: List<AWS::EC2::Subnet::Id>
  SecurityGroupIds:
    Type: List<AWS::EC2::SecurityGroup::Id>
  ...

Globals:
  Function:
    PublishToLatestPublished: false
    ...

Resources:
  MyCapacityProvider:
    Type: AWS::Serverless::CapacityProvider
    Properties:
      VpcConfig:
        SubnetIds: !Ref SubnetIds
        SecurityGroupIds: !Ref SecurityGroupIds
      InstanceRequirements:
        AllowedTypes:
          - {{m7i.large}}
          - {{m7a.large}}
      ...

  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: src/
      Handler: app.handler
      Runtime: python3.13
      MemorySize: 2048
      CapacityProviderConfig:
        Arn: !GetAtt MyCapacityProvider.Arn
      FunctionScalingConfig:
        MinExecutionEnvironments: 3
        MaxExecutionEnvironments: 10
      AutoPublishAlias: live
      ...

  ...
```

**Important**
If you set `CapacityProviderConfig` in the `Globals` section, it applies to every function in the template. No function in the template can then set `ProvisionedConcurrencyConfig` or `VpcConfig`.

## Plan for instance capacity during deployment
<a name="authoring-lambda-managed-instances-capacity"></a>

Stack creation waits until Lambda starts execution environments on the capacity provider's instances. Amazon EC2 capacity might not be available for the allowed instance types in the Availability Zones of the capacity provider's subnets. In that case, the function fails to stabilize and the stack operation fails. To reduce this risk, allow more than one instance type in the capacity provider's [InstanceRequirements](sam-resource-capacityprovider.md#sam-capacityprovider-instancerequirements), and use subnets in more than one Availability Zone.

For GPU functions, Lambda falls back to another allowed instance type when the best-fit type has no capacity. Each allowed instance type must therefore have enough accelerator memory for the function's [AcceleratorConfig](sam-resource-function.md#sam-function-acceleratorconfig). For more information, see [Understanding accelerator memory](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-gpu.html#lambda-managed-instances-gpu-accelerator-memory) in the *AWS Lambda Developer Guide*.

## Learn more
<a name="authoring-lambda-managed-instances-learn"></a>

To learn more about Lambda Managed Instances, see the following topics in the *AWS Lambda Developer Guide*:
+ [Lambda Managed Instances](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html)
+ [$LATEST.PUBLISHED version in Lambda Managed Instances](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-version-publishing.html)
+ [Scaling Lambda Managed Instances](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-scaling.html)
+ [Run GPU-accelerated Event Functions on Lambda Managed Instances](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-gpu.html)
