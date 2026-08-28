---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetHumanReadableSummary.html
---

# GetHumanReadableSummary
<a name="API_GetHumanReadableSummary"></a>

Retrieves a human readable summary for a given entity. At this time, the only supported entity type is `delegation-request`

This method uses a Large Language Model (LLM) to generate the summary.

 If a delegation request has no owner or owner account, `GetHumanReadableSummary` for that delegation request can be called by any account. If the owner account is assigned but there is no owner id, only identities within that owner account can call `GetHumanReadableSummary` for the delegation request to retrieve a summary of that request. Once the delegation request is fully owned, the owner of the request gets a default permission to get that delegation request. For more details, read [default permissions granted to delegation requests](). These rules are identical to [GetDelegationRequest](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetDelegationRequest.html) API behavior, such that a party who has permissions to call [GetDelegationRequest](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetDelegationRequest.html) for a given delegation request will always be able to retrieve the human readable summary for that request.

## Request Parameters
<a name="API_GetHumanReadableSummary_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EntityArn **
Arn of the entity to be summarized. At this time, the only supported entity type is `delegation-request`
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** Locale **
A string representing the locale to use for the summary generation. The supported locale strings are based on the [ Supported languages of the AWS Management Console ](/awsconsolehelpdocs/latest/gsg/change-language.html#supported-languages).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 12.
Required: No

## Response Elements
<a name="API_GetHumanReadableSummary_ResponseElements"></a>

The following elements are returned by the service.

 ** Locale **
The locale that this response was generated for. This maps to the input locale.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 12.

 ** SummaryContent **
Summary content in the specified locale. Summary content is non-empty only if the `SummaryState` is `AVAILABLE`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.

 ** SummaryState **
State of summary generation. This generation process is asynchronous and this attribute indicates the state of the generation process.
Type: String
Valid Values: `AVAILABLE | NOT_AVAILABLE | NOT_SUPPORTED | FAILED`

## Errors
<a name="API_GetHumanReadableSummary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_GetHumanReadableSummary_Examples"></a>

### Example
<a name="API_GetHumanReadableSummary_Example_1"></a>

This example illustrates one usage of GetHumanReadableSummary.

#### Sample Request
<a name="API_GetHumanReadableSummary_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=GetHumanReadableSummary
&EntityArn=arn%3Aaws%3Aiam%3A%3A561761503536%3Adelegation-request%2Fe4bdcdae-4f66-11eD-ELEG-ATIONEXAMPLE
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetHumanReadableSummary_Example_1_Response"></a>

```
<GetHumanReadableSummaryResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <GetHumanReadableSummaryResult>
    <SummaryContent>Human readable summary in Markdown format</SummaryContent>
    <Locale>en</Locale>
    <SummaryState>AVAILABLE</SummaryState>
  </GetHumanReadableSummaryResult>
  <ResponseMetadata>
    <RequestId>e4bdcdae-4f66-11e4-aefa-bfd6aEXAMPLE</RequestId>
  </ResponseMetadata>
</GetHumanReadableSummaryResponse>
```

## See Also
<a name="API_GetHumanReadableSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/GetHumanReadableSummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/GetHumanReadableSummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GetHumanReadableSummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/GetHumanReadableSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GetHumanReadableSummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/GetHumanReadableSummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/GetHumanReadableSummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/GetHumanReadableSummary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/GetHumanReadableSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GetHumanReadableSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
