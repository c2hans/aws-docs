---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::ListenerRule AuthenticateCognitoConfig
<a name="aws-properties-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig"></a>

Specifies information required when integrating with Amazon Cognito to authenticate users.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-syntax.json"></a>

```
{
  "[AuthenticationRequestExtraParams](#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-authenticationrequestextraparams)" : {{{{{Key}}: {{Value}}, ...}}},
  "[OnUnauthenticatedRequest](#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-onunauthenticatedrequest)" : {{String}},
  "[Scope](#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-scope)" : {{String}},
  "[SessionCookieName](#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-sessioncookiename)" : {{String}},
  "[SessionTimeout](#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-sessiontimeout)" : {{Integer}},
  "[UserPoolArn](#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-userpoolarn)" : {{String}},
  "[UserPoolClientId](#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-userpoolclientid)" : {{String}},
  "[UserPoolDomain](#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-userpooldomain)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-syntax.yaml"></a>

```
  [AuthenticationRequestExtraParams](#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-authenticationrequestextraparams): {{
    {{Key}}: {{Value}}}}
  [OnUnauthenticatedRequest](#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-onunauthenticatedrequest): {{String}}
  [Scope](#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-scope): {{String}}
  [SessionCookieName](#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-sessioncookiename): {{String}}
  [SessionTimeout](#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-sessiontimeout): {{Integer}}
  [UserPoolArn](#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-userpoolarn): {{String}}
  [UserPoolClientId](#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-userpoolclientid): {{String}}
  [UserPoolDomain](#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-userpooldomain): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-properties"></a>

`AuthenticationRequestExtraParams`  <a name="cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-authenticationrequestextraparams"></a>
The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z0-9]+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnUnauthenticatedRequest`  <a name="cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-onunauthenticatedrequest"></a>
The behavior if the user is not authenticated. The following are possible values:
+ deny`` - Return an HTTP 401 Unauthorized error.
+ allow`` - Allow the request to be forwarded to the target.
+ authenticate`` - Redirect the request to the IdP authorization endpoint. This is the default value.
*Required*: No
*Type*: String
*Allowed values*: `deny | allow | authenticate`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scope`  <a name="cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-scope"></a>
The set of user claims to be requested from the IdP. The default is `openid`.
To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SessionCookieName`  <a name="cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-sessioncookiename"></a>
The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SessionTimeout`  <a name="cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-sessiontimeout"></a>
The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolArn`  <a name="cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-userpoolarn"></a>
The Amazon Resource Name (ARN) of the Amazon Cognito user pool.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolClientId`  <a name="cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-userpoolclientid"></a>
The ID of the Amazon Cognito user pool client.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolDomain`  <a name="cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-userpooldomain"></a>
The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
