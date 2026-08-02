---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_SendCisSessionTelemetry.html
---

# SendCisSessionTelemetry
<a name="API_SendCisSessionTelemetry"></a>

 Sends a CIS session telemetry. This API is used by the Amazon Inspector SSM plugin to communicate with the Amazon Inspector service. The Amazon Inspector SSM plugin calls this API to start a CIS scan session for the scan ID supplied by the service.

## Request Syntax
<a name="API_SendCisSessionTelemetry_RequestSyntax"></a>

```
PUT /cissession/telemetry/send HTTP/1.1
Content-type: application/json

{
   "messages": [
      {
         "cisRuleDetails": {{blob}},
         "ruleId": "{{string}}",
         "status": "{{string}}"
      }
   ],
   "scanJobId": "{{string}}",
   "sessionToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SendCisSessionTelemetry_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SendCisSessionTelemetry_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [messages](#API_SendCisSessionTelemetry_RequestSyntax) **   <a name="inspector2-SendCisSessionTelemetry-request-messages"></a>
The CIS session telemetry messages.
Type: Array of [CisSessionMessage](API_CisSessionMessage.md) objects
Array Members: Minimum number of 1 item. Maximum number of 150 items.
Required: Yes

 ** [scanJobId](#API_SendCisSessionTelemetry_RequestSyntax) **   <a name="inspector2-SendCisSessionTelemetry-request-scanJobId"></a>
A unique identifier for the scan job.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [sessionToken](#API_SendCisSessionTelemetry_RequestSyntax) **   <a name="inspector2-SendCisSessionTelemetry-request-sessionToken"></a>
The unique token that identifies the CIS session.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_SendCisSessionTelemetry_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_SendCisSessionTelemetry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SendCisSessionTelemetry_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** ConflictException **
A conflict occurred. This exception occurs when the same resource is being modified by concurrent requests.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_SendCisSessionTelemetry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/SendCisSessionTelemetry)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/SendCisSessionTelemetry)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/SendCisSessionTelemetry)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/SendCisSessionTelemetry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/SendCisSessionTelemetry)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/SendCisSessionTelemetry)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/SendCisSessionTelemetry)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/SendCisSessionTelemetry)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/SendCisSessionTelemetry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/SendCisSessionTelemetry)
