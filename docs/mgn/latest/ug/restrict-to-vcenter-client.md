---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/restrict-to-vcenter-client.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Restrict permission to act on a source server associated with given AWS vCenter client
<a name="restrict-to-vcenter-client"></a>

To restrict access to source servers associated with a given AWS vCenter client, use the condition element ` mgn:VcenterClientId ` condition key. The following example demonstrates a policy that allows an AWS vCenter client to call the ` mgn:UpdateAgentSourcePropertiesForMgn ` action only on a source server associated with the calling AWS vCenter client.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
