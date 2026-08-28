---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/troubleshooting-bulk.html
---

# Troubleshooting bulk import and export operations
<a name="troubleshooting-bulk"></a>

To handle and diagnose errors produced during a transfer job, see the AWS IoT TwinMaker **GetMetadataTransferJob** API:

1. After creating and running a transfer job, call the **GetMetadataTransferJob** API:

   ```
   aws iottwinmaker get-metadata-transfer-job \
   --metadata-transfer-job-id your_metadata_transfer_job_id \
   --region us-east-1
   ```

1.  The state of the job changes to one of the below states:
   + COMPLETED
   + CANCELLED
   + ERROR

1.  The **GetMetadataTransferJob** API returns a [ MetadataTransferJobProgress](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_MetadataTransferJobProgress.html) object.

1. The **MetadataTransferJobProgress** object contains the following parameters:
   + **failedCount** : Indicates the count of assets that failed during the transfer process.
   + **skippedCount** : Indicates the count of assets that were skipped during the transfer process.
   + **succeededCount** : Indicates the count of assets that succeeded during the transfer process.
   + **totalCount** : Indicates the total count of assets involved in the transfer process.

1. Additionally a **reportUrl** element is returned by the API call, which contains a pre-signed URL. If your transfer job has errors that needs investigation, you can download a full error report at this URL.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
