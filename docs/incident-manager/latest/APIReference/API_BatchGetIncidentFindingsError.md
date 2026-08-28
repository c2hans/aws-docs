---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_BatchGetIncidentFindingsError.html
---

# BatchGetIncidentFindingsError
<a name="API_BatchGetIncidentFindingsError"></a>

Details about an error returned for a [BatchGetIncidentFindings](API_BatchGetIncidentFindings.md) operation.

## Contents
<a name="API_BatchGetIncidentFindingsError_Contents"></a>

 ** code **   <a name="IncidentManager-Type-BatchGetIncidentFindingsError-code"></a>
The code associated with an error that was returned for a `BatchGetIncidentFindings` operation.
Type: String
Required: Yes

 ** findingId **   <a name="IncidentManager-Type-BatchGetIncidentFindingsError-findingId"></a>
The ID of a specified finding for which an error was returned for a `BatchGetIncidentFindings` operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: Yes

 ** message **   <a name="IncidentManager-Type-BatchGetIncidentFindingsError-message"></a>
The description for an error that was returned for a `BatchGetIncidentFindings` operation.
Type: String
Required: Yes

## See Also
<a name="API_BatchGetIncidentFindingsError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/BatchGetIncidentFindingsError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/BatchGetIncidentFindingsError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/BatchGetIncidentFindingsError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
