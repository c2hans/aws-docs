---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/devops-agent-integration.html
---

# AWS DevOps Agent integration
<a name="devops-agent-integration"></a>

With [AWS DevOps Agent](https://aws.amazon.com/devops-agent/), you can automate investigation of your load test results directly from the Distributed Load Testing on AWS solution. When you connect an Agent Space, you can send completed test runs to the agent for analysis. The agent proactively identifies performance bottlenecks, determines root causes, and suggests remediation steps—without requiring you to manually correlate Amazon CloudWatch metrics, logs, and traces.

## Prerequisites
<a name="devops-agent-prerequisites"></a>

Before connecting an Agent Space to Distributed Load Testing on AWS (DLT), complete the following:
+ The Agent Space must be in the same AWS account as your DLT deployment.
+ The Agent Space must be tagged with the key `dlt-integration` and value `allowed`. This tag establishes dual consent—both the DLT operator and the Agent Space administrator must take explicit action before DLT can access the Agent Space.
+ The `dlt-integration: allowed` tag must be present before DLT can accept test-connection or investigation requests, even if the Agent Space ARN is valid.

To add the tag, choose the [AWS DevOps Agent console](https://console.aws.amazon.com/aidevops) and choose your Agent Space. Choose the **Configuration** tab. Scroll down to the **Tags** section, choose **Add new tag**, enter `dlt-integration` as the key and `allowed` as the value, then choose **Save**.

## Register an Agent Space
<a name="devops-agent-register"></a>

After your Agent Space is tagged, complete the following steps to register it with DLT:

1. Choose **Agent Integration** in the DLT web console left sidebar.

1. In the **DevOps Agent Connections** section, choose **Register Agent Space**.

1. Enter a display name and paste the Agent Space ARN from the AWS DevOps Agent console.

1. Choose **Test Connection** to verify that the ARN is reachable and that the `dlt-integration: allowed` tag is present.

1. After the connection is confirmed, choose **Save**.

You can register multiple Agent Spaces and select between them when triggering an investigation.

## Investigate a test run
<a name="devops-agent-investigate"></a>

After registering at least one Agent Space, you can start an investigation from any completed test run. The **Investigate with DevOps Agent** button appears on each test run detail page. Complete the following steps:

1. Choose **Investigate with DevOps Agent** after a test run completes—successful, failed, or partial.

1. If you registered multiple Agent Spaces, choose one from the list.

1. Optionally, provide additional context such as a description of recent infrastructure changes or the expected performance baseline.

1. Choose **Submit**.

The investigation appears in the **Investigations** tab of the test run detail page, where you can track its status and choose the link to view findings in the AWS DevOps Agent console.

**Note**
AWS DevOps Agent enforces a 10,000-character limit on the investigation description. The description sent by the solution combines your optional context with a DLT-generated summary of the test run (test configuration, baseline comparison, top errors sorted by count, and per-endpoint breakdown). To fit within the limit, the solution prioritizes the test configuration and user-provided context, and trims lower-priority sections—starting with the per-endpoint breakdown—when the combined length would otherwise exceed 10,000 characters.

## Review findings
<a name="devops-agent-findings"></a>

AWS DevOps Agent investigations typically complete within a few minutes but might differ depending on the Agent Space configuration. When complete, choose **View findings** in the **Investigations** tab to open the findings in the AWS DevOps Agent console.

Findings include the following:
+ A structured root-cause analysis that identifies which components contributed to latency or errors.
+ A list of symptoms observed during the test window.
+ Concrete remediation suggestions.

Investigations remain in the DLT **Investigations** tab for the lifetime of the test run record, so you can refer back to prior analyses as your application evolves.

## Suggested workflow
<a name="devops-agent-suggested-workflow"></a>

To get the most out of the AWS DevOps Agent integration, use it as part of an iterative performance tuning loop: deploy, load test, investigate, remediate, and repeat. Each pass through the loop gives the agent more history to compare against and gives you measurable evidence that a change improved performance.

1.  **Deploy** — Deploy your application to the environment you want to test, and complete the one-time setup described in [Prerequisites](#devops-agent-prerequisites) and [Register an Agent Space](#devops-agent-register).

1.  **Establish a baseline** — Run your test scenario against a known-good build and designate the run as a baseline (refer to [Baseline comparison](explore-test-results.md#baseline-comparison)). When a baseline is set, the solution includes a comparison against it with your investigation request, so the agent can distinguish a regression from normal variation.

1.  **Load test** — Run the test scenario after each application or infrastructure change. Keep the scenario configuration constant between runs so results remain comparable.

1.  **Investigate** — After the run completes, choose **Investigate with DevOps Agent** on the test run detail page. Provide context about what changed since the last run — recent deployments, configuration changes, or the performance you expected — so the agent can focus its analysis.

1.  **Remediate** — Review the root cause and remediation suggestions in the **Investigations** tab, or open the findings in the AWS DevOps Agent console to generate a mitigation plan. Apply the fix to your application or infrastructure.

1.  **Repeat** — Re-run the test scenario and compare the results against your baseline to verify the fix. When performance improves, designate the new run as your baseline and continue the loop with your next change.

**Note**
Each test run supports one active investigation at a time. Archive a completed investigation from the **Investigations** tab before starting a new one on the same test run.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Distributed Load Testing on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
