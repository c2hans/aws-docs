---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_AddRegionAction.html
---

# AddRegionAction
<a name="API_AddRegionAction"></a>

Defines the AWS Region and AWS KMS key to add to the replication set.

## Contents
<a name="API_AddRegionAction_Contents"></a>

 ** regionName **   <a name="IncidentManager-Type-AddRegionAction-regionName"></a>
The AWS Region name to add to the replication set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20.
Required: Yes

 ** sseKmsKeyId **   <a name="IncidentManager-Type-AddRegionAction-sseKmsKeyId"></a>
The AWS KMS key ID to use to encrypt your replication set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_AddRegionAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/AddRegionAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/AddRegionAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/AddRegionAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
