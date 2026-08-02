---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/cross-account-ingestion.html
---

# Cross-account ingestion
<a name="cross-account-ingestion"></a>

Centralized Logging with OpenSearch supports ingesting AWS Service logs and Application logs in different AWS accounts within the same Region. After deploying Centralized Logging with OpenSearch in one account (main account), you can launch the CloudFormation stack in a different account (member account), and associate the two accounts (main account and member account) to implement cross-account ingestion.

## Concepts
<a name="concepts-1"></a>
+  **Main account**: One account in which you deployed the Centralized Logging with OpenSearch console. The OpenSearch clusters must also be in the same account.
+  **Member account**: Another account from which you want to ingest AWS Service logs or application logs.

The CloudFormation stack in the member account has the least privileges. Centralized Logging with OpenSearch must provision some AWS resources in the member account to collect logs, and will assume an IAM role provisioned in the member account to list or create resources.

For more information, refer to the [Architecture](architecture-overview.md#architecture-diagram) section.

## Add a member account
<a name="add-a-member-account"></a>

 **Step 1. Launch a CloudFormation stack in the member account**

1. Sign in to the Centralized Logging with OpenSearch console.

1. In the navigation pane, under **Resources**, choose **Member Accounts**.

1. Choose the **Link an Account** button. It displays the steps to deploy the CloudFormation stack in the member account.

1. Important

1. You must copy the template URL, which will be used later.

1. Go to the CloudFormation console of the member account.

1. Choose the Create stack button and choose With new resources (standard).

1. In the **Create stack** page, enter the template URL you have copied in the **Amazon S3 URL**.

1. Follow the steps to create the CloudFormation stack and wait until the CloudFormation stack is provisioned.

1. Go to the **Outputs** tab to check the parameters, which will be used in **Step 2**.

 **Step 2. Link a member account**

1. Go back to the Centralized Logging with OpenSearch console.

1. (Optional) In the navigation panel, under **Resources**, choose **Member Accounts**.

1. In **Step 2. Link an account**, enter the parameters using the Outputs parameters from **Step 1**.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/cross-account-ingestion.html)

1. Click the **Link** button.
