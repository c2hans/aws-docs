---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-gates-version.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Specifying the version of a gate
<a name="workflows-gates-version"></a>

By default, when you add a gate to a workflow, CodeCatalyst adds the full version to the workflow definition file using the format:

`v{{major}}.{{minor}}.{{patch}}`

For example:

```
My-Gate:
  Identifier: aws/approval@v1
```

You can lengthen the version so that the workflow uses a specific major or minor version of the gate. For instructions, see [Specifying the action version to use](workflows-action-versions.md). The referenced topic refers to workflow actions but applies equally to gates.

For more information about gates in CodeCatalyst, see [Gating a workflow run](workflows-gates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
