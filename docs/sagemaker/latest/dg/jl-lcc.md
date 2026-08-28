---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/jl-lcc.html
---

# Lifecycle configurations with JupyterLab
<a name="jl-lcc"></a>

Lifecycle configurations are shell scripts that are triggered by JupyterLab lifecycle events, such as starting a new JupyterLab notebook. You can use lifecycle configurations to automate customization for your JupyterLab environment. This customization includes installing custom packages, configuring notebook extensions, preloading datasets, and setting up source code repositories.

Using lifecycle configurations gives you flexibility and control to configure JupyterLab to meet your specific needs. For example, you can create a minimal set of base container images with the most commonly used packages and libraries. Then you can use lifecycle configurations to install additional packages for specific use cases across your data science and machine learning teams.

**Note**
Each script has a limit of **16,384 characters**.

**Topics**
+ [Lifecycle configuration creation](jl-lcc-create.md)
+ [Debug lifecycle configurations](jl-lcc-debug.md)
+ [Detach lifecycle configurations](jl-lcc-delete.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
