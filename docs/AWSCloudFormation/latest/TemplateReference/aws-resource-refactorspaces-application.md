---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-refactorspaces-application.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RefactorSpaces::Application
<a name="aws-resource-refactorspaces-application"></a>

**Note**
AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Creates an AWS Migration Hub Refactor Spaces application. The account that owns the environment also owns the applications created inside the environment, regardless of the account that creates the application. Refactor Spaces provisions an Amazon API Gateway, API Gateway VPC link, and Network Load Balancer for the application proxy inside your account.

In environments created with a [CreateEnvironment:NetworkFabricType](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType) of `NONE` you need to configure [ VPC to VPC connectivity](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.html) between your service VPC and the application proxy VPC to route traffic through the application proxy to a service with a private URL endpoint. For more information, see [ Create an application](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/getting-started-create-application.html) in the *Refactor Spaces User Guide*.

## Syntax
<a name="aws-resource-refactorspaces-application-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-refactorspaces-application-syntax.json"></a>

```
{
  "Type" : "AWS::RefactorSpaces::Application",
  "Properties" : {
      "[ApiGatewayProxy](#cfn-refactorspaces-application-apigatewayproxy)" : {{ApiGatewayProxyInput}},
      "[EnvironmentIdentifier](#cfn-refactorspaces-application-environmentidentifier)" : {{String}},
      "[Name](#cfn-refactorspaces-application-name)" : {{String}},
      "[ProxyType](#cfn-refactorspaces-application-proxytype)" : {{String}},
      "[Tags](#cfn-refactorspaces-application-tags)" : {{[ Tag, ... ]}},
      "[VpcId](#cfn-refactorspaces-application-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-refactorspaces-application-syntax.yaml"></a>

```
Type: AWS::RefactorSpaces::Application
Properties:
  [ApiGatewayProxy](#cfn-refactorspaces-application-apigatewayproxy): {{
    ApiGatewayProxyInput}}
  [EnvironmentIdentifier](#cfn-refactorspaces-application-environmentidentifier): {{String}}
  [Name](#cfn-refactorspaces-application-name): {{String}}
  [ProxyType](#cfn-refactorspaces-application-proxytype): {{String}}
  [Tags](#cfn-refactorspaces-application-tags): {{
    - Tag}}
  [VpcId](#cfn-refactorspaces-application-vpcid): {{String}}
```

## Properties
<a name="aws-resource-refactorspaces-application-properties"></a>

`ApiGatewayProxy`  <a name="cfn-refactorspaces-application-apigatewayproxy"></a>
The endpoint URL of the Amazon API Gateway proxy.
*Required*: No
*Type*: [ApiGatewayProxyInput](aws-properties-refactorspaces-application-apigatewayproxyinput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnvironmentIdentifier`  <a name="cfn-refactorspaces-application-environmentidentifier"></a>
The unique identifier of the environment.
*Required*: Yes
*Type*: String
*Pattern*: `^env-([0-9A-Za-z]{10}$)`
*Minimum*: `14`
*Maximum*: `14`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-refactorspaces-application-name"></a>
The name of the application.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!app-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProxyType`  <a name="cfn-refactorspaces-application-proxytype"></a>
The proxy type of the proxy created within the application.
*Required*: Yes
*Type*: String
*Allowed values*: `API_GATEWAY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-refactorspaces-application-tags"></a>
The tags assigned to the application.
*Required*: No
*Type*: Array of [Tag](aws-properties-refactorspaces-application-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-refactorspaces-application-vpcid"></a>
The ID of the virtual private cloud (VPC).
*Required*: Yes
*Type*: String
*Pattern*: `^vpc-[-a-f0-9]{8}([-a-f0-9]{9})?$`
*Minimum*: `12`
*Maximum*: `21`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-refactorspaces-application-return-values"></a>

### Ref
<a name="aws-resource-refactorspaces-application-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a composite ID following this format: `<EnvironmentId>|<ApplicationId>`, for example, `env-1234654123|app-1234654123`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-refactorspaces-application-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-refactorspaces-application-return-values-fn--getatt-fn--getatt"></a>

`ApiGatewayId`  <a name="ApiGatewayId-fn::getatt"></a>
The resource ID of the API Gateway for the proxy.

`ApplicationIdentifier`  <a name="ApplicationIdentifier-fn::getatt"></a>
The unique identifier of the application.

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the application.

`NlbArn`  <a name="NlbArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Network Load Balancer.

`NlbName`  <a name="NlbName-fn::getatt"></a>
The name of the Network Load Balancer configured by the API Gateway proxy.

`ProxyUrl`  <a name="ProxyUrl-fn::getatt"></a>
The endpoint URL of the Amazon API Gateway proxy.

`StageName`  <a name="StageName-fn::getatt"></a>
The name of the API Gateway stage. The name defaults to `prod`.

`VpcLinkId`  <a name="VpcLinkId-fn::getatt"></a>
The `VpcLink` ID of the API Gateway proxy.
