---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/reference.html
---

# Reference
<a name="reference"></a>

 This section includes information about an optional feature for collecting unique metrics for this Guidance and a [list of builders](#contributors) who contributed to this Guidance.

## Anonymized data collection
<a name="anonymized-data-collection"></a>

 This Guidance includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this Guidance and related services and products. When invoked, the following information is collected and sent to AWS:
+  **Guidance ID** – The Guidance identifier
+  **Unique ID (UUID)** – Randomly generated, unique identifier for each Data Transfer from Amazon Glacier Vaults to Amazon S3 deployment
+  **Timestamp** – Data-collection timestamp
+  **Data** – The Guidance collects and sends the following statistics:
  +  **Region** – Selected AWS Region
  +  **Version** – Version of the Guidance deployment
  +  **StorageClass** – Selected destination S3 storage class
  +  **RetrievalTier** – Type of Amazon Glacier retrieval (for example, Bulk)
  +  **VaultSize** – Source Amazon Glacier vault size
  +  **ArchiveCount** – Number of Amazon Glacier archives

 AWS owns the data gathered though this survey. Data collection is subject to the [Privacy Notice](https://aws.amazon.com/privacy/). To opt out of this feature, complete the following steps before launching the AWS CloudFormation template.

1.  Download the AWS CloudFormation template to your local hard drive.

1.  Open the [AWS CloudFormation template](https://solutions-reference.s3.amazonaws.com/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3.template) with a text editor.

1.  Modify the `Environment` variable section for the `SendAnonymizedStats` Lambda function from:

   ```
   "SEND_ANONYMIZED_STATS": "Yes"
   ```

    to:

   ```
   "SEND_ANONYMIZED_STATS": "No"
   ```

1.  Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1.  Select **Create stack**.

1.  On the **Create stack** page, **Specify template** section, select **Upload a template file**.

1.  Under **Upload a template file**, choose **Choose file** and select the edited template from your local drive.

1.  Choose **Next** and follow the steps in [Launch the stack](step-1-launch-the-stack.md) in the Deploy the Guidance section of this guide.

## Contributors
<a name="contributors"></a>
+  Bassem Wanis
+  Kamyar Ziabari
+  Nathaniel Schaaf
+  Garvit Singh
+  Simon Krol
+  Evgeny Minkevich

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer from Amazon S3 Glacier Vaults to Amazon S3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
