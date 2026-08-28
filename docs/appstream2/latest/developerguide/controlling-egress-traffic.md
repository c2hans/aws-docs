---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/controlling-egress-traffic.html
---

# Controlling egress traffic
<a name="controlling-egress-traffic"></a>

Where data loss is a concern, it’s important to cover off what a User can access once they are inside of their WorkSpaces Applications instance. What does the network exit (or egress) path look like? It is a common requirement to have public internet access available to the end user inside their WorkSpaces Applications instance, so placing a WebProxy or Content Filtering Solution in the network path needs to be considered. Other considerations include a local Antivirus application and other endpoint security measures inside the AppStream instance (see the section “Endpoint Security and Antivirus” for more information).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
