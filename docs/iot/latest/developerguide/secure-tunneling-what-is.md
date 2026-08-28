---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling-what-is.html
---

# What is secure tunneling?
<a name="secure-tunneling-what-is"></a>

Use secure tunneling to access devices that are deployed behind port-restricted firewalls at remote sites. You can connect to the destination device from your laptop or desktop computer as the source device by using the AWS Cloud. The source and destination communicate by using an open source local proxy that runs on each device. The local proxy communicates with the AWS Cloud by using an open port that is allowed by firewall, typically 443. Data that is transmitted through the tunnel is encrypted using Transported Layer Security (TLS).

**Topics**
+ [Secure tunneling concepts](secure-tunneling-concepts.md)
+ [How secure tunneling works](how-secure-tunneling-works.md)
+ [Secure tunnel lifecycle](tunnel-lifecycle.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
