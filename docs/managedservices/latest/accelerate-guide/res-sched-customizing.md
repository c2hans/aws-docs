---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/res-sched-customizing.html
---

# Customizing AMS Resource Scheduler
<a name="res-sched-customizing"></a>

When onboarded, AMS Resource Scheduler is deployed as a CloudFormation stack, with name `ams-resource-scheduler`, in the primary AWS region for your AMS Accelerate account. You can configure the properties of AMS Resource Scheduler based on your preferences through CloudFormation stack parameters and performing a stack update. For information on updating CloudFormation stacks, see [Updating stacks directly](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-direct.html).

We recommend you customize the following properties and leave the rest at default for optimal functionality.
+ **Tag name**: The name of the tag that Resource Scheduler will use to associate instance schedules with resources. The default value is `Schedule`.
+ **Service(s) to schedule**: A comma-separated list of services that Resource Scheduler can manage. The default value is "`ec2,rds,autoscaling`". Valid values are "ec2", "rds" and "autoscaling".
+ **Default time zone**:Specify the default time zone for the Resource Scheduler to use. The default value is `UTC`.
+ **CMK for encrypted EBS volumes**: A comma-separated list of Amazon KMS Customer Managed Key (CMK) ARNs that Resource Scheduler can be granted permissions to.
+ **License manager license for EC2 instance**: A comma-separated list of AWS Licence Manager ARNs to that Resource Scheduler can be granted permissions to.

**Note**
AMS occasionally releases features and fixes to keep AMS Resource Scheduler up to date in your account. When this happens, any customization that you make to the AMS Resource Scheduler stack via stack parameters are preserved.
We strongly recommend against making any customization directly to any of the component resource of AMS Resource Scheduler. Doing so impacts Resource Scheduler functionality and AMS’s ability to keep it up to date.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
