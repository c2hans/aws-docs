---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable.html
---

# Domain configurations
<a name="iot-custom-endpoints-configurable"></a>

In AWS IoT Core, you can use domain configurations to configure and manage the behaviors of your data endpoints. With domain configurations, you can generate multiple AWS IoT Core data endpoints, customize them with your own fully qualified domain names (FQDN) and associated server certificates, and also associate a custom authorizer. For more information, see [Custom authentication and authorization](custom-authentication.md).

**Topics**
+ [What is a domain configuration?](iot-domain-configuration-what-is.md)
+ [Creating and configuring AWS managed domains](iot-custom-endpoints-configurable-aws.md)
+ [Creating and configuring customer managed domains](iot-custom-endpoints-configurable-custom.md)
+ [Managing domain configurations](iot-custom-endpoints-managing.md)
+ [Configuring TLS settings in domain configurations](iot-endpoints-tls-config.md)
+ [Server certificate configuration for OCSP stapling](iot-custom-endpoints-cert-config.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
