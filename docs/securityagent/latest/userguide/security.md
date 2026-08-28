---
source_url: https://docs.aws.amazon.com/securityagent/latest/userguide/security.html
---

# Security in AWS Security Agent
<a name="security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+  **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS Security Agent in the AWS Cloud. This includes the service infrastructure, AI models, and penetration testing agents. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/).
+  **Security in the cloud** – Your responsibility includes the following areas:
  + Managing access to AWS Security Agent through IAM policies and permissions
  + Protecting the content you provide to the service, including design documents, code repositories, and application URLs for penetration testing
  + Configuring which repositories and applications are monitored
  + Reviewing and acting on security findings provided by the service
  + Securing your applications based on the remediation guidance provided
  + The sensitivity of your data, your company’s requirements, and applicable laws and regulations

This documentation helps you understand how to apply the shared responsibility model when using AWS Security Agent.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
