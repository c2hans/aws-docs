---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/va-opt-out.html
---

# Understanding data storage, opt-out, and data-retention policies for the Amazon Chime SDK
<a name="va-opt-out"></a>

The Amazon Chime SDK uses voice data to provide and improve the speaker search service. As part of that, we use enrollment audio, the recorded snippets used to create voice embeddings, to train our machine learning and artificial intelligence models. You can opt out of having your data used to train the models, and the topics in this section explain how.

**Topics**
+ [Understanding data storage for speaker search for the Amazon Chime SDK](speaker-search-data-storage.md)
+ [Handling opt outs for speaker search for the Amazon Chime SDK](va-handle-opt-outs.md)
+ [Understanding data retention for Amazon Chime SDK voice analytics](va-data-retention.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
