---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListWorkspaces.html
---

# ListWorkspaces
<a name="API_ListWorkspaces"></a>

Retrieves information about workspaces in the current account.

## Request Syntax
<a name="API_ListWorkspaces_RequestSyntax"></a>

```
POST /workspaces-list HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListWorkspaces_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListWorkspaces_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListWorkspaces_RequestSyntax) **   <a name="tm-ListWorkspaces-request-maxResults"></a>
The maximum number of results to return at one time. The default is 25.
Valid Range: Minimum value of 1. Maximum value of 250.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 200.
Required: No

 ** [nextToken](#API_ListWorkspaces_RequestSyntax) **   <a name="tm-ListWorkspaces-request-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListWorkspaces_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "workspaceSummaries": [
      {
         "arn": "string",
         "creationDateTime": number,
         "description": "string",
         "linkedServices": [ "string" ],
         "updateDateTime": number,
         "workspaceId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWorkspaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListWorkspaces_ResponseSyntax) **   <a name="tm-ListWorkspaces-response-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`

 ** [workspaceSummaries](#API_ListWorkspaces_ResponseSyntax) **   <a name="tm-ListWorkspaces-response-workspaceSummaries"></a>
A list of objects that contain information about the workspaces.
Type: Array of [WorkspaceSummary](API_WorkspaceSummary.md) objects

## Errors
<a name="API_ListWorkspaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error has occurred.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The service quota was exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
Failed
HTTP Status Code: 400

## See Also
<a name="API_ListWorkspaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/ListWorkspaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/ListWorkspaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ListWorkspaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/ListWorkspaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ListWorkspaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/ListWorkspaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/ListWorkspaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/ListWorkspaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/ListWorkspaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ListWorkspaces)
