---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_ListExtensibleSourceServers.html
---

# ListExtensibleSourceServers
<a name="API_ListExtensibleSourceServers"></a>

Returns a list of source servers on a staging account that are extensible, which means that: a. The source server is not already extended into this Account. b. The source server on the Account we’re reading from is not an extension of another source server.

## Request Syntax
<a name="API_ListExtensibleSourceServers_RequestSyntax"></a>

```
POST /ListExtensibleSourceServers HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "stagingAccountID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListExtensibleSourceServers_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListExtensibleSourceServers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListExtensibleSourceServers_RequestSyntax) **   <a name="drs-ListExtensibleSourceServers-request-maxResults"></a>
The maximum number of extensible source servers to retrieve.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 300.
Required: No

 ** [nextToken](#API_ListExtensibleSourceServers_RequestSyntax) **   <a name="drs-ListExtensibleSourceServers-request-nextToken"></a>
The token of the next extensible source server to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [stagingAccountID](#API_ListExtensibleSourceServers_RequestSyntax) **   <a name="drs-ListExtensibleSourceServers-request-stagingAccountID"></a>
The Id of the staging Account to retrieve extensible source servers from.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: Yes

## Response Syntax
<a name="API_ListExtensibleSourceServers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "hostname": "string",
         "tags": {
            "string" : "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListExtensibleSourceServers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListExtensibleSourceServers_ResponseSyntax) **   <a name="drs-ListExtensibleSourceServers-response-items"></a>
A list of source servers on a staging Account that are extensible.
Type: Array of [StagingSourceServer](API_StagingSourceServer.md) objects

 ** [nextToken](#API_ListExtensibleSourceServers_ResponseSyntax) **   <a name="drs-ListExtensibleSourceServers-response-nextToken"></a>
The token of the next extensible source server to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_ListExtensibleSourceServers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Quota code.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
 ** serviceCode **
Service code.
HTTP Status Code: 429

 ** UninitializedAccountException **
The account performing the request has not been initialized.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
Validation exception reason.
HTTP Status Code: 400

## See Also
<a name="API_ListExtensibleSourceServers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/ListExtensibleSourceServers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/ListExtensibleSourceServers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/ListExtensibleSourceServers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/ListExtensibleSourceServers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/ListExtensibleSourceServers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/ListExtensibleSourceServers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/ListExtensibleSourceServers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/ListExtensibleSourceServers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/ListExtensibleSourceServers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/ListExtensibleSourceServers)
