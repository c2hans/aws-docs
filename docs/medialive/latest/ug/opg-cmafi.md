---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/opg-cmafi.html
---

# Creating a CMAF Ingest output group
<a name="opg-cmafi"></a>

When you create a AWS Elemental MediaLive channel, you might want to include a CMAF Ingest output group. For information about the use cases for a CMAF Ingest output group, see [Containers, protocols, and downstream systems](outputs-supported-containers-downstream-systems.md).

Note that MediaLive generates a quality score for outputs in a CMAF Ingest output group. For more information, see [Working with MQCS](mqcs.md).

**Topics**
+ [Organize encodes into outputs](design-cmafi-package.md)
+ [Obtain destination](downstream-system-cmafi-empv2.md)
+ [Create output group](creating-cmafi-output-group.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
