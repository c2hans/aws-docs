---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_ListSoftwareSets.html
---

# ListSoftwareSets
<a name="API_ListSoftwareSets"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

Returns a list of software sets.

## Request Syntax
<a name="API_ListSoftwareSets_RequestSyntax"></a>

```
GET /softwaresets?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSoftwareSets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListSoftwareSets_RequestSyntax) **   <a name="workspacesthinclient-ListSoftwareSets-request-uri-maxResults"></a>
The maximum number of results that are returned per call. You can use `nextToken` to obtain further pages of results.
This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListSoftwareSets_RequestSyntax) **   <a name="workspacesthinclient-ListSoftwareSets-request-uri-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken error*.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `\S*`

## Request Body
<a name="API_ListSoftwareSets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSoftwareSets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "softwareSets": [
      {
         "arn": "string",
         "id": "string",
         "releasedAt": number,
         "supportedUntil": number,
         "validationStatus": "string",
         "version": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSoftwareSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSoftwareSets_ResponseSyntax) **   <a name="workspacesthinclient-ListSoftwareSets-response-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken error*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `\S*`

 ** [softwareSets](#API_ListSoftwareSets_ResponseSyntax) **   <a name="workspacesthinclient-ListSoftwareSets-response-softwareSets"></a>
Describes software sets.
Type: Array of [SoftwareSetSummary](API_SoftwareSetSummary.md) objects

## Errors
<a name="API_ListSoftwareSets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).
The server encountered an internal error and is unable to complete the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the next request.
HTTP Status Code: 500

 ** ThrottlingException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).
The request was denied due to request throttling.
 ** quotaCode **
The code for the quota in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
 ** retryAfterSeconds **
The number of seconds to wait before retrying the next request.
 ** serviceCode **
The code for the service in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
HTTP Status Code: 429

 ** ValidationException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).
The input fails to satisfy the specified constraints.
 ** fieldList **
A list of fields that didn't validate.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListSoftwareSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-thin-client-2023-08-22/ListSoftwareSets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-thin-client-2023-08-22/ListSoftwareSets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-thin-client-2023-08-22/ListSoftwareSets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-thin-client-2023-08-22/ListSoftwareSets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-thin-client-2023-08-22/ListSoftwareSets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-thin-client-2023-08-22/ListSoftwareSets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-thin-client-2023-08-22/ListSoftwareSets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-thin-client-2023-08-22/ListSoftwareSets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-thin-client-2023-08-22/ListSoftwareSets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-thin-client-2023-08-22/ListSoftwareSets)
