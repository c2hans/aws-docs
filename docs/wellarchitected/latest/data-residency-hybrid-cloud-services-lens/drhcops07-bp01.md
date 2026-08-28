---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcops07-bp01.html
---

# DRHCOPS07-BP01 Use AWS services and tools for automation and infrastructure as code (IaC) across hybrid and edge environments
<a name="drhcops07-bp01"></a>

 Automation helps you provide consistent deployment, configuration, and monitoring processes, even for applications and data that need to reside in specific locations due to data residency requirements. This approach improves operational efficiency, reduces errors, and facilitates governance and compliance across your hybrid and edge infrastructure.

 **Desired outcome:** Adopt AWS services and tools for automation and infrastructure as code (IaC) to consistently provision, manage, and maintain hybrid and edge environments, including AWS Outposts and Local Zones.

 **Benefits of establishing this best practice:** Using AWS automation across hybrid and edge deployments enables consistent configuration management, streamlined deployments, and efficient scaling of resources. It reduces manual effort, minimizes human errors, and promotes standardization.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-14"></a>

 Use AWS services like AWS CloudFormation, AWS Outposts installer for servers, and AWS Serverless Application Model (AWS SAM) to automate infrastructure provisioning and application deployments across edge and cloud environments. Implement infrastructure as code (IaC) principles, which produces consistent and repeatable processes for deploying, configuring, and managing resources, even in locations with data residency requirements.

 Additionally, tools like Terraform and Ansible can be used for automation and deployment on AWS Outposts, which are AWS-managed infrastructure and services deployed at your on-premises facilities.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
