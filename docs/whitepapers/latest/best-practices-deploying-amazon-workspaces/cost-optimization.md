---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/cost-optimization.html
---

# Cost optimization
<a name="cost-optimization"></a>

## Self-service WorkSpace management capabilities
<a name="self-service-workspace-management-capabilities"></a>

 In Amazon WorkSpaces, self-service WorkSpace management capabilities can be enabled for users to provide them with more control over their experience. Allowing users self-service capability can reduce your IT support staff workload for Amazon WorkSpaces. When self-service capabilities are enabled, it allows users to perform one or more of the following tasks directly from their Windows, macOS, or Linux client for Amazon WorkSpaces:
+  Cache their credentials on their client. This lets users reconnect to their WorkSpace without re-entering their credentials.
+  Restart their WorkSpace.
+  Increase the size of the root and user volumes on their WorkSpace.
+  Change the compute type (bundle) for their WorkSpace.
+  Switch the running mode of their WorkSpace.
+  Rebuild their WorkSpace.

 There are no ongoing cost implications for allowing users the Restart and Rebuild options for their WorkSpaces. Users should be aware that a Rebuild of their WorkSpace will cause their WorkSpace to be unavailable for up to an hour, as the rebuild process takes place.

 Options to increase the size of the volumes, change the compute type, and switch the running mode can incur additional costs for WorkSpaces. A best practice is to enable self-service to reduce the workload for the support team. Self-service for additional cost items should be allowed within a workflow process that ensures that authorization for additional charges has been obtained. This can be through a dedicated self-service portal for WorkSpaces, or by integration with existing Information Technology Service Manage (ITSM) services, such as [ServiceNow](https://www.servicenow.com/).

 For more detailed information, refer to [Enabling Self-Service WorkSpace Management Capabilities for Your Users](https://docs.aws.amazon.com/workspaces/latest/adminguide/enable-user-self-service-workspace-management.html). For an example describing enabling a structured portal for user self-service, refer to [Automate Amazon WorkSpaces with a Self-Service Portal](https://aws.amazon.com/blogs/desktop-and-application-streaming/automate-amazon-workspaces-with-a-self-service-portal/).

## Amazon WorkSpaces Cost Optimizer
<a name="amazon-workspaces-cost-optimizer"></a>

The Amazon WorkSpaces Cost Optimizer solution analyzes all of your Amazon WorkSpaces usage data. Depending on your usage, it automatically converts the WorkSpace to the most cost-effective billing option (hourly or monthly). This solution helps you monitor your WorkSpace usage and optimize costs, and uses AWS CloudFormation to automatically provision and configure the necessary AWS services to analyze usage every 24 hours and convert individual WorkSpaces. The latest version, 2.4 gives customers the flexibility to deploy the solution in an existing VPC, configure optional for region and termination. It also improved the accuracy of billing hour calculations for WorkSpaces and enhanced reporting metadata. If you have previously deployed an earlier version (v2.2.1 or lower) of this solution, follow the [update stack documentation](https://docs.aws.amazon.com/solutions/latest/workspaces-cost-optimizer/update-the-stack.html) to update the Amazon WorkSpaces Cost Optimizer CloudFormation stack to get the latest version of the solution’s framework.

 The *running mode* of a WorkSpace determines its immediate availability and billing. Here are the current running WorkSpaces running mode:

 **AlwaysOn** — Use when paying a fixed monthly fee for unlimited usage of WorkSpaces. This mode is best for users who use their WorkSpace as their primary desktop and needs instant access to a running WorkSpace at all times.

 **AutoStop** — Use when paying for WorkSpaces by the hour. With this mode, WorkSpaces stop after a specified period of inactivity and the state of apps and data is saved. To set the automatic stop time, use AutoStop Time (hours). This mode is best for users who only need part-time access to their WorkSpaces.

 A best practice is to monitor usage and set the Amazon WorkSpaces’ running mode to be the most cost effective using a solution such as the [Amazon WorkSpaces Cost Optimizer](https://aws.amazon.com/solutions/implementations/amazon-workspaces-cost-optimizer/). This solution deploys an [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) events rule that invokes an [AWS Lambda](https://aws.amazon.com/lambda/) function every 24 hours.

 This solution can convert individual WorkSpaces from an hourly billing model to a monthly billing model on any day after it meets the threshold. If the solution converts a WorkSpace from hourly billing to monthly billing, the solution does not convert the WorkSpace back to hourly billing until the beginning of the next month, and only if usage was below the threshold. However, the billing model can be manually changed at any time using the AWS Management Console or Amazon WorkSpaces API. The solution’s AWS CloudFormation template includes parameters that will run these conversions and allow for running the solution in dry run mode to provide reports of the recommendations.

### Opting out with tags
<a name="opting-out-with-tags"></a>

 To prevent the solution from converting a WorkSpace between billing models, apply a resource tag to the WorkSpace using the tag key Skip\_Convert and any tag value. This solution will log tagged WorkSpaces, but it will not convert the tagged WorkSpaces. Remove the tag at any time to resume automatic conversion for that WorkSpace. For more details, refer to [Amazon WorkSpaces Cost Optimizer](https://aws.amazon.com/solutions/amazon-workspaces-cost-optimizer/).

### Opting in regions
<a name="opting-in-regions"></a>

 By default, this solution will monitor WorkSpaces in all available AWS Region by scanning for directories registered with Amazon WorkSpaces in the same AWS account. You can provide a comma separated list of AWS Regions that you want to monitor in the **List of AWS Regions** input parameter to limit the regions to monitor.

### Deployment in an existing VPC
<a name="deployment-in-an-existing-vpc"></a>

 This solution requires a VPC to run the ECS task. By default, the solution will create a new VPC, but you can deploy in an existing VPC by providing the subnet IDs and security group ID as part of the input parameter. Your current subnet has a route to the Internet for the ECS task to pull the Docker image hosted in a public Amazon ECR repository.

### Termination of unused WorkSpaces
<a name="termination-of-unused-workspaces"></a>

 This solution allows you to terminate unused WorkSpaces on the last day of the month when all the criteria have been met. You can opt in to this feature by changing the **TerminateUnusedWorkSpaces** input parameter to the CloudFormation template. A best practice is to run this feature in Dry Run mode for a couple of months and check the monthly reports to review the WorkSpaces marked for termination.
