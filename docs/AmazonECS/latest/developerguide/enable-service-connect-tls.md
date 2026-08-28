---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/enable-service-connect-tls.html
---

# Enabling TLS for Amazon ECS Service Connect
<a name="enable-service-connect-tls"></a>

You enable traffic encryption when you create or update a Service Connect service.

**To enable traffic encryption for a service in an existing namespace using the AWS Management Console**

1. You need to have the infrastructure IAM role. For more information about this role, see [Amazon ECS infrastructure IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html                     ).

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. In the navigation pane, choose **Namespaces**.

1. Choose the **Namespace** with the **Service** you'd like to enable traffic encryption for.

1. Choose the **Service** you'd like to enable traffic encryption for.

1. Choose **Update Service** and scroll down to the Service Connect section.

1. Choose **Turn on traffic encryption** under your service information to enable TLS.

1. For **Service Connect TLS role**, choose an existing infrastructure IAM role or create a new one.

1. For **Signer certificate authority**, choose an existing certificate authority or create a new one.

   For more information, see see [AWS Private Certificate Authority certificates and Service Connect](service-connect-tls.md#service-connect-tls-certificates).

1. For **Choose an AWS KMS key**, choose an AWS owned and managed key or you can choose a different key. You can also choose to create a new one.

For an example of using the AWS CLI to configure TLS for your service, [Configuring Amazon ECS Service Connect with the AWS CLI](create-service-connect.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
