---
source_url: https://docs.aws.amazon.com/glue/latest/dg/twilio-connector-limitations.html
---

# Limitations and notes for Twilio connector
<a name="twilio-connector-limitations"></a>

The following are limitations or notes for the Twilio connector:
+ Record-based partitioning is not supported, as there is no provision to retrieve the total count of records from Twilio.
+ The fields `date_sent`, `start_time`, and `end_time` are of the Datetime datatype, but when filtering, they only support date values (time components are not considered).
+ Filtering the "from" or "to" fields works only if the values do not include any prefix (for example, a protocol or label). If a prefix is present, filtering for the respective field does not work. For example if you pass "to": "whatsapp:\+14xxxxxxxxxx" as a filter then Twilio won't return a response. You need to pass it as "to": "\+14xxxxxxxx", then it will return records if they exist.
+ The "identity" field filter is mandatory when querying the `conversation-participant-conversation` entity.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
