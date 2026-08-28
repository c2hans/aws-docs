---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/sample-note-for-screenpop.html
---

# Sample Screenpop flow in Connect Customer
<a name="sample-note-for-screenpop"></a>

**Note**
This topic explains a sample flow that is included with Connect Customer. For information about locating the sample flows in your instance, see [Sample flows in Connect Customer](contact-flow-samples.md).

Type: Flow (inbound)

This flow shows you how to use Screenpop, a Contact Control Panel feature, to load a web page with parameters based on attributes.

In this sample flow, a **Set contact attributes** block is used to create an attribute from a text string. As an attribute, the text can be passed to the CCP to display a note to an agent.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
