---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/containerize-java-a2c/automate.html
---

# Automation
<a name="automate"></a>

When migrating multiple servers, using the command line to run the AWS App2Container workflow is not a scalable solution. For example, manually managing and tracking the progress of each workflow can become overwhelming. The migration can be further complicated if the application server doesn't have internet access or sufficient hardware resources, or if the Docker engine can't be installed. If you manage servers by using Red Hat Ansible or Jenkins, you can use that tool to orchestrate the App2Container workflow.

## Automation using Ansible
<a name="ansible"></a>

Ansible Playbook automates serial performance of tasks, monitoring migration progress for each application, which reduces human intervention and eventually speeds up migration. The playbook can be run from the worker machine or a proxy instance that can communicate with both the application server and the worker machine. The playbook can containerize multiple application servers in parallel. For more insight on how Ansible can be used to automate the App2Container end to end workflow, see the [Automate AWS App2Container workflow using Ansible](https://aws.amazon.com/blogs/containers/automate-aws-app2container-workflow-using-ansible/) blog post.

## Automation using Jenkins
<a name="jenkins"></a>

Using Jenkins, you can centralize control and manage modernization of multiple application servers. You can use the Jenkins user interface to visualize the App2Container workflow. Jenkins facilitates the integration of the existing continuous integration pipeline of the application to one that is created by App2Container.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
