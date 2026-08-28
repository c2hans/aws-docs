---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/input-mediaconnect-push.html
---

# Channel input—MediaConnect push input
<a name="input-mediaconnect-push"></a>

To verify that the input is set up correctly, look at the **MediaConnect flows** section. It shows the ARNs of the AWS Elemental MediaConnect flows that are the source for this input. These ARNs were automatically generated when you created the input:
+ If the channel is set up as a standard channel, two ARNs are generated.
+ If the channel is set up as a single-pipeline channel, one ARN is generated.

For example:

**arn:aws:mediaconnect:us-west-1:111122223333:flow:1bgf67:sports-event-A** and

**arn:aws:mediaconnect:us-west-1:111122223333:flow:9pmlk76:sports-event-B**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
