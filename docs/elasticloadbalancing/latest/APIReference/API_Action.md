---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_Action.html
---

# Action
<a name="API_Action"></a>

Information about an action.

Each rule must include exactly one of the following routing actions: `forward`, `fixed-response`, or `redirect`, and it must be the last action to be performed.

Optionally, a rule for an HTTPS listener can also include one of the following user authentication actions: `authenticate-oidc`, `authenticate-cognito`, or `jwt-validation`.

## Contents
<a name="API_Action_Contents"></a>

 ** Type **
The type of action.
Type: String
Valid Values: `forward | authenticate-oidc | authenticate-cognito | redirect | fixed-response | jwt-validation`
Required: Yes

 ** AuthenticateCognitoConfig **
[HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only when `Type` is `authenticate-cognito`.
Type: [AuthenticateCognitoActionConfig](API_AuthenticateCognitoActionConfig.md) object
Required: No

 ** AuthenticateOidcConfig **
[HTTPS listeners] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when `Type` is `authenticate-oidc`.
Type: [AuthenticateOidcActionConfig](API_AuthenticateOidcActionConfig.md) object
Required: No

 ** FixedResponseConfig **
[Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when `Type` is `fixed-response`.
Type: [FixedResponseActionConfig](API_FixedResponseActionConfig.md) object
Required: No

 ** ForwardConfig **
Information for creating an action that distributes requests among multiple target groups. Specify only when `Type` is `forward`.
If you specify both `ForwardConfig` and `TargetGroupArn`, you can specify only one target group using `ForwardConfig` and it must be the same target group specified in `TargetGroupArn`.
Type: [ForwardActionConfig](API_ForwardActionConfig.md) object
Required: No

 ** JwtValidationConfig **
[HTTPS listeners] Information for validating JWT access tokens in client requests. Specify only when `Type` is `jwt-validation`.
Type: [JwtValidationActionConfig](API_JwtValidationActionConfig.md) object
Required: No

 ** Order **
The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50000.
Required: No

 ** RedirectConfig **
[Application Load Balancer] Information for creating a redirect action. Specify only when `Type` is `redirect`.
Type: [RedirectActionConfig](API_RedirectActionConfig.md) object
Required: No

 ** TargetGroupArn **
The Amazon Resource Name (ARN) of the target group. Specify only when `Type` is `forward` and you want to route to a single target group. To route to multiple target groups, you must use `ForwardConfig` instead.
Type: String
Required: No

## See Also
<a name="API_Action_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/Action)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/Action)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/Action)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
