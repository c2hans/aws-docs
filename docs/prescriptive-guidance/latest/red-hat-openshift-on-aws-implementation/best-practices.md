---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/red-hat-openshift-on-aws-implementation/best-practices.html
---

# Best practices
<a name="best-practices"></a>

Follow these best practices when you set up a Red Hat OpenShift cluster on AWS:
+ List all prerequisites and make sure the installation program is set up correctly.
+ Review security guidelines. For example, you might consider [removing the  default cluster administrator](https://docs.openshift.com/container-platform/4.6/authentication/remove-kubeadmin.html) after installation.
+ Check the compatibility of all command line tools, including OpenShift CLI (oc), Kubernetes command line tool (kubectl), AWS CLI, and rosa CLI.
+ Consider [rotating all credentials](https://docs.openshift.com/container-platform/4.7/post_installation_configuration/cluster-tasks.html#post-install-rotate-remove-cloud-creds).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
