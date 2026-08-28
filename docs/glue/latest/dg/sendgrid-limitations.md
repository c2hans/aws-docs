---
source_url: https://docs.aws.amazon.com/glue/latest/dg/sendgrid-limitations.html
---

# SendGrid limitations
<a name="sendgrid-limitations"></a>

The following are limitations or notes for SendGrid:
+ Incremental pull is only supported by the Stats entity on the `start_date` field and by the Contact entity on the `event_timestamp` field.
+ Pagination is only supported by the Marketing Campaign Stats (Automations), Marketing Campaign Stats (Single Sends), Single Sends, and Lists entities.
+ For the Stats entity, `start_date` is a mandatory filter parameter.
+ An API key with Restricted Access can’t support read access for the Email API and Stats entities. Use an API key with Full Access. For more information, see [API Overview](https://www.twilio.com/docs/sendgrid/api-reference/api-keys/create-api-keys#api-overview).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
