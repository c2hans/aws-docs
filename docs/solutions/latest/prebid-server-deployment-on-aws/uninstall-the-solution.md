---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

## Using the destroy script (Recommended)
<a name="using-the-destroy-script"></a>

The solution provides a `destroy.sh` script that automates the cleanup process and handles stack dependencies correctly.

### Basic usage
<a name="basic-usage"></a>

Run the destroy script from the solution root directory:

```
./destroy.sh --profile <your-aws-cli-profile> --region <your-region>
```

The script automatically:
+ Detects which stacks are deployed (Prebid Server, Bidder Simulator)
+ Deletes the RTB Fabric Link before stack destruction (avoids dependency conflicts)
+ Destroys stacks in the correct order (Prebid Server first, then Bidder Simulator)
+ Provides confirmation prompts before deletion

### RTB Fabric Link cleanup
<a name="fabric-link-cleanup"></a>

Before destroying CloudFormation stacks, `destroy.sh` automatically invokes `deployment/simulator-fabric-link.sh delete` to remove the RTB Fabric Link. This step is necessary because the Fabric Link must be deleted before the Requester Gateway (which is part of the PrebidServerStack) can be destroyed. Deleting the link first avoids CloudFormation dependency conflicts during stack teardown.

The cleanup step:

1. Reads the Fabric Link ID from the SSM Parameter Store (`/{stack-name}/fabric-link/link-id`)

1. Calls the RTB Fabric DeleteLink API to remove the link

1. Deletes the SSM parameter

If the automatic Fabric Link cleanup fails (for example, if the link was already deleted manually or the SSM parameter does not exist), the script prints a warning and continues with stack destruction. This ensures that `destroy.sh` does not halt on transient errors or previously cleaned-up resources.

### Preview mode
<a name="preview-mode"></a>

To see what would be destroyed without actually deleting resources:

```
./destroy.sh --dry-run --profile <your-aws-cli-profile> --region <your-region>
```

### Additional options
<a name="additional-options"></a>

For all available options and usage details:

```
./destroy.sh --help
```

You can uninstall the Guidance for Deploying a Prebid Server on AWS solution from the AWS Management Console or by using the AWS Command Line Interface.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. On the **Stacks** page, select this solution’s installation stack.

1. Choose **Delete**.

## Using AWS Cloud Development Kit (AWS CDK)
<a name="using-aws-cdk"></a>

Run blow command from the root of the project directory

```
$ cdk destroy
```

## Deleting the Amazon S3 buckets
<a name="deleting-the-amazon-s3-buckets"></a>

To prevent accidental data loss, this solution is configured to retain the solution-created Amazon S3 buckets when you delete its AWS CloudFormation stack. After uninstalling the solution, you can manually delete the S3 buckets if you do not need to retain their data. Each stack contains the following seven S3 buckets:
+  `ALBAccessLogsBucket`
+  `ArtifactsBucket`
+  `CloudFrontAccessLogsBucket`
+  `DockerConfigsBucket`
+  `DataSyncMetricsBucket`
+  `MetricsEtlBucket`
+  `CloudTrailLoggingBucket`

Follow these steps to delete each Amazon S3 bucket.

1. Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3/home).

1. Choose **Buckets** from the left navigation pane.

1. Locate the S3 buckets whose name begins with prefix, ` <stack-name> `.

1. For each S3 bucket, select the bucket then choose **Empty** then **Delete**.

To delete the S3 bucket using AWS CLI, run the following command:

```
$ aws s3 rb s3://<bucket-name> --force
```

## Cleaning up orphaned RTB Fabric resources
<a name="cleaning-up-orphaned-rtb-fabric-resources"></a>

In rare cases, RTB Fabric resources may become orphaned if the automatic cleanup fails or if a stack deletion is interrupted. This can happen when:
+ A Fabric Link is stuck in `PENDING` state (known issue)
+ The `destroy.sh` script’s automatic link deletion step fails and the subsequent stack deletion also fails due to dependency conflicts
+ A stack deletion is manually cancelled or times out

### Identifying orphaned resources
<a name="identifying-orphaned-resources"></a>

Check for orphaned Fabric Links by listing links associated with your Requester Gateway:

```
aws rtbfabric list-links --gateway-id <requester-gateway-id> \
    --profile <your-profile> --region <your-region>
```

Check for orphaned SSM parameters:

```
aws ssm get-parameter \
    --name "/<stack-name>/fabric-link/link-id" \
    --profile <your-profile> --region <your-region>
```

### Manually deleting a Fabric Link
<a name="manually-deleting-a-fabric-link"></a>

If a Fabric Link exists but was not cleaned up automatically, delete it manually:

```
# Get the link ID from SSM (if still present)
LINK_ID=$(aws ssm get-parameter \
    --name "/prebid-server-deployment-on-aws/fabric-link/link-id" \
    --query "Parameter.Value" --output text \
    --profile <your-profile> --region <your-region>)

# Delete the Fabric Link
aws rtbfabric delete-link --link-id "$LINK_ID" \
    --profile <your-profile> --region <your-region>

# Delete the SSM parameter
aws ssm delete-parameter \
    --name "/prebid-server-deployment-on-aws/fabric-link/link-id" \
    --profile <your-profile> --region <your-region>
```

If the link is stuck in `PENDING` state and the `delete-link` command fails, wait a few minutes and retry. Links in `PENDING` state may take time to become deletable.

### Retrying stack deletion after manual cleanup
<a name="retrying-stack-deletion"></a>

After manually removing the Fabric Link, retry the stack deletion:

```
aws cloudformation delete-stack \
    --stack-name prebid-server-deployment-on-aws \
    --profile <your-profile> --region <your-region>

aws cloudformation wait stack-delete-complete \
    --stack-name prebid-server-deployment-on-aws \
    --profile <your-profile> --region <your-region>
```

Alternatively, re-run `destroy.sh` which will detect the remaining stacks and attempt deletion again.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
