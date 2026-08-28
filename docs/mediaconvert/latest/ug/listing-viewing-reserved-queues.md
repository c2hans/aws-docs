---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/listing-viewing-reserved-queues.html
---

# Listing reserved queues
<a name="listing-viewing-reserved-queues"></a>

You can list the AWS Elemental MediaConvert queues that are associated with your AWS account and get details about those queues. The following tabs show two options for listing your queues.

------
#### [ Console  ]

To list your reserved queues by using the MediaConvert console, open the [Queues](https://console.aws.amazon.com/mediaconvert/home#/queues/list) page.

------
#### [ AWS CLI  ]

The following `list-queues` example lists all of your queues.

```
aws mediaconvert list-queues
```

For more information about how list queues by using the AWS CLI, see the [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-queues.html).

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
