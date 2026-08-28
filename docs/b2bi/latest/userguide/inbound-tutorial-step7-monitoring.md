---
source_url: https://docs.aws.amazon.com/b2bi/latest/userguide/inbound-tutorial-step7-monitoring.html
---

# Step 7: Monitor your inbound workflow
<a name="inbound-tutorial-step7-monitoring"></a>

Monitoring helps you track transformation success, identify issues, and maintain operational visibility for your inbound EDI processing. AWS B2B Data Interchange integrates with CloudWatch and EventBridge for comprehensive monitoring.

## Check CloudWatch logs
<a name="inbound-cloudwatch-monitoring"></a>

**To review transformation logs**

1. Open the CloudWatch console.

1. Navigate to **Log groups**.

1. Find the log group named `/aws/vendedlogs/b2bi/p-{{your-profile-id}}`.

1. Review transformation logs for success/failure status.

## Set up EventBridge monitoring (optional)
<a name="inbound-eventbridge-monitoring"></a>

**To configure event notifications**

1. Open the EventBridge console.

1. Create a rule to capture AWS B2B Data Interchange events.

1. Configure notifications for transformation completion.

## Monitor Amazon S3 directories
<a name="inbound-s3-monitoring"></a>
+ Regularly check input directories for processing status
+ Monitor output directories for transformed files
+ Review any error files that may appear

## Monitoring points
<a name="inbound-monitoring-points"></a>
+ Transformation success/failure rates
+ Processing time for documents
+ Error patterns and frequencies
+ Amazon S3 storage usage

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
