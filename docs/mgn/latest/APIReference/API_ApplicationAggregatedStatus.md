---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ApplicationAggregatedStatus.html
---

# ApplicationAggregatedStatus
<a name="API_ApplicationAggregatedStatus"></a>

Application aggregated status.

## Contents
<a name="API_ApplicationAggregatedStatus_Contents"></a>

 ** healthStatus **   <a name="mgn-Type-ApplicationAggregatedStatus-healthStatus"></a>
Application aggregated status health status.
Type: String
Valid Values: `HEALTHY | LAGGING | ERROR`
Required: No

 ** lastUpdateDateTime **   <a name="mgn-Type-ApplicationAggregatedStatus-lastUpdateDateTime"></a>
Application aggregated status last update dateTime.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** progressStatus **   <a name="mgn-Type-ApplicationAggregatedStatus-progressStatus"></a>
Application aggregated status progress status.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETED`
Required: No

 ** totalSourceServers **   <a name="mgn-Type-ApplicationAggregatedStatus-totalSourceServers"></a>
Application aggregated status total source servers amount.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_ApplicationAggregatedStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ApplicationAggregatedStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ApplicationAggregatedStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ApplicationAggregatedStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
