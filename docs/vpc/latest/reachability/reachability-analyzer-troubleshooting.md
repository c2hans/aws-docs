---
source_url: https://docs.aws.amazon.com/vpc/latest/reachability/reachability-analyzer-troubleshooting.html
---

# Troubleshooting Reachability Analyzer
<a name="reachability-analyzer-troubleshooting"></a>

The following error messages are returned by Reachability Analyzer:

**The request failed due to insufficient permissions**
Verify that you have the required permissions. For more information, see [Required API permissions for Reachability Analyzer](security_iam_required-API-permissions.md).

**The network configuration is not supported**
Verify that you are using resources that are supported by Reachability Analyzer. For more information, see [Intermediate components](how-reachability-analyzer-works.md#intermediate-components).

**The request failed due to modifications in network resources during the analysis**
You can't update your network while the analysis is running.

**The request failed due to missing component [{{component}}]**
Verify that the resource ARNs are correct. For more information, see the [Service Authorization Reference](https://docs.aws.amazon.com/service-authorization/latest/reference/).

**The request failed due to inaccessible resource [{{resource}}]**
Verify that you have permission to access the specified resource.

**The request failed due to throttling errors from [{{service}}]**
Check for other applications or services that are currently consuming read capacity for the specified service.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Virtual Private Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
