---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-operations-perspective/application-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Application management
<a name="application-management"></a>

 **Investigate and remediate application issues in a single pane of glass. **

 An application is a logical group of AWS resources that you want to operate as a unit. Whether you take an approach of “[you build it, you run it](https://aws.amazon.com/blogs/enterprise-strategy/enterprise-devops-why-you-should-run-what-you-build/)” or have separate operations teams, it is often simpler to view information and take operations actions in the context of an application rather than on individual components. Applications often have different requirements for cost, monitoring, compliance, automation, and many other factors. Being able to view information, make decisions, and take actions within the context of the application and its requirements simplifies operational oversight and accelerates the remediation of application issues.

## Start
<a name="start-8"></a>

 To get started with application management, use [AWS Systems Manager Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html), [Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html), [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html), or [AWS Launch Wizard](https://docs.aws.amazon.com/launchwizard/index.html) to specify the AWS resources that define your application. Applications can be defined as custom applications using a combination of tags, [AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html), or [AWS CloudFormation stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html). Application Manager automatically imports metadata about resources that were created by AWS CloudFormation, AWS Launch Wizard, Amazon ECS, and Amazon EKS. Application Manager then displays those resources in predefined categories.

 Once you have defined your application, you can view information about it. The [Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html) overview displays a summary of Amazon CloudWatch alarms, [OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html), [Amazon CloudWatch Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html), and [AWS Config compliance and runbook history](https://docs.aws.amazon.com/config/latest/developerguide/view-compliance-history.html). To start with, focus on cost and monitoring.

 Use the alarms that you have already created following the [Observability](observability.md) guidance in this document to automatically visualize alarms in Application Manager. Enable [Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-setting-up.html) with the application that you have created to visualize additional alarms created automatically and to view insights using intelligent problem detection, metric anomalies, and log errors.

 [Log groups](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-viewing-logs.html) related to your application are listed in Application Manager, allowing you to see all of these log groups in one place, with a link to the log group itself for further analysis. The resources view in Application Manager lets you [view all of the AWS resources associated with your application](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-viewing-resources.html) as well as viewing the cost of your application.

## Advance
<a name="advance-8"></a>

 Once you have organized your applications and set up [patch management](patch-management.md), you will be able to view [AWS Systems Manager State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html) association compliance information, as well as other [State Manager associations](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-associations.html) related to your application. If you have enabled AWS Config, you will be able to see [Config rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) compliance and [Config Resource compliance](https://docs.aws.amazon.com/config/latest/developerguide/evaluating-your-resources.html), as well as the number of configuration changes that have been made to that resource.

 [OpsItems](event-management-aiops.md#advance-1)** **can also be viewed in the context of your application. The OpsItems tab displays OpsItems for resources in your application.

## Excel
<a name="excel-8"></a>

 As described in the [incident and problem management](incident-and-problem-management.md) section, you can remediate issues in your application using [Automation runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html). You can start any runbook filtered by the type of resource used in your application, or you can choose the name of the resource in your application, which will then filter runbooks by that resource type.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
