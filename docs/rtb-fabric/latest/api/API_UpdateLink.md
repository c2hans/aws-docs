---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UpdateLink.html
---

# UpdateLink
<a name="API_UpdateLink"></a>

Updates the configuration of a link between gateways.

Allows you to modify settings and parameters for an existing link.

## Request Syntax
<a name="API_UpdateLink_RequestSyntax"></a>

```
PATCH /gateway/{{gatewayId}}/link/{{linkId}} HTTP/1.1
Content-type: application/json

{
   "logSettings": {
      "applicationLogs": {
         "sampling": {
            "errorLog": {{number}},
            "filterLog": {{number}}
         }
      }
   },
   "timeoutInMillis": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateLink_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayId](#API_UpdateLink_RequestSyntax) **   <a name="rtbfabric-UpdateLink-request-uri-gatewayId"></a>
The unique identifier of the gateway.
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`
Required: Yes

 ** [linkId](#API_UpdateLink_RequestSyntax) **   <a name="rtbfabric-UpdateLink-request-uri-linkId"></a>
The unique identifier of the link.
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `link-[a-z0-9-]{1,25}`
Required: Yes

## Request Body
<a name="API_UpdateLink_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [logSettings](#API_UpdateLink_RequestSyntax) **   <a name="rtbfabric-UpdateLink-request-logSettings"></a>
Settings for the application logs.
Type: [LinkLogSettings](API_LinkLogSettings.md) object
Required: No

 ** [timeoutInMillis](#API_UpdateLink_RequestSyntax) **   <a name="rtbfabric-UpdateLink-request-timeoutInMillis"></a>
The timeout value in milliseconds.
Type: Long
Valid Range: Minimum value of 100. Maximum value of 5000.
Required: No

## Response Syntax
<a name="API_UpdateLink_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "linkId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_UpdateLink_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [linkId](#API_UpdateLink_ResponseSyntax) **   <a name="rtbfabric-UpdateLink-response-linkId"></a>
The unique identifier of the link.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `link-[a-z0-9-]{1,25}`

 ** [status](#API_UpdateLink_ResponseSyntax) **   <a name="rtbfabric-UpdateLink-response-status"></a>
The status of the request.
Type: String
Valid Values: `PENDING_CREATION | PENDING_REQUEST | REQUESTED | ACCEPTED | ACTIVE | REJECTED | FAILED | PENDING_DELETION | DELETED | PENDING_UPDATE | PENDING_ISOLATION | ISOLATED | PENDING_RESTORATION`

## Errors
<a name="API_UpdateLink_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request could not be completed because you do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed because of a conflict in the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request could not be completed because of an internal server error. Try your call again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request could not be completed because the resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request could not be completed because it fails satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateLink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/UpdateLink)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/UpdateLink)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/UpdateLink)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/UpdateLink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/UpdateLink)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/UpdateLink)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/UpdateLink)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/UpdateLink)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/UpdateLink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/UpdateLink)
