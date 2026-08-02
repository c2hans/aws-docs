---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/uninstall-the-centralized-logging-with-opensearch.html
---

# Uninstall the solution
<a name="uninstall-the-centralized-logging-with-opensearch"></a>

You will encounter an IAM role missing error if you delete the Centralized Logging with OpenSearch main stack before you delete the log pipelines. Centralized Logging with OpenSearch console launches additional CloudFormation stacks to ingest logs. If you want to uninstall the Centralized Logging with OpenSearch solution. We recommend you to delete log pipelines (incl. AWS Service log pipelines and application log pipelines) before uninstalling the solution.

 **Step 1. Delete Application Log Pipelines**

**Important**
Delete all the log ingestion before deleting an application log pipeline.

1. Go to the Centralized Logging with OpenSearch console, in the left sidebar, choose **Application Log**.

1. Click the application log pipeline to view details.

1. In the ingestion tab, delete all the application log ingestion in the pipeline.

1. Uninstall/Disable the Fluent Bit agent.
   + EC2 (Optional): after removing the log ingestion from Instance Group. Fluent Bit will automatically stop ship logs, it is optional for you to stop the Fluent Bit in your instances. Here are the commands for stopping Fluent Bit agent.

     ```
     sudo service fluent-bit stop
        sudo systemctl disable fluent-bit.service
     ```
   + EKS DaemonSet (Mandatory): if you have chosen to deploy the Fluent Bit agent using DaemonSet, you must delete your Fluent Bit agent. Otherwise, the agent will continue to ship logs to Centralized Logging with OpenSearch pipelines.

     ```
     kubectl delete -f ~/fluent-bit-logging.yaml
     ```
   + EKS SideCar (Mandatory): remove the fluent-bit agent in your .yaml file, and restart your pod.

1. Delete the Application Log pipeline.

1. Repeat step 2 to Step 5 to delete all your application log pipelines.

 **Step 2. Delete AWS Service Log Pipelines**

1. Go to the Centralized Logging with OpenSearch console, in the left sidebar, choose **AWS Service Log**.

1. Select and delete the AWS Service Log Pipeline one by one.

 **Step 3. Clean up imported OpenSearch domains**

1.  [Delete Access Proxy](access-proxy-1.md#delete-a-proxy), if you have created the proxy using Centralized Logging with the OpenSearch console.

1.  [Delete Alarms](domain-alarms.md#delete-alarms), if you have created alarms using Centralized Logging with the OpenSearch console.

1. Delete VPC peering connection between Centralized Logging with OpenSearch’s VPC and OpenSearch’s VPC.

   1. Go to [Amazon VPC Console](https://console.aws.amazon.com/vpc/).

   1. Choose **Peering connections** in the left sidebar.

   1. Find and delete the VPC peering connection between the Centralized Logging with OpenSearch’s VPC and OpenSearch’s VPC. You may not have Peering Connections if you did not use the "Automatic" mode when importing OpenSearch domains.

1. (Optional) Remove imported OpenSearch Domains. (This will not delete the Amazon OpenSearch Service domain in the AWS account.)

 **Step 4. Delete Centralized Logging with OpenSearch stack**

1. Go to the [CloudFormation console](https://console.aws.amazon.com/cloudfromation/).

1. Find CloudFormation Stack of the Centralized Logging with OpenSearch solution.

1. (Optional) Delete S3 buckets created by Centralized Logging with OpenSearch.
**Important**
The S3 bucket whose name contains **LoggingBucket** is the centralized bucket for your AWS service log. You might have enabled AWS Services to send logs to this S3 bucket. Deleting this bucket will cause AWS Services failed to send logs.

   \+ .. Choose the CloudFormation stack of the Centralized Logging with OpenSearch solution, and select the **Resources** tab. .. In the search bar, enter AWS::S3::Bucket. This will show all the S3 buckets created by Centralized Logging with OpenSearch solution, and the **Physical ID** field is the S3 bucket name. .. Go to the Amazon S3 console, and find the S3 bucket using the bucket name. **Empty** and **Delete** the S3 bucket.

1. Delete the CloudFormation Stack of the Centralized Logging with OpenSearch solution.
