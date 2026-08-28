---
source_url: https://docs.aws.amazon.com/personalize/latest/dg/action-interaction-tracker-id.html
---

# Finding the ID of your action interaction event tracker
<a name="action-interaction-tracker-id"></a>

When you create an Action interactions dataset, Amazon Personalize automatically creates an *action interaction* event tracker for you. You specify the tracker's ID in the PutActionInteractions API operation. Amazon Personalize uses it to direct new data to the *Action interactions dataset* in your dataset group.

 You can find your event tracker's ID on the details page of your Action interactions dataset in the Amazon Personalize console. And you can find the ID by calling the DescribeDataset API operation. The following Python code prints the tracking ID for an Action interactions dataset.

```
import boto3

personalize = boto3.client(service_name='personalize')

response = personalize.describe_dataset(
  datasetArn="{{Action interactions dataset ARN}}"
)

print(response['trackingId'])
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Personalize. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query personalize` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
