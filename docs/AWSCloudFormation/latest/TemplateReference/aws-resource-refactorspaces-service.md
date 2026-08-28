---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-refactorspaces-service.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RefactorSpaces::Service
<a name="aws-resource-refactorspaces-service"></a>

**Note**
AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Creates an AWS Migration Hub Refactor Spaces service. The account owner of the service is always the environment owner, regardless of which account in the environment creates the service. Services have either a URL endpoint in a virtual private cloud (VPC), or a Lambda function endpoint.

**Important**
If an AWS resource is launched in a service VPC, and you want it to be accessible to all of an environment’s services with VPCs and routes, apply the `RefactorSpacesSecurityGroup` to the resource. Alternatively, to add more cross-account constraints, apply your own security group.

## Syntax
<a name="aws-resource-refactorspaces-service-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-refactorspaces-service-syntax.json"></a>

```
{
  "Type" : "AWS::RefactorSpaces::Service",
  "Properties" : {
      "[ApplicationIdentifier](#cfn-refactorspaces-service-applicationidentifier)" : {{String}},
      "[Description](#cfn-refactorspaces-service-description)" : {{String}},
      "[EndpointType](#cfn-refactorspaces-service-endpointtype)" : {{String}},
      "[EnvironmentIdentifier](#cfn-refactorspaces-service-environmentidentifier)" : {{String}},
      "[LambdaEndpoint](#cfn-refactorspaces-service-lambdaendpoint)" : {{LambdaEndpointInput}},
      "[Name](#cfn-refactorspaces-service-name)" : {{String}},
      "[Tags](#cfn-refactorspaces-service-tags)" : {{[ Tag, ... ]}},
      "[UrlEndpoint](#cfn-refactorspaces-service-urlendpoint)" : {{UrlEndpointInput}},
      "[VpcId](#cfn-refactorspaces-service-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-refactorspaces-service-syntax.yaml"></a>

```
Type: AWS::RefactorSpaces::Service
Properties:
  [ApplicationIdentifier](#cfn-refactorspaces-service-applicationidentifier): {{String}}
  [Description](#cfn-refactorspaces-service-description): {{String}}
  [EndpointType](#cfn-refactorspaces-service-endpointtype): {{String}}
  [EnvironmentIdentifier](#cfn-refactorspaces-service-environmentidentifier): {{String}}
  [LambdaEndpoint](#cfn-refactorspaces-service-lambdaendpoint): {{
    LambdaEndpointInput}}
  [Name](#cfn-refactorspaces-service-name): {{String}}
  [Tags](#cfn-refactorspaces-service-tags): {{
    - Tag}}
  [UrlEndpoint](#cfn-refactorspaces-service-urlendpoint): {{
    UrlEndpointInput}}
  [VpcId](#cfn-refactorspaces-service-vpcid): {{String}}
```

## Properties
<a name="aws-resource-refactorspaces-service-properties"></a>

`ApplicationIdentifier`  <a name="cfn-refactorspaces-service-applicationidentifier"></a>
The unique identifier of the application.
*Required*: Yes
*Type*: String
*Pattern*: `^app-([0-9A-Za-z]{10}$)`
*Minimum*: `14`
*Maximum*: `14`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-refactorspaces-service-description"></a>
A description of the service.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_\s\.\!\*\#\@\']+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndpointType`  <a name="cfn-refactorspaces-service-endpointtype"></a>
The endpoint type of the service.
*Required*: Yes
*Type*: String
*Allowed values*: `LAMBDA | URL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnvironmentIdentifier`  <a name="cfn-refactorspaces-service-environmentidentifier"></a>
The unique identifier of the environment.
*Required*: Yes
*Type*: String
*Pattern*: `^env-([0-9A-Za-z]{10}$)`
*Minimum*: `14`
*Maximum*: `14`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LambdaEndpoint`  <a name="cfn-refactorspaces-service-lambdaendpoint"></a>
A summary of the configuration for the AWS Lambda endpoint type.
*Required*: No
*Type*: [LambdaEndpointInput](aws-properties-refactorspaces-service-lambdaendpointinput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-refactorspaces-service-name"></a>
The name of the service.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!svc-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-refactorspaces-service-tags"></a>
The tags assigned to the service.
*Required*: No
*Type*: Array of [Tag](aws-properties-refactorspaces-service-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UrlEndpoint`  <a name="cfn-refactorspaces-service-urlendpoint"></a>
The summary of the configuration for the URL endpoint type.
*Required*: No
*Type*: [UrlEndpointInput](aws-properties-refactorspaces-service-urlendpointinput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcId`  <a name="cfn-refactorspaces-service-vpcid"></a>
The ID of the virtual private cloud (VPC).
*Required*: No
*Type*: String
*Pattern*: `^vpc-[-a-f0-9]{8}([-a-f0-9]{9})?$`
*Minimum*: `12`
*Maximum*: `21`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-refactorspaces-service-return-values"></a>

### Ref
<a name="aws-resource-refactorspaces-service-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a composite ID following this format: `<EnvironmentId>|<ApplicationId>|<ServiceId>`. For example, `env-1234654123|app-1234654123|svc-1234654123`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-refactorspaces-service-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-refactorspaces-service-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the service.

`ServiceIdentifier`  <a name="ServiceIdentifier-fn::getatt"></a>
The unique identifier of the service.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
