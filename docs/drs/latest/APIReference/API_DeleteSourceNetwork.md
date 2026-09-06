---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteSourceNetwork.html
---

# DeleteSourceNetwork
<a name="API_DeleteSourceNetwork"></a>

Delete Source Network resource.

## Request Syntax
<a name="API_DeleteSourceNetwork_RequestSyntax"></a>

```
POST /DeleteSourceNetwork HTTP/1.1
Content-type: application/json

{
   "sourceNetworkID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteSourceNetwork_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteSourceNetwork_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sourceNetworkID](#API_DeleteSourceNetwork_RequestSyntax) **   <a name="drs-DeleteSourceNetwork-request-sourceNetworkID"></a>
ID of the Source Network to delete.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `sn-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_DeleteSourceNetwork_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteSourceNetwork_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteSourceNetwork_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the target resource.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource for this operation was not found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

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

## See Also
<a name="API_DeleteSourceNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/DeleteSourceNetwork)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/DeleteSourceNetwork)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DeleteSourceNetwork)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/DeleteSourceNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DeleteSourceNetwork)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/DeleteSourceNetwork)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/DeleteSourceNetwork)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/DeleteSourceNetwork)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/DeleteSourceNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DeleteSourceNetwork)
