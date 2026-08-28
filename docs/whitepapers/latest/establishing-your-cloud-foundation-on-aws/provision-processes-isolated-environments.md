---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/provision-processes-isolated-environments.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Provision processes for isolated environments
<a name="provision-processes-isolated-environments"></a>

At a smaller scale, request and review processes for creating isolated resource environments often start with manual based inputs to a cloud management team through a ticketing system or other request process. The cloud team will then analyze the request and ensure a set of information is included such as: owner, email address, cost center, project number, and SDLC environment. Additional customer specific meta data may also be collected based on requirements. If an application review board or enterprise architecture board are present within the customer environment they may also review the request. For certain types of environments, it may be decided that approvals are not required or an auto-approval mechanism may be put in place.

Once approved, the isolated environment is created with a baseline configuration and controls that apply to all environments. Configuration and controls may also be applied based on the metadata within the request. Non-production or production environments, for example, may have different requirements and controls applied. Baseline configurations might include the removal of default password configurations, authentication methods, integration with an existing identity provider, IP allocation, network segmentation and connectivity, logging, and security tooling. Additional customer required controls will be implemented at this point, often driven by industry specific regulatory requirements or cloud control best practice guidance through common frameworks such as [Cloud Security Alliance - Cloud Controls Matrix](https://cloudsecurityalliance.org/research/cloud-controls-matrix/) or [NIST Cybersecurity Framework (CSF) Reference Tool](https://www.nist.gov/cyberframework/nist-cybersecurity-framework-csf-reference-tool).

As your environment matures, request, review, and approval processes can be automated using integration with existing IT service management or human workflow tools. Deployment processes can leverage automation through GitOps deployment pipelines and infrastructure as code.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
