---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_DeleteGeofenceCollection.html
---

# DeleteGeofenceCollection
<a name="API_WaypointGeofencing_DeleteGeofenceCollection"></a>

Deletes a geofence collection from your AWS account.

**Note**
This operation deletes the resource permanently. If the geofence collection is the target of a tracker resource, the devices will no longer be monitored.

## Request Syntax
<a name="API_WaypointGeofencing_DeleteGeofenceCollection_RequestSyntax"></a>

```
DELETE /geofencing/v0/collections/{{CollectionName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_WaypointGeofencing_DeleteGeofenceCollection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CollectionName](#API_WaypointGeofencing_DeleteGeofenceCollection_RequestSyntax) **   <a name="location-WaypointGeofencing_DeleteGeofenceCollection-request-uri-CollectionName"></a>
The name of the geofence collection to be deleted.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_WaypointGeofencing_DeleteGeofenceCollection_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_WaypointGeofencing_DeleteGeofenceCollection_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_WaypointGeofencing_DeleteGeofenceCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_WaypointGeofencing_DeleteGeofenceCollection_Errors"></a>

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
<a name="API_WaypointGeofencing_DeleteGeofenceCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waypointgeofencing-2020-11-19/DeleteGeofenceCollection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waypointgeofencing-2020-11-19/DeleteGeofenceCollection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointgeofencing-2020-11-19/DeleteGeofenceCollection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waypointgeofencing-2020-11-19/DeleteGeofenceCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointgeofencing-2020-11-19/DeleteGeofenceCollection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waypointgeofencing-2020-11-19/DeleteGeofenceCollection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waypointgeofencing-2020-11-19/DeleteGeofenceCollection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waypointgeofencing-2020-11-19/DeleteGeofenceCollection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/waypointgeofencing-2020-11-19/DeleteGeofenceCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointgeofencing-2020-11-19/DeleteGeofenceCollection)
