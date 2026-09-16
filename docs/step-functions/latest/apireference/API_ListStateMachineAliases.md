---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListStateMachineAliases.html
---

# ListStateMachineAliases
<a name="API_ListStateMachineAliases"></a>

Lists [aliases](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html) for a specified state machine ARN. Results are sorted by time, with the most recently created aliases listed first.

To list aliases that reference a state machine [version](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html), you can specify the version ARN in the `stateMachineArn` parameter.

If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.

 **Related operations:**
+  [CreateStateMachineAlias](API_CreateStateMachineAlias.md)
+  [DescribeStateMachineAlias](API_DescribeStateMachineAlias.md)
+  [UpdateStateMachineAlias](API_UpdateStateMachineAlias.md)
+  [DeleteStateMachineAlias](API_DeleteStateMachineAlias.md)

## Request Syntax
<a name="API_ListStateMachineAliases_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "stateMachineArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListStateMachineAliases_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListStateMachineAliases_RequestSyntax) **   <a name="StepFunctions-ListStateMachineAliases-request-maxResults"></a>
The maximum number of results that are returned per call. You can use `nextToken` to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.
This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListStateMachineAliases_RequestSyntax) **   <a name="StepFunctions-ListStateMachineAliases-request-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [stateMachineArn](#API_ListStateMachineAliases_RequestSyntax) **   <a name="StepFunctions-ListStateMachineAliases-request-stateMachineArn"></a>
The Amazon Resource Name (ARN) of the state machine for which you want to list aliases.
If you specify a state machine version ARN, this API returns a list of aliases for that version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_ListStateMachineAliases_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "stateMachineAliases": [
      {
         "creationDate": number,
         "stateMachineAliasArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListStateMachineAliases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListStateMachineAliases_ResponseSyntax) **   <a name="StepFunctions-ListStateMachineAliases-response-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [stateMachineAliases](#API_ListStateMachineAliases_ResponseSyntax) **   <a name="StepFunctions-ListStateMachineAliases-response-stateMachineAliases"></a>
Aliases for the state machine.
Type: Array of [StateMachineAliasListItem](API_StateMachineAliasListItem.md) objects

## Errors
<a name="API_ListStateMachineAliases_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArn **
The provided Amazon Resource Name (ARN) is not valid.
HTTP Status Code: 400

 ** InvalidToken **
The provided token is not valid.
HTTP Status Code: 400

 ** ResourceNotFound **
Could not find the referenced resource.
HTTP Status Code: 400

 ** StateMachineDeleting **
The specified state machine is being deleted.
HTTP Status Code: 400

 ** StateMachineDoesNotExist **
The specified state machine does not exist.
HTTP Status Code: 400

## See Also
<a name="API_ListStateMachineAliases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/ListStateMachineAliases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/ListStateMachineAliases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/ListStateMachineAliases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/ListStateMachineAliases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/ListStateMachineAliases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/ListStateMachineAliases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/ListStateMachineAliases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/ListStateMachineAliases)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/ListStateMachineAliases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/ListStateMachineAliases)
