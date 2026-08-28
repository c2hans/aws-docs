---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/opensearch-service-migration/operations-security.html
---

# Operations and security
<a name="operations-security"></a>

When you migrate to Amazon OpenSearch Service, your operational activities will change. You will no longer be responsible for provisioning nodes, adding storage, installing and patching operating system, configuring and maintaining high availability, scaling, and other low-level activities. Instead, you can focus your attention on building your use cases and new user experiences.

Amazon OpenSearch Service offers logging, monitoring, and troubleshooting features that you will need to become familiar with to optimize your operational processes.

## Runbooks and new processes
<a name="runbooks"></a>

During the planning stage, identify existing processes that will need to be modified or eliminated. You can then add new operational processes that you might not have had bandwidth for in the past.

While Amazon OpenSearch Service takes away the undifferentiated heavy lifting, you will still need to ensure that your application is designed and monitored to deliver the best performance. You will need to configure monitoring and alerting for your domain so that you are fully aware of any health issues due to internal or external factors. You will need to schedule and initiate upgrades to the latest versions.

All such operational activities will require creating runbooks and modifying existing runbooks. To monitor infrastructure and to analyze operational metrics in Amazon OpenSearch Service, it's crucial to maintain runbooks. Runbooks ensure that you operate consistently according to your compliance and regulatory requirements. If you have not been using runbooks, it's a good time to consider doing so. Create processes to periodically run pre-planned steps to ensure remediation processes such as recovery from application crashes and unexpected failures are fully automated.

## Support and ticketing system
<a name="support"></a>

 To capture incidents associated with your deployments, we recommend planning and operating a ticketing system (you might already be doing so). You might need to train your support staff on how to create support tickets with [AWS Support](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html). We recommend streamlining the process of escalations during ticket triage.

The [Operational excellence](stage-6-operational-excellence.md) section later in this guide will provide you with links to a number of best practices and areas that you may need to consider in your runbooks and build processes around.

## Security
<a name="security"></a>

At AWS, security is the top priority. Amazon OpenSearch Service provides multi-layer security. The service takes care of all security patches and offers network isolation via VPC, fine-grained access control, and multi-tenant support. Your data is encrypted at rest using keys that you create and control through AWS Key Management Service (AWS KMS). The node-to-node encryption capability provides Transport Layer Security (TLS) for all communications between instances in a domain. Amazon OpenSearch Service is also HIPAA eligible, and compliant with PCI DSS, SOC, ISO, and FedRAMP standards to help you meet industry-specific or regulatory requirements.

During the planning stage, identify the people and processes that interact with the domain, choose a network topology, and plan for authentication and authorization for each principal. Depending on your organizational security and compliance requirements, you can use multiple security features to create an environment that meets your business needs. In addition, consider the following factors:
+ **VPC** – You can configure Amazon OpenSearch Service within a virtual private cloud (VPC) on AWS. This is the [recommended configuration](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html). We do not recommend creating a domain with a public endpoint. Plan to create the necessary network architecture to allow your client applications and users to access the target environment.
+ **Authentication** – Amazon OpenSearch Service supports multiple ways to authenticate a user or software client. It supports [Amazon Cognito](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cognito-auth.html) or [SAML authentication](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/saml.html) with your existing identity provider to access [OpenSearch Dashboards](https://opensearch.org/docs/latest/dashboards/index/). It also offers integration with IAM identities, and [basic HTTP authentication using an internal user database](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac-walkthrough-basic.html). You should plan to configure and test an appropriate option for authentication. For more information, see the [OpenSearch Service security documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security.html).
+ **Authorization** – We recommend that you follow the principle of least privilege in configuring access to the service. Amazon OpenSearch Service provides fine-grained access control to help you configure access at document, row, and column levels.

Familiarize yourself with the security features and test them during the PoC stage.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
