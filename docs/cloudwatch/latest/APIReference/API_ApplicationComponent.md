---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ApplicationComponent.html
---

# ApplicationComponent
<a name="API_ApplicationComponent"></a>

Describes a standalone resource or similarly grouped resources that the application is made up of.

## Contents
<a name="API_ApplicationComponent_Contents"></a>

 ** ComponentName **   <a name="appinsights-Type-ApplicationComponent-ComponentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `(?:^[\d\w\-_\.+]*$)|(?:^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$)`
Required: No

 ** ComponentRemarks **   <a name="appinsights-Type-ApplicationComponent-ComponentRemarks"></a>
 If logging is supported for the resource type, indicates whether the component has configured logs to be monitored.
Type: String
Required: No

 ** DetectedWorkload **   <a name="appinsights-Type-ApplicationComponent-DetectedWorkload"></a>
 Workloads detected in the application component.
Type: String to string to string map map
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Valid Keys: `CUSTOM | DEFAULT | DOT_NET_CORE | DOT_NET_WORKER | DOT_NET_WEB_TIER | DOT_NET_WEB | SQL_SERVER | SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP | MYSQL | POSTGRESQL | JAVA_JMX | ORACLE | SAP_HANA_MULTI_NODE | SAP_HANA_SINGLE_NODE | SAP_HANA_HIGH_AVAILABILITY | SAP_ASE_SINGLE_NODE | SAP_ASE_HIGH_AVAILABILITY | SQL_SERVER_FAILOVER_CLUSTER_INSTANCE | SHAREPOINT | ACTIVE_DIRECTORY | SAP_NETWEAVER_STANDARD | SAP_NETWEAVER_DISTRIBUTED | SAP_NETWEAVER_HIGH_AVAILABILITY`
Required: No

 ** Monitor **   <a name="appinsights-Type-ApplicationComponent-Monitor"></a>
Indicates whether the application component is monitored.
Type: Boolean
Required: No

 ** OsType **   <a name="appinsights-Type-ApplicationComponent-OsType"></a>
 The operating system of the component.
Type: String
Valid Values: `WINDOWS | LINUX`
Required: No

 ** ResourceType **   <a name="appinsights-Type-ApplicationComponent-ResourceType"></a>
The resource type. Supported resource types include EC2 instances, Auto Scaling group, Classic ELB, Application ELB, and SQS Queue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[0-9a-zA-Z:_]*`
Required: No

 ** Tier **   <a name="appinsights-Type-ApplicationComponent-Tier"></a>
The stack tier of the application component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Valid Values: `CUSTOM | DEFAULT | DOT_NET_CORE | DOT_NET_WORKER | DOT_NET_WEB_TIER | DOT_NET_WEB | SQL_SERVER | SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP | MYSQL | POSTGRESQL | JAVA_JMX | ORACLE | SAP_HANA_MULTI_NODE | SAP_HANA_SINGLE_NODE | SAP_HANA_HIGH_AVAILABILITY | SAP_ASE_SINGLE_NODE | SAP_ASE_HIGH_AVAILABILITY | SQL_SERVER_FAILOVER_CLUSTER_INSTANCE | SHAREPOINT | ACTIVE_DIRECTORY | SAP_NETWEAVER_STANDARD | SAP_NETWEAVER_DISTRIBUTED | SAP_NETWEAVER_HIGH_AVAILABILITY`
Required: No

## See Also
<a name="API_ApplicationComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/ApplicationComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/ApplicationComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/ApplicationComponent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
