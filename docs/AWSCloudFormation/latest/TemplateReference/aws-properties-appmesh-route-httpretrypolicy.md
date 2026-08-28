---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-route-httpretrypolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::Route HttpRetryPolicy
<a name="aws-properties-appmesh-route-httpretrypolicy"></a>

An object that represents a retry policy. Specify at least one value for at least one of the types of `RetryEvents`, a value for `maxRetries`, and a value for `perRetryTimeout`. Both `server-error` and `gateway-error` under `httpRetryEvents` include the Envoy `reset` policy. For more information on the `reset` policy, see the [Envoy documentation](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/router_filter#x-envoy-retry-on).

## Syntax
<a name="aws-properties-appmesh-route-httpretrypolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-route-httpretrypolicy-syntax.json"></a>

```
{
  "[HttpRetryEvents](#cfn-appmesh-route-httpretrypolicy-httpretryevents)" : {{[ String, ... ]}},
  "[MaxRetries](#cfn-appmesh-route-httpretrypolicy-maxretries)" : {{Integer}},
  "[PerRetryTimeout](#cfn-appmesh-route-httpretrypolicy-perretrytimeout)" : {{Duration}},
  "[TcpRetryEvents](#cfn-appmesh-route-httpretrypolicy-tcpretryevents)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-appmesh-route-httpretrypolicy-syntax.yaml"></a>

```
  [HttpRetryEvents](#cfn-appmesh-route-httpretrypolicy-httpretryevents): {{
    - String}}
  [MaxRetries](#cfn-appmesh-route-httpretrypolicy-maxretries): {{Integer}}
  [PerRetryTimeout](#cfn-appmesh-route-httpretrypolicy-perretrytimeout): {{
    Duration}}
  [TcpRetryEvents](#cfn-appmesh-route-httpretrypolicy-tcpretryevents): {{
    - String}}
```

## Properties
<a name="aws-properties-appmesh-route-httpretrypolicy-properties"></a>

`HttpRetryEvents`  <a name="cfn-appmesh-route-httpretrypolicy-httpretryevents"></a>
Specify at least one of the following values.
+ **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511
+ **gateway-error** – HTTP status codes 502, 503, and 504
+ **client-error** – HTTP status code 409
+ **stream-error** – Retry on refused stream
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxRetries`  <a name="cfn-appmesh-route-httpretrypolicy-maxretries"></a>
The maximum number of retry attempts.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PerRetryTimeout`  <a name="cfn-appmesh-route-httpretrypolicy-perretrytimeout"></a>
The timeout for each retry attempt.
*Required*: Yes
*Type*: [Duration](aws-properties-appmesh-route-duration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TcpRetryEvents`  <a name="cfn-appmesh-route-httpretrypolicy-tcpretryevents"></a>
Specify a valid value. The event occurs before any processing of a request has started and is encountered when the upstream is temporarily or permanently unavailable.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
