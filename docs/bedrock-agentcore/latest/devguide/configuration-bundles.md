---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/configuration-bundles.html
---

# Configuration bundles
<a name="configuration-bundles"></a>

A configuration bundle is a versioned, immutable snapshot of your agent’s dynamic configuration — system prompts, model IDs, tool descriptions, and any other key-value pairs your agent reads at runtime. Bundles decouple agent behavior from code, enabling you to change how your agent responds without redeploying code.

<a name="configuration-bundles-concepts"></a> **Key concepts**
+  **Components** are keyed by the ARN of the AgentCore resource they configure (for example, a runtime ARN). Each component contains a `configuration` object with arbitrary key-value pairs.
+  **Versions** are immutable. Every update creates a new version with a unique UUID. Versions form a chain via `parentVersionIds`, similar to git commits.
+  **Branches** organize version lineage (for example, `mainline`, `experiment-1`).
+  **Bundle names** must start with a letter and can contain letters, digits, and underscores (no hyphens). Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}`.

<a name="configuration-bundles-when-to-use"></a> **When to use configuration bundles**
+  **A/B testing.** Each variant in an A/B test references a specific bundle version. The gateway injects the bundle reference into each request.
+  **Recommendations.** The Recommendations API can read the current configuration from a bundle and write the optimized configuration as a new bundle version.
+  **Rollback.** Because versions are immutable, you can roll back to any previous version by referencing its version ID.
+  **Audit trail.** The version chain provides a complete history of configuration changes.

**Topics**
+ [Getting started with configuration bundles](configuration-bundles-getting-started.md)
+ [Create a configuration bundle](configuration-bundles-create.md)
+ [Update a configuration bundle](configuration-bundles-update.md)
+ [Get a configuration bundle](configuration-bundles-get.md)
+ [List configuration bundles](configuration-bundles-list.md)
+ [Delete a configuration bundle](configuration-bundles-delete.md)
+ [Use configuration bundles at runtime](configuration-bundles-runtime.md)
+ [Configuration bundle encryption](configuration-bundles-encryption.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
