---
source_url: https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-group.html
---

# Managing a schedule group in EventBridge Scheduler
<a name="managing-schedule-group"></a>

A *schedule group* is an Amazon EventBridge Scheduler resource that you use to organize your schedules.

Your AWS account comes with a `default` scheduler group. You can associate a new schedule with the `default` group or with schedule groups that you create and manage. You can create up to [500 schedule groups](https://docs.aws.amazon.com/scheduler/latest/UserGuide/scheduler-quotas.html) in your AWS account. With EventBridge Scheduler, you organize schedule groups, instead of individual schedules, by applying [tags](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).

A *tag* is a label comprised of a case-sensitive key and a case-sensitive value that you define. You can create tags to categorize schedules by criteria like purpose, owner, or environment. For example, you can identify the environment that your schedules belong to with the following tag: `environment:{{production}}`.

**Important**
Do not add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including billing. Tags are not intended to be used for private or sensitive data.

A schedule group has two possible [states](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_GetScheduleGroup.html#scheduler-GetScheduleGroup-response-State): **ACTIVE** and **DELETING**.

When you first create a group, it is `ACTIVE` by default. You can add schedules to an `ACTIVE` group. When you delete a group, the state changes to `DELETING` until EventBridge Scheduler finishes the deletion of the associated schedules. After EventBridge Scheduler deletes the schedules in the group, the group is no longer available in your account.

Use the following topics to create a schedule group and apply a tag to it. You'll also associate a schedule with the group. Finally, you'll delete the group.

**Topics**
+ [Creating a schedule group in EventBridge Scheduler](managing-schedule-group-create.md)
+ [Deleting a schedule group in EventBridge Scheduler](managing-schedule-group-delete.md)
+ [Related resources](#managing-schedule-group-related-resources)

## Related resources
<a name="managing-schedule-group-related-resources"></a>

 For more information on schedule groups, see the following resources:
+ [CreateScheduleGroup](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_CreateScheduleGroup.html) operation in the *EventBridge Scheduler API Reference*.
+ [DeleteScheduleGroup](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_DeleteScheduleGroup.html) operation in the *EventBridge Scheduler API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge Scheduler. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query scheduler` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
