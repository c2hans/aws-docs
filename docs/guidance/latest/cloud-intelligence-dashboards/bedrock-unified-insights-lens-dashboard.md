---
source_url: https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/bedrock-unified-insights-lens-dashboard.html
---

# Bedrock Unified Insights Lens Dashboard (BUILD)

## Introduction
<a name="introduction"></a>

The Bedrock Unified Insights Lens Dashboard (BUILD) provides enterprise visibility into [Amazon Bedrock](https://aws.amazon.com/bedrock/) model invocation activity across your AWS accounts. It tracks per-account and per-model token consumption, request patterns, errors, and response characteristics. Cloud financial management (FinOps) and engineering leaders can use this data to manage Bedrock usage at scale and correlate invocation data with cost.

Key capabilities include:
+ Request and token usage by account, Region, operation, model, and caller, with a **Group By** control
+ Input, output, total, cache read, and cache write token tracking, and the prompt cache hit rate
+ Error, throttling, and stop reason analysis, including responses cut off by the token limit
+ Traffic type (single Region or cross-Region inference), capacity model, and service tier
+ Request-level detail with prompt and response previews (truncated to 1,000 characters) and per-column filters
+ Daily trend analysis for usage growth monitoring

The dashboard has the following tabs. Each tab ends with a request-level detail table, so you can go from a chart to the individual requests behind it.

Explore the [demo dashboard with synthetic data](https://cid.workshops.aws.dev/demo?dashboard=build) to see each tab in action.

**Example**
Start on the Overview tab for the top-level picture: how much Bedrock is used, how many tokens it consumes, and who the biggest consumers are. This tab provides:
+ Headline KPIs: requests, callers, accounts, error rate, and input, output, cache read, and cache write tokens
+ Token consumption per day by the dimension you choose with the **Group By** control: account, Region, operation, model, model category, caller role, caller session, or any taxonomy field you added
+ Total tokens and a top-10 ranking for the same dimension
+ Daily request and token trends, and requests and tokens by model
![The Overview tab showing KPI tiles for requests, callers, accounts, error rate and tokens, and daily token consumption grouped by caller role with a donut and a ranking of the top roles.](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/images/dashboards/build-overview.png)
Use the Usage Breakdown tab to see who and what uses Bedrock. This tab provides:
+ Operations, model categories, models, and Regions as donuts, each with a daily trend; the **Show** control switches them between tokens and requests
+ Tokens and requests per account, and tokens per day stacked by account
+ Average request size and a heat map of daily token volume
+ A ranked table of tokens and requests by account, caller role, and caller session, with a daily trend and a data bar
![The Usage Breakdown tab showing donuts and daily trends of tokens by operation, model category, model and Region, and token usage by account.](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/images/dashboards/build-usage-breakdown.png)
Find what fails and why on the Reliability tab. This tab provides:
+ Headline KPIs: error rate, failed requests, throttled requests, and responses stopped by the maximum token limit
+ Successful and failed requests per day
+ The daily percentage of each request outcome: successful, validation error, throttled, server error, not found, or other error
+ Requests by outcome and error code, and the stop reason breakdown
![The Reliability tab showing KPI tiles for error rate, failed and throttled requests and max token cutoffs, daily successful and failed requests, request outcomes per day, errors by error code and stop reasons.](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/images/dashboards/build-reliability.png)
See how your traffic is served on the Capacity & Cost Drivers tab. This tab provides:
+ Traffic types: on-demand in a single Region, through a geographic or global cross-Region inference profile, or through an application inference profile
+ Capacity model (on-demand or provisioned) and the service tier reported by the model, each with a daily trend
+ Cache read and cache write tokens per day, and the daily prompt cache hit rate
![The Capacity and Cost Drivers tab showing donuts and daily trends of traffic types, capacity model and service tier, cache read and write tokens per day and the cache hit rate.](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/images/dashboards/build-capacity-cost-drivers.png)
Investigate individual requests on the Raw Data Explorer tab. This tab provides:
+ A request-level table with time, request ID, account, Region, caller session and role, model, operation, error code, stop reason, prompt and response previews, and token counts
+ A filter above each column of that table
+ A token usage table per request, including cache read and cache write tokens
![The Raw Data Explorer tab showing a row of filters above a request-level table with time, request ID, account, Region, caller, model, operation, error code, stop reason and prompt preview columns.](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/images/dashboards/build-raw-data-explorer.png)

All tabs share the filter controls for date range (the last 6 months by default), Region, operation, model ID, caller session, and AWS account.

## Architecture
<a name="architecture"></a>

The Bedrock Unified Insights Lens module uses a **pull-based** architecture and never makes changes in your source accounts. The data flows as follows:

1. You enable Amazon Bedrock model invocation logging in each source account and Region, with Amazon S3 delivery to a bucket you own, and grant the collection Lambda function read access to that bucket with a bucket policy.

1. An Amazon EventBridge Scheduler schedule in the Data Collection account triggers the collection Lambda function daily.

1. On each run, the Lambda function lists the source buckets you configured and reconciles their contents against what it has already imported.

1. The Lambda function copies only the new Bedrock log objects into the destination bucket in the Data Collection account, as JSONL under a Hive-partitioned path.

1. The Lambda function registers each `(account_id, region, year, month, day)` partition directly in AWS Glue, so the data is queryable in Amazon Athena immediately.

1. The Amazon Quick dashboard reads the data through the `bedrock_invocations_view` Athena view.

There is no Glue crawler, no Glue ETL job, and no Step Functions state machine.

The diagram shows the data flow from your Bedrock log buckets through the collection Lambda function to AWS Glue and Amazon Athena, and then to the Amazon Quick dashboard. The numbers in the diagram match the steps above.

![Animated architecture diagram of the Bedrock Unified Insights Lens Dashboard. In a source account](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/data-collection/bedrock-architecture.gif)

## Prerequisites
<a name="prerequisites"></a>

1. Deploy one or more of the foundational dashboards: [CUDOS, Cost Intelligence, or KPI Dashboard](cudos-cid-kpi.md). This deployment enables the required Amazon Athena and Amazon Quick resources for this dashboard.

1.  [Enable Amazon Bedrock model invocation logging](#enable-bedrock-logging) with Amazon S3 delivery in each source account and Region where you use Amazon Bedrock. Write down the bucket name and the key prefix, if any, of each log location. You need them in [Step 1](#step-1-enable-the-bedrock-module-in-the-data-collection-stack).

**Note**
This module is pull-based: it reads only the S3 locations you specify through `BedrockSourceBuckets`, and access is granted by a bucket policy you apply. The module does not enable or change logging, assume a cross-account role, deploy a StackSet, or modify your source accounts. You do not need to update the read-permissions stack for this module.

### Enable Bedrock model invocation logging
<a name="enable-bedrock-logging"></a>

You enable Amazon Bedrock model invocation logging yourself in each account and Region you want to collect, with S3 delivery to a bucket you own. The module reads whatever you configure; it does not change these settings.

1. Create an S3 bucket for the logs, or choose an existing one. The bucket must be in the same account and Region as the logging configuration, and its access control lists (ACLs) must be disabled.

1. In each source account and Region, enable model invocation logging with S3 delivery. You can do this in the Amazon Bedrock console (**Settings** → **Model invocation logging**) or with the AWS CLI:

   ```bash
   aws bedrock put-model-invocation-logging-configuration \
     --region us-east-1 \
     --logging-config '{
       "s3Config": {
         "bucketName": "YOUR-BEDROCK-LOGS-BUCKET-NAME"
       },
       "textDataDeliveryEnabled": true,
       "imageDataDeliveryEnabled": true,
       "embeddingDataDeliveryEnabled": true,
       "videoDataDeliveryEnabled": true
     }'
   ```

    `keyPrefix` is optional. If you omit it, you add only the bucket name to `BedrockSourceBuckets` in Step 1. If you set it (for example, `"model-invocation-logs/"`), you add that prefix without its trailing slash to the bucket’s entry, for example `YOUR-BEDROCK-LOGS-BUCKET-NAME/model-invocation-logs`.

1. When you configure logging, Amazon Bedrock attaches the bucket policy that lets it write the logs, if your identity has the `s3:GetBucketPolicy` and `s3:PutBucketPolicy` permissions. Otherwise, add that policy yourself. For the policy, see the [model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) page of the Amazon Bedrock User Guide.

1. If the bucket uses server-side encryption with a customer managed AWS KMS key (SSE-KMS), the key policy must allow Amazon Bedrock to use the key for log delivery. For the statement, see the same page of the Amazon Bedrock User Guide.

1. Repeat for each account and Region you want collected. Amazon Bedrock allows only one model invocation logging configuration per account and Region.

**Note**
Enabling model invocation logging captures prompt and response content. Enable it only where that is acceptable for your organization’s data-handling requirements.

## Deployment
<a name="deployment"></a>

Deployment consists of enabling the data collection module in the Data Collection Stack, granting the collection Lambda function read access to your log buckets, and deploying the Amazon Quick dashboard.

### Step 1: Enable the Bedrock Module in the Data Collection Stack [In Data Collection Account]
<a name="step-1-enable-the-bedrock-module-in-the-data-collection-stack"></a>

The Bedrock data collection module is part of the [Data Collection Stack](data-collection.md) version v3.14.12 or later. Enable it when you deploy or update the stack in your **Data Collection** account.

1. Sign in to your **Data Collection** account and open the [AWS CloudFormation](https://console.aws.amazon.com/cloudformation) console.

1.  [Deploy](data-collection-deployment.md) the Data Collection Stack (first-time setup) or [Update](data-collection-update.md) your existing Data Collection Stack.

1. In the **Parameters** section, set **Include Amazon Bedrock Data Collection Module** to `yes`.

1. In **Bedrock Source Locations**, provide a comma-separated list of `bucket-name` or `bucket-name/prefix` entries, using the bucket names and prefixes you wrote down in the prerequisites. A bare bucket means Bedrock writes under `AWSLogs/` at the bucket root; an entry with a prefix means Bedrock writes under `prefix/AWSLogs/`. Do not include `s3://` or a trailing slash. For example, `bedrock-logs-111111111111-us-east-1,bedrock-logs-222222222222-us-east-1/model-invocation-logs` collects one root-delivery bucket and one prefixed bucket.

1. If your source buckets are encrypted with a customer managed KMS key, add the key ARNs to **DataBucketsKmsKeysArns**. The module then grants the collection Lambda function `kms:Decrypt` on exactly those keys.

1. Complete the stack deployment or update. After the stack reaches `CREATE_COMPLETE` or `UPDATE_COMPLETE`, AWS CloudFormation creates the Bedrock collection Lambda function, its EventBridge Scheduler schedule, and the `bedrock_logs` Glue table. The `bedrock_invocations_view` Athena view is created by `cid-cmd` when you deploy the dashboard (see [Step 4](#step-4-deploy-the-bedrock-unified-insights-lens-dashboard)); you do not need to run a saved query to create it.

**Note**
The collection Lambda function runs daily on an EventBridge Scheduler schedule. On each run it reconciles the last 30 days of the source buckets against the destination, using the destination bucket as the import checkpoint, and copies only objects it has not already imported. The collector copies files in parallel, registers each day’s Athena partition as soon as that day is processed, and begins a clean shutdown when approximately 60 seconds remain in its 10-minute execution limit.
Large 30-day or historical backfills can require several invocations. Invoke the Lambda function asynchronously, monitor its final JSON result in CloudWatch Logs, and repeat the same command after the previous invocation finishes while `"stopped_early": true`. Already imported objects are skipped. Do not run overlapping invocations.

```bash
aws lambda invoke --function-name CID-DC-bedrock-Lambda \
  --region <data-collection-region> \
  --invocation-type Event \
  --payload '{"days": 365}' --cli-binary-format raw-in-base64-out \
  /dev/stdout
aws logs tail /aws/lambda/CID-DC-bedrock-Lambda \
  --region <data-collection-region> --follow
```
An asynchronous response confirms only that Lambda accepted the request. Backfill duration depends on the number and size of source objects, not only the requested number of days. Each invocation can run for approximately nine minutes before clean shutdown begins. Logs older than the requested window are not collected, so use the `days` payload to import history older than 30 days.

### Step 2: Grant Read Access [In each source account]
<a name="step-2-grant-read-access-to-bedrock-log-buckets"></a>

The collection Lambda function reads your log buckets through the role `CID-DC-bedrock-LambdaRole`, which the stack creates in Step 1. You grant that role read access with a bucket policy on each source bucket. Apply the policy after Step 1, because Amazon S3 rejects a policy whose principal is a role that does not exist yet. If a source bucket is in the Data Collection account itself, you do not need a bucket policy: the permissions that the stack gives the role are enough.

After the Data Collection Stack deploys, the Bedrock module exposes a ** `BucketPolicyExample` ** output with an illustrative policy for one source bucket and the `LambdaRoleArn` filled in. Apply a separate pair of statements to each source bucket, and keep the statement that lets Amazon Bedrock write the logs.

1. Add the following statements to the policy of each source bucket. Replace `<data-collection-account-id>` and `<bucket>`. For a `bucket-name/prefix` entry, put `<prefix>/` before `AWSLogs/` in the `Resource` of the first statement, and use `<prefix>/AWSLogs/*` for the `s3:prefix` condition. Use the exact role ARN from the `LambdaRoleArn` output, and do not use a wildcard principal.

   ```json
   {
     "Sid": "AllowCIDBedrockDataCollectionRead",
     "Effect": "Allow",
     "Principal": {"AWS": "arn:aws:iam::<data-collection-account-id>:role/CID-DC-bedrock-LambdaRole"},
     "Action": "s3:GetObject",
     "Resource": "arn:aws:s3:::<bucket>/AWSLogs/*"
   },
   {
     "Sid": "AllowCIDBedrockDataCollectionList",
     "Effect": "Allow",
     "Principal": {"AWS": "arn:aws:iam::<data-collection-account-id>:role/CID-DC-bedrock-LambdaRole"},
     "Action": "s3:ListBucket",
     "Resource": "arn:aws:s3:::<bucket>",
     "Condition": {"StringLike": {"s3:prefix": "AWSLogs/*"}}
   }
   ```

1. If the source bucket is encrypted with a customer managed KMS key in another account, also add this statement to the key policy, so the role can decrypt the log objects when it reads them through Amazon S3. The AWS managed key `aws/s3` cannot be shared with another account, so cross-account collection needs either SSE-S3 or a customer managed key.

   ```json
   {
     "Sid": "AllowCIDBedrockDataCollectionDecrypt",
     "Effect": "Allow",
     "Principal": {"AWS": "arn:aws:iam::<data-collection-account-id>:role/CID-DC-bedrock-LambdaRole"},
     "Action": "kms:Decrypt",
     "Resource": "*",
     "Condition": {"StringEquals": {"kms:ViaService": "s3.<bucket-region>.amazonaws.com"}}
   }
   ```

### Step 3: Trigger Data Collection [In Data Collection Account]
<a name="step-3-trigger-data-collection"></a>

After the read access is in place, run the collection Lambda function once to verify that data flows correctly. Without this, the first collection happens at the next scheduled run.

1. Invoke the collection Lambda function asynchronously with a one-day window (or wait for the next scheduled run):

   ```bash
   aws lambda invoke \
     --function-name CID-DC-bedrock-Lambda \
     --region <data-collection-region> \
     --invocation-type Event \
     --payload '{"days": 1}' --cli-binary-format raw-in-base64-out \
     /dev/stdout
   aws logs tail /aws/lambda/CID-DC-bedrock-Lambda \
     --region <data-collection-region> --follow
   ```

1. Wait for the final JSON result in CloudWatch Logs, and then run a test query in Athena to confirm that data is accessible:

   ```sql
   SELECT * FROM optimization_data.bedrock_logs LIMIT 10;
   ```

**Note**
A one-day verification usually finishes faster than a 30-day backfill, but duration depends on the number and size of log objects. The Lambda function can run for approximately nine minutes before it begins a clean shutdown with approximately 60 seconds remaining. If the final result contains `"stopped_early": true`, repeat the same invocation after the current invocation finishes.
To reconcile the default 30-day window explicitly, run:

```bash
aws lambda invoke --function-name CID-DC-bedrock-Lambda \
  --region <data-collection-region> \
  --invocation-type Event \
  --payload '{"days": 30}' --cli-binary-format raw-in-base64-out \
  /dev/stdout
```
Large 30-day or historical backfills can require several invocations. Re-run the same command after each invocation finishes while `"stopped_early": true`. The destination bucket acts as a checkpoint, so previously imported objects are skipped. Each processed day’s partition is registered before the invocation returns, including a partially processed day. Do not run overlapping invocations.
If the query returns no results, verify the following:
Amazon Bedrock model invocation logging is enabled with S3 delivery in the source account and Region, and Bedrock has generated at least one invocation log.
The source location is listed in the **Bedrock Source Locations** (`BedrockSourceBuckets`) parameter as `bucket-name` for root delivery or `bucket-name/prefix` for prefixed delivery.
The final JSON result in CloudWatch Logs has an empty `errors` list. An `AccessDenied` error points to the bucket policy or the KMS key policy.
The source bucket policy grants the collection Lambda function role access to the same location, using the per-bucket pattern in this step. If you deleted and redeployed the Bedrock module, the role was recreated: save the bucket policy again, because Amazon S3 binds a role principal to the role it was created for.
If the source bucket is encrypted with a customer managed KMS key, its ARN is listed in `DataBucketsKmsKeysArns`, and, if the key is in another account, its key policy allows the role to decrypt.
The logs are no older than the window you collected. Invoke the Lambda function with a larger `days` value to import older logs.

### Step 4: Deploy the Bedrock Unified Insights Lens Dashboard [In Data Collection Account]
<a name="step-4-deploy-the-bedrock-unified-insights-lens-dashboard"></a>

**Note**
Before deploying the dashboard, verify all of the following:
+ Amazon Quick is subscribed in the Data Collection account.
+ The `bedrock_logs` table in the Data Collection database (`optimization_data` by default) contains at least one partition, which means the collection Lambda function has run at least once and imported log files. If the table is missing, the deployment stops with a prerequisites error.

During deployment, `cid-cmd` creates the `bedrock_invocations_view` Athena view in the Athena database you select. The view reads the `bedrock_logs` table from the Data Collection database, which `cid-cmd` finds by looking for that table (the default is `optimization_data`).

**Example**
 **Prerequisite**: To install this dashboard using CloudFormation, you need to install Foundational Dashboards CFN with version v4.0.0 or above as described [here](deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard)

1. Sign in to your **Data Collection** account. Choose the following Launch Stack button to open the **pre-populated stack template** in your CloudFormation.

    [![Launch Stack button that opens the pre-populated CloudFormation stack for the Bedrock Unified Insights Lens Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cid-plugin.yml&stackName=Bedrock-Unified-Insights-Lens-Dashboard&param_DashboardId=bedrock-unified-insights-lens-dashboard&param_RequiresDataCollection=yes)

1. (Optional) Change the **Stack name** for your template.

1. Leave **Parameters** values as they are.

1. Review the configuration and choose **Create stack**.

1. The stack starts in **CREATE\_IN\_PROGRESS** status. When complete, the stack shows **CREATE\_COMPLETE**.

1. Check the stack output for the dashboard URL.
**Note**
 **Troubleshooting:** If you see the error `No export named cid-CidExecArn found` during stack deployment, make sure you have completed the prerequisite steps.

1. Sign in to your **Data Collection** account.

1. Open a command-line interface with permissions to run API requests in your AWS account. We recommend [AWS CloudShell](https://console.aws.amazon.com/cloudshell/home).

1. Run the following command to download and install the CID CLI tool:

   ```bash
   pip3 install --upgrade cid-cmd
   ```

1. Run the following command to deploy the dashboard:

   ```bash
   cid-cmd deploy --dashboard-id bedrock-unified-insights-lens-dashboard
   ```

   Follow the instructions from the deployment wizard. For more information about command line options, see the [README](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/?tab=readme-ov-file#command-line-tool-cid-cmd) or run `cid-cmd --help`.

## Adding New Source Accounts
<a name="adding-new-source-accounts"></a>

To start collecting Bedrock invocation data from additional accounts:

1.  [Enable Bedrock model invocation logging](#enable-bedrock-logging) with S3 delivery in the new account and Region.

1. Add the new bucket’s full source location to **Bedrock Source Locations** (`BedrockSourceBuckets`) by updating the Data Collection Stack. Use `bucket-name` for root delivery or `bucket-name/prefix` for prefixed delivery, as in [Step 1](#step-1-enable-the-bedrock-module-in-the-data-collection-stack).

1. Apply the per-bucket policy statements as in [Step 2](#step-2-grant-read-access-to-bedrock-log-buckets).

1. On the next scheduled run (or after an asynchronous manual invocation as in [Step 3](#step-3-trigger-data-collection)), the collection Lambda function starts reconciling the new bucket’s last 30 days and registers each processed `(account_id, region, year, month, day)` partition automatically. A high-volume 30-day window can require several non-overlapping invocations. To import more than 30 days of history, invoke the Lambda function with a wider window (`--payload '{"days": N}'`) and repeat it while `"stopped_early": true`.

You do not need to redeploy the dashboard. New accounts automatically appear as filter values after the next Amazon Quick SPICE refresh.

## Update
<a name="update"></a>

When a new version of the dashboard template is released, update your dashboard by running the following command:

```bash
cid-cmd update --dashboard-id bedrock-unified-insights-lens-dashboard
```

## Sample Athena Queries
<a name="sample-athena-queries"></a>

All queries in this section can be run in the Amazon Athena console. The queries on `bedrock_logs` use the Data Collection database (`optimization_data` by default). The queries on `bedrock_invocations_view` use the Athena database you selected when you deployed the dashboard.

**Note**
If the collection Lambda function has not yet run, queries against `bedrock_logs` return no results. Verify that the Lambda function has run at least once and imported log files (see [Step 3](#step-3-trigger-data-collection)) before running these queries. The view returns only the last 6 months of data.

 **Preview the table**

```sql
SELECT *
FROM optimization_data.bedrock_logs
LIMIT 10;
```

 **Requests by account and model**

```sql
SELECT account_id,
       modelid,
       COUNT(*) AS request_count,
       SUM(input.inputtokencount)  AS total_input_tokens,
       SUM(output.outputtokencount) AS total_output_tokens
FROM optimization_data.bedrock_logs
GROUP BY account_id, modelid
ORDER BY request_count DESC;
```

 **Tokens and stop reasons in the last 30 days (flattened view)**

```sql
SELECT account_id,
       modelid,
       region,
       stop_reason,
       COUNT(*)                 AS requests,
       SUM(input_tokens)        AS total_input_tokens,
       SUM(output_tokens)       AS total_output_tokens,
       SUM(cache_read_tokens)   AS total_cache_read_tokens,
       SUM(cache_write_tokens)  AS total_cache_write_tokens,
       SUM(total_tokens)        AS total_tokens
FROM bedrock_invocations_view
WHERE timestamp >= date_add('day', -30, current_timestamp)
GROUP BY account_id, modelid, region, stop_reason
ORDER BY requests DESC;
```

 **Error rate by model**

```sql
SELECT modelid,
       COUNT(*) AS requests,
       COUNT_IF(errorcode IS NOT NULL) AS failed_requests,
       ROUND(100.0 * COUNT_IF(errorcode IS NOT NULL) / COUNT(*), 2) AS error_rate_percent
FROM bedrock_invocations_view
GROUP BY modelid
ORDER BY failed_requests DESC;
```

 **Tokens by caller (role and session)**

```sql
SELECT split_part(identity_arn, '/', 2) AS caller_role,
       split_part(identity_arn, '/', 3) AS caller_session,
       COUNT(*)                         AS requests,
       SUM(total_tokens)                AS total_tokens
FROM bedrock_invocations_view
WHERE identity_arn LIKE '%:assumed-role/%'
GROUP BY 1, 2
ORDER BY total_tokens DESC
LIMIT 20;
```

 **Prompt cache hit rate by model**

The hit rate is the share of input tokens served from the prompt cache: cache read tokens divided by the sum of input, cache read, and cache write tokens.

```sql
SELECT modelid,
       SUM(cache_read_tokens) AS cache_read_tokens,
       ROUND(100.0 * SUM(COALESCE(cache_read_tokens, 0))
             / NULLIF(SUM(COALESCE(input_tokens, 0) + COALESCE(cache_read_tokens, 0) + COALESCE(cache_write_tokens, 0)), 0), 2) AS cache_hit_rate_percent
FROM bedrock_invocations_view
GROUP BY modelid
HAVING SUM(COALESCE(cache_read_tokens, 0)) > 0
ORDER BY cache_read_tokens DESC;
```

 **Join Bedrock invocation logs to CUR 2.0 cost data**

This query joins the view to AWS Cost and Usage Report (CUR 2.0) data on account, model, caller, and day, returning per-account, per-model, per-caller, per-day cost alongside request count and token totals.
+  **Caller**: CUR 2.0 records the caller’s IAM role or user ARN in `line_item_iam_principal`, while the invocation logs record the session ARN (`assumed-role/<role>/<session>`). The query compares the account and the role or user name on both sides, so it works with either form.
+  **Day**: IAM principal attribution reaches CUR 2.0 at a daily grain per usage type, so the query matches by day, not by hour.
+  **Model**: the query compares the model ID on both sides after removing the ARN and the cross-Region inference prefix (such as `us.` or `global.`), so a call through `us.anthropic.claude-haiku-4-5-20251001-v1:0` matches both the foundation-model and the inference-profile line items. Calls through an application inference profile do not match, because the profile ID does not contain the model name.

**Important**
each side is aggregated to `(account, model, caller, day)` in a CTE **before** the join. Joining the raw rows directly would fan out. CUR has a separate line item per usage type (input tokens, output tokens, cache), so each request would match several CUR rows and each CUR row would match every request of that day, inflating `request_count`, token totals, and especially cost. Aggregating first makes the join one-to-one per day.

**Note**
 `line_item_iam_principal` is populated only in a CUR 2.0 export created with the caller identity option, and only for costs incurred after that. For the setup, see [IAM principal attribution](https://docs.aws.amazon.com/bedrock/latest/userguide/cost-mgmt-iam-principal-tracking.html) in the Amazon Bedrock User Guide. Without it, the principal values are empty and this query returns no rows. In that case, remove the caller columns and the caller join condition, and match on account, model, and day only. Replace `cid_data_export.cur2` with your CUR 2.0 table.

```sql
WITH requests AS (
    SELECT
        account_id,
        -- model ID without the ARN and the cross-Region inference prefix (us., eu., global., ...)
        regexp_replace(element_at(split(modelid, '/'), -1), '^(us|us-gov|eu|apac|jp|au|ca|global)\.', '') AS model_key,
        -- role name of arn:aws:sts::<account>:assumed-role/<role>/<session>, or user name of an IAM user
        COALESCE(regexp_extract(identity_arn, '(?:assumed-role|role)/([^/]+)', 1),
                 regexp_extract(identity_arn, ':user/(.+)$', 1))          AS caller,
        date_trunc('day', timestamp)                                      AS usage_day,
        COUNT(requestid)                                                  AS request_count,
        SUM(input_tokens)                                                 AS total_input_tokens,
        SUM(output_tokens)                                                AS total_output_tokens
    FROM bedrock_invocations_view
    GROUP BY 1, 2, 3, 4
),
cur AS (
    SELECT
        line_item_usage_account_id                                        AS account_id,
        regexp_replace(element_at(split(line_item_resource_id, '/'), -1), '^(us|us-gov|eu|apac|jp|au|ca|global)\.', '') AS model_key,
        COALESCE(regexp_extract(line_item_iam_principal, '(?:assumed-role|role)/([^/]+)', 1),
                 regexp_extract(line_item_iam_principal, ':user/(.+)$', 1)) AS caller,
        date_trunc('day', line_item_usage_start_date)                     AS usage_day,
        SUM(line_item_unblended_cost)                                     AS unblended_cost
    FROM cid_data_export.cur2
    WHERE lower(product_servicecode) LIKE '%bedrock%'
      AND line_item_iam_principal IS NOT NULL
      AND line_item_iam_principal <> ''
    GROUP BY 1, 2, 3, 4
)
SELECT
    r.account_id,
    r.caller,
    r.model_key                      AS modelid,
    r.usage_day,
    r.request_count,
    r.total_input_tokens,
    r.total_output_tokens,
    c.unblended_cost
FROM requests r
JOIN cur c
    ON  r.account_id = c.account_id
    AND r.model_key  = c.model_key
    AND r.caller     = c.caller
    AND r.usage_day  = c.usage_day
ORDER BY c.unblended_cost DESC;
```

**Join logic**

| Bedrock field | CUR 2.0 field | Match type |
| --- | --- | --- |
|  `account_id`  |  `line_item_usage_account_id`  | exact |
|  `modelid` (last ARN segment, without the cross-Region prefix) |  `line_item_resource_id` (last ARN segment, without the cross-Region prefix) | exact on the bare model ID, so `anthropic.claude-haiku-4-5-20251001-v1:0` matches the foundation-model ARN and the `us.` or `global.` inference-profile ARN |
|  `identity_arn` (role or user name) |  `line_item_iam_principal` (role or user name) | exact on the name, within the same account |
|  `date_trunc('day', timestamp)`  |  `date_trunc('day', line_item_usage_start_date)`  | exact on the day |

## Glue Table Schema
<a name="glue-table-schema"></a>

The `bedrock_logs` table in the Data Collection database stores the raw normalized request records collected from source accounts. The `bedrock_invocations_view` view flattens the nested token and body fields for easier querying. `cid-cmd` creates and updates this view automatically when you deploy or update the dashboard. The view returns only the last 6 months of data.

### `bedrock_logs` table
<a name="bedrock_logs-table"></a>

| Column | Type | Notes |
| --- | --- | --- |
|  `schematype`  | string |  |
|  `schemaversion`  | string |  |
|  `timestamp`  | string | ISO 8601 timestamp of the request |
|  `requestid`  | string | Unique request identifier |
|  `operation`  | string | Bedrock API operation name, for example `Converse`, `ConverseStream`, `InvokeModel`  |
|  `modelid`  | string | Model ID, inference profile ID, or inference profile ARN, as the caller passed it |
|  `errorcode`  | string | Error code on failed requests (NULL on success) |
|  `inferenceregion`  | string | Region the model ran in (for cross-Region inference profiles) |
|  `identity_arn`  | string | IAM ARN of the caller |
|  `requestmetadata`  | map<string,string> | Request metadata key-value pairs that the caller set: the `requestMetadata` field for Converse and ConverseStream, or the `X-Amzn-Bedrock-Request-Metadata` header for InvokeModel and InvokeModelWithResponseStream |
|  `collection_time`  | string | Timestamp when the record was collected |
|  `input`  | struct | Contains: `inputbodyjson` (string), `inputcontenttype` (string), `inputtokencount` (int) |
|  `output`  | struct | Contains: `outputbodyjson` (string), `outputcontenttype` (string), `outputtokencount` (int) |
|  `account_id`  | string | Partition key: source AWS account ID |
|  `region`  | string | Partition key: AWS Region of the request |
|  `year`  | string | Partition key |
|  `month`  | string | Partition key |
|  `day`  | string | Partition key |

### `bedrock_invocations_view` flattened view
<a name="bedrock_invocations_view-flattened-view"></a>

The view keeps the table columns `account_id`, `timestamp` (as a timestamp), `region`, `requestid`, `operation`, `modelid`, `identity_arn`, `requestmetadata` (as JSON), `errorcode`, `inferenceregion`, `year`, `month`, and `day`, and adds the following fields. The dashboard derives the caller role and session from `identity_arn`.

| Field | Type | Source |
| --- | --- | --- |
|  `input_tokens`  | int |  `input.inputtokencount`: input tokens that were not served from the prompt cache |
|  `output_tokens`  | int |  `output.outputtokencount`  |
|  `cache_read_tokens`  | int |  `COALESCE` of `$.usage.cacheReadInputTokens`, `$.usage.cacheReadInputTokenCount`, `$.usage.cache_read_input_tokens`  |
|  `cache_write_tokens`  | int |  `COALESCE` of `$.usage.cacheWriteInputTokens`, `$.usage.cacheWriteInputTokenCount`, `$.usage.cache_creation_input_tokens`  |
|  `total_tokens`  | int | Input, output, cache read, and cache write tokens (missing values count as 0) |
|  `input_content_type`, `output_content_type`  | string |  `input.inputcontenttype`, `output.outputcontenttype`  |
|  `latency_ms`  | int |  `$.metrics.latencyMs` (Converse and ConverseStream only) |
|  `max_tokens_requested`  | int | The maximum token setting in the request (`inferenceConfig.maxTokens`, `max_tokens`, `max_completion_tokens`, `max_output_tokens`, or `inferenceConfig.max_new_tokens`) |
|  `temperature`  | double |  `inferenceConfig.temperature` or `temperature`  |
|  `system_prompt`  | string |  `Yes` when the request has a system prompt, otherwise `No`  |
|  `service_tier`  | string |  `$.service_tier` or `$.usage.service_tier`, when the model reports one |
|  `stop_reason`  | string |  `COALESCE` of `$.stopReason` and `$.stop_reason`, and of the OpenAI-style `finish_reason` (mapped to `end_turn` and `max_tokens`) and the Responses API status |
|  `response_preview`  | string | First available response text field of the supported response formats (Converse, Anthropic Messages, Titan, OpenAI-style chat completions and Responses API), capped at 1,000 characters with `substr(…​, 1, 1000)`  |
|  `prompt_preview`  | string | First available prompt text field of the supported request formats (including image prompts), capped at 1,000 characters |

**Note**
The view reads each record as a single JSON document. For these cases the response text, the stop reason, or the token fields are empty:
Streaming calls made with `InvokeModelWithResponseStream`: the response is a list of chunks, so `response_preview` and `stop_reason` are empty. Token counts are still filled.
Embedding, rerank, and image-generation calls have no response text. Some models return no token counts.
Responses that contain only a reasoning block, or only a tool call, have no response text.
Request and response bodies larger than 100 KB, and binary data, are stored by Amazon Bedrock as separate objects. The collector skips those objects, so the previews of those requests are empty.
Calls through an application inference profile show the profile ID instead of a model name, because the log does not contain the model. In the dashboard, the Traffic Type and Model Category fields are calculated from the model ID, so treat them as estimates.

## Security Considerations
<a name="security-considerations"></a>
+  **No changes to source accounts**: The module is pull-based. It does not deploy any infrastructure, IAM roles, or logging configuration into your source accounts. You own and control the Bedrock logging configuration and the log bucket.
+  **Reads only the locations you list**: The collection Lambda function role gets one inline policy per `BedrockSourceBuckets` entry, granting `s3:ListBucket` on that bucket and `s3:GetObject` only under the `AWSLogs/` folder of the listed location, with or without the prefix. It has no read access to buckets or prefixes you have not listed. The role’s combined inline policy size allows about 35 source locations. The role is not granted `sts:AssumeRole` and does not assume any cross-account role.
+  **Scoped write access**: The collection Lambda function role can write (`s3:PutObject`) only under the `bedrock/` prefix of the Data Collection destination bucket, list that prefix to find what it has already imported, and register partitions only on the `bedrock_logs` Glue table.
+  **You control the bucket policy**: Read access is granted by a bucket policy you apply separately to each source bucket. Restrict `s3:GetObject` and the `s3:prefix` listing condition to that bucket’s configured location, and use only the collection Lambda function role principal from the module’s `BucketPolicyExample` output.
+  **Optional KMS**: If your source log buckets are encrypted with a customer managed KMS key, list the key ARNs in `DataBucketsKmsKeysArns`. The module grants the collection Lambda function `kms:Decrypt` only on those keys. The Data Collection destination bucket uses SSE-S3.
+  **Prompt and response content**: The collected records and the previews in the dashboard contain the prompts and responses of your applications. Limit access to the Data Collection account, the Athena database, and the dashboard to people who may see that content.

## Authors
<a name="authors"></a>
+ Steph Gooch, Principal Tech Advocate
+ Yuriy Prykhodko, Principal Technical Account Manager

## Feedback & Support
<a name="bedrock-unified-insights-lens-dashboard-feedback-support"></a>

For feedback and support, see the [Feedback and Support](feedback-support.md) guide.

**Note**
These dashboards and their content: (a) are for informational purposes only, (b) represent current AWS product offerings and practices, which are subject to change without notice, and (c) does not create any commitments or assurances from AWS and its affiliates, suppliers or licensors. AWS content, products or services are provided "as is" without warranties, representations, or conditions of any kind, whether express or implied. The responsibilities and liabilities of AWS to its customers are controlled by AWS agreements, and this document is not part of, nor does it modify, any agreement between AWS and its customers.
