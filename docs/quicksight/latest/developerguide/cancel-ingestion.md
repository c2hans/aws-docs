---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/cancel-ingestion.html
---

# CancelIngestion
<a name="cancel-ingestion"></a>

Use the `CancelIngestion` operation to cancel an ongoing ingestion of data into SPICE.

To use this operation, you need the ID of the dataset that is undergoing the ingestion that you want to cancel and the ID of the ingestion you want to cancel. You can use the `ListDataSets` operation to list all datasets and their corresponding dataset IDs. You can use the `ListIngestions` operation to list all ingestion IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight cancel-ingestion
    --aws-account-id {{AWSACCOUNTID}}
    --data-set-id {{DATASETID}}
    --ingestion-id {{INGESTIONID}}
```

------

For more information about the `CancelIngestion` operation, see [CancelIngestion](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CancelIngestion) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
