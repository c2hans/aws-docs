---
source_url: https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/features-and-benefits.html
---

# Features and benefits
<a name="features-and-benefits"></a>

The Cost Optimizer for Amazon WorkSpaces Solution provides the following features:

## Dry run mode
<a name="dry-run-mode"></a>

We recommend that you run this solution in the dry run mode (activated by default) for a few months, review the daily and monthly reports, and manually implement any desired changes. Dry run mode provides insight into how the recommended changes may affect your WorkSpaces costs. This mode also allows you to evaluate and analyze the solution’s recommendations without the solution automatically implementing billing changes. When you are comfortable with the recommendations provided by the solution and would like these recommendations to be automatically implemented, change the template parameter **Dry Run Mode** to `No`. The solution will then begin to automatically implement future billing changes based on the recommendations provided in its daily and monthly reports.

## Automatic billing conversion
<a name="automatic-billing-conversion"></a>

When the **Dry Run Mode** parameter is set to `No`, the solution converts a WorkSpace to monthly or hourly billing model, depending on the WorkSpace utilization for the given month. If WorkSpace utilization exceeds the usage threshold, the billing model changes to monthly on the day the utilization exceeds the threshold. The conversion from monthly to hourly mode happens on the last day of the month. If WorkSpace utilization for the month was lesser than or equal to usage threshold, the billing model changes to hourly on the last day of the month.

### Hourly to monthly
<a name="hourly-to-monthly"></a>

This solution calculates the hourly WorkSpace usage for each WorkSpace once per day, right before midnight GMT. This calculation includes that day’s usage. When the **Dry Run Mode** parameter is set to `No`, the solution automatically converts individual WorkSpaces from an hourly billing model to a monthly billing model if the WorkSpace exceeds an hourly usage threshold for that WorkSpace type.

**Important**
The solution is designed to calculate the hourly WorkSpace usage once per day. Do not manually trigger the ECS task multiple times per day or modify the EventBridge rule schedule, as this will result in inaccurate billable hours calculations and incorrect WorkSpace billing mode conversions.

By default, the threshold is set close to the hourly and monthly billing break-even point. However, you can use the solution’s hub template parameters to change the threshold for when each WorkSpace converts from hourly to monthly billing.

**Note**
Because the solution cannot convert WorkSpaces before the calculation at midnight, the default configuration may result in some WorkSpaces exceeding the threshold for up to 24 hours. For example, the default threshold for a Standard instance is set to `85`. If, at midnight on Monday, your usage is `84`, the WorkSpace will not be converted to monthly billing. If the usage exceeds `85` after midnight on Monday, the WorkSpace will not be converted until the calculation at midnight on Tuesday.
If several of your WorkSpaces consistently exceed the threshold before being converted, consider lowering the threshold. If several of your WorkSpaces are prematurely converted before exceeding the threshold, consider raising the threshold.
To mitigate this potential discrepancy, we recommend carefully monitoring your usage using dry run mode and adjusting the threshold to your needs before setting the **Dry Run Mode** parameter to `No`.

Once the solution converts a WorkSpace from hourly billing to monthly billing, the solution will not convert the WorkSpace back to hourly billing until the beginning of the next month, if usage was below the monthly usage threshold. However, you can manually change the billing model at any time using the [AWS Management Console](https://console.aws.amazon.com/console/).

### Monthly to hourly
<a name="monthly-to-hourly"></a>

For customers who want to convert WorkSpaces from monthly billing to hourly billing immediately, the solution’s CloudFormation template includes a parameter (**Simulate End of Month**) that will run these conversions at the time of deployment.

## Unused WorkSpaces termination
<a name="terminate-unused-workspaces"></a>

**Important**
Don’t set the parameters **Simulate End of Month Cleanup** and **Terminate workspaces not used for a month** to `Yes` at the same time. Doing this will unexpectedly terminate WorkSpaces.
The **Simulate End of Month Cleanup** parameter will run the solution as if it’s the last day of the month and then terminate WorkSpaces unexpectedly. To use the **Terminate unused WorkSpaces** feature, set **Simulate End of Month Cleanup** to `No`.

The solution provides a feature to terminate unused WorkSpaces permanently. The solution automatically identifies and excludes [standby workspaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/multi-region-resilience.html) from termination to preserve disaster recovery capabilities. Standby workspaces are backup workspaces associated with primary workspaces for disaster recovery purposes and are never terminated regardless of usage patterns. By default, this feature is set to `No`, and you can allow this by selecting `Yes` or `Dry Run` for the input parameter **Terminate Unused WorkSpaces**.

You can use the input parameter **Number of months for termination check** to set the duration for the unused period. For example, if you select a value of two months, the solution will select the WorkSpaces that were unused for two months for termination.

**Note**
Opting into this feature terminates unused WorkSpaces and can cause changes to your existing CloudFormation stack. Changes to existing CloudFormation resources might cause a drift between the resource state and its definition in the stack. Ensure that these changes do not impact your existing resources and applications before opting into this feature.

For a WorkSpace to be eligible for termination, it needs to meet the following criteria:
+ The WorkSpace must be a primary WorkSpace (standby workspaces are automatically excluded)
+ The WorkSpace is available from the first day of the unused period that you set.
+ The **LastKnownUserConnectionTimestamp**, which indicates the last time a user logged into the WorkSpace, is earlier than the first day of the unused period that you set.
+ The **Launch in Dry Run Mode** input parameter is set to `No`.

If this criteria is met, the WorkSpace will be eligible for termination. Then the solution checks for the following options for the parameter **Terminate Unused Workspaces**:
+  **Yes** - You can opt into this feature by selecting `Yes` for the **Terminate Unused Workspaces** input parameter. If opted in, the solution will identify all the WorkSpaces not used during the user-defined period based on the last known user connection timestamp. The solution will only terminate the WorkSpace if it met previously listed criteria
+  **Dry Run** - When you select `Dry Run` for the **Terminate Unused Workspaces** input parameter, the solution checks for all the conditions for a WorkSpace to be terminated and update the report, but it won’t terminate the WorkSpace. The generated report will be marked as `Yes- Dry Run` for the WorkSpace.

**Note**
We recommend running this feature in Dry Run mode for the first few months and checking the monthly reports to review which WorkSpaces are marked for deletion. The reports will show WorkspaceType as PRIMARY or STANDBY to help you understand which workspaces are being evaluated.
+  **No** - By default, the option is turned off (set to `No`). The WorkSpace will not be terminated and the report will not have any entry for this WorkSpace.

This check for terminating unused WorkSpaces will run only on the last day of the month or if the customers select `Yes` for the parameter **Simulate End of Month Cleanup.**

## Opt out WorkSpaces
<a name="opt-out-workspaces"></a>

To prevent the solution from converting a WorkSpace between billing models or terminating it as an unused WorkSpace, apply a resource tag to the WorkSpace using the tag key `Skip_Convert` and any tag value. This solution will log tagged WorkSpaces, but it will not convert or terminate the tagged WorkSpaces. Remove the tag at any time to resume automatic conversion and termination check for that WorkSpace.

## Opt in Regions
<a name="opt-in-regions"></a>

This solution provides the **List of AWS Regions** input parameter, which specifies the AWS Regions monitored by the solution. You can provide a comma-separated list of AWS Regions that you want to monitor. If this input parameter is left blank, the solution will default to monitoring WorkSpaces in all the AWS Regions for the account.

## Deployment in an existing Amazon VPC
<a name="deployment-to-existing-vpc"></a>

This solution creates a new [Amazon Virtual Private Cloud (Amazon VPC)](https://aws.amazon.com/vpc/) to run the Amazon ECS task. If desired, you can deploy the solution in an existing Amazon VPC by providing the subnet IDs and security group ID as part of the input parameters to the CloudFormation template. To run the solution in an existing Amazon VPC, the Amazon ECS task needs to run in a public subnet, or a private subnet with a route to the Internet. This route is necessary because the Amazon ECS task will pull the Docker image hosted in a public [Amazon Elastic Container Registry (Amazon ECR)](https://aws.amazon.com/ecr/) repository. The security group used to run the ECS task will allow you to pull this image from ECR repository. To deploy the solution in an existing VPC select `No`for the input parameter **Create New VPC**. Provide the details for you existing VPC in the input section **Existing VPC settings**. Do not change the default values for the section **New VPC Settings**.

**Note**
In order for the solution to be deployed to a PUBLIC SUBNET, the subnet itself has to have auto-assign public IPs enabled.

## Maintenance calculation
<a name="maintenance-calculation"></a>

If you run your patches or other maintenance scripts by changing the WorkSpaces to `ALWAYS_ON` mode, you will need to account for the `ALWAYS_ON` hours and adjust the threshold values in the CloudFormation template accordingly. For example, if you change the mode from `AUTO_STOP` to `ALWAYS_ON` for 10 hours to run the maintenance scripts, you should subtract 10 hours from the set threshold value in the CloudFormation template.

The solution automatically accounts for default AWS maintenance activities on AUTO\_STOP workspaces when maintenance mode is enabled in the directory. For directories with maintenance mode enabled, the solution adds one hour of usage to AUTO\_STOP workspaces at the end of each month to account for maintenance windows.
