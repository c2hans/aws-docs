---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-connection-authparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Connection AuthParameters
<a name="aws-properties-events-connection-authparameters"></a>

Tthe authorization parameters to use for the connection.

## Syntax
<a name="aws-properties-events-connection-authparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-connection-authparameters-syntax.json"></a>

```
{
  "[ApiKeyAuthParameters](#cfn-events-connection-authparameters-apikeyauthparameters)" : {{ApiKeyAuthParameters}},
  "[BasicAuthParameters](#cfn-events-connection-authparameters-basicauthparameters)" : {{BasicAuthParameters}},
  "[ConnectivityParameters](#cfn-events-connection-authparameters-connectivityparameters)" : {{ConnectivityParameters}},
  "[InvocationHttpParameters](#cfn-events-connection-authparameters-invocationhttpparameters)" : {{ConnectionHttpParameters}},
  "[OAuthParameters](#cfn-events-connection-authparameters-oauthparameters)" : {{OAuthParameters}}
}
```

### YAML
<a name="aws-properties-events-connection-authparameters-syntax.yaml"></a>

```
  [ApiKeyAuthParameters](#cfn-events-connection-authparameters-apikeyauthparameters): {{
    ApiKeyAuthParameters}}
  [BasicAuthParameters](#cfn-events-connection-authparameters-basicauthparameters): {{
    BasicAuthParameters}}
  [ConnectivityParameters](#cfn-events-connection-authparameters-connectivityparameters): {{
    ConnectivityParameters}}
  [InvocationHttpParameters](#cfn-events-connection-authparameters-invocationhttpparameters): {{
    ConnectionHttpParameters}}
  [OAuthParameters](#cfn-events-connection-authparameters-oauthparameters): {{
    OAuthParameters}}
```

## Properties
<a name="aws-properties-events-connection-authparameters-properties"></a>

`ApiKeyAuthParameters`  <a name="cfn-events-connection-authparameters-apikeyauthparameters"></a>
The API Key parameters to use for authorization.
*Required*: No
*Type*: [ApiKeyAuthParameters](aws-properties-events-connection-apikeyauthparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BasicAuthParameters`  <a name="cfn-events-connection-authparameters-basicauthparameters"></a>
The authorization parameters for Basic authorization.
*Required*: No
*Type*: [BasicAuthParameters](aws-properties-events-connection-basicauthparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectivityParameters`  <a name="cfn-events-connection-authparameters-connectivityparameters"></a>
For private OAuth authentication endpoints. The parameters EventBridge uses to authenticate against the endpoint.
For more information, see [Authorization methods for connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection-auth.html) in the * *Amazon EventBridge User Guide* *.
*Required*: No
*Type*: [ConnectivityParameters](aws-properties-events-connection-connectivityparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvocationHttpParameters`  <a name="cfn-events-connection-authparameters-invocationhttpparameters"></a>
Additional parameters for the connection that are passed through with every invocation to the HTTP endpoint.
*Required*: No
*Type*: [ConnectionHttpParameters](aws-properties-events-connection-connectionhttpparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuthParameters`  <a name="cfn-events-connection-authparameters-oauthparameters"></a>
The OAuth parameters to use for authorization.
*Required*: No
*Type*: [OAuthParameters](aws-properties-events-connection-oauthparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
