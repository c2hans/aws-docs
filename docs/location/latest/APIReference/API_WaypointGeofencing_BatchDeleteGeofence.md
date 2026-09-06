---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchDeleteGeofence.html
---

# BatchDeleteGeofence
<a name="API_WaypointGeofencing_BatchDeleteGeofence"></a>

Deletes a batch of geofences from a geofence collection.

**Note**
This operation deletes the resource permanently.

## Request Syntax
<a name="API_WaypointGeofencing_BatchDeleteGeofence_RequestSyntax"></a>

```
POST /geofencing/v0/collections/{{CollectionName}}/delete-geofences HTTP/1.1
Content-type: application/json

{
   "GeofenceIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_WaypointGeofencing_BatchDeleteGeofence_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CollectionName](#API_WaypointGeofencing_BatchDeleteGeofence_RequestSyntax) **   <a name="location-WaypointGeofencing_BatchDeleteGeofence-request-uri-CollectionName"></a>
The geofence collection storing the geofences to be deleted.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_WaypointGeofencing_BatchDeleteGeofence_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GeofenceIds](#API_WaypointGeofencing_BatchDeleteGeofence_RequestSyntax) **   <a name="location-WaypointGeofencing_BatchDeleteGeofence-request-GeofenceIds"></a>
The batch of geofences to be deleted.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

## Response Syntax
<a name="API_WaypointGeofencing_BatchDeleteGeofence_ResponseSyntax"></a>

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
   ]
}
```

## Response Elements
<a name="API_WaypointGeofencing_BatchDeleteGeofence_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_WaypointGeofencing_BatchDeleteGeofence_ResponseSyntax) **   <a name="location-WaypointGeofencing_BatchDeleteGeofence-response-Errors"></a>
Contains error details for each geofence that failed to delete.
Type: Array of [BatchDeleteGeofenceError](API_WaypointGeofencing_BatchDeleteGeofenceError.md) objects

## Errors
<a name="API_WaypointGeofencing_BatchDeleteGeofence_Errors"></a>

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
<a name="API_WaypointGeofencing_BatchDeleteGeofence_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waypointgeofencing-2020-11-19/BatchDeleteGeofence)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waypointgeofencing-2020-11-19/BatchDeleteGeofence)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointgeofencing-2020-11-19/BatchDeleteGeofence)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waypointgeofencing-2020-11-19/BatchDeleteGeofence)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointgeofencing-2020-11-19/BatchDeleteGeofence)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waypointgeofencing-2020-11-19/BatchDeleteGeofence)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waypointgeofencing-2020-11-19/BatchDeleteGeofence)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waypointgeofencing-2020-11-19/BatchDeleteGeofence)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waypointgeofencing-2020-11-19/BatchDeleteGeofence)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointgeofencing-2020-11-19/BatchDeleteGeofence)
