---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_Collector.html
---

# Collector
<a name="API_Collector"></a>

 Process data collector that runs in the environment that you specify.

## Contents
<a name="API_Collector_Contents"></a>

 ** collectorHealth **   <a name="migrationhubstrategy-Type-Collector-collectorHealth"></a>
 Indicates the health of a collector.
Type: String
Valid Values: `COLLECTOR_HEALTHY | COLLECTOR_UNHEALTHY`
Required: No

 ** collectorId **   <a name="migrationhubstrategy-Type-Collector-collectorId"></a>
 The ID of the collector.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** collectorVersion **   <a name="migrationhubstrategy-Type-Collector-collectorVersion"></a>
 Current version of the collector that is running in the environment that you specify.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** configurationSummary **   <a name="migrationhubstrategy-Type-Collector-configurationSummary"></a>
Summary of the collector configuration.
Type: [ConfigurationSummary](API_ConfigurationSummary.md) object
Required: No

 ** hostName **   <a name="migrationhubstrategy-Type-Collector-hostName"></a>
 Hostname of the server that is hosting the collector.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** ipAddress **   <a name="migrationhubstrategy-Type-Collector-ipAddress"></a>
 IP address of the server that is hosting the collector.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** lastActivityTimeStamp **   <a name="migrationhubstrategy-Type-Collector-lastActivityTimeStamp"></a>
 Time when the collector last pinged the service.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** registeredTimeStamp **   <a name="migrationhubstrategy-Type-Collector-registeredTimeStamp"></a>
 Time when the collector registered with the service.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Collector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/Collector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/Collector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/Collector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
