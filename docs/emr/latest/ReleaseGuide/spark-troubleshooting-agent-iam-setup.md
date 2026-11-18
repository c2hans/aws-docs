---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-troubleshooting-agent-iam-setup.html
---

# IAM permissions for the Apache Spark agents
<a name="spark-troubleshooting-agent-iam-setup"></a>

## Prerequisites
<a name="spark-troubleshooting-agent-iam-prerequisites"></a>

Before you begin, make sure that you have the following:
+ An AWS account with IAM administrative access
+ AWS CLI installed and configured. For more information, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

Set the following variables for use in later commands:

```
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
REGION=$(aws configure get region)
```

## How the Apache Spark agents use your permissions
<a name="spark-agents-iam-how"></a>

The Amazon SageMaker Unified Studio (SMUS) MCP server authorizes operations at the AWS service level using the IAM identity that your MCP client is configured with. No separate MCP-specific permissions are required. The agents act as that identity, so they can only access what that identity is permitted to access.

The policies on this page describe the permissions that the agents use at full capability. You choose how much of that access to grant. The agents use these permissions to read your job runs, logs, and Spark UI data. They don't start, modify, or stop your jobs. Attach the permissions that you want the agents to have to the IAM identity that your MCP client uses. This is normally the role that you already use to analyze your Spark jobs. Confirm that the role has the permissions in [Step 2: Attach permissions for your deployment mode](#spark-troubleshooting-agent-iam-step2), and point your MCP client at it, as described in [Step 3: Configure your MCP client](#spark-troubleshooting-agent-iam-step3).

If you want the agents to run under a separate, scoped identity instead of your own, create a dedicated role, as described in [Step 1: (Optional) Create a dedicated agent role](#spark-troubleshooting-agent-iam-step1). For an AWS CloudFormation template that creates the role, and for other ways to tighten the agents' access, see [How can I get more fine-grained control over the agents' permissions?](spark-troubleshooting-agent-troubleshooting.md#spark-agents-qa-fine-grained).

## Step 1: (Optional) Create a dedicated agent role
<a name="spark-troubleshooting-agent-iam-step1"></a>

Skip this step if you use your existing IAM role. Complete it only if you want to give the agents their own identity: a dedicated role that you create for the MCP server and grant only the access that you choose.

**To create the IAM role (AWS CLI)**

1. Create a trust policy document that allows your account to assume the role:

   ```
   cat > mcp-trust-policy.json << EOF
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "AllowAccountToAssumeRole",
         "Effect": "Allow",
         "Principal": { "AWS": "arn:aws:iam::${ACCOUNT_ID}:root" },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   EOF
   ```

1. Create the role:

   ```
   aws iam create-role \
     --role-name SparkTroubleshootingMCPRole \
     --assume-role-policy-document file://mcp-trust-policy.json
   ```

## Step 2: Attach permissions for your deployment mode
<a name="spark-troubleshooting-agent-iam-step2"></a>

Attach the permissions policy that matches your Spark deployment platform to the IAM identity that the agents use. This is either your existing role or the dedicated role from [Step 1: (Optional) Create a dedicated agent role](#spark-troubleshooting-agent-iam-step1). The following commands use `SparkTroubleshootingMCPRole` as an example. Replace the `--role-name` value with your own role name. You can attach one or more of the following policies, depending on which platforms you use.

**Note**
The Apache Spark Optimization Agent supports only AWS Glue (Option B) and EMR Serverless (Option C). The Apache Spark Troubleshooting Agent can use all of the following options.

### Option A: EMR on EC2
<a name="spark-troubleshooting-agent-iam-emr-ec2"></a>

1. Create the policy document:

   ```
   cat > emr-ec2-policy.json << 'EOF'
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "EMREC2ReadAccess",
         "Effect": "Allow",
         "Action": [
           "elasticmapreduce:DescribeCluster",
           "elasticmapreduce:DescribeStep",
           "elasticmapreduce:ListSteps",
           "elasticmapreduce:ListClusters",
           "elasticmapreduce:DescribeJobFlows"
         ],
         "Resource": ["*"]
       },
       {
         "Sid": "EMRS3LogAccess",
         "Effect": "Allow",
         "Action": ["s3:GetObject", "s3:ListBucket"],
         "Resource": "*"
       },
       {
         "Sid": "EMRPersistentApp",
         "Effect": "Allow",
         "Action": [
           "elasticmapreduce:CreatePersistentAppUI",
           "elasticmapreduce:DescribePersistentAppUI",
           "elasticmapreduce:GetPersistentAppUIPresignedURL"
         ],
         "Resource": ["*"]
       }
     ]
   }
   EOF
   ```

1. Create and attach the policy:

   ```
   aws iam put-role-policy \
     --role-name SparkTroubleshootingMCPRole \
     --policy-name EMREC2TroubleshootingAccess \
     --policy-document file://emr-ec2-policy.json
   ```

Alternatively, you can attach the [AmazonElasticMapReduceFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonElasticMapReduceFullAccess.html) AWS managed policy if your role already uses it:

```
aws iam attach-role-policy \
  --role-name SparkTroubleshootingMCPRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonElasticMapReduceFullAccess
```

### Option B: AWS Glue
<a name="spark-troubleshooting-agent-iam-glue"></a>

1. Create the policy document:

   ```
   cat > glue-policy.json << EOF
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "GlueReadAccess",
         "Effect": "Allow",
         "Action": [
           "glue:GetJob",
           "glue:GetJobRun",
           "glue:GetJobRuns",
           "glue:GetJobs",
           "glue:BatchGetJobs"
         ],
         "Resource": ["arn:aws:glue:*:${ACCOUNT_ID}:job/*"]
       },
       {
         "Sid": "GlueCloudWatchLogsAccess",
         "Effect": "Allow",
         "Action": ["logs:GetLogEvents", "logs:FilterLogEvents"],
         "Resource": ["arn:aws:logs:*:${ACCOUNT_ID}:log-group:/aws-glue/*"]
       },
       {
         "Sid": "GlueSparkWebUI",
         "Effect": "Allow",
         "Action": [
           "glue:RequestLogParsing",
           "glue:GetLogParsingStatus",
           "glue:GetEnvironment",
           "glue:GetStage",
           "glue:GetStages",
           "glue:GetStageFiles",
           "glue:BatchGetStageFiles",
           "glue:GetStageAttempt",
           "glue:GetStageAttemptTaskList",
           "glue:GetStageAttemptTaskSummary",
           "glue:GetExecutors",
           "glue:GetExecutorsThreads",
           "glue:GetStorage",
           "glue:GetStorageUnit",
           "glue:GetQueries",
           "glue:GetQuery",
           "glue:GetDashboardUrl"
         ],
         "Resource": ["arn:aws:glue:*:${ACCOUNT_ID}:job/*"]
       },
       {
         "Sid": "GluePassRoleAccess",
         "Effect": "Allow",
         "Action": "iam:PassRole",
         "Resource": "arn:aws:iam::${ACCOUNT_ID}:role/{{my-job-execution-role-prefix}}*",
         "Condition": {
           "StringLike": {
             "iam:PassedToService": "glue.amazonaws.com"
           }
         }
       }
     ]
   }
   EOF
   ```

   Replace {{my-job-execution-role-prefix}} with the name prefix of your AWS Glue job execution roles.

1. Attach the policy:

   ```
   aws iam put-role-policy \
     --role-name SparkTroubleshootingMCPRole \
     --policy-name GlueTroubleshootingAccess \
     --policy-document file://glue-policy.json
   ```

### Option C: EMR Serverless
<a name="spark-troubleshooting-agent-iam-emr-serverless"></a>

1. Create the policy document:

   ```
   cat > emr-serverless-policy.json << EOF
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "EMRServerlessReadAccess",
         "Effect": "Allow",
         "Action": [
           "emr-serverless:GetJobRun",
           "emr-serverless:GetApplication",
           "emr-serverless:ListApplications",
           "emr-serverless:ListJobRuns",
           "emr-serverless:ListJobRunAttempts",
           "emr-serverless:GetDashboardForJobRun",
           "emr-serverless:ListTagsForResource"
         ],
         "Resource": ["*"]
       },
       {
         "Sid": "EMRServerlessCloudWatchLogsAccess",
         "Effect": "Allow",
         "Action": ["logs:GetLogEvents", "logs:FilterLogEvents"],
         "Resource": ["arn:aws:logs:*:${ACCOUNT_ID}:log-group:/aws/emr-serverless/*"]
       },
       {
         "Sid": "EMRServerlessS3LogsAccess",
         "Effect": "Allow",
         "Action": ["s3:GetObject", "s3:ListBucket"],
         "Resource": "*"
       }
     ]
   }
   EOF
   ```

1. Attach the policy:

   ```
   aws iam put-role-policy \
     --role-name SparkTroubleshootingMCPRole \
     --policy-name EMRServerlessTroubleshootingAccess \
     --policy-document file://emr-serverless-policy.json
   ```

### Option D: EMR on EKS
<a name="spark-troubleshooting-agent-iam-emr-eks"></a>

1. Create the policy document:

   ```
   cat > emr-eks-policy.json << EOF
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Action": [
                   "emr-containers:DescribeVirtualCluster",
                   "emr-containers:DescribeJobRun",
                   "emr-containers:ListJobRuns",
                   "emr-containers:ListVirtualClusters"
               ],
               "Resource": "*",
               "Effect": "Allow",
               "Sid": "EMREKSReadAccess"
           },
           {
               "Action": [
                   "logs:GetLogEvents",
                   "logs:DescribeLogGroups",
                   "logs:DescribeLogStreams"
               ],
               "Resource": "*",
               "Effect": "Allow",
               "Sid": "EMRCloudWatchLogAccess"
           },
           {
               "Action": [
                   "elasticmapreduce:CreatePersistentAppUI",
                   "elasticmapreduce:DescribePersistentAppUI",
                   "elasticmapreduce:GetPersistentAppUIPresignedURL"
               ],
               "Resource": "*",
               "Effect": "Allow",
               "Sid": "EMRPersistentApp"
           },
           {
               "Action": [
                   "s3:GetObject",
                   "s3:ListBucket"
               ],
               "Resource": "*",
               "Effect": "Allow",
               "Sid": "EMREKSS3LogAccess"
           }
       ]
   }
   EOF
   ```

1. Attach the policy:

   ```
   aws iam put-role-policy \
     --role-name SparkTroubleshootingMCPRole \
     --policy-name EMREKSTroubleshootingAccess \
     --policy-document file://emr-eks-policy.json
   ```

### Optional: KMS permissions for encrypted CloudWatch Logs
<a name="spark-troubleshooting-agent-iam-kms"></a>

If your CloudWatch Logs are encrypted with a customer managed KMS key, add the following (replace `<KEY_ID>` with your KMS key ID):

```
aws iam put-role-policy \
  --role-name SparkTroubleshootingMCPRole \
  --policy-name KMSCloudWatchLogsDecrypt \
  --policy-document "{
    \"Version\": \"2012-10-17\",
    \"Statement\": [{
      \"Effect\": \"Allow\",
      \"Action\": [\"kms:Decrypt\", \"kms:DescribeKey\"],
      \"Resource\": \"arn:aws:kms:${REGION}:${ACCOUNT_ID}:key/<KEY_ID>\"
    }]
  }"
```

## Step 3: Configure your MCP client
<a name="spark-troubleshooting-agent-iam-step3"></a>

Configure your MCP client with AWS credentials for the identity that the agents use. For the supported MCP clients, see [Set up the Apache Spark agents](spark-troubleshooting-agent-setup.md).
+ **Using your existing role** – Point the client at the AWS profile that you already use, the one whose permissions you confirmed in [Step 2: Attach permissions for your deployment mode](#spark-troubleshooting-agent-iam-step2). No additional role ARN is needed.
+ **Using a dedicated role** – Configure the client to assume the role that you created in [Step 1: (Optional) Create a dedicated agent role](#spark-troubleshooting-agent-iam-step1):

  ```
  echo "arn:aws:iam::${ACCOUNT_ID}:role/SparkTroubleshootingMCPRole"
  ```

For how to configure AWS credentials, refer to your MCP client's documentation. This is typically through an AWS profile that uses your identity or assumes the role.

## Condition keys for MCP server requests
<a name="spark-troubleshooting-agent-mcp-permissions-change"></a>

Two condition keys are automatically added to all requests made through the SMUS MCP server:
+ `aws:ViaAWSMCPService` – Set to `true` for any request made through an AWS managed MCP server.
+ `aws:CalledViaAWSMCP` – Set to the MCP server service principal (for example, `sagemaker-unified-studio-mcp.amazonaws.com`).

You can use these condition keys to control access to your resources when requests originate from an AWS managed MCP server.

**Example: Allow AWS Glue read operations only when accessed through the SMUS MCP server:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowGlueReadViaSMUSMCP",
      "Effect": "Allow",
      "Action": ["glue:GetJob", "glue:GetJobRun", "glue:GetJobRuns"],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:CalledViaAWSMCP": "sagemaker-unified-studio-mcp.amazonaws.com"
        }
      }
    }
  ]
}
```

**Example: Deny delete operations when accessed through any AWS managed MCP server:**

```
{
  "Effect": "Deny",
  "Action": ["s3:DeleteObject", "s3:DeleteBucket"],
  "Resource": "*",
  "Condition": {
    "Bool": {
      "aws:ViaAWSMCPService": "true"
    }
  }
}
```

For more information about condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.
