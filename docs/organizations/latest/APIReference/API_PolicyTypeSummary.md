---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_PolicyTypeSummary.html
---

# PolicyTypeSummary
<a name="API_PolicyTypeSummary"></a>

Contains information about a policy type and its status in the associated root.

## Contents
<a name="API_PolicyTypeSummary_Contents"></a>

 ** Status **   <a name="organizations-Type-PolicyTypeSummary-Status"></a>
The status of the policy type as it relates to the associated root. To attach a policy of the specified type to a root or to an OU or account in that root, it must be available in the organization and enabled for that root.
Type: String
Valid Values: `ENABLED | PENDING_ENABLE | PENDING_DISABLE`
Required: No

 ** Type **   <a name="organizations-Type-PolicyTypeSummary-Type"></a>
The name of the policy type.
Type: String
Valid Values: `SERVICE_CONTROL_POLICY | RESOURCE_CONTROL_POLICY | TAG_POLICY | BACKUP_POLICY | AISERVICES_OPT_OUT_POLICY | CHATBOT_POLICY | DECLARATIVE_POLICY_EC2 | SECURITYHUB_POLICY | INSPECTOR_POLICY | UPGRADE_ROLLOUT_POLICY | BEDROCK_POLICY | S3_POLICY | NETWORK_SECURITY_DIRECTOR_POLICY`
Required: No

## See Also
<a name="API_PolicyTypeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/PolicyTypeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/PolicyTypeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/PolicyTypeSummary)
