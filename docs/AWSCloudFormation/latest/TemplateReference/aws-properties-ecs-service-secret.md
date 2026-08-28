---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-secret.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service Secret
<a name="aws-properties-ecs-service-secret"></a>

An object representing the secret to expose to your container. Secrets can be exposed to a container in the following ways:
+ To inject sensitive data into your containers as environment variables, use the `secrets` container definition parameter.
+ To reference sensitive information in the log configuration of a container, use the `secretOptions` container definition parameter.

For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html) in the *Amazon Elastic Container Service Developer Guide*.

## Syntax
<a name="aws-properties-ecs-service-secret-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-secret-syntax.json"></a>

```
{
  "[Name](#cfn-ecs-service-secret-name)" : {{String}},
  "[ValueFrom](#cfn-ecs-service-secret-valuefrom)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-service-secret-syntax.yaml"></a>

```
  [Name](#cfn-ecs-service-secret-name): {{String}}
  [ValueFrom](#cfn-ecs-service-secret-valuefrom): {{String}}
```

## Properties
<a name="aws-properties-ecs-service-secret-properties"></a>

`Name`  <a name="cfn-ecs-service-secret-name"></a>
The name of the secret.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueFrom`  <a name="cfn-ecs-service-secret-valuefrom"></a>
The secret to expose to the container. The supported values are either the full ARN of the AWS Secrets Manager secret or the full ARN of the parameter in the SSM Parameter Store.
For information about the require AWS Identity and Access Management permissions, see [Required IAM permissions for Amazon ECS secrets](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data-secrets.html#secrets-iam) (for Secrets Manager) or [Required IAM permissions for Amazon ECS secrets](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data-parameters.html) (for Systems Manager Parameter store) in the *Amazon Elastic Container Service Developer Guide*.
If the SSM Parameter Store parameter exists in the same Region as the task you're launching, then you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-ecs-service-secret--examples"></a>

### Specifying a secret in a service
<a name="aws-properties-ecs-service-secret--examples--Specifying_a_secret_in_a_service"></a>

The following example specifies a secret for the service.

#### JSON
<a name="aws-properties-ecs-service-secret--examples--Specifying_a_secret_in_a_service--json"></a>

```
  {
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
         "ECSTaskDefinition": {
            "Type": "AWS::ECS::TaskDefinition",
            "Properties": {
                "ContainerDefinitions": [
                    {
                        "Essential": true,
                        "Image": "amazon/amazon-ecs-sample",
                        "Name": "example"
                    }
                ],
                "ExecutionRoleArn": "arn:aws:iam::aws_account_id:role/ecsTaskExecutionRole",
                "Family": "task-definition-cfn",
                "Secrets": {
                    "Name": "TestKey",
                    "ValueFrom": 'arn:aws:secretsmanager:region:aws_account_id:secret:secret-name'
                }
            }

        }
        }
    }
```

#### YAML
<a name="aws-properties-ecs-service-secret--examples--Specifying_a_secret_in_a_service--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  ECSTaskDefinition:
    Type: 'AWS::ECS::TaskDefinition'
    Properties:
      ContainerDefinitions:
          Essential: true
          Image: 'amazon/amazon-ecs-sample'
          Name: example
      ExecutionRoleArn: 'arn:aws:iam::aws_account_id:role/ecsTaskExecutionRole'
      Family: task-definition-cfn
      Secrets:
          Name: TestKey
          ValueFrom:'arn:aws:secretsmanager:region:aws_account_id:secret:secret-name'
```

## See also
<a name="aws-properties-ecs-service-secret--seealso"></a>
+  [Associate an Application Load Balancer with a service](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#aws-resource-ecs-service--examples--Associate_an_Application_Load_Balancer_with_a_service)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
