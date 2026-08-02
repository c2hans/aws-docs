---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_telemetry_customer_telemetry.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS04-BP03 Implement user activity telemetry
<a name="ops_telemetry_customer_telemetry"></a>

Instrument your application code to emit information about user activity. Examples of user activity include click streams or started, abandoned, and completed transactions. Use this information to help understand how the application is used, patterns of usage, and to determine when a response is required. Capturing real user activity allows you to build synthetic activity that can be used to monitor and test your workload in production.

 **Desired outcome:**
+  Your workload emits telemetry about user activity across all applications.
+  You leverage synthetic user activity to monitor your application during off-peak hours.

 **Common anti-patterns:**
+ Your developers have deployed a new feature without user telemetry. You cannot tell if your customers are using the feature without asking them.
+ After a deployment to your front-end application, you see increased utilization. Because you lack user activity telemetry, it is difficult to identify the exact issue.
+  An issue occurs in your application during off-peak hours. You do not notice the issue until the morning when your users come online because you have not configured synthetic user activity.

 **Benefits of establishing this best practice:**
+  Understand common user patterns or unexpected behaviors to optimize functionality of the application to fit your business goals.
+  Monitor the application from the perspective of your users to detect problems with user experience, such as broken links or slow click responses
+  Identify the root cause of issues by tracing the steps your impacted user has taken.
+  Synthetic user activity can provide early warning signs of performance degradation during off-peak hours, allowing you to take corrective action before actual users are affected.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Design your application code to emit information about user activity. Use this information to help understand how the application is used, patterns of usage, and to determine when a response is required. Utilize synthetic user activity to provide insight into application performance during off-peak hours.

 **Customer example**

 AnyCompany Retail implements user activity telemetry at several layers in their application. The front-end telemetry tracks pointer and movement events while the backend microservices emit telemetry tracking events like adding an item to the user's cart and checking out. Together they provide observability into the user experience. AnyCompany Retail also uses synthetic user telemetry to catch problems when there are fewer users on the workload.

 **Implementation steps**

1.  Instrument your application to emit telemetry (metrics, events, logs, and traces) about user activity. Once instrumented, front-end components emit telemetry automatically as the user interacts with the user interface. Backend applications emit telemetry on user events and transactions.

   1.  [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) can provide insight into end user experience for front-end applications.

   1.  You can use the [AWS Distro for Open Telemetry](https://aws-otel.github.io/) to instrument and capture telemetry from your applications.

   1.  [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html) can analyze user behavior through campaigns, providing insight on user engagement.

   1.  Customers with Enterprise Support can request the [Building a Monitoring Strategy Workshop](https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/) from their Technical Account Manager. This workshop helps you build an observability strategy for your workload.

1.  Establish synthetic user activity to monitor your application. Synthetic user activity simulates user actions to validate that your application is working properly.

   1.  [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) can simulate user activity using canaries.

 **Level of effort for the implementation plan:** High. It may take significant development effort to fully instrument your application to collect user activity telemetry.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS04-BP01 Implement application telemetry](ops_telemetry_application_telemetry.md) - Application telemetry is required in order to build in user activity telemetry.
+  [OPS04-BP02 Implement and configure workload telemetry](ops_telemetry_workload_telemetry.md) - Some user activity telemetry may also be considered workload telemetry.

 **Related documents:**
+ [ How to Monitor your Applications Effectively ](https://aws.amazon.com/startups/start-building/how-to-monitor-applications/)

 **Related videos:**
+ [AWS re:Invent 2020: Monitoring production services at Amazon ](https://www.youtube.com/watch?v=hnPcf_Czbvw)
+ [AWS re:Invent 2021 - Optimize applications through end user insights with Amazon CloudWatch RUM ](https://www.youtube.com/watch?v=NMaeujY9A9Y)
+ [ Testing and Monitoring APIs on AWS - AWS Online Tech Talks ](https://www.youtube.com/watch?v=VQM38CZyjFY)

 **Related examples:**
+ [ Amazon CloudWatch RUM Web Client ](https://github.com/aws-observability/aws-rum-web)
+ [AWS Distro for Open Telemetry ](https://aws-otel.github.io/)
+ [ Implementing Real User Monitoring of Amplify Application using Amazon CloudWatch RUM ](https://aws.amazon.com/blogs/mobile/implementing-real-user-monitoring-of-amplify-application-using-amazon-cloudwatch-rum/)
+ [ One Observability Workshop ](https://catalog.workshops.aws/observability/en-US/intro)

 **Related services:**
+ [ Amazon CloudWatch RUM ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html)
+ [ Amazon CloudWatch Synthetics ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
+ [ Amazon Pinpoint ](https://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html)
