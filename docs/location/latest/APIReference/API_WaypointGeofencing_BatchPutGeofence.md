---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchPutGeofence.html
---

# BatchPutGeofence
<a name="API_WaypointGeofencing_BatchPutGeofence"></a>

A batch request for storing geofence geometries into a given geofence collection, or updates the geometry of an existing geofence if a geofence ID is included in the request.

## Request Syntax
<a name="API_WaypointGeofencing_BatchPutGeofence_RequestSyntax"></a>

```
POST /geofencing/v0/collections/{{CollectionName}}/put-geofences HTTP/1.1
Content-type: application/json

{
   "Entries": [
      {
         "GeofenceId": "{{string}}",
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
   ]
}
```

## URI Request Parameters
<a name="API_WaypointGeofencing_BatchPutGeofence_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CollectionName](#API_WaypointGeofencing_BatchPutGeofence_RequestSyntax) **   <a name="location-WaypointGeofencing_BatchPutGeofence-request-uri-CollectionName"></a>
The geofence collection storing the geofences.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_WaypointGeofencing_BatchPutGeofence_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Entries](#API_WaypointGeofencing_BatchPutGeofence_RequestSyntax) **   <a name="location-WaypointGeofencing_BatchPutGeofence-request-Entries"></a>
The batch of geofences to be stored in a geofence collection.
Type: Array of [BatchPutGeofenceRequestEntry](API_WaypointGeofencing_BatchPutGeofenceRequestEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## Response Syntax
<a name="API_WaypointGeofencing_BatchPutGeofence_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Errors": [
      {
         "Error": {
            "Code": "string",
            "Message": "string"
         },
         "GeofenceId": "string"
      }
   ],
   "Successes": [
      {
         "CreateTime": "string",
         "GeofenceId": "string",
         "UpdateTime": "string"
      }
   ]
}
```

## Response Elements
<a name="API_WaypointGeofencing_BatchPutGeofence_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_WaypointGeofencing_BatchPutGeofence_ResponseSyntax) **   <a name="location-WaypointGeofencing_BatchPutGeofence-response-Errors"></a>
Contains additional error details for each geofence that failed to be stored in a geofence collection.
Type: Array of [BatchPutGeofenceError](API_WaypointGeofencing_BatchPutGeofenceError.md) objects

 ** [Successes](#API_WaypointGeofencing_BatchPutGeofence_ResponseSyntax) **   <a name="location-WaypointGeofencing_BatchPutGeofence-response-Successes"></a>
Contains each geofence that was successfully stored in a geofence collection.
Type: Array of [BatchPutGeofenceSuccess](API_WaypointGeofencing_BatchPutGeofenceSuccess.md) objects

## Errors
<a name="API_WaypointGeofencing_BatchPutGeofence_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

HTTP Status Code: 403

 ** InternalServerException **

HTTP Status Code: 500

 ** ResourceNotFoundException **

HTTP Status Code: 404

 ** ThrottlingException **

HTTP Status Code: 429

 ** ValidationException **

HTTP Status Code: 400

## See Also
<a name="API_WaypointGeofencing_BatchPutGeofence_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waypointgeofencing-2020-11-19/BatchPutGeofence)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waypointgeofencing-2020-11-19/BatchPutGeofence)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointgeofencing-2020-11-19/BatchPutGeofence)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waypointgeofencing-2020-11-19/BatchPutGeofence)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointgeofencing-2020-11-19/BatchPutGeofence)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waypointgeofencing-2020-11-19/BatchPutGeofence)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waypointgeofencing-2020-11-19/BatchPutGeofence)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waypointgeofencing-2020-11-19/BatchPutGeofence)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waypointgeofencing-2020-11-19/BatchPutGeofence)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointgeofencing-2020-11-19/BatchPutGeofence)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
