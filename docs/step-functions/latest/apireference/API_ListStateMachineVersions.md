---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListStateMachineVersions.html
---

# ListStateMachineVersions
<a name="API_ListStateMachineVersions"></a>

Lists [versions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html) for the specified state machine Amazon Resource Name (ARN).

The results are sorted in descending order of the version creation time.

If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.

 **Related operations:**
+  [PublishStateMachineVersion](API_PublishStateMachineVersion.md)
+  [DeleteStateMachineVersion](API_DeleteStateMachineVersion.md)

## Request Syntax
<a name="API_ListStateMachineVersions_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "stateMachineArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListStateMachineVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListStateMachineVersions_RequestSyntax) **   <a name="StepFunctions-ListStateMachineVersions-request-maxResults"></a>
The maximum number of results that are returned per call. You can use `nextToken` to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.
This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListStateMachineVersions_RequestSyntax) **   <a name="StepFunctions-ListStateMachineVersions-request-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [stateMachineArn](#API_ListStateMachineVersions_RequestSyntax) **   <a name="StepFunctions-ListStateMachineVersions-request-stateMachineArn"></a>
The Amazon Resource Name (ARN) of the state machine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_ListStateMachineVersions_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "stateMachineVersions": [
      {
         "creationDate": number,
         "stateMachineVersionArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListStateMachineVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListStateMachineVersions_ResponseSyntax) **   <a name="StepFunctions-ListStateMachineVersions-response-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [stateMachineVersions](#API_ListStateMachineVersions_ResponseSyntax) **   <a name="StepFunctions-ListStateMachineVersions-response-stateMachineVersions"></a>
Versions for the state machine.
Type: Array of [StateMachineVersionListItem](API_StateMachineVersionListItem.md) objects

## Errors
<a name="API_ListStateMachineVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArn **
The provided Amazon Resource Name (ARN) is not valid.
HTTP Status Code: 400

 ** InvalidToken **
The provided token is not valid.
HTTP Status Code: 400

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** reason **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListStateMachineVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/ListStateMachineVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/ListStateMachineVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/ListStateMachineVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/ListStateMachineVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/ListStateMachineVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/ListStateMachineVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/ListStateMachineVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/ListStateMachineVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/ListStateMachineVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/ListStateMachineVersions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
