---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/automated-nf-installation-and-configuration.html
---

# Automated NF installation and configuration
<a name="automated-nf-installation-and-configuration"></a>

 AWS TNB performs the installation and configuration of the 5G NFs (for example, CU, AMF, UPF, and SMF) on the provisioned infrastructure.

 **Recommendations:** Verify the NF packages and Helm charts are properly designed to use the capabilities of Kubernetes and the underlying cloud infrastructure. Implement automated testing and canary deployments to validate the NF installations.

 **Practical advice:** Monitor the NF deployments for errors or issues and leverage the AWS TNB APIs to programmatically retrieve logs and metrics for troubleshooting. Establish automated rollback and recovery procedures in case of deployment failures.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
