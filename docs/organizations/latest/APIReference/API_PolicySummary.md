---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_PolicySummary.html
---

# PolicySummary
<a name="API_PolicySummary"></a>

Contains information about a policy, but does not include the content. To see the content of a policy, see [DescribePolicy](API_DescribePolicy.md).

## Contents
<a name="API_PolicySummary_Contents"></a>

 ** Arn **   <a name="organizations-Type-PolicySummary-Arn"></a>
The Amazon Resource Name (ARN) of the policy.
For more information about ARNs in Organizations, see [ARN Formats Supported by Organizations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies) in the * AWS Service Authorization Reference*.
Type: String
Pattern: `^(arn:aws:organizations::\d{12}:policy\/o-[a-z0-9]{10,32}\/[0-9a-z_]+\/p-[0-9a-z]{10,32})|(arn:aws:organizations::aws:policy\/[0-9a-z_]+\/p-[0-9a-zA-Z_]{10,128})`
Required: No

 ** AwsManaged **   <a name="organizations-Type-PolicySummary-AwsManaged"></a>
A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.
Type: Boolean
Required: No

 ** Description **   <a name="organizations-Type-PolicySummary-Description"></a>
The description of the policy.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\S]*`
Required: No

 ** Id **   <a name="organizations-Type-PolicySummary-Id"></a>
The unique identifier (ID) of the policy.
The [regex pattern](http://wikipedia.org/wiki/regex) for a policy ID string requires "p-" followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (\_).
Type: String
Length Constraints: Maximum length of 130.
Pattern: `^p-[0-9a-zA-Z_]{8,128}$`
Required: No

 ** Name **   <a name="organizations-Type-PolicySummary-Name"></a>
The friendly name of the policy.
The [regex pattern](http://wikipedia.org/wiki/regex) that is used to validate this parameter is a string of any of the characters in the ASCII character range.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\s\S]*`
Required: No

 ** Type **   <a name="organizations-Type-PolicySummary-Type"></a>
The type of policy.
Type: String
Valid Values: `SERVICE_CONTROL_POLICY | RESOURCE_CONTROL_POLICY | TAG_POLICY | BACKUP_POLICY | AISERVICES_OPT_OUT_POLICY | CHATBOT_POLICY | DECLARATIVE_POLICY_EC2 | SECURITYHUB_POLICY | INSPECTOR_POLICY | UPGRADE_ROLLOUT_POLICY | BEDROCK_POLICY | S3_POLICY | NETWORK_SECURITY_DIRECTOR_POLICY`
Required: No

## See Also
<a name="API_PolicySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/PolicySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/PolicySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/PolicySummary)
