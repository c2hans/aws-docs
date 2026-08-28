---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-ciphers.html
---

# Security policy for HTTP APIs in API Gateway
<a name="http-api-ciphers"></a>

API Gateway enforces a security policy of `TLS_1_2` for all HTTP API endpoints.

A *security policy* is a predefined combination of minimum TLS version and cipher suites offered by Amazon API Gateway. The TLS protocol addresses network security problems such as tampering and eavesdropping between a client and server. When your clients establish a TLS handshake to your API through the custom domain, the security policy enforces the TLS version and cipher suite options your clients can choose to use. This security policy accepts TLS 1.2 and TLS 1.3 traffic and rejects TLS 1.0 traffic.

## Supported TLS protocols and ciphers for HTTP APIs
<a name="http-api-ciphers-list"></a>

The following table describes the supported TLS protocols for HTTP APIs.

| **TLS protocols** | **TLS\_1\_2 security policy** |
| --- | --- |
| TLSv1.3 | ![](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes |
| TLSv1.2 | ![](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes |

The following table describes the TLS ciphers that are available for the TLS 1\_2 security policy for HTTP APIs.

| **TLS ciphers** | **TLS\_1\_2 security policy** |
| --- | --- |
| TLS-AES-128-GCM-SHA256 | ![](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes |
| TLS-AES-256-GCM-SHA384 | ![](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes |
| TLS-CHACHA20-POLY1305-SHA256 | ![](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes |
| ECDHE-ECDSA-AES128-GCM-SHA256 | ![](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes |
| ECDHE-RSA-AES128-GCM-SHA256 | ![](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes |
| ECDHE-ECDSA-AES128-SHA256 | ![](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes |
| ECDHE-RSA-AES128-SHA256 | ![](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes |
| ECDHE-ECDSA-AES256-GCM-SHA384 | ![](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes |
| ECDHE-RSA-AES256-GCM-SHA384 | ![](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes |
| ECDHE-ECDSA-AES256-SHA384 | ![](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes |
| ECDHE-RSA-AES256-SHA384 | ![](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes |
| AES128-GCM-SHA256 | ![](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes |
| AES128-SHA256 | ![](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes |
| AES256-GCM-SHA384 | ![](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes |
| AES256-SHA256 | ![](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes |

## OpenSSL and RFC cipher names
<a name="apigateway-secure-connections-openssl-rfc-cipher-names-http"></a>

OpenSSL and IETF RFC 5246 use different names for the same ciphers. For a list of the cipher names, see [OpenSSL and RFC cipher names](apigateway-security-policies-list.md#apigateway-secure-connections-openssl-rfc-cipher-names).

## Information about REST APIs and WebSocket APIs
<a name="apigateway-http-additional-apis"></a>

For more information about REST APIs and WebSocket APIs, see [Choose a security policy for your custom domain in API Gateway](apigateway-custom-domain-tls-version.md) and [Security policy for WebSocket APIs in API Gateway](websocket-api-ciphers.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
