---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mwaaserverless-workflow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MWAAServerless::Workflow
<a name="aws-resource-mwaaserverless-workflow"></a>

Creates a new workflow in Amazon Managed Workflows for Apache Airflow Serverless. This operation initializes a workflow with the specified configuration including the workflow definition, execution role, and optional settings for encryption, logging, and networking. You must provide the workflow definition as a YAML file stored in Amazon S3 that defines the DAG structure using supported AWS operators. Amazon Managed Workflows for Apache Airflow Serverless automatically creates the first version of the workflow and sets up the necessary execution environment with multi-tenant isolation and security controls.

## Syntax
<a name="aws-resource-mwaaserverless-workflow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mwaaserverless-workflow-syntax.json"></a>

```
{
  "Type" : "AWS::MWAAServerless::Workflow",
  "Properties" : {
      "[DefinitionS3Location](#cfn-mwaaserverless-workflow-definitions3location)" : {{S3Location}},
      "[Description](#cfn-mwaaserverless-workflow-description)" : {{String}},
      "[EncryptionConfiguration](#cfn-mwaaserverless-workflow-encryptionconfiguration)" : {{EncryptionConfiguration}},
      "[LoggingConfiguration](#cfn-mwaaserverless-workflow-loggingconfiguration)" : {{LoggingConfiguration}},
      "[Name](#cfn-mwaaserverless-workflow-name)" : {{String}},
      "[NetworkConfiguration](#cfn-mwaaserverless-workflow-networkconfiguration)" : {{NetworkConfiguration}},
      "[RoleArn](#cfn-mwaaserverless-workflow-rolearn)" : {{String}},
      "[Tags](#cfn-mwaaserverless-workflow-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[TriggerMode](#cfn-mwaaserverless-workflow-triggermode)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-mwaaserverless-workflow-syntax.yaml"></a>

```
Type: AWS::MWAAServerless::Workflow
Properties:
  [DefinitionS3Location](#cfn-mwaaserverless-workflow-definitions3location): {{
    S3Location}}
  [Description](#cfn-mwaaserverless-workflow-description): {{String}}
  [EncryptionConfiguration](#cfn-mwaaserverless-workflow-encryptionconfiguration): {{
    EncryptionConfiguration}}
  [LoggingConfiguration](#cfn-mwaaserverless-workflow-loggingconfiguration): {{
    LoggingConfiguration}}
  [Name](#cfn-mwaaserverless-workflow-name): {{String}}
  [NetworkConfiguration](#cfn-mwaaserverless-workflow-networkconfiguration): {{
    NetworkConfiguration}}
  [RoleArn](#cfn-mwaaserverless-workflow-rolearn): {{String}}
  [Tags](#cfn-mwaaserverless-workflow-tags): {{
    {{Key}}: {{Value}}}}
  [TriggerMode](#cfn-mwaaserverless-workflow-triggermode): {{String}}
```

## Properties
<a name="aws-resource-mwaaserverless-workflow-properties"></a>

`DefinitionS3Location`  <a name="cfn-mwaaserverless-workflow-definitions3location"></a>
The Amazon S3 location of the workflow definition file for this version.
*Required*: Yes
*Type*: [S3Location](aws-properties-mwaaserverless-workflow-s3location.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-mwaaserverless-workflow-description"></a>
The description of the workflow.
*Required*: No
*Type*: String
*Pattern*: `^.+$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionConfiguration`  <a name="cfn-mwaaserverless-workflow-encryptionconfiguration"></a>
The configuration for encrypting workflow data at rest and in transit. Specifies the encryption type and optional KMS key for customer-managed encryption.
*Required*: No
*Type*: [EncryptionConfiguration](aws-properties-mwaaserverless-workflow-encryptionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LoggingConfiguration`  <a name="cfn-mwaaserverless-workflow-loggingconfiguration"></a>
The configuration for workflow logging. Specifies the CloudWatch log group where workflow execution logs are stored. Amazon Managed Workflows for Apache Airflow Serverless automatically exports worker logs and task-level information to the specified log group in your account using remote logging functionality. This provides comprehensive observability for debugging and monitoring workflow execution across the distributed, serverless environment.
*Required*: No
*Type*: [LoggingConfiguration](aws-properties-mwaaserverless-workflow-loggingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-mwaaserverless-workflow-name"></a>
The name of the workflow.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkConfiguration`  <a name="cfn-mwaaserverless-workflow-networkconfiguration"></a>
Network configuration for the workflow execution environment, including VPC security groups and subnets for secure network access. When specified, Amazon Managed Workflows for Apache Airflow Serverless deploys ECS worker tasks in your customer VPC to provide secure connectivity to your resources. If not specified, tasks run in the service's default worker VPC with network isolation from other customers. This configuration enables secure access to VPC-only resources like RDS databases or private endpoints.
*Required*: No
*Type*: [NetworkConfiguration](aws-properties-mwaaserverless-workflow-networkconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-mwaaserverless-workflow-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that Amazon Managed Workflows for Apache Airflow Serverless assumes when executing the workflow. This role must have the necessary permissions to access the required AWS services and resources that your workflow tasks will interact with. The role is used for task execution in the isolated, multi-tenant environment and should follow the principle of least privilege. Amazon Managed Workflows for Apache Airflow Serverless validates role access during workflow creation but runtime permission checks are performed by the target services.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:iam::[0-9]{12}:role(/[a-zA-Z0-9+=,.@_-]{1,512})*?/[a-zA-Z0-9+=,.@_-]{1,64}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-mwaaserverless-workflow-tags"></a>
A map of tags to assign to the workflow resource. Tags are key-value pairs that are used for resource organization and cost allocation.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\w\d+\-\.\:/@]{1,128}$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TriggerMode`  <a name="cfn-mwaaserverless-workflow-triggermode"></a>
The trigger mode for the workflow execution.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mwaaserverless-workflow-return-values"></a>

### Ref
<a name="aws-resource-mwaaserverless-workflow-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the workflow ARN.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-mwaaserverless-workflow-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-mwaaserverless-workflow-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the workflow was created, in ISO 8601 date-time format.

`ModifiedAt`  <a name="ModifiedAt-fn::getatt"></a>
The timestamp when the workflow was last modified, in ISO 8601 date-time format.

`WorkflowArn`  <a name="WorkflowArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the workflow.

`WorkflowStatus`  <a name="WorkflowStatus-fn::getatt"></a>
The current status of the workflow.

`WorkflowVersion`  <a name="WorkflowVersion-fn::getatt"></a>
The version identifier of the workflow.
