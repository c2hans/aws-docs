---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/cost-optimization.html
---

# Cost optimization
<a name="cost-optimization"></a>

 Cost optimization focuses on avoiding unneeded costs. Key topics include understanding and controlling where money is being spent, and choosing the most appropriate and correct number of resource types. Analyze spend over time and scaling to meet business needs. The following WorkSpaces Applications resources incur pay-as-you-go fees:
+  Always-On fleet instances
+  On-Demand fleet instances
+  On-Demand stopped instance fee
+  Image builder instances
+  User fees

 For current pricing information, refer to the AWS website for [*Amazon WorkSpaces Applications pricing*](https://aws.amazon.com/appstream2/pricing/).

## Designing cost efficient WorkSpaces Applications deployments
<a name="designing-cost-efficient-appstream-2.0-deployments"></a>

First step in planning and design of WorkSpaces Applications deployment is using [simple pricing tool](http://aws.amazon.com/blogs/desktop-and-application-streaming/amazon-appstream-2-0-releases-a-simple-pricing-tool/) to estimate the baseline of your AWS fees related to your usage. Provide your total number of users, actual concurrent usage per hour, instance type, and fleet utilization, and the pricing tool estimates your per-user price. It also shows the estimated price savings when you use an On-Demand fleet instead of an Always-On fleet.

Customers like the WorkSpaces Applications pricing model of paying only for the instances they provision to meet their users’ streaming needs. This model is different from their existing application streaming environments. These are typically based on provisioning for peak capacity, even during nights, weekends, and holidays, when the load is lower. The Amazon AppStream 2.0 Pricing Tool provides only an estimate of your AWS fees related to your usage of WorkSpaces Applications , and doesn’t include any taxes that might apply. Your actual fees depend on a variety of factors, including your actual usage of AWS services.

The WorkSpaces Applications Pricing Tool is provided as a Microsoft Excel or OpenOffice Calc spreadsheet that enables you to enter basic information about your fleet, then provides a cost estimate for the WorkSpaces Applications environment for on-demand and always-on fleets based on your usage pattern. You could simulate costs based on historical or anticipated usage trends. Elastic fleets free the administrator of the need to predict usage, create, maintain scaling policies and images by having these features built-in. Elastic fleets and instances running of Amazon Linux 2 (all fleet types) are billed for duration of the streaming session, in seconds, with a minimum of 15 minutes.

## Optimizing costs with choice of instance type
<a name="optimizing-costs-with-choice-of-instance-type"></a>

For fleet and image builder instances, there are a range of different instance families and types available that you choose for your application.

**End user testing** — The next step is to rollout the WorkSpaces Applications fleet to a group of pilot users for testing to validate our choice of instance type. It is important to request pilot users to test all their regular and heavy workflows to capture metrics around memory, CPU and graphics so that you can capture baseline performance metrics. The pilot group should contain the various user roles that use the application to ensure you are testing it from multiple user experiences. The user acceptance testing enables you to gather feedback on streaming session experience. When creating or updating a stack, there is an option to use a custom feedback URL. Users are redirected to this URL after they choose the Send Feedback link to submit feedback about their application streaming experience. If there is a performance bottleneck, use Windows performance metrics to analyze resource constraints. For example, if the current fleet instance type stream.standard.medium is showing resource constraint, then upgrade the instance type to stream.standard.large. Conversely, if performance metrics show high levels of under-use of resources, consider downgrading the instance type.

## Optimizing costs with fleet type choice
<a name="optimizing-costs-with-fleet-type-choice"></a>

 When creating a new WorkSpaces Applications fleet, developers must choose either an Always- On or On-Demand fleet type. While choosing the instance type from the pricing perspective, it is important to understand how WorkSpaces Applications manages fleet instances. For Always-On fleets, fleet instances stay in the running state. Therefore, when users try to stream sessions, fleet instances are always ready to start streaming sessions.

 For On-Demand fleets, after fleet instances are launched, they are kept in the stopped state. The stopped instance fee is lower than the running instance fee, which can help with reducing costs. The On-Demand fleet instances must be started from a stopped state. A user must wait approximately two minutes for their streaming session to be available.

Elastic fleets are good candidates for applications that are self-contained and can be installed to virtual hard drives saved in an Amazon Simple Storage Service (Amazon S3) bucket. Elastic fleets may further reduce costs for some use cases due to the per-second billing charged only for the duration of streaming. The rate is a function of the instance type and size and operating system that you choose when creating the fleet.

 If end users need fleet instances during business hours, it is better to keep the same streaming sessions. This is because fleet instances are charged per hour, and every time a new streaming session starts, that incurs another fleet instance fee.

 *Table 10 — WorkSpaces Applications fleet type comparison*

|  **Fleet type**  |   **Advantages**   |   **Considerations**   |
| --- | --- | --- |
|  Always-On  |  Less wait time for streaming sessions  |  Users pay for the hourly instance fee as there is no option to keep instances in stopped state.  |
|  On-Demand  |  Cost saving as instances stay in stopped state  |  Longer wait time for streaming sessions  |
| Elastic | Per-second billing maybe useful for use cases that have sporadic usage patterns for applications that can be installed on virtual hard disk  | As the size of application virtual hard disk becomes bigger, the time taken to mount it to a streaming instance can be long |

 WorkSpaces Applications monitors your fleet utilization and performs automatic adjustments to fleet capacity to meet your user demand at the lowest possible cost. The capacity adjustments are made based on scaling policies that you define, based either on the current utilization or based on a schedule. Regularly review fleet usage metrics to validate that the fleet scaling policies do not have high levels of spare capacity.

## Scaling policies
<a name="scaling-policies1"></a>

Fleet Auto Scaling allows you to optimize fleet resources by not having to over-commit resources waiting for users to login. Administrators can adjust the size of the fleet based on a variety of utilization to match the user demand. Use CloudWatch WorkSpaces Applications Fleet Metrics or third party monitoring tools to learn about user activity and configure scaling policies to expand or shrink WorkSpaces Applications fleets based on expected usage. User logs are an essential mechanism to gain understanding of real usage. This insight can be used to dynamically change fleet size based with Auto Scaling.

In many cases, WorkSpaces Applications fleets are created based on maximum number of users and not adjusted for different times of the day and week such as nights and weekends. Often times, the concurrent user count of streamed applications is less than the total number of users especially when users have the flexibility to work remotely. It is important to take these factors into consideration while projecting usage patterns. Overestimating leads to over-provisioning of WorkSpaces Applications instances resulting in additional costs. To arrive an optimal configuration, you may need to combine one or more scheduled scaling policies with scale out policies.

To learn more about implementing Scaling Policies, review [Scaling your Amazon AppStream 2.0 fleets](http://aws.amazon.com/blogs/desktop-and-application-streaming/scale-your-amazon-appstream-2-0-fleets/).

## User fees
<a name="user-fees"></a>

 User fees are charged per user, per month in each AWS Region where users stream applications from WorkSpaces Applications fleet instances. Instead of generating different user IDs, have consistent user IDs for WorkSpaces Applications users. User fees are not charged when connecting to image builders.

 Schools, universities, and certain public institutions may qualify for a reduced Microsoft RDS SAL user fee of $0.44 per user per month. For qualification requirements, refer to [*Microsoft Licensing Terms and Documents*](https://aka.ms/licensingdocs).

 If you have Microsoft License Mobility, you may be eligible to bring your own Microsoft RDS Client Access Licenses (CALs) and use them with Amazon WorkSpaces Applications. If you are covered by your own license, you won’t incur monthly user fees. For more information about whether you can use your existing Microsoft RDS CAL licenses with Amazon WorkSpaces Applications, refer to the [*AWS License Mobility guidance*](https://aws.amazon.com/windows/resources/licensemobility/), or consult with your Microsoft licensing representative.

## Image Builder usage
<a name="image-builder-usage"></a>

 WorkSpaces Applications Image Builder instances are charged hourly. The Image Builder instance charge includes compute, storage, and any network traffic used by the streaming protocol. All Image Builder instances that are running are charged the applicable running instance fee. This fee is based on the instance type and size, even when no administrators are connected.

 As a best practice to optimize the cost, shut down an Image Builder instance when it is not being used. CloudWatch Events rules can be used to schedule a daily job, such as invoking a Lambda function to stop image builder instances.

 You can keep your WorkSpaces Applications image up-to-date by using managed WorkSpaces Applications image updates. This update method provides the latest Windows operating system updates and driver updates, and the latest WorkSpaces Applications agent software. When using this method to update images, an Image Builder is automatically started, and stopped, as part of the managed service process.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
