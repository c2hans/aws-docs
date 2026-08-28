---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/security-and-operations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Security and Operations
<a name="security-and-operations"></a>

## Application Security
<a name="application-security"></a>

Application security posture and requirements vary based on the type of application, scale of deployment, and choice of environment, but there are common principles and practices that serve as solid foundations across all types of applications.

The key principle for developing secure .NET applications is ensuring that requests from upstream users and systems are trusted, and ensuring that requests sent to downstream systems are also trusted. Applications need to safeguard any credentials or sensitive information they require to operate, control the exposure of the data they process, and integrate with security providers in a protected and maintainable way.

Running applications in a secure manner starts with developing secure applications, but also requires operating them in a secure environment. Security is the highest priority at AWS, and there are various AWS services that can help meet the requirements of the most security-sensitive organizations.

The following sections focus on developing secure applications. For more information on security, including auditing, data governance, network security, and encryption in transit and at rest, see [AWS Cloud Security](https://aws.amazon.com/security/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
