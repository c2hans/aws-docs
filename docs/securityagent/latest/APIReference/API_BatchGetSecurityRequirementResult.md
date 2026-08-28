---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchGetSecurityRequirementResult.html
---

# BatchGetSecurityRequirementResult
<a name="API_BatchGetSecurityRequirementResult"></a>

Contains information about a successfully retrieved security requirement.

## Contents
<a name="API_BatchGetSecurityRequirementResult_Contents"></a>

 ** createdAt **   <a name="securityagent-Type-BatchGetSecurityRequirementResult-createdAt"></a>
The date and time the security requirement was created, in UTC format.
Type: Timestamp
Required: Yes

 ** description **   <a name="securityagent-Type-BatchGetSecurityRequirementResult-description"></a>
A description of the security requirement.
Type: String
Required: Yes

 ** domain **   <a name="securityagent-Type-BatchGetSecurityRequirementResult-domain"></a>
The security domain the requirement belongs to.
Type: String
Required: Yes

 ** evaluation **   <a name="securityagent-Type-BatchGetSecurityRequirementResult-evaluation"></a>
The evaluation criteria used to assess compliance with this requirement.
Type: String
Required: Yes

 ** name **   <a name="securityagent-Type-BatchGetSecurityRequirementResult-name"></a>
The name of the security requirement.
Type: String
Required: Yes

 ** packId **   <a name="securityagent-Type-BatchGetSecurityRequirementResult-packId"></a>
The unique identifier of the pack containing the security requirement.
Type: String
Required: Yes

 ** updatedAt **   <a name="securityagent-Type-BatchGetSecurityRequirementResult-updatedAt"></a>
The date and time the security requirement was last updated, in UTC format.
Type: Timestamp
Required: Yes

 ** remediation **   <a name="securityagent-Type-BatchGetSecurityRequirementResult-remediation"></a>
The recommended remediation steps when the requirement is not met.
Type: String
Required: No

## See Also
<a name="API_BatchGetSecurityRequirementResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchGetSecurityRequirementResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchGetSecurityRequirementResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchGetSecurityRequirementResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
