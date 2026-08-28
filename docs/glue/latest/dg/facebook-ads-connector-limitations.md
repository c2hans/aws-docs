---
source_url: https://docs.aws.amazon.com/glue/latest/dg/facebook-ads-connector-limitations.html
---

# Limitations and notes for Facebook Ads connector
<a name="facebook-ads-connector-limitations"></a>

The following are limitations or notes for the Facebook Ads connector:
+ As Facebook Ads supports dynamic metadata, all fields can be queried. All the fields support filtration and records are fetched if the data is available, or else Facebook returns a Bad request (400) response with a proper error message.
+ An app's call count is the number of calls a user can make during a rolling one-hour window 200 multiplied by the number of users. For rate limit details, see [Rate Limits](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/), and [Business Use Case Rate Limits](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#buc-rate-limits).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
