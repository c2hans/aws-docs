---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_PutGeofence.html
---

# PutGeofence
<a name="API_PutGeofence"></a>

Stores a geofence geometry in a given geofence collection, or updates the geometry of an existing geofence if a geofence ID is included in the request.

## Request Syntax
<a name="API_PutGeofence_RequestSyntax"></a>

```
PUT /geofencing/v0/collections/{{CollectionName}}/geofences/{{GeofenceId}} HTTP/1.1
Content-type: application/json

{
   "GeofenceProperties": {
      "{{string}}" : "{{string}}"
   },
   "Geometry": {
      "Circle": {
         "Center": [ {{number}} ],
         "Radius": {{number}}
      },
      "Geobuf": {{blob}},
      "MultiPolygon": [
         [
            [
               [ {{number}} ]
            ]
         ]
      ],
      "Polygon": [
         [
            [ {{number}} ]
         ]
      ]
   }
}
```

## URI Request Parameters
<a name="API_PutGeofence_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CollectionName](#API_PutGeofence_RequestSyntax) **   <a name="location-PutGeofence-request-uri-CollectionName"></a>
The geofence collection to store the geofence in.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** [GeofenceId](#API_PutGeofence_RequestSyntax) **   <a name="location-PutGeofence-request-uri-GeofenceId"></a>
An identifier for the geofence. For example, `ExampleGeofence-1`.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

## Request Body
<a name="API_PutGeofence_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GeofenceProperties](#API_PutGeofence_RequestSyntax) **   <a name="location-PutGeofence-request-GeofenceProperties"></a>
Associates one of more properties with the geofence. A property is a key-value pair stored with the geofence and added to any geofence event triggered with that geofence.
Format: `"key" : "value"`
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 3 items.
Key Length Constraints: Minimum length of 1. Maximum length of 20.
Value Length Constraints: Minimum length of 1. Maximum length of 40.
Required: No

 ** [Geometry](#API_PutGeofence_RequestSyntax) **   <a name="location-PutGeofence-request-Geometry"></a>
Contains the details to specify the position of the geofence. Can be a circle, a polygon, or a multipolygon. `Polygon` and `MultiPolygon` geometries can be defined using their respective parameters, or encoded in Geobuf format using the `Geobuf` parameter. Including multiple geometry types in the same request will return a validation error.
The geofence `Polygon` and `MultiPolygon` formats support a maximum of 1,000 total vertices. The `Geobuf` format supports a maximum of 100,000 vertices.
Type: [GeofenceGeometry](API_GeofenceGeometry.md) object
Required: Yes

## Response Syntax
<a name="API_PutGeofence_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreateTime": "string",
   "GeofenceId": "string",
   "UpdateTime": "string"
}
```

## Response Elements
<a name="API_PutGeofence_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreateTime](#API_PutGeofence_ResponseSyntax) **   <a name="location-PutGeofence-response-CreateTime"></a>
The timestamp for when the geofence was created in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`
Type: Timestamp

 ** [GeofenceId](#API_PutGeofence_ResponseSyntax) **   <a name="location-PutGeofence-response-GeofenceId"></a>
The geofence identifier entered in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`

 ** [UpdateTime](#API_PutGeofence_ResponseSyntax) **   <a name="location-PutGeofence-response-UpdateTime"></a>
The timestamp for when the geofence was last updated in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`
Type: Timestamp

## Errors
<a name="API_PutGeofence_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.
HTTP Status Code: 403

 ** ConflictException **
The request was unsuccessful because of a conflict.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed to process because of an unknown server error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource that you've entered was not found in your AWS account.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because of request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** FieldList **
The field where the invalid entry was detected.
 ** Reason **
A message with the reason for the validation exception error.
HTTP Status Code: 400

## See Also
<a name="API_PutGeofence_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/PutGeofence)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/PutGeofence)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/PutGeofence)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/PutGeofence)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/PutGeofence)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/PutGeofence)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/PutGeofence)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/PutGeofence)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/PutGeofence)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/PutGeofence)
