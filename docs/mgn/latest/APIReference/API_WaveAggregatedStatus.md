---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_WaveAggregatedStatus.html
---

# WaveAggregatedStatus
<a name="API_WaveAggregatedStatus"></a>

Wave aggregated status.

## Contents
<a name="API_WaveAggregatedStatus_Contents"></a>

 ** healthStatus **   <a name="mgn-Type-WaveAggregatedStatus-healthStatus"></a>
Wave aggregated status health status.
Type: String
Valid Values: `HEALTHY | LAGGING | ERROR`
Required: No

 ** lastUpdateDateTime **   <a name="mgn-Type-WaveAggregatedStatus-lastUpdateDateTime"></a>
Wave aggregated status last update dateTime.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** progressStatus **   <a name="mgn-Type-WaveAggregatedStatus-progressStatus"></a>
Wave aggregated status progress status.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETED`
Required: No

 ** replicationStartedDateTime **   <a name="mgn-Type-WaveAggregatedStatus-replicationStartedDateTime"></a>
DateTime marking when the first source server in the wave started replication.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** totalApplications **   <a name="mgn-Type-WaveAggregatedStatus-totalApplications"></a>
Wave aggregated status total applications amount.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_WaveAggregatedStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/WaveAggregatedStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/WaveAggregatedStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/WaveAggregatedStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
