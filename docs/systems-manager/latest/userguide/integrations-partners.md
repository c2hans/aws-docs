---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/integrations-partners.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Integration with other products and services
<a name="integrations-partners"></a>

AWS Systems Manager has built-in integration for the products and services shown in the following table.

|  |  |
| --- |--- |
| Ansible | [https://www.ansible.com/](https://www.ansible.com/) is an IT automation platform that makes your applications and systems easier to deploy.<br />Systems Manager provides the Systems Manager document (SSM document) `AWS-ApplyAnsiblePlaybooks` which allows you to create State Manager associations that run Ansible playbooks. Learn more [Creating associations that run Ansible playbooks](systems-manager-state-manager-ansible.md)  |
| Chef | [https://www.chef.io/](https://www.chef.io/) is an IT automation tool that makes your applications and systems easier to deploy.<br />Systems Manager provides the `AWS-ApplyChefRecipes` SSM document, which allows you to create associations in State Manager, a tool in AWS Systems Manager, that run Chef recipes. Learn more [Creating associations that run Chef recipes](systems-manager-state-manager-chef.md) <br />Systems Manager also integrates with [https://www.chef.io/products/chef-inspec/](https://www.chef.io/products/chef-inspec/) profiles, allowing you to run compliance scans and view compliant and noncompliant nodes. Learn more [Using Chef InSpec profiles with Systems Manager Compliance](integration-chef-inspec.md)  |
| GitHub | [https://github.com/](https://github.com/) provides hosting for software development version control and collaboration.<br />Systems Manager provides the SSM document `AWS-RunDocument`, which allows you to run other SSM documents stored in GitHub, and the SSM document `AWS-RunRemoteScript` , which allows you to run scripts stored in GitHub.[See the AWS documentation website for more details](http://docs.aws.amazon.com/systems-manager/latest/userguide/integrations-partners.html) |
| Jenkins | [https://www.jenkins.io/](https://www.jenkins.io/) is an open-source automation server that allows developers to reliably build, test, and deploy their software.<br />Automation, a tool in Systems Manager, can be used as a post-build step to pre-install application releases into Amazon Machine Images (AMIs). Learn more [Updating AMIs using Automation and Jenkins](automation-tutorial-update-patch-ami-jenkins-integration.md)  |
| ServiceNow | [https://www.servicenow.com/](https://www.servicenow.com/) is an enterprise service management system that allows you to manage your IT services and operations.<br />Automation, Change Manager, Incident Manager, and OpsCenter, all tools in Systems Manager, integrate with ServiceNow by using the AWS Service Management Connector. With this integration, you can view, create, update, add correspondence, and resolve AWS Support cases from ServiceNow. Learn more [Integrating with ServiceNow](integrations-partners-servicenow.md)   |
| Terraform | HashiCorp [Terraform](https://registry.terraform.io/) is an open-source *infrastructure as code* (IaC) software tool that provides a command line interface (CLI) workflow to manage various cloud services. For Systems Manager, you can use Terraform to manage or provision the following:<br />**Resources**[See the AWS documentation website for more details](http://docs.aws.amazon.com/systems-manager/latest/userguide/integrations-partners.html)<br />**Data sources**[See the AWS documentation website for more details](http://docs.aws.amazon.com/systems-manager/latest/userguide/integrations-partners.html) |

**Topics**
+ [Running scripts from GitHub](integration-remote-scripts.md)
+ [Using Chef InSpec profiles with Systems Manager Compliance](integration-chef-inspec.md)
+ [Integrating with ServiceNow](integrations-partners-servicenow.md)
