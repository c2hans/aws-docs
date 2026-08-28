---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-multi-cluster-prereqs.html
---

# Multi-cluster prerequisites for AWS CloudHSM
<a name="cloudhsm_cli-multi-cluster-prereqs"></a>

Before configuring your cluster in AWS CloudHSM to connect to multiple clusters, you must meet the following prerequisites:
+ Two or more AWS CloudHSM clusters to which you’d like to connect to, along with their cluster certificates.
+ An EC2 instance with Security Groups correctly configured to connect to all of the clusters above. For more information about how to set up a cluster and the client instance, refer to [Getting started with AWS CloudHSM](getting-started.md).
+ To set up multi-cluster functionality, you must have already downloaded and installed the CloudHSM CLI. If you have not already done this, refer to the instructions in [Getting started with AWS CloudHSM Command Line Interface (CLI)](cloudhsm_cli-getting-started.md).
+  You will not be able to access a cluster configured with `./configure-cli[.exe] -a` since it will not be associated with a `cluster-id`. You can reconfigure it by following `config-cli add-cluster` as described in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
