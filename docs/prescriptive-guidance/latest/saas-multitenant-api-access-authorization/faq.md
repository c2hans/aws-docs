---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to commonly raised questions about implementing API access control and authorization in multi-tenant SaaS applications.

**Q. What is the difference between authorization and authentication?**

**A. **Authentication is the process of verifying who a user is. Authorization grants permissions to users to access a specific resource.

**Q. What is the difference between authorization and tenant isolation in a SaaS application?**

**A. **Tenant isolation refers to explicit mechanisms that are used in a SaaS system to ensure that each tenant's resources, even when operating on shared infrastructure, are isolated. Multi-tenant authorization refers to the authorization of inbound actions and preventing them from being implemented on the wrong tenant. A hypothetical user could be authenticated and authorized, but might still be able to access the resources of another tenant. Nothing about authentication and authorization necessarily blocks this access, but tenant isolation is required to achieve this objective. For more information about these two concepts, see the [tenant isolation](https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/tenant-isolation.html) discussion in the *AWS SaaS Architecture Fundamentals* whitepaper.

**Q. Why do I need to consider tenant isolation for my SaaS application?**

**A. **SaaS applications have multiple tenants. A tenant can be a customer organization or any external entity that uses that SaaS application. Depending on how the application is designed, this means that tenants may be accessing shared APIs, databases, or other resources. It is important to maintain tenant isolation—that is, constructs that tightly control access to resources, and block any attempt to access resources of another tenant—to prevent users from one tenant accessing another tenant's private information. SaaS applications are often designed to make sure that tenant isolation is maintained throughout an application and that tenants can access only their own resources.

**Q. Why do I need an access control model?**

**A. **Access control models are used to create a consistent method of determining how to grant access to resources in an application. This can be done by assigning roles to users that are closely aligned with business logic, or it can be based on other contextual attributes such as the time of day or whether a user meets a predefined condition. Access control models form the basic logic your application uses when making authorization decisions to determine the user permissions.

**Q. Is API access control necessary for my application?**

**A. **Yes. APIs should always verify that the caller has the appropriate access. Pervasive API access control also ensures that access is only granted based on tenants so that appropriate isolation can be maintained.

**Q. Why are policy engines or PDPs recommended for authorization?**

**A. **A policy decision point (PDP) allows authorization logic in application code to be offloaded to a separate system. This can simplify application code. It also provides an easy-to-use idempotent interface for making authorization decisions for APIs, microservices, Backend for Frontend (BFF) layers, or any other application component.

**Q. What is a PEP?**

**A. **A policy enforcement point (PEP) is responsible for receiving authorization requests that are sent to the PDP for evaluation. A PEP can be anywhere in an application where data and resources must be protected, or where authorization logic is applied. PEPs are relatively simple compared to PDPs. A PEP is responsible only for requesting and evaluating an authorization decision and does not require any authorization logic to be incorporated into it.

**Q. How should I choose between Amazon Verified Permissions** **and OPA?**

**A. **To choose between Verified Permissions and Open Policy Agent (OPA), always keep your use case and your unique requirements in mind. Verified Permissions provides a fully managed way to define fine-grained permissions, audit permissions across applications, and centralize the policy administration system for your applications while meeting your application latency requirements with millisecond processing. OPA is an open source, general-purpose policy engine that also can help you unify policy across your application stack. In order to run OPA you need to host it in your AWS environment, typically with a container or AWS Lambda functions.

Verified Permissions uses the open source Cedar policy language, whereas OPA uses Rego. Therefore, familiarity with one of these languages might sway you to choose that solution. However, we recommend that you read about both languages and then work back from the problem you're trying to solve to find the best solution for your use case.

**Q. Are there open-source alternatives to Verified Permissions** **and OPA?**

**A. **There are a few open-source systems that are similar to Verified Permissions and the Open Policy Agent (OPA), such as the [Common Expression Language (CEL)](https://opensource.google/projects/cel). This guide focuses on on both Verified Permissions, as a scalable permissions management and fine-grained authorization service, and OPA, which is widely adopted, documented, and adaptable to many different types of applications and authorization requirements.

**Q. Do I need to write an authorization service to use OPA, or can I interact with OPA directly?**

**A. **You can interact with OPA directly. An authorization service in the context of this guidance refers to a service that translates authorization decision requests into OPA queries, and vice versa. If your application can query and accept OPA responses directly, there is no need to introduce this additional complexity.

**Q. How do I monitor my OPA agents for uptime and auditing purposes?**

**A. **OPA provides logging and basic uptime monitoring, although its default configuration will likely be insufficient for enterprise deployments. For more information, see the [DevOps, monitoring, and logging](devops.md) section earlier in this guide.

**Q. How can I monitor Verified Permissions for uptime and auditing purposes?**

**A. **Verified Permissions is an AWS managed service, and can be monitored for availability through the AWS Health Dashboard. Additionally, Verified Permissions is capable of logging to AWS CloudTrail, Amazon CloudWatch Logs, Amazon S3, and Amazon Data Firehose.

**Q. Which operating systems and AWS services can I use to run OPA?**

**A. **You can [run OPA on macOS, Windows, and Linux](https://www.openpolicyagent.org/docs/latest/#running-opa). OPA agents can be configured on Amazon Elastic Compute Cloud (Amazon EC2) agents as well as containerization services such as Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS).

**Q. Which operating systems and AWS** **services can I use to run Verified Permissions?**

**A. **Verified Permissions is an AWS managed service and is operated by AWS. No additional configuration, installation, or hosting is necessary to use Verified Permissions except for the capability to make authorization requests to the service.

**Q. Can I run OPA on AWS Lambda?**

**A. **You can run OPA on Lambda as a Go library. For information about how you can do this for an [API Gateway Lambda authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html), see the AWS blog post [Creating a custom Lambda authorizer using Open Policy Agent](https://aws.amazon.com/blogs/opensource/creating-a-custom-lambda-authorizer-using-open-policy-agent/).

**Q. How should I decide between a distributed PDP and centralized PDP approach?**

**A.** This depends on your application. It will most likely be determined based on the latency difference between a distributed and centralized PDP model. We recommend that you build a proof of concept and test your application's performance to verify your solution.

**Q. Can I use OPA for use cases besides APIs?**

**A. **Yes. The OPA documentation provides examples for [Kubernetes](https://www.openpolicyagent.org/docs/kubernetes), [Envoy](https://www.openpolicyagent.org/docs/envoy), [Docker](https://www.openpolicyagent.org/docs/latest/docker-authorization/), [Kafka](https://www.openpolicyagent.org/docs/latest/kafka-authorization/), [SSH and sudo](https://www.openpolicyagent.org/docs/latest/ssh-and-sudo-authorization/), and [Terraform](https://www.openpolicyagent.org/docs/latest/terraform/). Additionally, OPA can return arbitrary JSON responses to queries by using Rego partial rules. Depending on the query, OPA can be used to answer many questions with JSON responses.

**Q. Can I use Verified Permissions** **for use cases besides APIs?**

**A. **Yes. Verified Permissions can provide an `ALLOW` or `DENY` response for any authorization request it receives. Verified Permissions can provide authorization responses for any application or service that requires authorization decisions.

**Q. Can I create policies in Verified Permissions by using the IAM policy language?**

**A. **No. You must use the Cedar policy language to author policies. Cedar is designed to support permissions management for customer application resources, whereas the AWS Identity and Access Management (IAM) policy language evolved to support access control for AWS resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
