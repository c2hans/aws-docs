---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

This section describes how to completely remove the Spatial Data Management Application from your AWS account.

## Prerequisites
<a name="uninstall-prerequisites"></a>

### Configure AWS CLI
<a name="configure-aws-cli"></a>

Before running any commands, configure your AWS CLI with the appropriate region and profile:

```
# Set your AWS Region (replace with your deployment region)
export AWS_REGION=<your-region>

# Set your AWS CLI profile (if using named profiles)
export AWS_PROFILE=<your-profile-name>

# Verify configuration
aws sts get-caller-identity
```

All subsequent commands in this guide use these environment variables. You can also specify `--region` and `--profile` flags directly in each command.

## Before You Uninstall
<a name="before-you-uninstall"></a>

### Important Warnings
<a name="important-warnings"></a>

**Warning**
Uninstalling will delete all application resources. S3 buckets are retained by default to prevent accidental data loss. DynamoDB PITR backups are retained for 35 days after table deletion. This operation cannot be undone. If you provided optional parameters for existing DNS resources, AWS Deadline Cloud farms, or render queues during deployment, don’t delete those resources. They might be used by other applications or use cases in your account.

### Backup Critical Data
<a name="backup-critical-data"></a>

Before uninstalling, backup any data you want to keep:

#### 1. Export DynamoDB Tables
<a name="export-dynamodb-tables"></a>

```
# Create on-demand backups (replace <resource-prefix> with your resource naming prefix)
for table in $(aws dynamodb list-tables --query 'TableNames[?contains(@, `<resource-prefix>`)]' --output text); do
  aws dynamodb create-backup \
    --table-name $table \
    --backup-name "${table}-final-backup-$(date +%Y%m%d)"
done
```

#### 2. Download S3 Assets
<a name="download-s3-assets"></a>

```
# Get asset bucket name (replace <stack-name> with your CloudFormation stack name)
ASSET_BUCKET=$(aws cloudformation describe-stacks \
  --stack-name <stack-name> \
  --query 'Stacks[0].Outputs[?OutputKey==`AssetBucketName`].OutputValue' \
  --output text)

# Sync to local directory
aws s3 sync s3://$ASSET_BUCKET ./backup/assets/
```

#### 3. Export CloudWatch Logs
<a name="export-cloudwatch-logs"></a>

```
# Export logs to S3 for archival (replace <log-group-name> and <backup-bucket> with your values)
aws logs create-export-task \
  --log-group-name <log-group-name> \
  --from $(date -d '30 days ago' +%s)000 \
  --to $(date +%s)000 \
  --destination <backup-bucket> \
  --destination-prefix cloudwatch-logs/
```

## Uninstallation Methods
<a name="uninstallation-methods"></a>

### Method 1: CloudFormation Stack Deletion (Recommended)
<a name="method-1-cloudformation-stack-deletion"></a>

This method deletes all resources except S3 buckets (which are retained by default).

#### Option A: Using AWS Console
<a name="option-a-using-aws-console"></a>

1. Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/)

1. In the navigation pane, choose **Stacks**

1. Select your stack from the list

1. Choose **Delete**

1. In the confirmation dialog, choose **Delete stack**

1. Monitor the deletion progress in the **Events** tab
   + Stack status changes to `DELETE_IN_PROGRESS`
   + Individual resources show `DELETE_IN_PROGRESS` then `DELETE_COMPLETE`
   + Final stack status shows `DELETE_COMPLETE` (stack disappears from list)

Expected time: 10-15 minutes

#### Option B: Using AWS CLI
<a name="option-b-using-aws-cli"></a>

 **Step 1: Delete the Stack**

```
# Replace <stack-name> with your CloudFormation stack name
aws cloudformation delete-stack \
  --stack-name <stack-name>
```

 **Step 2: Monitor Deletion Progress**

```
# Replace <stack-name> with your CloudFormation stack name
aws cloudformation describe-stack-events \
  --stack-name <stack-name> \
  --query 'StackEvents[*].[Timestamp,ResourceStatus,ResourceType,LogicalResourceId]' \
  --output table
```

 **Step 3: Wait for Completion**

```
# Replace <stack-name> with your CloudFormation stack name
aws cloudformation wait stack-delete-complete \
  --stack-name <stack-name>
```

Expected time: 10-15 minutes

### Method 2: Force Delete (If Stack Deletion Fails)
<a name="method-2-force-delete"></a>

If stack deletion fails due to resource dependencies:

#### Step 1: Identify Stuck Resources
<a name="step-1-identify-stuck-resources"></a>

```
# Replace <stack-name> with your CloudFormation stack name
aws cloudformation describe-stack-events \
  --stack-name <stack-name> \
  --query 'StackEvents[?ResourceStatus==`DELETE_FAILED`].[LogicalResourceId,ResourceStatusReason]' \
  --output table
```

#### Step 2: Manually Delete Stuck Resources
<a name="step-2-manually-delete-stuck-resources"></a>

Common stuck resources and solutions:

 **Lambda ENIs (Elastic Network Interfaces):**

```
# List ENIs (replace <resource-prefix> with your resource naming prefix)
aws ec2 describe-network-interfaces \
  --filters "Name=description,Values=*<resource-prefix>*" \
  --query 'NetworkInterfaces[*].[NetworkInterfaceId,Status]'

# Wait for ENIs to be released (automatic, takes 5-10 minutes)
```

 **S3 Buckets with Objects:**

```
# Empty bucket before deletion (replace <bucket-name> with your bucket name)
aws s3 rm s3://<bucket-name> --recursive

# Delete bucket
aws s3 rb s3://<bucket-name>
```

 **VPC Endpoints:**

```
# Delete VPC endpoints (replace <vpc-endpoint-id> with your VPC endpoint ID)
aws ec2 delete-vpc-endpoints \
  --vpc-endpoint-ids <vpc-endpoint-id>
```

#### Step 3: Retry Stack Deletion
<a name="step-3-retry-stack-deletion"></a>

```
# Replace <stack-name> with your CloudFormation stack name
aws cloudformation delete-stack \
  --stack-name <stack-name>
```

## Post-Deletion Cleanup
<a name="post-deletion-cleanup"></a>

After stack deletion completes, manually clean up retained resources.

**Warning**
The commands in this section use grep patterns and queries to filter resources by naming conventions. If your AWS account hosts multiple applications or use cases, review the command output carefully before executing deletions to avoid accidentally removing resources used by other applications.

### 1. Delete S3 Buckets
<a name="delete-s3-buckets"></a>

**Warning**
This permanently deletes all stored assets and logs.

```
# List retained buckets
aws s3 ls | grep spatial-data-management

# Empty and delete each bucket
for bucket in $(aws s3 ls | grep spatial-data-management | awk '{print $3}'); do
  echo "Deleting bucket: $bucket"
  aws s3 rm s3://$bucket --recursive
  aws s3 rb s3://$bucket
done
```

### 2. Delete CloudWatch Log Groups
<a name="delete-cloudwatch-log-groups"></a>

```
# List log groups (replace <log-group-prefix> with your log group prefix)
aws logs describe-log-groups \
  --log-group-name-prefix <log-group-prefix> \
  --query 'logGroups[*].logGroupName'

# Delete each log group
for log_group in $(aws logs describe-log-groups --log-group-name-prefix <log-group-prefix> --query 'logGroups[*].logGroupName' --output text); do
  aws logs delete-log-group --log-group-name $log_group
done
```

### 3. Delete KMS Keys
<a name="delete-kms-keys"></a>

KMS keys enter a pending deletion state (7-30 days) and cannot be immediately deleted.

```
# List KMS keys
aws kms list-aliases \
  --query 'Aliases[?contains(AliasName, `spatial-data-management`)]'

# Schedule key deletion (minimum 7 days)
aws kms schedule-key-deletion \
  --key-id <key-id> \
  --pending-window-in-days 7
```

### 4. Delete Secrets Manager Secrets
<a name="delete-secrets-manager-secrets"></a>

```
# List secrets (replace <resource-prefix> with your resource naming prefix)
aws secretsmanager list-secrets \
  --query 'SecretList[?contains(Name, `<resource-prefix>`)]'

# Delete secrets (with recovery window, replace <secret-id> with your secret ID)
aws secretsmanager delete-secret \
  --secret-id <secret-id> \
  --recovery-window-in-days 7
```

### 5. Delete Cognito User Pool
<a name="delete-cognito-user-pool"></a>

If not automatically deleted:

```
# Get user pool ID (replace <user-pool-name> with your user pool name)
USER_POOL_ID=$(aws cognito-idp list-user-pools \
  --max-results 60 \
  --query 'UserPools[?contains(Name, `<user-pool-name>`)].Id' \
  --output text)

# Delete user pool
aws cognito-idp delete-user-pool \
  --user-pool-id $USER_POOL_ID
```

## Verification
<a name="uninstall-verification"></a>

### Verify Stack Deletion
<a name="verify-stack-deletion"></a>

```
# Check stack status (should return error if deleted, replace <stack-name> with your stack name)
aws cloudformation describe-stacks \
  --stack-name <stack-name>
```

Expected: `Stack with id <stack-name> does not exist`

### Verify Resource Cleanup
<a name="verify-resource-cleanup"></a>

```
# Check for remaining Lambda functions (replace <resource-prefix> with your resource naming prefix)
aws lambda list-functions \
  --query 'Functions[?contains(FunctionName, `<resource-prefix>`)]'

# Check for remaining DynamoDB tables
aws dynamodb list-tables \
  --query 'TableNames[?contains(@, `<resource-prefix>`)]'

# Check for remaining S3 buckets (replace <bucket-prefix> with your bucket naming prefix)
aws s3 ls | grep <bucket-prefix>

# Check for remaining CloudWatch log groups (replace <log-group-prefix> with your log group prefix)
aws logs describe-log-groups \
  --log-group-name-prefix <log-group-prefix>
```

## Cost Impact After Uninstallation
<a name="cost-impact-after-uninstallation"></a>

### Immediate Cost Reduction
<a name="immediate-cost-reduction"></a>
+ Lambda invocations: $0
+ DynamoDB requests: $0
+ API Gateway requests: $0
+ CloudFront requests: $0
+ VPC endpoints: $0

### Ongoing Costs (If Not Cleaned Up)
<a name="ongoing-costs"></a>
+ S3 Storage (retained buckets)
+ CloudWatch Logs (retained logs)
+ KMS Keys (pending deletion)
+ DynamoDB Backups (PITR backups, 35 days)

### Complete Cleanup Cost
<a name="complete-cleanup-cost"></a>

After manual cleanup of all retained resources: $0
