---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/iam-for-amq-for-rabbitmq.html
---

# IAM authentication and authorization for Amazon MQ for RabbitMQ
<a name="iam-for-amq-for-rabbitmq"></a>

Amazon MQ for RabbitMQ supports multiple authentication and authorization methods. For information about all supported methods, see [Authentication and authorization for Amazon MQ for RabbitMQ brokers](rabbitmq-authentication.md).

IAM authentication and authorization allows broker users to authenticate using AWS IAM credentials through [IAM outbound federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html). In this method, IAM credentials are used to obtain JWT tokens from AWS Security Token Service (STS). These JWT tokens serve as OAuth 2.0 tokens for authentication, leveraging the existing OAuth 2.0 support in Amazon MQ for RabbitMQ where AWS acts as the OAuth 2.0 identity provider. AWS IAM handles user authentication, while resource permissions for virtual hosts, exchanges, queues, and topics are managed through IAM policies and scope aliases configured in RabbitMQ.

**Important considerations**
IAM authentication is supported on RabbitMQ versions 3.13, 4.2 and above. It isn't supported on Amazon MQ for ActiveMQ brokers.
IAM authentication requires IAM outbound federation to be configured and available in your AWS account.
This method builds on the existing OAuth 2.0 infrastructure in Amazon MQ for RabbitMQ, with AWS serving as the OAuth 2.0 identity provider.
Amazon MQ automatically creates a system user named `monitoring-AWS-OWNED-DO-NOT-DELETE` with monitoring-only permissions. This user uses RabbitMQ's internal authentication system even on IAM-enabled brokers and is restricted to loopback interface access only.

**Topics**
+ [How IAM authentication works](#iam-authentication-overview)
+ [Limitations](#iam-authentication-limitations)

## How IAM authentication works
<a name="iam-authentication-overview"></a>

IAM authentication for Amazon MQ for RabbitMQ uses [IAM outbound federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html) to enable AWS IAM credentials to authenticate with RabbitMQ brokers. IAM credentials are used to obtain JWT tokens from AWS Security Token Service (STS), and these JWT tokens serve as OAuth 2.0 tokens for authentication with the RabbitMQ broker.

## Limitations
<a name="iam-authentication-limitations"></a>

IAM authentication for Amazon MQ for RabbitMQ has the following limitation:
+ **Scope claim configuration** – You cannot use a scope claim directly because the JWT token from STS is nested. The key is `sts.amazonaws.com`, which requires using scope aliases in the RabbitMQ configuration to map IAM roles to RabbitMQ permissions. This limitation also prevents using IAM policies for authorization fully, requiring RabbitMQ configuration for authorization instead.

For information about how to configure IAM authentication and authorization for your Amazon MQ for RabbitMQ brokers, see [Using IAM authentication and authorization](rabbitmq-iam-tutorial.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MQ. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazon-mq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
