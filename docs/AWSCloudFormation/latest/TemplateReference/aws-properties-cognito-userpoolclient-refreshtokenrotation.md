---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpoolclient-refreshtokenrotation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolClient RefreshTokenRotation
<a name="aws-properties-cognito-userpoolclient-refreshtokenrotation"></a>

The configuration of your app client for refresh token rotation. When enabled, your app client issues new ID, access, and refresh tokens when users renew their sessions with refresh tokens. When disabled, token refresh issues only ID and access tokens.

## Syntax
<a name="aws-properties-cognito-userpoolclient-refreshtokenrotation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpoolclient-refreshtokenrotation-syntax.json"></a>

```
{
  "[Feature](#cfn-cognito-userpoolclient-refreshtokenrotation-feature)" : {{String}},
  "[RetryGracePeriodSeconds](#cfn-cognito-userpoolclient-refreshtokenrotation-retrygraceperiodseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cognito-userpoolclient-refreshtokenrotation-syntax.yaml"></a>

```
  [Feature](#cfn-cognito-userpoolclient-refreshtokenrotation-feature): {{String}}
  [RetryGracePeriodSeconds](#cfn-cognito-userpoolclient-refreshtokenrotation-retrygraceperiodseconds): {{Integer}}
```

## Properties
<a name="aws-properties-cognito-userpoolclient-refreshtokenrotation-properties"></a>

`Feature`  <a name="cfn-cognito-userpoolclient-refreshtokenrotation-feature"></a>
The state of refresh token rotation for the current app client.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetryGracePeriodSeconds`  <a name="cfn-cognito-userpoolclient-refreshtokenrotation-retrygraceperiodseconds"></a>
When you request a token refresh with `GetTokensFromRefreshToken`, the original refresh token that you're rotating out can remain valid for a period of time of up to 60 seconds. This allows for client-side retries. When `RetryGracePeriodSeconds` is `0`, the grace period is disabled and a successful request immediately invalidates the submitted refresh token.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
