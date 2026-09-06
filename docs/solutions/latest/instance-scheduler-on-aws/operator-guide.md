---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/operator-guide.html
---

# Operator guide
<a name="operator-guide"></a>

This guide is intended for users and operators of this solution and contains details on how to [configure schedules](#configure-schedules) and [monitor the solution](monitor-the-solution.md).

## Configure schedules
<a name="configure-schedules"></a>

**Important**
Misconfigured schedules can result in instances running continuously and incurring unexpected costs. Before applying schedules to your resources, verify the following:
The schedule name in the resource tag exactly matches a schedule defined in the configuration table. Misspelled or nonexistent schedule names will result in an `UnknownSchedule` error and the instance will not be stopped by the scheduler. Check for the `IS-Error` tag on your resources to identify this condition.
If `stop_new_instances` is set to `false`, instances that are running outside of a scheduled period when first tagged will not be stopped until the next scheduled stop transition. This can result in instances running longer than expected.
If `retain_running` is set to `true`, instances that are manually started before a running period begins will not be stopped at the end of that period. This is by design, but can lead to instances running indefinitely if not monitored.
When using `enforced: false` (the default), the scheduler will not restart instances that are manually stopped during a running period, and will not stop instances that are manually started outside of a running period after the initial stop transition.
We recommend enabling [informational tagging](monitor-the-solution.md#informational-tags) (enabled by default) and periodically reviewing the `IS-Error` and `IS-LastAction` tags on your resources to confirm that scheduling is operating as expected.

Once the solution has been successfully deployed, you can begin to configure schedules. Instance Scheduler on AWS supports two methods of managing schedules as described below.

**Note**
The solution can support any number of schedules, each of which can contain one or more periods that define when instances controlled by that schedule should be running. For more information, refer to [Schedules](scheduler-cli.md) and [Periods](period-reference.md).

### Using Infrastructure as Code (recommended)
<a name="using-infrastructure-as-code-recommended"></a>

Instance Scheduler on AWS provides an AWS CloudFormation CustomResource that you can use to manage your schedules and periods using Infrastructure as Code (IaC).

For information on how to manage schedules using IaC, please refer to [Manage Schedules Using Infrastructure as Code (IaC)](manage-schedules-using-infrastructure-as-code-iac.md).

### Using the Amazon DynamoDB Console and Instance Scheduler on AWS CLI
<a name="using-the-amazon-dynamodb-console-and-instance-scheduler-on-aws-cli"></a>

**Important**
If you used the custom resource to manage any schedules using IaC, you must not use the DynamoDB console or scheduler CLI to delete or modify those schedules or their periods. If you do, you will create a conflict between the stored parameters in CloudFormation and the values in the table. Also, do not use periods managed by CloudFormation in schedules created using the DynamoDB console or the scheduler CLI.

When deploying the Instance Scheduler on AWS hub stack, the solution created an Amazon DynamoDB table containing several sample periods and schedules that you can use as a reference to create your own custom periods and schedules. To create a schedule in DynamoDB, modify one of the schedules in the configuration table (ConfigTable) or create a new one. To create a schedule using the CLI, first [Install the Scheduler CLI](scheduler-cli-4.md#install-the-scheduler-cli) and then use the [Available commands](scheduler-cli-4.md#available-commands).

**Note**
For examples of how to create several sample schedules using IaC, DynamoDB, and the InstanceScheduler CLI, please refer to [Sample schedules](sample-schedules.md).

This section provides instruction and reference on how to use, monitor and update the solution as well as troubleshooting and support information.

## Tag instances for scheduling
<a name="tag-instances-for-scheduling"></a>

When you deployed the AWS CloudFormation template, you defined the name (tag key) for the solution’s *custom tag*. For Instance Scheduler on AWS to recognize an Amazon EC2 or Amazon RDS instance, the tag key on that instance must match this custom tag key. Therefore, it is important that you apply tags consistently and correctly to all applicable instances. You can continue to use existing [tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) for your instances while using this solution. For more information, refer to [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) and [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html).

On the AWS Management Console, use the [Tag Editor](https://console.aws.amazon.com/resource-groups/tag-editor/) to apply or modify tags for multiple resources at a time. You can also apply and modify tags manually in the console.

Shortly after tagging a resource, an IS-ManagedBy tag will be applied to the resource by Instance Scheduler to indicate that the resource is now being managed by the scheduler. You can look for this tag to confirm that the resource has been correctly registered for scheduling.

**Note**
For Auto Scaling groups specifically, this also applies if the schedule tag is already present at creation time, such as when the group is created through AWS CloudFormation, Terraform, the AWS CDK, or the AWS CLI/SDK. Instance Scheduler detects the new group and registers it for scheduling without requiring you to re-apply the tag afterward.

### Setting the tag value
<a name="setting-the-tag-value"></a>

When you apply a tag to an instance, use the tag key you defined during initial configuration (by default the tag key is Schedule) and set the tag value to the name of the schedule that should apply to the instance. If you would like to change the tag key, you can do so by [updating the solution parameters](update-the-solution.md).

**Note**
For Amazon RDS instances, the tag value can be from 1 to 256 Unicode characters in length and cannot be prefixed with aws:. The string can contain only the set of Unicode letters, digits, white-space, '\_', '.', '/', '=', '', '-' (Java regex: "^([\\\\p{L}\\\\p{Z}\\\\p{N}\_.:/=\\\\-]\*)$"). For more information, refer to [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html).

### EC2 instances with encrypted EBS volumes
<a name="ec2-instances-with-encrypted-ebs-volumes"></a>

If your EC2 DB instances have EBS volumes encrypted with customer-managed KMS keys, you must give the Instance Scheduler role the KMS:CreateGrant permission to be able to start those instances. For more information, refer to [Encrypted EC2 EBS Volumes](security-1.md#encrypted-ec2-ebs-volumes).

### EC2 instances managed in License Manager
<a name="ec2-instances-managed-in-license-manager"></a>

If your EC2 instances are managed in AWS License Manager, you must give the Instance Scheduler role the appropriate License Manager permissions to be able to start and stop those instances. For more information, refer to [EC2 License Manager](security-1.md#ec2-license-manager).
