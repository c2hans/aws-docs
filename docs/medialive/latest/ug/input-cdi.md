---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/input-cdi.html
---

# Channel input—CDI VPC push input
<a name="input-cdi"></a>

To verify that the input is set up correctly, look at the **Input destinations** section. It shows the two locations on MediaLive that the upstream system will push the source to when the channel is running. These locations were automatically generated when you created the input:
+ If the channel is set up as a standard channel, two locations are generated.
+ If the channel is set up as a single-pipeline channel, one location is generated.

For example:

**10.99.39.23:5000**

**192.0.2.54:5000**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
