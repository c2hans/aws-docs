---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-resource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGateway::Resource
<a name="aws-resource-apigateway-resource"></a>

The `AWS::ApiGateway::Resource` resource creates a resource in an API.

## Syntax
<a name="aws-resource-apigateway-resource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-apigateway-resource-syntax.json"></a>

```
{
  "Type" : "AWS::ApiGateway::Resource",
  "Properties" : {
      "[ParentId](#cfn-apigateway-resource-parentid)" : {{String}},
      "[PathPart](#cfn-apigateway-resource-pathpart)" : {{String}},
      "[RestApiId](#cfn-apigateway-resource-restapiid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-apigateway-resource-syntax.yaml"></a>

```
Type: AWS::ApiGateway::Resource
Properties:
  [ParentId](#cfn-apigateway-resource-parentid): {{String}}
  [PathPart](#cfn-apigateway-resource-pathpart): {{String}}
  [RestApiId](#cfn-apigateway-resource-restapiid): {{String}}
```

## Properties
<a name="aws-resource-apigateway-resource-properties"></a>

`ParentId`  <a name="cfn-apigateway-resource-parentid"></a>
The parent resource's identifier.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PathPart`  <a name="cfn-apigateway-resource-pathpart"></a>
The last path segment for this resource.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RestApiId`  <a name="cfn-apigateway-resource-restapiid"></a>
The string identifier of the associated RestApi.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-apigateway-resource-return-values"></a>

### Ref
<a name="aws-resource-apigateway-resource-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource ID, such as `abc123`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-apigateway-resource-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-apigateway-resource-return-values-fn--getatt-fn--getatt"></a>

`ResourceId`  <a name="ResourceId-fn::getatt"></a>
The ID for the resource. For example: `abc123`.

## Examples
<a name="aws-resource-apigateway-resource--examples"></a>

### Create resource
<a name="aws-resource-apigateway-resource--examples--Create_resource"></a>

The following example creates a `stack` resource for the `MyApi` API.

#### JSON
<a name="aws-resource-apigateway-resource--examples--Create_resource--json"></a>

```
{
    "Stack": {
        "Type": "AWS::ApiGateway::Resource",
        "Properties": {
            "RestApiId": {
                "Ref": "MyApi"
            },
            "ParentId": {
                "Fn::GetAtt": [
                    "MyApi",
                    "RootResourceId"
                ]
            },
            "PathPart": "stack"
        }
    }
}
```

#### YAML
<a name="aws-resource-apigateway-resource--examples--Create_resource--yaml"></a>

```
Stack:
  Type: 'AWS::ApiGateway::Resource'
  Properties:
    RestApiId: !Ref MyApi
    ParentId: !GetAtt
      - MyApi
      - RootResourceId
    PathPart: stack
```

## See also
<a name="aws-resource-apigateway-resource--seealso"></a>
+ [resource:create](https://docs.aws.amazon.com/apigateway/latest/api/API_CreateResource.html) in the *Amazon API Gateway REST API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
