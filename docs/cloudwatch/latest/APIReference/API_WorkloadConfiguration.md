---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_WorkloadConfiguration.html
---

# WorkloadConfiguration
<a name="API_WorkloadConfiguration"></a>

The configuration of the workload.

## Contents
<a name="API_WorkloadConfiguration_Contents"></a>

 ** Configuration **   <a name="appinsights-Type-WorkloadConfiguration-Configuration"></a>
The configuration settings of the workload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Pattern: `[\S\s]+`
Required: No

 ** Tier **   <a name="appinsights-Type-WorkloadConfiguration-Tier"></a>
The configuration of the workload tier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Valid Values: `CUSTOM | DEFAULT | DOT_NET_CORE | DOT_NET_WORKER | DOT_NET_WEB_TIER | DOT_NET_WEB | SQL_SERVER | SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP | MYSQL | POSTGRESQL | JAVA_JMX | ORACLE | SAP_HANA_MULTI_NODE | SAP_HANA_SINGLE_NODE | SAP_HANA_HIGH_AVAILABILITY | SAP_ASE_SINGLE_NODE | SAP_ASE_HIGH_AVAILABILITY | SQL_SERVER_FAILOVER_CLUSTER_INSTANCE | SHAREPOINT | ACTIVE_DIRECTORY | SAP_NETWEAVER_STANDARD | SAP_NETWEAVER_DISTRIBUTED | SAP_NETWEAVER_HIGH_AVAILABILITY`
Required: No

 ** WorkloadName **   <a name="appinsights-Type-WorkloadConfiguration-WorkloadName"></a>
The name of the workload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: No

## See Also
<a name="API_WorkloadConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/WorkloadConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/WorkloadConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/WorkloadConfiguration)
