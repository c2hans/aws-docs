---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_GetGeofence.html
---

# GetGeofence
<a name="API_GetGeofence"></a>

Retrieves the geofence details from a geofence collection.

**Note**
The returned geometry will always match the geometry format used when the geofence was created.

## Request Syntax
<a name="API_GetGeofence_RequestSyntax"></a>

```
GET /geofencing/v0/collections/{{CollectionName}}/geofences/{{GeofenceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetGeofence_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CollectionName](#API_GetGeofence_RequestSyntax) **   <a name="location-GetGeofence-request-uri-CollectionName"></a>
The geofence collection storing the target geofence.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** [GeofenceId](#API_GetGeofence_RequestSyntax) **   <a name="location-GetGeofence-request-uri-GeofenceId"></a>
The geofence you're retrieving details for.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

## Request Body
<a name="API_GetGeofence_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetGeofence_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreateTime": "string",
   "GeofenceId": "string",
   "GeofenceProperties": {
      "string" : "string"
   },
   "Geometry": {
      "Circle": {
         "Center": [ number ],
         "Radius": number
      },
      "Geobuf": blob,
      "MultiPolygon": [
         [
            [
               [ number ]
            ]
         ]
      ],
      "Polygon": [
         [
            [ number ]
         ]
      ]
   },
   "Status": "string",
   "UpdateTime": "string"
}
```

## Response Elements
<a name="API_GetGeofence_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreateTime](#API_GetGeofence_ResponseSyntax) **   <a name="location-GetGeofence-response-CreateTime"></a>
The timestamp for when the geofence collection was created in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`
Type: Timestamp

 ** [GeofenceId](#API_GetGeofence_ResponseSyntax) **   <a name="location-GetGeofence-response-GeofenceId"></a>
The geofence identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`

 ** [GeofenceProperties](#API_GetGeofence_ResponseSyntax) **   <a name="location-GetGeofence-response-GeofenceProperties"></a>
User defined properties of the geofence. A property is a key-value pair stored with the geofence and added to any geofence event triggered with that geofence.
Format: `"key" : "value"`
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 3 items.
Key Length Constraints: Minimum length of 1. Maximum length of 20.
Value Length Constraints: Minimum length of 1. Maximum length of 40.

 ** [Geometry](#API_GetGeofence_ResponseSyntax) **   <a name="location-GetGeofence-response-Geometry"></a>
Contains the geofence geometry details describing the position of the geofence. Can be a circle, a polygon, or a multipolygon.
Type: [GeofenceGeometry](API_GeofenceGeometry.md) object

 ** [Status](#API_GetGeofence_ResponseSyntax) **   <a name="location-GetGeofence-response-Status"></a>
Identifies the state of the geofence. A geofence will hold one of the following states:
+  `ACTIVE` — The geofence has been indexed by the system.
+  `PENDING` — The geofence is being processed by the system.
+  `FAILED` — The geofence failed to be indexed by the system.
+  `DELETED` — The geofence has been deleted from the system index.
+  `DELETING` — The geofence is being deleted from the system index.
Type: String

 ** [UpdateTime](#API_GetGeofence_ResponseSyntax) **   <a name="location-GetGeofence-response-UpdateTime"></a>
The timestamp for when the geofence collection was last updated in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`
Type: Timestamp

## Errors
<a name="API_GetGeofence_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.
HTTP Status Code: 403

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
<a name="API_GetGeofence_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/GetGeofence)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/GetGeofence)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/GetGeofence)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/GetGeofence)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/GetGeofence)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/GetGeofence)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/GetGeofence)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/GetGeofence)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/GetGeofence)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/GetGeofence)
