---
source_url: https://docs.aws.amazon.com/healthimaging/latest/devguide/tagging.html
---

# Tagging resources with AWS HealthImaging
<a name="tagging"></a>

You can assign metadata to HealthImaging resources ([data stores](getting-started-concepts.md#concept-data-store) and [image sets](getting-started-concepts.md#concept-image-set)) in the form of tags. Each tag is a label consisting of a user-defined key and value. Tags help you manage, identify, organize, search for, and filter resources.

**Important**
Do not store protected health information (PHI), personally identifiable information (PII), or other confidential or sensitive information in tags. Tags are not intended to be used for private or sensitive data.

The following topics describe how to use HealthImaging tagging operations using the AWS Management Console, AWS CLI, and AWS SDKs. For more information, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) in the *AWS General Reference Guide*.

**Topics**
+ [Tagging a resource](tag-resource.md)
+ [Listing tags for a resource](list-tag-resource.md)
+ [Untagging a resource](untag-resource.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
