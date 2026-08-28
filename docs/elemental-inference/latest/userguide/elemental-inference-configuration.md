---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/userguide/elemental-inference-configuration.html
---

# Creating an Elemental Inference workflow
<a name="elemental-inference-configuration"></a>

You must create a feed and enable at least one AI feature in that feed. After you have created the feed, you must associate one resource, which represents the source media that Elemental Inference will work on.

When you are ready, you must deliver the source media to Elemental Inference. Elemental Inference will produce metadata for each of the features that you set up. You must obtain that metadata and use it to produce the desired media, for example, to produce a video file of an event.

**Topics**
+ [Step A: Create the feed in Elemental Inference](create-feed.md)
+ [Step B: Format the source media](source-format.md)
+ [Step C: Deliver the source media](deliver-source.md)
+ [Step D: Query the metadata](query-metadata-query.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Inference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-inference` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
