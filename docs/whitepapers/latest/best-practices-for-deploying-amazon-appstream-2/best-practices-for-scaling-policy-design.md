---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/best-practices-for-scaling-policy-design.html
---

# Best practices for scaling policy design
<a name="best-practices-for-scaling-policy-design"></a>

## Combine scaling policies
<a name="combine-scaling-policies"></a>

 Many customers choose to combine different types of scaling policies in a single fleet to increase the power and flexibility of Auto Scaling in WorkSpaces Applications. For example, you might configure a scheduled scaling policy to increase your fleet minimum at 6:00 AM in anticipation of users starting their work day, and to decrease the fleet minimum at 4:00 PM before users stop working. You can combine this scheduled scaling policy with target tracking or step scaling policies to maintain a specific level of utilization and scale-in or -out during the day to handle spiky usage. The combination of scheduled scaling and target tracking scaling can help reduce the impact of a sharp increase in utilization levels when capacity is needed immediately.

## Avoid scaling churn
<a name="avoid-scaling-churn"></a>

 Consider whether your fleet might experience a high degree of churn due to your use case. Churn occurs when a large number of users start and then end sessions in a short period of time. This might occur when many users simultaneously access an application in your fleet for just a few minutes before signing off.

 In such situations, your fleet size may drop far below the desired capacity, as instances are ended when users end their sessions. Step scaling policies may not add instances quickly enough to offset churn and, as a result, your fleet gets stuck at a certain size.

 You can identify churn by examining CloudWatch metrics for your fleet. Periods of time when your fleet has non-zero pending capacity without change (or with very little change) in desired capacity indicate that high churn is likely occurring. To account for high churn situations, use target tracking scaling policies and pick a target utilization so that (100 – target utilization percent) is more than churn rate in a 15-minute period. For example, if 10% of your fleet will be ended in a 15-minute period due to user turnover, set a capacity utilization target of 90% or less to offset high churn.

## Understand maximum provisioning rate
<a name="understand-maximum-provisioning-rate"></a>

 Customers who are managing WorkSpaces Applications fleets for a large number of users should consider provisioning rate limits. This limit will impact how quickly instances can be added to a fleet or across all fleets within an AWS account.

 There are two limits to consider:
+  For a single fleet, WorkSpaces Applications provisions at a maximum rate of 20 instances per minute.
+  For a single AWS account, WorkSpaces Applications provisions at a rate of rate of 60 instances per minute (with a burst of 100 instances per minute).

 If more than three fleets are scaled up in parallel, the account provisioning rate limit is shared across these fleets (for example, six fleets scaling in parallel could each provision up to 10 instances per minute). In addition, consider the amount of time for a given streaming instance to finish provisioning in response to a scaling event. For fleets not joined to an Active Directory domain, this is typically 15 minutes. For fleets joined to an Active Directory domain, this can take as long as 25 minutes.

 Given those constraints, consider the following examples:
+  If you want to scale a single fleet from 0 to 1000 instances, it will take 50 minutes (1000 instances/20 instances per minute) for provisioning to complete, and then an additional 15-25 minutes for all instances to become available for end users, for a total of 65-75 minutes.
+  If you want to simultaneously scale three fleets from 0 to 333 instances (for a total of 999 instances in the AWS account), it will take approximately 17 minutes (999/60 instances per minute) for all fleets to complete provisioning and then an additional 15 minutes for those instances to become available for end users, for a total of 32-42 minutes.

## Utilize multiple Availability Zones
<a name="utilize-multiple-availability-zones"></a>

 Choose multiple AZs in the Region for your fleet deployment. When you select multiple AZs for your fleet, you increase the likelihood that your fleet will be able to add instances in response to a scaling event. The CloudWatch metric PendingCapacity is a starting point to assess how optimized the fleet AZ design is in large fleet deployments. A high, sustained value for PendingCapacity can indicate a need to extend horizontal (across AZs) scaling. For more information, refer to [*Monitoring Amazon WorkSpaces Applications Resources*](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring.html).

 For example, if auto scaling attempts to provision instances to increase the size of your fleet and the selected AZ has insufficient capacity, auto scaling will instead add instances in the other AZs which you’ve specified for your fleet. For more information about Availability Zones and WorkSpaces Applications design, refer to [**Availability Zones**](availability-zones.md) in this document.

## Monitor Insufficient Capacity Error metrics
<a name="monitor-insufficient-capacity-error-metrics"></a>

 “Insufficient Capacity Error” is a CloudWatch metric for WorkSpaces Applications fleets. This metric specifies the number of session requests rejected due to lack of capacity.

 When you make changes to your scaling policies, it is helpful to create a CloudWatch alarm to notify you when any Insufficient Capacity Errors occur. This enables you to quickly adjust your scaling policies to optimize availability for users. The administration guide gives detailed steps to [*monitor your WorkSpaces Applications resources*](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
