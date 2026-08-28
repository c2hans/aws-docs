---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jeg-config-options.html
---

# Jupyter Enterprise Gateway (JEG) configuration options
<a name="jeg-config-options"></a>

Amazon EMR on EKS uses Jupyter Enterprise Gateway (JEG) to turn on interactive endpoints. You can set the following values for the allow-listed JEG configurations when you create the endpoint.
+ **`RemoteMappingKernelManager.cull_idle_timeout`** – Timeout in seconds (integer), after which a kernel is considered idle and ready to be culled. Values of `0` or lower deactivate culling. Short timeouts might result in kernels being culled for users with poor network connections.
+ **`RemoteMappingKernelManager.cull_interval`** – The interval in seconds (integer) on which to check for idle kernels that exceed the cull timeout value.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
