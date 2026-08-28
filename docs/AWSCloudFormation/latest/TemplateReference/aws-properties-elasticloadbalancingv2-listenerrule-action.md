---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listenerrule-action.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::ListenerRule Action
<a name="aws-properties-elasticloadbalancingv2-listenerrule-action"></a>

Specifies an action for a listener rule.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listenerrule-action-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listenerrule-action-syntax.json"></a>

```
{
  "[AuthenticateCognitoConfig](#cfn-elasticloadbalancingv2-listenerrule-action-authenticatecognitoconfig)" : {{AuthenticateCognitoConfig}},
  "[AuthenticateOidcConfig](#cfn-elasticloadbalancingv2-listenerrule-action-authenticateoidcconfig)" : {{AuthenticateOidcConfig}},
  "[FixedResponseConfig](#cfn-elasticloadbalancingv2-listenerrule-action-fixedresponseconfig)" : {{FixedResponseConfig}},
  "[ForwardConfig](#cfn-elasticloadbalancingv2-listenerrule-action-forwardconfig)" : {{ForwardConfig}},
  "[JwtValidationConfig](#cfn-elasticloadbalancingv2-listenerrule-action-jwtvalidationconfig)" : {{JwtValidationConfig}},
  "[Order](#cfn-elasticloadbalancingv2-listenerrule-action-order)" : {{Integer}},
  "[RedirectConfig](#cfn-elasticloadbalancingv2-listenerrule-action-redirectconfig)" : {{RedirectConfig}},
  "[TargetGroupArn](#cfn-elasticloadbalancingv2-listenerrule-action-targetgrouparn)" : {{String}},
  "[Type](#cfn-elasticloadbalancingv2-listenerrule-action-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listenerrule-action-syntax.yaml"></a>

```
  [AuthenticateCognitoConfig](#cfn-elasticloadbalancingv2-listenerrule-action-authenticatecognitoconfig): {{
    AuthenticateCognitoConfig}}
  [AuthenticateOidcConfig](#cfn-elasticloadbalancingv2-listenerrule-action-authenticateoidcconfig): {{
    AuthenticateOidcConfig}}
  [FixedResponseConfig](#cfn-elasticloadbalancingv2-listenerrule-action-fixedresponseconfig): {{
    FixedResponseConfig}}
  [ForwardConfig](#cfn-elasticloadbalancingv2-listenerrule-action-forwardconfig): {{
    ForwardConfig}}
  [JwtValidationConfig](#cfn-elasticloadbalancingv2-listenerrule-action-jwtvalidationconfig): {{
    JwtValidationConfig}}
  [Order](#cfn-elasticloadbalancingv2-listenerrule-action-order): {{Integer}}
  [RedirectConfig](#cfn-elasticloadbalancingv2-listenerrule-action-redirectconfig): {{
    RedirectConfig}}
  [TargetGroupArn](#cfn-elasticloadbalancingv2-listenerrule-action-targetgrouparn): {{String}}
  [Type](#cfn-elasticloadbalancingv2-listenerrule-action-type): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listenerrule-action-properties"></a>

`AuthenticateCognitoConfig`  <a name="cfn-elasticloadbalancingv2-listenerrule-action-authenticatecognitoconfig"></a>
[HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only when `Type` is `authenticate-cognito`.
*Required*: No
*Type*: [AuthenticateCognitoConfig](aws-properties-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthenticateOidcConfig`  <a name="cfn-elasticloadbalancingv2-listenerrule-action-authenticateoidcconfig"></a>
[HTTPS listeners] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when `Type` is `authenticate-oidc`.
*Required*: No
*Type*: [AuthenticateOidcConfig](aws-properties-elasticloadbalancingv2-listenerrule-authenticateoidcconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FixedResponseConfig`  <a name="cfn-elasticloadbalancingv2-listenerrule-action-fixedresponseconfig"></a>
[Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when `Type` is `fixed-response`.
*Required*: No
*Type*: [FixedResponseConfig](aws-properties-elasticloadbalancingv2-listenerrule-fixedresponseconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ForwardConfig`  <a name="cfn-elasticloadbalancingv2-listenerrule-action-forwardconfig"></a>
Information for creating an action that distributes requests among multiple target groups. Specify only when `Type` is `forward`.
If you specify both `ForwardConfig` and `TargetGroupArn`, you can specify only one target group using `ForwardConfig` and it must be the same target group specified in `TargetGroupArn`.
*Required*: No
*Type*: [ForwardConfig](aws-properties-elasticloadbalancingv2-listenerrule-forwardconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JwtValidationConfig`  <a name="cfn-elasticloadbalancingv2-listenerrule-action-jwtvalidationconfig"></a>
[HTTPS listeners] Information for validating JWT access tokens in client requests. Specify only when `Type` is `jwt-validation`.
*Required*: No
*Type*: [JwtValidationConfig](aws-properties-elasticloadbalancingv2-listenerrule-jwtvalidationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Order`  <a name="cfn-elasticloadbalancingv2-listenerrule-action-order"></a>
The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `50000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedirectConfig`  <a name="cfn-elasticloadbalancingv2-listenerrule-action-redirectconfig"></a>
[Application Load Balancer] Information for creating a redirect action. Specify only when `Type` is `redirect`.
*Required*: No
*Type*: [RedirectConfig](aws-properties-elasticloadbalancingv2-listenerrule-redirectconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetGroupArn`  <a name="cfn-elasticloadbalancingv2-listenerrule-action-targetgrouparn"></a>
The Amazon Resource Name (ARN) of the target group. Specify only when `Type` is `forward` and you want to route to a single target group. To route to multiple target groups, you must use `ForwardConfig` instead.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-elasticloadbalancingv2-listenerrule-action-type"></a>
The type of action.
*Required*: Yes
*Type*: String
*Allowed values*: `forward | authenticate-oidc | authenticate-cognito | redirect | fixed-response | jwt-validation`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
