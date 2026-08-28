---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UsageTopAccountsResult.html
---

# UsageTopAccountsResult
<a name="API_UsageTopAccountsResult"></a>

Information about the usage statistics, calculated by top accounts by feature.

## Contents
<a name="API_UsageTopAccountsResult_Contents"></a>

 ** accounts **   <a name="guardduty-Type-UsageTopAccountsResult-accounts"></a>
The accounts that contributed to the total usage cost.
Type: Array of [UsageTopAccountResult](API_UsageTopAccountResult.md) objects
Required: No

 ** feature **   <a name="guardduty-Type-UsageTopAccountsResult-feature"></a>
Features by which you can generate the usage statistics.
 `RDS_LOGIN_EVENTS` is currently not supported with `topAccountsByFeature`.
Type: String
Valid Values: `FLOW_LOGS | CLOUD_TRAIL | DNS_LOGS | S3_DATA_EVENTS | EKS_AUDIT_LOGS | EBS_MALWARE_PROTECTION | RDS_LOGIN_EVENTS | LAMBDA_NETWORK_LOGS | EKS_RUNTIME_MONITORING | EC2_RUNTIME_MONITORING | FARGATE_RUNTIME_MONITORING | RDS_DBI_PROTECTION_PROVISIONED | RDS_DBI_PROTECTION_SERVERLESS | AI_PROTECTION`
Required: No

## See Also
<a name="API_UsageTopAccountsResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/UsageTopAccountsResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/UsageTopAccountsResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/UsageTopAccountsResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
