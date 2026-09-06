---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListVehicles.html
---

# ListVehicles
<a name="API_ListVehicles"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

 Retrieves a list of summaries of created vehicles.

**Note**
This API operation uses pagination. Specify the `nextToken` parameter in the request to return more results.

## Request Syntax
<a name="API_ListVehicles_RequestSyntax"></a>

```
{
   "attributeNames": [ "{{string}}" ],
   "attributeValues": [ "{{string}}" ],
   "listResponseScope": "{{string}}",
   "maxResults": {{number}},
   "modelManifestArn": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListVehicles_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [attributeNames](#API_ListVehicles_RequestSyntax) **   <a name="iotfleetwise-ListVehicles-request-attributeNames"></a>
The fully qualified names of the attributes. You can use this optional parameter to list the vehicles containing all the attributes in the request. For example, `attributeNames` could be "`Vehicle.Body.Engine.Type, Vehicle.Color`" and the corresponding `attributeValues` could be "`1.3 L R2, Blue`" . In this case, the API will filter vehicles with an attribute name `Vehicle.Body.Engine.Type` that contains a value of `1.3 L R2` AND an attribute name `Vehicle.Color` that contains a value of "`Blue`". A request must contain unique values for the `attributeNames` filter and the matching number of `attributeValues` filters to return the subset of vehicles that match the attributes filter condition.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** [attributeValues](#API_ListVehicles_RequestSyntax) **   <a name="iotfleetwise-ListVehicles-request-attributeValues"></a>
Static information about a vehicle attribute value in string format. You can use this optional parameter in conjunction with `attributeNames` to list the vehicles containing all the `attributeValues` corresponding to the `attributeNames` filter. For example, `attributeValues` could be "`1.3 L R2, Blue`" and the corresponding `attributeNames` filter could be "`Vehicle.Body.Engine.Type, Vehicle.Color`". In this case, the API will filter vehicles with attribute name `Vehicle.Body.Engine.Type` that contains a value of `1.3 L R2` AND an attribute name `Vehicle.Color` that contains a value of "`Blue`". A request must contain unique values for the `attributeNames` filter and the matching number of `attributeValues` filter to return the subset of vehicles that match the attributes filter condition.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [listResponseScope](#API_ListVehicles_RequestSyntax) **   <a name="iotfleetwise-ListVehicles-request-listResponseScope"></a>
When you set the `listResponseScope` parameter to `METADATA_ONLY`, the list response includes: vehicle name, Amazon Resource Name (ARN), creation time, and last modification time.
Type: String
Valid Values: `METADATA_ONLY`
Required: No

 ** [maxResults](#API_ListVehicles_RequestSyntax) **   <a name="iotfleetwise-ListVehicles-request-maxResults"></a>
The maximum number of items to return, between 1 and 100, inclusive.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [modelManifestArn](#API_ListVehicles_RequestSyntax) **   <a name="iotfleetwise-ListVehicles-request-modelManifestArn"></a>
 The Amazon Resource Name (ARN) of a vehicle model (model manifest). You can use this optional parameter to list only the vehicles created from a certain vehicle model.
Type: String
Required: No

 ** [nextToken](#API_ListVehicles_RequestSyntax) **   <a name="iotfleetwise-ListVehicles-request-nextToken"></a>
A pagination token for the next set of results.
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## Response Syntax
<a name="API_ListVehicles_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "vehicleSummaries": [
      {
         "arn": "string",
         "attributes": {
            "string" : "string"
         },
         "creationTime": number,
         "decoderManifestArn": "string",
         "lastModificationTime": number,
         "modelManifestArn": "string",
         "vehicleName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListVehicles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListVehicles_ResponseSyntax) **   <a name="iotfleetwise-ListVehicles-response-nextToken"></a>
 The token to retrieve the next set of results, or `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [vehicleSummaries](#API_ListVehicles_ResponseSyntax) **   <a name="iotfleetwise-ListVehicles-response-vehicleSummaries"></a>
 A list of vehicles and information about them.
Type: Array of [VehicleSummary](API_VehicleSummary.md) objects

## Errors
<a name="API_ListVehicles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request couldn't be completed because the server temporarily failed.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
HTTP Status Code: 500

 ** ThrottlingException **
The request couldn't be completed due to throttling.
 ** quotaCode **
The quota identifier of the applied throttling rules for this request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
 ** serviceCode **
The code for the service that couldn't be completed due to throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The list of fields that fail to satisfy the constraints specified by an AWS service.
 ** reason **
The reason the input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListVehicles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/ListVehicles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/ListVehicles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/ListVehicles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/ListVehicles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/ListVehicles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/ListVehicles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/ListVehicles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/ListVehicles)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/ListVehicles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/ListVehicles)
