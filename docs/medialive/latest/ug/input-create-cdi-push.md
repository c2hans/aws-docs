---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/input-create-cdi-push.html
---

# Setting up a CDI input
<a name="input-create-cdi-push"></a>

This section describes how to create a CDI push input. With a CDI source, the upstream system *pushes* the content to MediaLive.

To perform this setup, you must work with an Amazon VPC user, with an operator at the upstream system, and you must work within MediaLive.

**Note**
Make sure that the content provider is using the latest version of the [AWS CDI SDK](https://aws.amazon.com/media-services/resources/cdi/) on their CDI source device.

**Topics**
+ [Request setup on the VPC](setup-vpc-cdi-vpc.md)
+ [Create a CDI input](setup-input-cdi-vpc.md)
+ [Ensure correct setup on the upstream system](setup-uss-cdi-vpc.md)
+ [Result of this procedure](setup-result-cdi-vpc.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
