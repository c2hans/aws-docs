---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/step-3-resume-the-transfer-workflow.html
---

# Step 3: Resume the transfer workflow
<a name="step-3-resume-the-transfer-workflow"></a>

1.  Sign in to the [Systems Manager console](https://console.aws.amazon.com/systems-manager).

1.  Under **Shared Resources**, select **Documents**.

1.  On the **Documents** page, select **Owned by me**, and choose the document called `Resume-Data-Retrieval-for-Glacier-S3-${{<NAME_OF_STACK>}}`.

1.  Choose **Execute Automation**.

1.  Enter the following under **Input Parameters** on the **Execute Automation Runbook** page.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/step-3-resume-the-transfer-workflow.html)

**Note**
To monitor the progress of the transfer after launching the workflow, please refer to the Guidance’s [Cloudwatch dashboard](use-the-guidance.md#access-the-cloudwatch-dashboard). Please note that it might take 5-12 hours before the dashboard ***Workflow Run ID*** dropdown menu entries get updated with the new entry after launching the transfer.
