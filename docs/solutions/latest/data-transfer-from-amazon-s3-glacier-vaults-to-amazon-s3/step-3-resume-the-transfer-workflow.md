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

<table>
<thead>
  <tr><th> Parameter </th><th> Value </th><th> Notes </th></tr>
</thead>
<tbody>
  <tr><td><b>AcknowledgeAdditionalCostForCrossRegionTransfer</b></td><td><code>NO</code></td><td>Select <code>YES</code> only if you are aware of the excessive additional cost when selecting a destination bucket in a different region than the S3 Glacier vault. See <a href="https://aws.amazon.com/s3/glacier/pricing/#Data_transfer_pricing">Amazon S3 Glacier data transfer pricing</a>.</td></tr>
  <tr><td><b>ProvidedInventory</b></td><td>{{&lt;Requires input&gt;}}</td><td>Input with two options [<code>YES,NO</code>] indicate if the inventory is provided.</td></tr>
  <tr><td><b>WorkflowRun</b></td><td>{{&lt;Requires input&gt;}}</td><td> Provide the same <code>workflow_run</code> value used in the initial execution of the transfer workflow.</td></tr>
  <tr><td><b>Description</b></td><td> <i>&lt;Optional input&gt;</i> </td><td>Provide an extended description for this migration.</td></tr>
  <tr><td><b>NamingOverrideFile</b></td><td> <i>&lt;Optional input&gt;</i> </td><td>Provide a presigned URL of the <b>NamingOverride</b> ﬁle and the bucket that is storing the ﬁle if you want to <a href="architecture-overview.md#creating-custom-file-names-for-s3-objects">customize S3 object key names</a>.</td></tr>
  <tr><td><b>S3 Storage class</b></td><td>{{&lt;Requires input&gt;}}</td><td>Select the S3 storage class for the migrated archives. See <a href="https://aws.amazon.com/s3/pricing/">Amazon S3 pricing</a>. </td></tr>
</tbody>
</table>

**Note**
To monitor the progress of the transfer after launching the workflow, please refer to the Guidance’s [Cloudwatch dashboard](use-the-guidance.md#access-the-cloudwatch-dashboard). Please note that it might take 5-12 hours before the dashboard ***Workflow Run ID*** dropdown menu entries get updated with the new entry after launching the transfer.
