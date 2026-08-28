---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/deleting-a-queue.html
---

# Deleting a queue
<a name="deleting-a-queue"></a>

You can delete any queue other than the default queue. You can't delete a queue that contains unprocessed jobs. The following tabs show how to delete an on-demand queue.

------
#### [ Console  ]

To delete an on-demand queue by using the MediaConvert console:

1. Open the [Queues](https://console.aws.amazon.com/mediaconvert/home#/queues/list) page in the MediaConvert console.

1. Select the queue.

1. Choose **Delete queue**.

------
#### [ AWS CLI  ]

The following `delete-queue` example deletes on-demand queue.

```
aws mediaconvert delete-queue \
	--name {{Queue1}}
```

For more information about how to delete an on-demand queue by using the AWS CLI, see the [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/delete-queue.html).

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
