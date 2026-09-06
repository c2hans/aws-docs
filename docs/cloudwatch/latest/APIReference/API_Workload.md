---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_Workload.html
---

# Workload
<a name="API_Workload"></a>

Describes the workloads on a component.

## Contents
<a name="API_Workload_Contents"></a>

 ** ComponentName **   <a name="appinsights-Type-Workload-ComponentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `(?:^[\d\w\-_\.+]*$)|(?:^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$)`
Required: No

 ** MissingWorkloadConfig **   <a name="appinsights-Type-Workload-MissingWorkloadConfig"></a>
Indicates whether all of the component configurations required to monitor a workload were provided.
Type: Boolean
Required: No

 ** Tier **   <a name="appinsights-Type-Workload-Tier"></a>
The tier of the workload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Valid Values: `CUSTOM | DEFAULT | DOT_NET_CORE | DOT_NET_WORKER | DOT_NET_WEB_TIER | DOT_NET_WEB | SQL_SERVER | SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP | MYSQL | POSTGRESQL | JAVA_JMX | ORACLE | SAP_HANA_MULTI_NODE | SAP_HANA_SINGLE_NODE | SAP_HANA_HIGH_AVAILABILITY | SAP_ASE_SINGLE_NODE | SAP_ASE_HIGH_AVAILABILITY | SQL_SERVER_FAILOVER_CLUSTER_INSTANCE | SHAREPOINT | ACTIVE_DIRECTORY | SAP_NETWEAVER_STANDARD | SAP_NETWEAVER_DISTRIBUTED | SAP_NETWEAVER_HIGH_AVAILABILITY`
Required: No

 ** WorkloadId **   <a name="appinsights-Type-Workload-WorkloadId"></a>
The ID of the workload.
Type: String
Length Constraints: Fixed length of 38.
Pattern: `w-[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}`
Required: No

 ** WorkloadName **   <a name="appinsights-Type-Workload-WorkloadName"></a>
The name of the workload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: No

 ** WorkloadRemarks **   <a name="appinsights-Type-Workload-WorkloadRemarks"></a>
If logging is supported for the resource type, shows whether the component has configured logs to be monitored.
Type: String
Required: No

## See Also
<a name="API_Workload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/Workload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/Workload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/Workload)
