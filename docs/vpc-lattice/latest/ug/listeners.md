---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html
---

# Listeners for your VPC Lattice service
<a name="listeners"></a>

Before you start using your VPC Lattice service, you must add a *listener*. A listener is a process that checks for connection requests, using the protocol and port that you configure. The rules that you define for a listener determine how the service routes requests to its registered targets.

![A service with a listener, listener rules, and two target groups.](http://docs.aws.amazon.com/vpc-lattice/latest/ug/images/service.png)

**Topics**
+ [Listener configuration](#listener-configuration)
+ [HTTP listeners](http-listeners.md)
+ [HTTPS listeners](https-listeners.md)
+ [TLS listeners](tls-listeners.md)
+ [Listener rules](listener-rules.md)
+ [Delete a listener](delete-listener.md)

## Listener configuration
<a name="listener-configuration"></a>

Listeners support the following protocols and ports:
+ **Protocols**: HTTP, HTTPS, TLS
+ **Ports**: 1-65535

If the listener protocol is HTTPS, VPC Lattice will provision and manage a TLS certificate that is associated with the VPC Lattice generated FQDN. VPC Lattice supports TLS on HTTP/1.1 and HTTP/2. When you configure a service with an HTTPS listener, VPC Lattice will automatically determine the HTTP protocol using Application-Layer Protocol Negotiation (ALPN). If ALPN is absent, VPC Lattice defaults to HTTP/1.1. For more information, see [HTTPS listeners](https-listeners.md).

VPC Lattice can listen on HTTP, HTTPS, HTTP/1.1, and HTTP/2 and communicate to targets in any of these protocols and versions. We do not require that the listener and target group protocols match. VPC Lattice manages the entire process of upgrading and downgrading between protocols and versions. For more information, see [Protocol version](target-groups.md#target-group-protocol-version).

You can create a TLS listener to ensure that your application decrypts the encrypted traffic instead of VPC Lattice. For more information, see [TLS listeners](tls-listeners.md).

VPC Lattice does not natively support WebSockets. However, you can still connect to Websocket-based services by using TLS Listeners or routing through VPC Lattice resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
