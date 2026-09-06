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
