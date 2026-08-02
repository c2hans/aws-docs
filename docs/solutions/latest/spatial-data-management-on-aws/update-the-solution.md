---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/update-the-solution.html
---

# Update the solution
<a name="update-the-solution"></a>

This section describes how to update the Spatial Data Management Application to a newer version.

## Update Overview
<a name="update-overview"></a>

Updates are performed using AWS CloudFormation stack updates, which modify existing resources in place where possible. Most updates can be performed with minimal downtime.

**Important**
Before proceeding, familiarize yourself with AWS CloudFormation update processes. For detailed information, see [Updating stacks using change sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html) in the AWS CloudFormation User Guide.

## Before You Update
<a name="before-you-update"></a>

### 1. Review Release Notes
<a name="review-release-notes"></a>

Check the release notes for the new version:
+ Breaking changes
+ New features
+ Deprecated functionality
+ Migration requirements

### 2. Backup Critical Data
<a name="backup-critical-data"></a>

Although Amazon DynamoDB has Point-in-Time Recovery enabled, create explicit backups:

```
# Backup DynamoDB tables (replace <STACK-NAME> with your stack name)
for table in $(aws dynamodb list-tables --query 'TableNames[?contains(@, `<STACK-NAME>`)]' --output text); do
  aws dynamodb create-backup \
    --table-name $table \
    --backup-name "${table}-pre-update-$(date +%Y%m%d)"
done
```

### 3. Review Current Configuration
<a name="review-current-configuration"></a>

Export current stack parameters:

```
# Replace <STACK-NAME> with your CloudFormation stack name
aws cloudformation get-template \
  --stack-name <STACK-NAME> \
  --query 'TemplateBody' > current-template.json

aws cloudformation describe-stacks \
  --stack-name <STACK-NAME> \
  --query 'Stacks[0].Parameters' > current-parameters.json
```

### 4. Test in Non-Production Environment
<a name="test-in-non-production"></a>

Always test updates in a development or staging environment first.

## Update Procedures
<a name="update-procedures"></a>

The following steps guide you through updating the solution using AWS CloudFormation change sets. You can also perform these steps through the AWS CloudFormation console. For detailed information about CloudFormation update processes, see [Updating stacks using change sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html) in the AWS CloudFormation User Guide.

### Standard Update (No Breaking Changes)
<a name="standard-update"></a>

#### Step 0: Get Your Stack Name
<a name="step-0-get-stack-name"></a>

If you don’t know your stack name, list all CloudFormation stacks to find it:

```
# List all stacks
aws cloudformation list-stacks \
  --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE \
  --query 'StackSummaries[*].[StackName,StackStatus]' \
  --output table
```

Look for your Spatial Data Management stack (for example, `SpatialDataManagement`). Use this stack name in the following steps by replacing `<STACK-NAME>` with your actual stack name.

#### Step 1: Download New Template
<a name="step-1-download-new-template"></a>

Download the latest CloudFormation template for the new version. For download instructions, see [Step 1: Launch stack](deploy-the-solution.md) in the Deploy the solution section.

#### Step 2: Review Changes
<a name="step-2-review-changes"></a>

Create a change set to preview changes before applying the update. Replace `<CHANGE-SET-NAME>` with a descriptive name based on the version you’re updating to (for example, `update-to-v1-1-0`). Refer to the [Document revisions](revisions.md) section or the version from the downloaded template to determine the appropriate version number.

```
# Create change set to preview changes
aws cloudformation create-change-set \
  --stack-name <STACK-NAME> \
  --change-set-name <CHANGE-SET-NAME> \
  --template-body file://new-template.json \
  --parameters file://current-parameters.json \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM
```

#### Step 3: Review Change Set
<a name="step-3-review-change-set"></a>

```
# Review the change set (use the same change set name from Step 2)
aws cloudformation describe-change-set \
  --stack-name <STACK-NAME> \
  --change-set-name <CHANGE-SET-NAME> \
  --query 'Changes[*].[Type,ResourceChange.Action,ResourceChange.LogicalResourceId,ResourceChange.ResourceType]' \
  --output table
```

#### Step 4: Execute Update
<a name="step-4-execute-update"></a>

```
aws cloudformation execute-change-set \
  --stack-name SpatialDataManagement \
  --change-set-name update-to-v1-1-0
```

#### Step 5: Monitor Update Progress
<a name="step-5-monitor-update-progress"></a>

```
aws cloudformation describe-stack-events \
  --stack-name SpatialDataManagement \
  --query 'StackEvents[*].[Timestamp,ResourceStatus,ResourceType,LogicalResourceId]' \
  --output table
```

## Update Impact by Component
<a name="update-impact-by-component"></a>

### Lambda Functions
<a name="lambda-functions"></a>
+  **Downtime:** Minimal (rolling update)
+  **Impact:** Brief cold start latency increase
+  **Duration:** 2-5 minutes per function

### DynamoDB Tables
<a name="dynamodb-tables"></a>
+  **Downtime:** None (in-place updates)
+  **Impact:** No impact on availability
+  **Duration:** Varies by change type

### API Gateway
<a name="api-gateway"></a>
+  **Downtime:** None (versioned deployments)
+  **Impact:** No impact
+  **Duration:** 1-2 minutes

### OpenSearch Serverless
<a name="opensearch-serverless"></a>
+  **Downtime:** Possible (depends on change)
+  **Impact:** Search functionality may be temporarily unavailable
+  **Duration:** 5-10 minutes for collection updates

### CloudFront Distribution
<a name="cloudfront-distribution"></a>
+  **Downtime:** None
+  **Impact:** Cache invalidation may be needed
+  **Duration:** 15-30 minutes for global propagation

### VPC Changes
<a name="vpc-changes"></a>
+  **Downtime:** Possible (depends on change)
+  **Impact:** Lambda cold starts may increase
+  **Duration:** 5-10 minutes

## Post-Update Validation
<a name="post-update-validation"></a>

### 1. Verify Stack Status
<a name="verify-stack-status"></a>

```
aws cloudformation describe-stacks \
  --stack-name SpatialDataManagement \
  --query 'Stacks[0].StackStatus'
```

Expected: `UPDATE_COMPLETE`

### 2. Test API Functionality
<a name="test-api-functionality"></a>

```
API_ENDPOINT=$(aws cloudformation describe-stacks \
  --stack-name SpatialDataManagement \
  --query 'Stacks[0].Outputs[?OutputKey==`ApiEndpoint`].OutputValue' \
  --output text)

# Test health endpoint
curl $API_ENDPOINT/health

# Test authenticated endpoint (requires token)
curl -H "Authorization: Bearer $TOKEN" $API_ENDPOINT/api/v1/libraries
```

### 3. Check Lambda Function Versions
<a name="check-lambda-function-versions"></a>

```
aws lambda list-functions \
  --query 'Functions[?contains(FunctionName, `SpatialDataManagement`)].[FunctionName,LastModified,State]' \
  --output table
```

## Rollback Procedures
<a name="rollback-procedures"></a>

### Automatic Rollback
<a name="automatic-rollback"></a>

CloudFormation automatically rolls back if update fails. Monitor rollback:

```
aws cloudformation describe-stack-events \
  --stack-name SpatialDataManagement \
  --query 'StackEvents[?contains(ResourceStatus, `ROLLBACK`)]'
```

### Manual Rollback
<a name="manual-rollback"></a>

If you need to manually rollback to previous version:

#### Option 1: Use Previous Template
<a name="option-1-use-previous-template"></a>

```
aws cloudformation update-stack \
  --stack-name SpatialDataManagement \
  --template-body file://current-template.json \
  --parameters file://current-parameters.json \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM
```

## Update Best Practices
<a name="update-best-practices"></a>

### 1. Maintenance Window
<a name="maintenance-window"></a>

Schedule updates during low-usage periods:
+ Notify users in advance
+ Plan for 30-60 minute maintenance window
+ Have rollback plan ready

### 2. Incremental Updates
<a name="incremental-updates"></a>

Update one major version at a time:
+ v1.0 → v1.1 → v1.2 (not v1.0 → v1.2 directly)
+ Review release notes for each version
+ Test each update separately

### 3. Monitoring During Update
<a name="monitoring-during-update"></a>

Set up CloudWatch alarms to monitor:
+ Lambda error rates
+ API Gateway 5xx errors
+ DynamoDB throttling
+ OpenSearch cluster health

### 4. Communication Plan
<a name="communication-plan"></a>
+ Notify stakeholders before update
+ Provide status updates during maintenance
+ Confirm successful completion
+ Document any issues encountered

## Version-Specific Update Notes
<a name="version-specific-update-notes"></a>

Before updating, refer to the [Document revisions](revisions.md) section for version-specific information. Review the release notes to determine if there are any special deployment sequences, breaking changes, or client update requirements for your target version.

## Next Steps
<a name="next-steps"></a>

After successful update:

1. Update monitoring dashboards if needed

1. Document update in change log
