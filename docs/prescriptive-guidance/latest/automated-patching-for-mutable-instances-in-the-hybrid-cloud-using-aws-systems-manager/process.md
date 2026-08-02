---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automated-patching-for-mutable-instances-in-the-hybrid-cloud-using-aws-systems-manager/process.html
---

# Patching process
<a name="process"></a>

The primary users of the patching solution are the application development and operations teams. Each application is typically deployed into multiple environments, such as development, test (integration, user acceptance, and so on), and production. The application teams have to plan the patching schedules for each environment, so when a patch is applied to the production environment, it has already been tested and determined to have no adverse effects on the application.

The following workflow provides an example of how you can plan patching windows for an application that is deployed in multiple environments and how to configure tags.

![Patch management workflow.](http://docs.aws.amazon.com/prescriptive-guidance/latest/automated-patching-for-mutable-instances-in-the-hybrid-cloud-using-aws-systems-manager/images/guide-img/9c36bc8c-880d-42f7-8b76-ddf8e3d52477/images/3739bffc-e0da-4a24-bd33-7d5755072707.png)

+ **Step 1.** Each application team plans their maintenance windows for their servers within various environments, and sets up the tags that represent the servers' patch groups and maintenance windows accordingly:
  + The **Patch Group** tag represents the servers within an application environment that are the targets of a specific patch baseline. Patch groups help ensure that the right patch baselines are deployed to the correct set of instances. Patch groups also help avoid deploying patches in the production environment before they have been adequately tested.
  + If the application servers include multiple operating systems, the application team creates patch groups based on the combination of the environment and operating system. A patch group can be registered with only one patch baseline, and an instance can be part of only one patch group.

    For example: `appname-DEV-WIN` and `appname-DEV-RHEL`
  + The **Maintenance Window** tag represents the schedule for patching the servers. **All servers in a patch group should be in the same maintenance window.** The maintenance window tag should follow a consistent format for cron and rate expressions so that a Lambda function that you define can parse the expressions easily. (In this guide, we'll refer to this Lambda function as `automate-patch`.)

    For example: `schedule-duration-cutoff-timezone`

    `cron(0 2 ? * SAT#3 *)` represents 02:00 AM on the third Saturday of every month. For detailed information about cron and rate expressions, see the [Systems Manager documentation](https://docs.aws.amazon.com/systems-manager/latest/userguide/reference-cron-and-rate-expressions.html).
+ **Step 2.** Systems Manager Patch Manager makes new patches available regularly through operating system-specific patch baselines based on the configurations defined.
  + For each operating system, you can define a custom patch baseline that includes the approval rules and the patches that need to be applied to the instances across the cloud environment.
+ **Step 3.** Your custom automation code configures Patch Manager to set up patching based on the **Patch Group** and **Maintenance Window** tags, and applies the patches to the development environment.
  + After patching is complete, the application development and support teams test the application and verify that everything works correctly.
  + If the application encounters any problems with the new patch, application teams ask the cloud services team to halt patching to other patch groups and other environments, by either disabling the maintenance windows or deregistering the patch task execution.
+ **Step 4.** After the development environment is patched successfully, patching is deployed to any other non-production environments. As with the development environment, the application is tested and verified to be working correctly in all non-production environments. If there are any issues, application teams ask the cloud services team to halt patching to the production environment.
+ **Step 5.** After all the non-production environments have been patched successfully, patching is applied to the production environment.
