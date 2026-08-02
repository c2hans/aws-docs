---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_telemetry_dependency_telemetry.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS04-BP04 Implement dependency telemetry
<a name="ops_telemetry_dependency_telemetry"></a>

Design and configure your workload to emit information about the status of resources it depends on. These are resources that are external to your workload. Examples of external dependencies can include external databases, DNS, and network connectivity. Use this information to determine when a response is required and provide additional context on workload state.

 **Desired outcome:**
+  Your workload emits telemetry about the status of external dependencies.
+  You are notified when dependencies are unhealthy.

 **Common anti-patterns:**
+ Your users cannot reach your site. You are unable to determine if the reason is a DNS issue without manually performing a check to see if your DNS provider is working.
+ Your shopping cart application is unable to complete transactions. You are unable to determine if it's a problem with your credit card processing provider without contacting them to verify.

 **Benefits of establishing this best practice:**
+  Monitoring external dependencies provides advance notice of issues.
+  Awareness of the health of your dependencies assists in troubleshooting.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Work with stakeholders to identify external dependencies that your workload depends on. External dependencies can include external databases, APIs, or network connectivity between your workload and resources in other environments. Develop a monitoring strategy to provide awareness of the health of dependencies and proactively alarm if the status changes.

 **Customer example**

 AnyCompany Retail’s ecommerce workload relies on a database located in another environment. Every night, data is populated in the database for use in the ecommerce platform. The network connectivity and database support are owned by other teams. The ecommerce team configured several canary alarms to alert them when the network connectivity drops, the database is unreachable, and when the job fails to complete.

 **Implementation steps**

1.  Identify external dependencies that your workload relies on. Implement telemetry to track the health or reachability of dependencies.

   1.  AWS customers can use the [AWS Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html) to monitor the health of AWS services and receive notifications of health events.

   1.  [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) can be used to monitor APIs, URLs, and website contents.

1.  Set up alerts to notify your organization when a dependency is unhealthy or unreachable.

   1.  Customers with Enterprise Support can request the [Building a Monitoring Strategy Workshop](https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/) from their Technical Account Manager. This workshop will help you build an observability strategy for your workload.

1.  Identify contacts for dependencies in cases where the dependency is unhealthy. Document how to contact the dependency owner, service agreements, and escalation process.

 **Level of effort for the implementation plan:** Medium. Implementing dependency telemetry may require building custom monitoring solutions.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS04-BP01 Implement application telemetry](ops_telemetry_application_telemetry.md) - You may build dependency monitoring into your application telemetry.

 **Related documents:**
+ [ Monitor your private internal endpoints 24x7 using CloudWatch Synthetics ](https://aws.amazon.com/blogs/mt/monitor-your-private-endpoints-using-cloudwatch-synthetics/)

 **Related videos:**
+ [AWS re:Invent 2018: Monitor All Your Things: Amazon CloudWatch in Action with BBC ](https://www.youtube.com/watch?v=uuBuc6OAcVY)
+ [AWS re:Invent 2022 - Developing an observability strategy ](https://www.youtube.com/watch?v=Ub3ATriFapQ)
+ [AWS re:Invent 2022 - Observability best practices at Amazon ](https://www.youtube.com/watch?v=zZPzXEBW4P8)

 **Related examples:**
+ [ One Observability Workshop ](https://catalog.workshops.aws/observability/en-US/intro)
+ [ Well-Architected Labs - Dependency Monitoring ](https://www.wellarchitectedlabs.com/operational-excellence/100_labs/100_dependency_monitoring/)

 **Related services:**
+  [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
+ [AWS Health](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html)
