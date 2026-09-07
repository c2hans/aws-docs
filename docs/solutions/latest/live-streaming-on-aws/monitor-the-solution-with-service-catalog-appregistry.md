---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws/monitor-the-solution-with-service-catalog-appregistry.html
---

# Monitor the solution with Service Catalog AppRegistry
<a name="monitor-the-solution-with-service-catalog-appregistry"></a>

How to monitor the Live Streaming on AWS solution with AppRegistry

The solution includes a Service Catalog AppRegistry resource to register the CloudFormation template and underlying resources as an application in both Service Catalog AppRegistry and AWS Systems Manager Application Manager.

AWS Systems Manager Application Manager gives you an application-level view into this solution and its resources so that you can:
+ Monitor its resources, costs for the deployed resources across stacks and AWS accounts, and logs associated with this solution from a central location.
+ View operations data for the resources of this solution in the context of an application. For example, deployment status, CloudWatch alarms, resource configurations, and operational issues.

The following figure depicts an example of the application view for the solution stack in Application Manager.

 **Depicts solution stack in Application Manager**

![appregistry1](https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws/images/appregistry1.png)

<a name="activate-cloudwatch-application-insights"></a>== Activate CloudWatch Application Insights . Sign in to the [Systems Manager console](https://console.aws.amazon.com/systems-manager). . In the navigation pane, choose **Application Manager**. . In **Applications**, search for the application name for this solution and select it.

\+

The application name will have **App Registry** in the **Application Source** column, and will have a combination of the solution name, Region, account ID, or stack name. . In the **Components** tree, choose the application stack you want to activate. . In the **Monitoring** tab, in **Application Insights**, select **Auto-configure Application Insights**.

 **Application Insights dashboard showing no detected problems and option to auto-configure.**

![appreg1](https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws/images/appreg1.png)

Monitoring for your applications is now activated and the following status box appears:

 **Application Insights dashboard showing successful monitoring activation message.**

![appreg2](https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws/images/appreg2.png)

<a name="confirm-cost-tags-associated-with-the-solution"></a>== Confirm cost tags associated with the solution

After you activate cost allocation tags associated with the solution, you must confirm the cost allocation tags to see the costs for this solution. To confirm cost allocation tags:

1. Sign in to the [Systems Manager console](https://console.aws.amazon.com/systems-manager).

1. In the navigation pane, choose **Application Manager**.

1. In **Applications**, choose the application name for this solution and select it.

   The application name will have **App Registry** in the **Application Source** column, and will have a combination of the solution name, Region, account ID, or stack name.

1. In the **Overview** tab, in **Cost**, select **Add user tag**.

    **Screenshot depicting the Application Cost add user tag screen**
![AppManager 1](https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws/images/AppManager_1.png)

1. On the **Add user tag** page, enter `confirm`, then select **Add user tag**.

The activation process can take up to 24 hours to complete and the tag data to appear.

<a name="activate-cost-allocation-tags-associated-with-the-solution"></a>== Activate cost allocation tags associated with the solution

After you activate Cost Explorer, you must activate the cost allocation tags associated with this solution to see the costs for this solution. The cost allocation tags can only be activated from the management account for the organization. To activate cost allocation tags:

1. Sign in to the [AWS Billing and Cost Management and Cost Management console](https://console.aws.amazon.com/billing/home).

1. In the navigation pane, select **Cost Allocation Tags**.

1. On the **Cost allocation tags** page, filter for the AppManagerCFNStackKey tag, then select the tag from the results shown.

1. Choose **Activate**.

<a name="activate-aws-cost-explorer"></a>== AWS Cost Explorer

You can see the overview of the costs associated with the application and application components within the Application Manager console through integration with AWS Cost Explorer, which must be first activated. Cost Explorer helps you manage costs by providing a view of your AWS resource costs and usage over time. To activate Cost Explorer for the solution:

1. Sign in to the [AWS Cost Management console](https://console.aws.amazon.com/cost-management/home).

1. In the navigation pane, select **Cost Explorer** to view the solution’s costs and usage over time.
