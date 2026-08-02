---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetPosition.html
---

# GetPosition
<a name="API_GetPosition"></a>

 *This action has been deprecated.*

Get the position information for a given resource.

**Important**
This action is no longer supported. Calls to retrieve the position information should use the [GetResourcePosition](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetResourcePosition.html) API operation instead.

## Request Syntax
<a name="API_GetPosition_RequestSyntax"></a>

```
GET /positions/{{ResourceIdentifier}}?resourceType={{ResourceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPosition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceIdentifier](#API_GetPosition_RequestSyntax) **   <a name="iotwireless-GetPosition-request-uri-ResourceIdentifier"></a>
Resource identifier used to retrieve the position information.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: Yes

 ** [ResourceType](#API_GetPosition_RequestSyntax) **   <a name="iotwireless-GetPosition-request-uri-ResourceType"></a>
Resource type of the resource for which position information is retrieved.
Valid Values: `WirelessDevice | WirelessGateway`
Required: Yes

## Request Body
<a name="API_GetPosition_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPosition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Accuracy": {
      "HorizontalAccuracy": number,
      "VerticalAccuracy": number
   },
   "Position": [ number ],
   "SolverProvider": "string",
   "SolverType": "string",
   "SolverVersion": "string",
   "Timestamp": "string"
}
```

## Response Elements
<a name="API_GetPosition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Accuracy](#API_GetPosition_ResponseSyntax) **   <a name="iotwireless-GetPosition-response-Accuracy"></a>
The accuracy of the estimated position in meters. An empty value indicates that no position data is available. A value of ‘0.0’ value indicates that position data is available. This data corresponds to the position information that you specified instead of the position computed by solver.
Type: [Accuracy](API_Accuracy.md) object

 ** [Position](#API_GetPosition_ResponseSyntax) **   <a name="iotwireless-GetPosition-response-Position"></a>
The position information of the resource.
Type: Array of floats

 ** [SolverProvider](#API_GetPosition_ResponseSyntax) **   <a name="iotwireless-GetPosition-response-SolverProvider"></a>
The vendor of the positioning solver.
Type: String
Valid Values: `Semtech`

 ** [SolverType](#API_GetPosition_ResponseSyntax) **   <a name="iotwireless-GetPosition-response-SolverType"></a>
The type of solver used to identify the position of the resource.
Type: String
Valid Values: `GNSS`

 ** [SolverVersion](#API_GetPosition_ResponseSyntax) **   <a name="iotwireless-GetPosition-response-SolverVersion"></a>
The version of the positioning solver.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.

 ** [Timestamp](#API_GetPosition_ResponseSyntax) **   <a name="iotwireless-GetPosition-response-Timestamp"></a>
The timestamp at which the device's position was determined.
Type: String
Pattern: `^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$`

## Errors
<a name="API_GetPosition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource does not exist.
 ** ResourceId **
Id of the not found resource.
 ** ResourceType **
Type of the font found resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_GetPosition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetPosition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetPosition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetPosition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetPosition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetPosition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetPosition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetPosition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetPosition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetPosition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetPosition)
