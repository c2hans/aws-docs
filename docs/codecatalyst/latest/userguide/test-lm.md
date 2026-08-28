---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/test-lm.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Testing lifecycle management for bundle outputs and merge conflicts
<a name="test-lm"></a>

You can locally test your blueprint’s lifecycle management and merge conflict resolution. A series of bundles under the `synth/` directory that represent the various phases of a lifecycle update is generated. To test the lifecycle management, you can run the following yarn command on your blueprint:`yarn blueprint: resynth`. To learn more about resynthesis and bundles, see [Resynthesis](custom-bp-concepts.md#resynthesis-concept) and [Generating files with resynthesis](merge-strategies-lm.md#three-way-merge-lm).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
