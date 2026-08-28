---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UsageCriteria.html
---

# UsageCriteria
<a name="API_UsageCriteria"></a>

Contains information about the criteria used to query usage statistics.

## Contents
<a name="API_UsageCriteria_Contents"></a>

 ** accountIds **   <a name="guardduty-Type-UsageCriteria-accountIds"></a>
The account IDs to aggregate usage statistics from.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Fixed length of 12.
Required: No

 ** dataSources **   <a name="guardduty-Type-UsageCriteria-dataSources"></a>
 *This member has been deprecated.*
The data sources to aggregate usage statistics from.
Type: Array of strings
Valid Values: `FLOW_LOGS | CLOUD_TRAIL | DNS_LOGS | S3_LOGS | KUBERNETES_AUDIT_LOGS | EC2_MALWARE_SCAN`
Required: No

 ** features **   <a name="guardduty-Type-UsageCriteria-features"></a>
The features to aggregate usage statistics from.
Type: Array of strings
Valid Values: `FLOW_LOGS | CLOUD_TRAIL | DNS_LOGS | S3_DATA_EVENTS | EKS_AUDIT_LOGS | EBS_MALWARE_PROTECTION | RDS_LOGIN_EVENTS | LAMBDA_NETWORK_LOGS | EKS_RUNTIME_MONITORING | EC2_RUNTIME_MONITORING | FARGATE_RUNTIME_MONITORING | RDS_DBI_PROTECTION_PROVISIONED | RDS_DBI_PROTECTION_SERVERLESS | AI_PROTECTION`
Required: No

 ** resources **   <a name="guardduty-Type-UsageCriteria-resources"></a>
The resources to aggregate usage statistics from. Only accepts exact resource names.
Type: Array of strings
Required: No

## See Also
<a name="API_UsageCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/UsageCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/UsageCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/UsageCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
