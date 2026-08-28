---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html
---

# Custom authentication and authorization
<a name="custom-authentication"></a>

 AWS IoT Core lets you define custom authorizers so that you can manage your own client authentication and authorization. This is useful when you need to use authentication mechanisms other than the ones that AWS IoT Core natively supports. (For more information about the natively supported mechanisms, see [Client authentication](client-authentication.md)).

 For example, if you are migrating existing devices in the field to AWS IoT Core and these devices use a custom bearer token or MQTT user name and password to authenticate, you can migrate them to AWS IoT Core without having to provision new identities for them. You can use custom authentication with any of the communication protocols that AWS IoT Core supports. For more information about the protocols that AWS IoT Core supports, see [Device communication protocols](protocols.md).

**Topics**
+ [Understanding the custom authentication workflow](custom-authorizer.md)
+ [Creating and managing custom authorizers (CLI)](config-custom-auth.md)
+ [Custom authentication with X.509 client certificates](custom-auth-509cert.md)
+ [Connecting to AWS IoT Core by using custom authentication](custom-auth.md)
+ [Troubleshooting your authorizers](custom-auth-troubleshooting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
