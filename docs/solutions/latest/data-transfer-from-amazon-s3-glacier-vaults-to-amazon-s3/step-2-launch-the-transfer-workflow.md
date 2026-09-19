---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/step-2-launch-the-transfer-workflow.html
---

# Step 2: Launch the transfer workflow
<a name="step-2-launch-the-transfer-workflow"></a>

**Important**
Avoid starting multiple transfers simultaneously. Multiple transfers can exceed Amazon Glacier quotas and induce throttling.
When you transfer multiple vaults, initiate transfers sequentially by starting a new transfer only after the previous one completes.

1.  Sign in to the [Systems Manager console](https://console.aws.amazon.com/systems-manager).

1.  Under **Shared Resources**, select **Documents**.

1.  On the **Documents** page, select **Owned by me**, and choose the document called `Launch-Data-Retrieval-for-Glacier-S3-${{<NAME_OF_STACK>}}`.

1.  Choose **Execute Automation**.

## (Optional) Download the vault inventory file
<a name="optional-download-the-vault-inventory-file"></a>

 If you want to download the vault inventory file as part of this migration, follow these steps.

1.  Sign in to the [Systems Manager console](https://console.aws.amazon.com/systems-manager).

1.  Under **Shared Resources**, select **Documents**.

1.  On the **Documents** page, select **Owned by me**, and choose the document called `Launch-Data-Retrieval-for-Glacier-S3-${{<NAME_OF_STACK>}}`.

1.  Choose **Execute Automation**.

1.  Enter the following under **Input Parameters** on the **Execute Automation Runbook** page.
**Note**
To enable the data transfer to a bucket in a different region from the S3 Glacier vault, you must manually adjust the automation document's content by setting the InputPayload parameter ` allow_cross_region_data_transfer` to true. By default, the Guidance restricts cross-region transfers to avoid potential costs.

<table>
<thead>
  <tr><th> Parameter </th><th> Value </th><th> Notes </th></tr>
</thead>
<tbody>
  <tr><td><b>AcknowledgeAdditionalCostForCrossRegionTransfer</b></td><td><code>NO</code></td><td>Select <code>YES</code> only if you are aware of the excessive additional cost when selecting a destination bucket in a different region than the S3 Glacier vault. See <a href="https://aws.amazon.com/s3/glacier/pricing/#Data_transfer_pricing">Amazon S3 Glacier data transfer pricing</a>.</td></tr>
  <tr><td><b>ProvidedInventory</b></td><td>{{&lt;Requires input&gt;}}</td><td>Input with two options [<code>YES,NO</code>] indicate if the inventory is provided.</td></tr>
  <tr><td><b>VaultName</b></td><td>{{&lt;Requires input&gt;}}</td><td> Enter the name of your Amazon Glacier vault. </td></tr>
  <tr><td><b>WorkflowRun</b></td><td>{{&lt;Requires input&gt;}} </td><td>Input to specify the workflow identifier of the workflow that needs to be resumed. Input to specify the workflow identifier of the workflow that needs to be resumed.</td></tr>
  <tr><td><b>Description</b></td><td> <i>&lt;Optional input&gt;</i> </td><td> Provide an extended description for this migration. </td></tr>
  <tr><td><b>NamingOverrideFile</b></td><td> <i>&lt;Optional input&gt;</i> </td><td>Provide a presigned URL of the <b>NamingOverride</b> ﬁle and the bucket that is storing the ﬁle if you want to <a href="architecture-overview.md#creating-custom-file-names-for-s3-objects">customize S3 object key names</a>.</td></tr>
  <tr><td><b>S3StorageClass</b></td><td>{{&lt;Requires input&gt;}}</td><td>Select the S3 storage class for the migrated archives. See <a href="https://aws.amazon.com/s3/pricing/">Amazon S3 pricing</a>. </td></tr>
</tbody>
</table>

1. Choose **Execute**.

1. It takes approximately less than 1 minute to execute the document and launch the transfer. To confirm that the transfer process started successfully, refer to the ***runScript ***step status under the ***Executed Steps*** section.
**Note**
To monitor the progress of the transfer after launching the workflow, please refer to the Guidance’s [Cloudwatch dashboard](use-the-guidance.md#access-the-cloudwatch-dashboard). Please note that it might take 5-12 hours before the dashboard ***Workflow Run ID*** dropdown menu entries get updated with the new entry after launching the transfer.

## (Optional) Provide the vault inventory file
<a name="optional-provide-the-vault-inventory-file"></a>

 If you want to provide the vault inventory file, follow these steps.

1.  Sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation).

   1.  On the **Stacks** page, select this Guidance's installation stack.

   1.  Choose the **Output** tab and find the inventory bucket name.

1.  Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3) and choose the inventory bucket from step 1b.

   1.  Choose **Create folder**. Enter the `workflow_run` value from the **WorkflowRun** parameter input. For more information about creating and using folders, see [Organizing objects in the Amazon S3 console by using folders](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) in the *Amazon Simple Storage Service User Guide*.

   1.  Create a subfolder called `original_inventory` in this new folder.

   1.  Copy the vault inventory file into this folder. For more information, see [Downloading a Vault Inventory in Amazon Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-inventory.html) in the *Amazon Glacier Developer Guide*.

   1.  Rename the vault inventory file to `inventory.csv`.

1.  Sign in to the [Systems Manager console](https://console.aws.amazon.com/systems-manager).

1. Under **Shared Resources**, select **Documents**.

1. On the **Documents** page, select **Owned by me**, and choose the document called `Launch-Data-Retrieval-for-Glacier-S3-${{<NAME_OF_STACK>}}`.

1.  Choose **Execute Automation**.

1.  Enter the following under **Input Parameters** on the **Execute Automation Runbook** page.
**Note**
To enable the data transfer to a bucket in a different region from the S3 Glacier vault, you must manually adjust the automation document's content by setting the InputPayload parameter `allow_cross_region_data_transfer `to true. By default, the Guidance restricts cross-region transfers to avoid potential costs.

<table>
<thead>
  <tr><th> Parameter </th><th> Value </th><th> Notes </th></tr>
</thead>
<tbody>
  <tr><td><b>AcknowledgeAdditionalCostForCrossRegionTransfer</b></td><td><code>NO</code></td><td>Select <code>YES</code> only if you are aware of the excessive additional cost when selecting a destination bucket in a different region than the S3 Glacier vault. See <a href="https://aws.amazon.com/s3/glacier/pricing/#Data_transfer_pricing">Amazon S3 Glacier data transfer pricing</a>.</td></tr>
  <tr><td><b>ProvidedInventory</b></td><td><code>Yes</code></td><td></td></tr>
  <tr><td><b>WorkflowRun</b></td><td>{{&lt;Requires input&gt;}}</td><td> Provide the name of your workflow run, which becomes the <code>workflow_run</code> value.</td></tr>
  <tr><td><b>Description</b></td><td> <i>&lt;Optional input&gt;</i> </td><td> Provide an extended description for this migration. </td></tr>
  <tr><td><b>NamingOverrideFile</b></td><td> <i>&lt;Optional input&gt;</i> </td><td>Provide a presigned URL of the <b>NamingOverride</b> ﬁle and the bucket that is storing the ﬁle if you want to <a href="architecture-overview.md#creating-custom-file-names-for-s3-objects">customize S3 object key names</a>.</td></tr>
  <tr><td><b>S3StorageClass</b></td><td>{{&lt;Requires input&gt;}}</td><td>Select the S3 storage class for the migrated archives. See <a href="https://aws.amazon.com/s3/pricing/">Amazon S3 pricing</a>. </td></tr>
</tbody>
</table>

1. Choose **Execute** It takes approximately less than 1 minute to execute the document and launch the transfer. To confirm that the transfer process started successfully, refer to the ***runScript*** step status under the ***Executed Steps*** section.

**Note**
To monitor the progress of the transfer after launching the workflow, please refer to the Guidance’s [Cloudwatch dashboard](use-the-guidance.md#access-the-cloudwatch-dashboard). Please note that it might take 5-12 hours before the dashboard ***Workflow Run ID*** dropdown menu entries get updated with the new entry after launching the transfer.
