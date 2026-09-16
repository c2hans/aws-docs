---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_UpdateGeofenceCollection.html
---

# UpdateGeofenceCollection
<a name="API_WaypointGeofencing_UpdateGeofenceCollection"></a>

Updates the specified properties of a given geofence collection.

## Request Syntax
<a name="API_WaypointGeofencing_UpdateGeofenceCollection_RequestSyntax"></a>

```
PATCH /geofencing/v0/collections/{{CollectionName}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "PricingPlan": "{{string}}",
   "PricingPlanDataSource": "{{string}}"
}
```

## URI Request Parameters
<a name="API_WaypointGeofencing_UpdateGeofenceCollection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CollectionName](#API_WaypointGeofencing_UpdateGeofenceCollection_RequestSyntax) **   <a name="location-WaypointGeofencing_UpdateGeofenceCollection-request-uri-CollectionName"></a>
The name of the geofence collection to update.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_WaypointGeofencing_UpdateGeofenceCollection_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_WaypointGeofencing_UpdateGeofenceCollection_RequestSyntax) **   <a name="location-WaypointGeofencing_UpdateGeofenceCollection-request-Description"></a>
Updates the description for the geofence collection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [PricingPlan](#API_WaypointGeofencing_UpdateGeofenceCollection_RequestSyntax) **   <a name="location-WaypointGeofencing_UpdateGeofenceCollection-request-PricingPlan"></a>
 *This parameter has been deprecated.*
No longer used. If included, the only allowed value is `RequestBasedUsage`.
Type: String
Valid Values: `RequestBasedUsage | MobileAssetTracking | MobileAssetManagement`
Required: No

 ** [PricingPlanDataSource](#API_WaypointGeofencing_UpdateGeofenceCollection_RequestSyntax) **   <a name="location-WaypointGeofencing_UpdateGeofenceCollection-request-PricingPlanDataSource"></a>
 *This parameter has been deprecated.*
This parameter is no longer used.
Type: String
Required: No

## Response Syntax
<a name="API_WaypointGeofencing_UpdateGeofenceCollection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CollectionArn": "string",
   "CollectionName": "string",
   "UpdateTime": "string"
}
```

## Response Elements
<a name="API_WaypointGeofencing_UpdateGeofenceCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CollectionArn](#API_WaypointGeofencing_UpdateGeofenceCollection_ResponseSyntax) **   <a name="location-WaypointGeofencing_UpdateGeofenceCollection-response-CollectionArn"></a>
The Amazon Resource Name (ARN) of the updated geofence collection. Used to specify a resource across AWS.
+ Format example: `arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollection`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`

 ** [CollectionName](#API_WaypointGeofencing_UpdateGeofenceCollection_ResponseSyntax) **   <a name="location-WaypointGeofencing_UpdateGeofenceCollection-response-CollectionName"></a>
The name of the updated geofence collection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`

 ** [UpdateTime](#API_WaypointGeofencing_UpdateGeofenceCollection_ResponseSyntax) **   <a name="location-WaypointGeofencing_UpdateGeofenceCollection-response-UpdateTime"></a>
The time when the geofence collection was last updated in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`
Type: Timestamp

## Errors
<a name="API_WaypointGeofencing_UpdateGeofenceCollection_Errors"></a>

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
<a name="API_WaypointGeofencing_UpdateGeofenceCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waypointgeofencing-2020-11-19/UpdateGeofenceCollection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waypointgeofencing-2020-11-19/UpdateGeofenceCollection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointgeofencing-2020-11-19/UpdateGeofenceCollection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waypointgeofencing-2020-11-19/UpdateGeofenceCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointgeofencing-2020-11-19/UpdateGeofenceCollection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waypointgeofencing-2020-11-19/UpdateGeofenceCollection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waypointgeofencing-2020-11-19/UpdateGeofenceCollection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waypointgeofencing-2020-11-19/UpdateGeofenceCollection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/waypointgeofencing-2020-11-19/UpdateGeofenceCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointgeofencing-2020-11-19/UpdateGeofenceCollection)
