---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/spank_faq.html
---

# Frequently asked questions about SPANK plugins on AWS PCS
<a name="spank_faq"></a>

This section addresses common questions about installing and configuring SPANK plugins on AWS PCS clusters.

**Do I need to install SPANK plugins on both login nodes and compute nodes?**
Some SPANK plugins don't require installation on all nodes; but for better compatibility, we recommend you install all SPANK plugins on every node.

**What additional configuration is needed for production use of SPANK plugins?**
Beyond the basic installation and configuration shown in the examples, production deployments typically require additional setup. Container-based plugins such as Pyxis might require you to set environment variables for Enroot, enable PMI (Process Management Interface), and configure permissions for the container runtime. See the specific plugin's documentation for detailed production deployment requirements.

**How do I troubleshoot SPANK plugin issues?**
AWS PCS doesn't manage SPANK plugins. Examine error logs on your compute nodes to troubleshoot issues.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
