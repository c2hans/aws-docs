---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/mpts-limits.html
---

# Restrictions for multiplexes
<a name="mpts-limits"></a>

Following is a summary of the restrictions associated with multiplexes:
+ There are service quotas for the number of multiplexes you can create. For more information, see [Quotas in MediaLive](limits.md).
+ These limitations apply to a multiplex:
  + Each multiplex produces only one MPTS. The MPTS has two pipelines, so it is sent to two destinations.
  + All multiplex outputs must include video.
+ These limitations apply to a program:
  + Each program in a multiplex is single use. It is attached only to one multiplex, and you can use it only for that multiplex.
+ These limitations apply to a channel in a multiplex:
  + Each channel is single use. You can attach it to only one program in the multiplex, and you can use it only for that multiplex.
  + Each channel contains one and only one output group, of type multiplex. It can't contain any other type of output group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
