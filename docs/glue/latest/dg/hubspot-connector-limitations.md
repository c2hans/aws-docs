---
source_url: https://docs.aws.amazon.com/glue/latest/dg/hubspot-connector-limitations.html
---

# Limitations and notes for HubSpot connector
<a name="hubspot-connector-limitations"></a>

The following are limitations or notes for the HubSpot connector:
+ The search endpoints are limited to 10,000 total results for any given query. Any partition having more than 10,000 records will result in a 400 error.
+ Other important limitations for the connector are described in [Limitations](https://developers.hubspot.com/docs/api/crm/search#limitations).
+ A maximum of three filtering statements are accepted by HubSpot.
+ Currently, HubSpot supports Associations between standard HubSpot objects (e.g. contact, company, deal, or ticket) and custom objects.
  + For a Free account: you can create only up to 10 association types between each object pairing (e.g. contacts and companies).
  + For a Super Admin account: you can create only up to 50 association types between each object pairing.
  + For more information, see [Associations v4](https://developers.hubspot.com/docs/api/crm/) and [Create and use association labels](https://knowledge.hubspot.com/object-settings/create-and-use-association-labels).
+ The 'Quote' and 'Communications' objects are not present for Associations as they are currently not supported in the connector.
+ For Async, SaaS sorts the values in ascending order only.
+ For the `Ticket` entity, SaaS doesn't return the `hs_object_id` field in the Async mode.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
