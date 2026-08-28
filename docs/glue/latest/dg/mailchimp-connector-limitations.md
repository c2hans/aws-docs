---
source_url: https://docs.aws.amazon.com/glue/latest/dg/mailchimp-connector-limitations.html
---

# Limitations
<a name="mailchimp-connector-limitations"></a>

The following are limitations for the Mailchimp connector:
+ Filtration is only supported by `Campaigns`, `Automations`, `Lists`, `Open Details`, `Members`, and `Segments` entities.
+ While using a filter on `DateTime` datatype field, you must pass values in this format: `yyyy-mm-ddThh:MM:ssZ`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
