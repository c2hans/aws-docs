---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/invoke-lambda.html
---

# Invoke Lambda functions from a proxy

You can configure Envoy to invoke AWS Lambda functions with the `envoy.filters.http.aws_lambda` filter. The proxy routes matching requests to a cluster that reaches the Lambda endpoint, and Envoy signs each invocation with your proxy role's credentials. The following example listens on port 80: requests to `/lambda` invoke `my-function`, requests to `/other` invoke `my-other-function`, and all other requests receive a `healthy` response without invoking a function.

## Prerequisites
<a name="invoke-lambda-prerequisites"></a>

Before you configure a proxy to invoke Lambda functions, make sure that you have the following:
+ One or more Lambda functions, and the ARN of each function.
+ A proxy role whose identity policy allows `lambda:InvokeFunction` on each function. For more information, see [Permissions](#invoke-lambda-permissions).
+ Network connectivity from the proxy's subnets to the Lambda endpoint. For more information, see [Networking](#invoke-lambda-networking).

## Configure the aws\_lambda filter
<a name="invoke-lambda-configuration"></a>

The following Envoy configuration invokes Lambda functions for requests that match the `/lambda` and `/other` routes.

```
static_resources:
  listeners:
    - name: listener_0
      address:
        socket_address:
          address: "::"
          port_value: 80
          ipv4_compat: true
      filter_chains:
        - filters:
            - name: envoy.filters.network.http_connection_manager
              typed_config:
                "@type": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
                stat_prefix: ingress_http
                route_config:
                  name: local_route
                  virtual_hosts:
                    - name: local_service
                      domains: ["*"]
                      routes:
                        - match:
                            prefix: "/lambda"
                          route:
                            cluster: lambda_egress_gateway
                        - match:
                            prefix: "/other"
                          route:
                            cluster: lambda_egress_gateway
                          typed_per_filter_config:
                            envoy.filters.http.aws_lambda:
                              "@type": type.googleapis.com/envoy.extensions.filters.http.aws_lambda.v3.PerRouteConfig
                              invoke_config:
                                arn: "arn:aws:lambda:us-east-1:123456789012:function:my-other-function"
                                payload_passthrough: false
                        - match:
                            prefix: "/"
                          direct_response:
                            status: 200
                            body:
                              inline_string: "healthy"
                http_filters:
                  - name: envoy.filters.http.aws_lambda
                    typed_config:
                      "@type": type.googleapis.com/envoy.extensions.filters.http.aws_lambda.v3.Config
                      arn: "arn:aws:lambda:us-east-1:123456789012:function:my-function"
                      payload_passthrough: false
                  - name: envoy.filters.http.router
                    typed_config:
                      "@type": type.googleapis.com/envoy.extensions.filters.http.router.v3.Router
  clusters:
    - name: lambda_egress_gateway
      type: LOGICAL_DNS
      dns_lookup_family: V4_ONLY
      connect_timeout: 5s
      lb_policy: ROUND_ROBIN
      metadata:
        filter_metadata:
          com.amazonaws.lambda:
            egress_gateway: true
      load_assignment:
        cluster_name: lambda_egress_gateway
        endpoints:
          - lb_endpoints:
              - endpoint:
                  address:
                    socket_address:
                      address: "lambda.us-east-1.amazonaws.com"
                      port_value: 443
      transport_socket:
        name: envoy.transport_sockets.tls
        typed_config:
          "@type": type.googleapis.com/envoy.extensions.transport_sockets.tls.v3.UpstreamTlsContext
          sni: "lambda.us-east-1.amazonaws.com"
          common_tls_context:
            validation_context:
              trusted_ca:
                filename: /etc/ssl/certs/ca-certificates.crt
```

Replace the example function ARNs `arn:aws:lambda:us-east-1:123456789012:function:my-function` and `arn:aws:lambda:us-east-1:123456789012:function:my-other-function` with the ARNs of your functions.

Replace `lambda.us-east-1.amazonaws.com` with the Lambda endpoint for your functions' Region.

## Credentials
<a name="invoke-lambda-credentials"></a>

Envoy signs each Lambda invocation with the credentials of your proxy role, which ELB for Envoy provides to the proxy.

**Important**
Do not set `credentials` or `credentials_profile` in the `aws_lambda` filter configuration or in a route's `invoke_config`. Either setting makes Envoy sign invocations with other credentials instead of your proxy role's credentials.

## Permissions
<a name="invoke-lambda-permissions"></a>

The identity policy of your proxy role must allow `lambda:InvokeFunction` on each function that the configuration invokes. Add the following statement to your proxy role's policy.

```
{
    "Effect": "Allow",
    "Action": "lambda:InvokeFunction",
    "Resource": [
        "arn:aws:lambda:us-east-1:123456789012:function:my-function",
        "arn:aws:lambda:us-east-1:123456789012:function:my-other-function"
    ]
}
```

Replace the `Resource` ARNs with the ARNs of your functions. For the role's other permissions and its trust policy, see [Create a proxy role](setting-up.md#setting-up-proxy-role).

## Lambda cluster
<a name="invoke-lambda-cluster"></a>

The cluster that sends requests to Lambda must carry the filter metadata `com.amazonaws.lambda` with `egress_gateway: true`. Without this metadata, the `aws_lambda` filter does not invoke a function for requests routed to the cluster. The `/` route has no cluster, so its requests never invoke a function.

The cluster connects to `lambda.<region>.amazonaws.com` on port 443 over TLS, and verifies the endpoint's certificate with the certificate authority (CA) bundle at `/etc/ssl/certs/ca-certificates.crt`.

## Networking
<a name="invoke-lambda-networking"></a>

The proxy connects to the Lambda endpoint from its subnets. The subnets must have a route to `lambda.<region>.amazonaws.com`, and the proxy's security groups must allow outbound HTTPS (TCP port 443) to it.

## Responses
<a name="invoke-lambda-responses"></a>

With `payload_passthrough: false`, the function returns a JSON object, and Envoy uses its `statusCode`, `headers`, and `body` as the status code, headers, and body of the HTTP response. For example, a function that returns the following object produces a `200` response with the body `Hello from Lambda`.

```
{
    "statusCode": 200,
    "headers": {"content-type": "text/plain"},
    "body": "Hello from Lambda"
}
```

When Lambda returns an error, Envoy returns Lambda's response to the client unchanged. For example, if the proxy role lacks `lambda:InvokeFunction` permission on the function, the client receives Lambda's `403` response, which names the proxy role as the caller.

## Apply and verify the configuration
<a name="invoke-lambda-verify"></a>

After you add the filter, cluster, and permissions, apply the configuration to your proxy. To update an existing proxy, see [Update a proxy configuration](update-proxy-configuration.md). To set the configuration when you create a proxy, see [Create a proxy](create-proxy.md).

**To verify that the proxy invokes your functions**

1. Send an HTTP request to a configured route, such as `/lambda`, through the proxy.

1. Confirm that the response comes from your function.

1. Send a request to the `/` route, and confirm that it returns `healthy` without invoking a function.
