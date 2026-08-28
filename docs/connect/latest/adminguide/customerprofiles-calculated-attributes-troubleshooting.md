---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/customerprofiles-calculated-attributes-troubleshooting.html
---

# Error messages and resolutions for Connect Customer Customer Profiles calculated attributes
<a name="customerprofiles-calculated-attributes-troubleshooting"></a>

The following table shows calculated attributes error messages, cause, and resolution for each error.

| Error message | Cause | Resolution |
| --- | --- | --- |
| Retrieval of a calculated attribute for a profile shows a null value | This is likely due to the calculated attribute not having data. After creation of a calculated attribute, new data must be ingested. | Ingest new data or re-ingest old data through integrations or the CreateProfile and PutProfileObject APIs. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
