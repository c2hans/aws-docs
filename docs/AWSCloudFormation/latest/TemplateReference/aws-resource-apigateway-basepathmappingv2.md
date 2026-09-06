---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-basepathmappingv2.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGateway::BasePathMappingV2
<a name="aws-resource-apigateway-basepathmappingv2"></a>

The `AWS::ApiGateway::BasePathMappingV2` resource creates a base path that clients who call your API must use in the invocation URL. Supported only for private custom domain names.

## Syntax
<a name="aws-resource-apigateway-basepathmappingv2-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-apigateway-basepathmappingv2-syntax.json"></a>

```
{
  "Type" : "AWS::ApiGateway::BasePathMappingV2",
  "Properties" : {
      "[BasePath](#cfn-apigateway-basepathmappingv2-basepath)" : {{String}},
      "[DomainNameArn](#cfn-apigateway-basepathmappingv2-domainnamearn)" : {{String}},
      "[RestApiId](#cfn-apigateway-basepathmappingv2-restapiid)" : {{String}},
      "[Stage](#cfn-apigateway-basepathmappingv2-stage)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-apigateway-basepathmappingv2-syntax.yaml"></a>

```
Type: AWS::ApiGateway::BasePathMappingV2
Properties:
  [BasePath](#cfn-apigateway-basepathmappingv2-basepath): {{String}}
  [DomainNameArn](#cfn-apigateway-basepathmappingv2-domainnamearn): {{String}}
  [RestApiId](#cfn-apigateway-basepathmappingv2-restapiid): {{String}}
  [Stage](#cfn-apigateway-basepathmappingv2-stage): {{String}}
```

## Properties
<a name="aws-resource-apigateway-basepathmappingv2-properties"></a>

`BasePath`  <a name="cfn-apigateway-basepathmappingv2-basepath"></a>
The base path name that callers of the private API must provide as part of the URL after the domain name.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainNameArn`  <a name="cfn-apigateway-basepathmappingv2-domainnamearn"></a>
The ARN of the domain name for the BasePathMappingV2 resource to be described.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RestApiId`  <a name="cfn-apigateway-basepathmappingv2-restapiid"></a>
The private API's identifier. This identifier is unique across all of your APIs in API Gateway.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Stage`  <a name="cfn-apigateway-basepathmappingv2-stage"></a>
Represents a unique identifier for a version of a deployed private RestApi that is callable by users. The Stage must depend on the `RestApi`'s stage. To create a dependency, add a DependsOn attribute to the BasePathMappingV2 resource.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-resource-apigateway-basepathmappingv2--examples"></a>

### Base path mapping creation example
<a name="aws-resource-apigateway-basepathmappingv2--examples--Base_path_mapping_creation_example"></a>

The following example creates a `BasePathMappingV2` resource called `MyBasePathMappingV2`.

#### JSON
<a name="aws-resource-apigateway-basepathmappingv2--examples--Base_path_mapping_creation_example--json"></a>

```
{
    "MyBasePathMappingV2": {
        "Type": "AWS::ApiGateway::BasePathMappingV2",
        "DependsOn": [
            "PrivateApiStage"
         ],
        "Properties": {
            "BasePath": "prod",
            "DomainNameArn": {
                "Fn::GetAtt": [
                    "MyDomainName",
                    "DomainNameArn"
                ]
            },
            "RestApiId": "a1b2c3",
            "Stage": "users"
        }
    }
}
```

#### YAML
<a name="aws-resource-apigateway-basepathmappingv2--examples--Base_path_mapping_creation_example--yaml"></a>

```
MyBasePathMappingV2:
  Type: AWS::ApiGateway::BasePathMappingV2
  DependsOn:
   - PrivateApiStage
  Properties:
    BasePath: prod
    DomainNameArn: !GetAtt MyDomainName.DomainNameArn
    RestApiId: a1b2c3
    Stage: users
```
