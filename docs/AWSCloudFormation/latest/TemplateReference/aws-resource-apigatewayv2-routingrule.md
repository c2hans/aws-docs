---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigatewayv2-routingrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGatewayV2::RoutingRule
<a name="aws-resource-apigatewayv2-routingrule"></a>

Represents a routing rule. When the incoming request to a domain name matches the conditions for a rule, API Gateway invokes a stage of a target API. Supported only for REST APIs.

## Syntax
<a name="aws-resource-apigatewayv2-routingrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-apigatewayv2-routingrule-syntax.json"></a>

```
{
  "Type" : "AWS::ApiGatewayV2::RoutingRule",
  "Properties" : {
      "[Actions](#cfn-apigatewayv2-routingrule-actions)" : {{[ Action, ... ]}},
      "[Conditions](#cfn-apigatewayv2-routingrule-conditions)" : {{[ Condition, ... ]}},
      "[DomainNameArn](#cfn-apigatewayv2-routingrule-domainnamearn)" : {{String}},
      "[Priority](#cfn-apigatewayv2-routingrule-priority)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-apigatewayv2-routingrule-syntax.yaml"></a>

```
Type: AWS::ApiGatewayV2::RoutingRule
Properties:
  [Actions](#cfn-apigatewayv2-routingrule-actions): {{
    - Action}}
  [Conditions](#cfn-apigatewayv2-routingrule-conditions): {{
    - Condition}}
  [DomainNameArn](#cfn-apigatewayv2-routingrule-domainnamearn): {{String}}
  [Priority](#cfn-apigatewayv2-routingrule-priority): {{Integer}}
```

## Properties
<a name="aws-resource-apigatewayv2-routingrule-properties"></a>

`Actions`  <a name="cfn-apigatewayv2-routingrule-actions"></a>
The resulting action based on matching a routing rules condition. Only InvokeApi is supported.
*Required*: Yes
*Type*: Array of [Action](aws-properties-apigatewayv2-routingrule-action.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Conditions`  <a name="cfn-apigatewayv2-routingrule-conditions"></a>
The conditions of the routing rule.
*Required*: Yes
*Type*: Array of [Condition](aws-properties-apigatewayv2-routingrule-condition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainNameArn`  <a name="cfn-apigatewayv2-routingrule-domainnamearn"></a>
The ARN of the domain name.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Priority`  <a name="cfn-apigatewayv2-routingrule-priority"></a>
The order in which API Gateway evaluates a rule. Priority is evaluated from the lowest value to the highest value. Rules can't have the same priority. Priority values 1-1,000,000 are supported.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-apigatewayv2-routingrule-return-values"></a>

### Ref
<a name="aws-resource-apigatewayv2-routingrule-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the routing rule, such as `a1b2c3e`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-apigatewayv2-routingrule-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-apigatewayv2-routingrule-return-values-fn--getatt-fn--getatt"></a>

`RoutingRuleArn`  <a name="RoutingRuleArn-fn::getatt"></a>
Represents an Amazon Resource Name (ARN).

`RoutingRuleId`  <a name="RoutingRuleId-fn::getatt"></a>
The identifier.

## Examples
<a name="aws-resource-apigatewayv2-routingrule--examples"></a>

### Routing rule creation
<a name="aws-resource-apigatewayv2-routingrule--examples--Routing_rule_creation"></a>

The following example creates a `RoutingRule` resource called `MyRoutingRule` that routes any incoming requests that have the header `x-version:beta` and the path `users` to the `prod` stage of REST API `abcd123`.

#### JSON
<a name="aws-resource-apigatewayv2-routingrule--examples--Routing_rule_creation--json"></a>

```
{
  "Resources": {
    "MyRoutingRule": {
      "Type": "AWS::ApiGatewayV2::RoutingRule",
      "Properties": {
        "DomainNameArn": "arn:aws:apigateway:us-west-2::/domainnames/example.com",
        "Priority": 100,
        "Conditions": [
          {
            "MatchHeaders": {
              "AnyOf": [
                {
                  "Header": "x-version",
                  "ValueGlob": "beta"
                }
              ]
            }
          },
          {
            "MatchBasePaths": {
              "AnyOf": [
                "users"
              ]
            }
          }
        ],
        "Actions": [
          {
            "InvokeApi": {
              "ApiId": "abcd123",
              "Stage": "prod"
            }
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-apigatewayv2-routingrule--examples--Routing_rule_creation--yaml"></a>

```
Resources:
  MyRoutingRule:
    Type: 'AWS::ApiGatewayV2::RoutingRule'
    Properties:
      DomainNameArn: arn:aws:apigateway:us-west-2::/domainnames/example.com
      Priority: 100
      Conditions:
        - MatchHeaders:
            AnyOf:
              - Header: "x-version"
                ValueGlob: "beta"
        - MatchBasePaths:
            AnyOf:
              - "users"
      Actions:
        - InvokeApi:
            ApiId: "abcd123"
            Stage: "prod"
```
