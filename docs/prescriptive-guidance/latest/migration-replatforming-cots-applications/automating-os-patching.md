---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-replatforming-cots-applications/automating-os-patching.html
---

# Automating ongoing OS patching
<a name="automating-os-patching"></a>

Legacy applications in on-premises data centers often rely on manual operational processes for ongoing OS patching and software updates. During your replatforming journey, we recommend that you automate OS patching by using [Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html) or other automated patching processes. Patch Manager provides a centralized and consistent process to gather operational insights and implement routine operational tasks on both the AWS Cloud and on-premises resources.

We recommend patching development environments earlier than the patching time window used for production environments. For more information about this, see the [Patch Manager runbook ](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html)for automating OS patching. You should also deploy canary testing to periodically test key application functionalities in pre-production or production environments, and alert support teams if the testing fails. This helps avoid unplanned outages for your application.

## Using automation tools and infrastructure as a code (IaC)
<a name="using-automation-tools-iac"></a>

As part of your application's replatforming journey, you should automate platform builds by using configuration management tools such as [Chef](https://www.chef.io/), [Puppet](https://puppet.com/), or [Ansible](https://www.ansible.com/). These tools enable a repeatable build of the application stack and formalize the steps for generating an application instance, including the stack's configuration.

We recommend that you provision your infrastructure by using IaC best practices. There are several options available for this, including [AWS Cloud Development Kit (CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html), [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) and [Terraform](https://www.terraform.io/). Chef, Ansible, and Puppet also have limited capabilities that might deliver enough automation for your use case.

Repeatable builds that use IaC and configuration management code help you test infrastructure without the overhead and risk of rebuilding those resources. Patching and updating an existing instance can cause a state that makes it difficult to reproduce and identify issues.

If a COTS application doesn't support automated installation, we recommend consulting the [AWS Partner Network (APN)](https://aws.amazon.com/partners/). For more information about this, see the [Platform perspective: Applications and infrastructure](https://d1.awsstatic.com/whitepapers/aws_cloud_adoption_framework.pdf) section of the AWS CAF whitepaper.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
