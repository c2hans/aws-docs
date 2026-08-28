---
source_url: https://docs.aws.amazon.com/dcv/latest/access-console/networking-connectivity.html
---

# Networking and connectivity
<a name="networking-connectivity"></a>

The Amazon DCV Access Console components can all be installed on a single host or on different hosts.

## Single host setup
<a name="single-host-setup"></a>

In a single host setup, the Authentication Server, the Handler component and the Web Client are all installed on a single host. An NGINX server can be used to proxy requests from the web browser to the appropriate component. The web browser should be able to initiate secure, persistent, bi-directional HTTPS connections with NGNIX. All the components need bi-directional HTTP connection between each other on the configured port (see table below). In addition, the Handler component needs to be able to initiate secure, persistent, bi-directional HTTPS connections with the Broker and the persistence store (DynamoDB or MariabDB/MySQL).

| Component | Default Port |
| --- | --- |
| Authentication Server | 3000 |
| Handler | 8080 |
| Web Client | 9000 |

## Multiple host setup
<a name="multiple-host-setup"></a>

In multiple host setup, the Authentication Server, the Handler component and the Web Client can be all installed on different servers. An NGNIX server can be used to proxy requests from the web browser to the Web Client and establish a HTTPS between them. The Authentication Server and the Handler can be configured to accept HTTPS connections. All the components need bi-directional HTTPs connection between them on port 443. In addition, the Handler component needs to be able to initiate secure, persistent, bi-directional HTTPs connections with the Broker and the persistence store (DynamoDB or MariabDB/MySQL).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
