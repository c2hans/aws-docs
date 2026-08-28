---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/elb-logging-enabled.html
---

# elb-logging-enabled
<a name="elb-logging-enabled"></a>

Checks if the Application Load Balancer and the Classic Load Balancer have logging enabled. The rule is NON\_COMPLIANT if the `access_logs.s3.enabled` is false or `access_logs.S3.bucket` is not equal to the s3BucketName that you provided.

**Note**
The rule does not apply to Network Load Balancers or Gateway Load Balancers.

**Identifier:** ELB\_LOGGING\_ENABLED

**Resource Types:** AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

s3BucketNames (Optional)Type: CSV
Comma-separated list of Amazon S3 bucket names for Amazon ELB to deliver the log files.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d797c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
