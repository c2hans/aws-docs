---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/source-code-analysis.html
---

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Strategy Recommendations source code analysis
<a name="source-code-analysis"></a>

Migration Hub Strategy Recommendations automatically identifies the applications in your portfolio and creates application components for them. For example, if there is a Java application in your portfolio, it's identified as an application component with a component type of **java**.

Strategy Recommendations analyzes the source code for the application components if you configure it to do so. For information about configuring an application component for source code analysis, see [Configure source code analysis for an application component](recommendations-view-app-components.md#recommendations-source-code-config).

Strategy Recommendations performs source code analysis for the Java and C\# programming languages.

For information about the prerequisites for using Strategy Recommendations source code analysis, see [Prerequisites for Strategy Recommendations](getting-started-prerequisites.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
