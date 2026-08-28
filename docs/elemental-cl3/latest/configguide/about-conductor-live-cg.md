---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/about-conductor-live-cg.html
---

# About this guide
<a name="about-conductor-live-cg"></a>

This guide describes how to configure the Conductor Live and worker nodes in a AWS Elemental Conductor Live cluster. It describes how to configure the Conductor Live manager node, AWS Elemental Live nodes, and AWS Elemental Statmux nodes (if your deployment includes that product).

This guide applies to all versions of the software that are currently available for download from AWS Elemental.

 **Phase 2 of installation**

This guide describes how to configure the Conductor Live nodes and worker nodes (Elemental Live and optionally Elemental Statmux) in a Conductor Live cluster. The guide describes the steps to initially set up the nodes in a cluster, and describes other procedures you might want to perform after the initial deployment. The guide assumes that you have already racked the servers, and you have installed software, if necessary.

****Prerequisite knowledge****
We assume that you know how to:
+ Connect to the Conductor Live web interface using your web browser.
+ Log in to a remote terminal (Linux) session in order to work via the command line interface.

**Note**
For  assistance with your AWS Elemental appliances and software products, see the forums and other helpful tools on the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
