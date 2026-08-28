---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-cfn-cmf-health-check.html
---

# Monitor a Deadline Cloud customer-managed fleet health check with CloudFormation
<a name="examples-cfn-cmf-health-check"></a>

The [cmf\_templates](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cmf_templates) directory in the samples repository includes a `deadline-fleet-health-check.yaml` CloudFormation template that sets up continuous health check monitoring for a single Deadline Cloud customer-managed fleet with auto scaling. The template creates a Lambda function, an EventBridge rule, and a CloudWatch alarm that you can configure with an SNS topic.

To deploy the template, you need:
+ A Deadline Cloud farm and customer-managed fleet. Copy the Farm ID, Fleet ID, and Fleet Name from the fleet details page in the Deadline Cloud management console.
+ An EC2 Auto Scaling group that scales the fleet. Copy the Auto Scaling group name from the EC2 Auto Scaling console.
+ An SNS topic and subscription for the health check alarm. Copy the SNS topic ARN.

For more information about customer-managed fleet auto scaling, see [Create fleet infrastructure with an Amazon EC2 Auto Scaling group](create-auto-scaling.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
