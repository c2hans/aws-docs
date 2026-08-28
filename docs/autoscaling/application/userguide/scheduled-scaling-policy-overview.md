---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/scheduled-scaling-policy-overview.html
---

# How scheduled scaling for Application Auto Scaling works
<a name="scheduled-scaling-policy-overview"></a>

This topic describes how scheduled scaling works and introduces the key considerations you need to understand to use it effectively.

**Topics**
+ [How it works](#scheduled-scaling-how-it-works)
+ [Considerations](#scheduled-scaling-considerations)
+ [Commonly used commands](#scheduled-scaling-commonly-used-commands)
+ [Related resources](#step-scaling-related-resources)
+ [Limitations](#scheduled-scaling-limitations)

## How it works
<a name="scheduled-scaling-how-it-works"></a>

To use scheduled scaling, create *scheduled actions*, which tell Application Auto Scaling to perform scaling activities at specific times. When you create a scheduled action, you specify the scalable target, when the scaling activity should occur, a minimum capacity, and a maximum capacity. You can create scheduled actions that scale one time only or that scale on a recurring schedule.

At the specified time, Application Auto Scaling scales based on the new capacity values, by comparing current capacity to the specified minimum and maximum capacity.
+ If current capacity is less than the specified minimum capacity, Application Auto Scaling scales out (increases capacity) to the specified minimum capacity.
+ If current capacity is greater than the specified maximum capacity, Application Auto Scaling scales in (decreases capacity) to the specified maximum capacity.

## Considerations
<a name="scheduled-scaling-considerations"></a>

When you create a scheduled action, keep the following in mind:
+ A scheduled action sets the `MinCapacity` and `MaxCapacity` to what is specified by the scheduled action at the date and time specified. The request can optionally include only one of these sizes. For example, you can create a scheduled action with only the minimum capacity specified. In some cases, however, you must include both sizes to ensure that the new minimum capacity is not greater than the maximum capacity, or the new maximum capacity is not less than the minimum capacity.
+ By default, the recurring schedules that you set are in Coordinated Universal Time (UTC). You can change the time zone to correspond to your local time zone or a time zone for another part of your network. When you specify a time zone that observes daylight saving time, the action automatically adjusts for Daylight Saving Time (DST). For more information, see [Schedule recurring scaling actions using Application Auto Scaling](scheduled-scaling-using-cron-expressions.md).
+ You can temporarily turn off scheduled scaling for a scalable target. This helps you prevent scheduled actions from being active without having to delete them. You can then resume scheduled scaling when you want to use it again. For more information, see [Suspend and resume scaling for Application Auto Scaling](application-auto-scaling-suspend-resume-scaling.md).
+ The order in which scheduled actions run is guaranteed for the same scalable target, but not for scheduled actions across scalable targets.
+ To complete a scheduled action successfully, the specified resource must be in a scalable state in the target service. If it isn't, the request fails and returns an error message, for example, `Resource Id [ActualResourceId] is not scalable. Reason: The status of all DB instances must be 'available' or 'incompatible-parameters'`.
+ Due to the distributed nature of Application Auto Scaling and the target services, the delay between the time the scheduled action is triggered and the time the target service honors the scaling action might be a few seconds. Because scheduled actions are run in the order that they are specified, scheduled actions with start times close to each other can take longer to run.

## Commonly used commands for scheduled action creation, management, and deletion
<a name="scheduled-scaling-commonly-used-commands"></a>

The commonly used commands for working with schedule scaling include:
+ [register-scalable-target](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/register-scalable-target.html) to register AWS or custom resources as scalable targets (a resource that Application Auto Scaling can scale), and to suspend and resume scaling.
+ [put-scheduled-action](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/put-scheduled-action.html) to add or modify scheduled actions for an existing scalable target.
+  [describe-scaling-activities](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/describe-scaling-activities.html) to return information about scaling activities in an AWS Region.
+ [describe-scheduled-actions](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/describe-scheduled-actions.html) to return information about scheduled actions in an AWS Region.
+ [delete-scheduled-action](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/delete-scheduled-action.html) to delete a scheduled action.

## Related resources
<a name="step-scaling-related-resources"></a>

For a detailed example of using scheduled scaling, see the blog post [Scheduling AWS Lambda Provisioned Concurrency for recurring peak usage](https://aws.amazon.com/blogs/compute/scheduling-aws-lambda-provisioned-concurrency-for-recurring-peak-usage/) on the AWS Compute Blog.

For information about creating scheduled actions for Auto Scaling groups, see [Scheduled scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Limitations
<a name="scheduled-scaling-limitations"></a>

The following are limitations when using scheduled scaling:
+ The names of scheduled actions must be unique per scalable target.
+ Application Auto Scaling doesn't provide second-level precision in schedule expressions. The finest resolution using a cron expression is 1 minute.
+ The scalable target can't be an Amazon MSK cluster. Scheduled scaling is not supported for Amazon MSK.
+ Console access to view, add, update, or remove scheduled actions on scalable resources depends on the resource that you use. For more information, see [AWS services that you can use with Application Auto Scaling](integrated-services-list.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
