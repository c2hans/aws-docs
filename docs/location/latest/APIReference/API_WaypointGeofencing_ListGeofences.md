---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ListGeofences.html
---

# ListGeofences
<a name="API_WaypointGeofencing_ListGeofences"></a>

Lists geofences stored in a given geofence collection.

## Request Syntax
<a name="API_WaypointGeofencing_ListGeofences_RequestSyntax"></a>

```
POST /geofencing/v0/collections/{{CollectionName}}/list-geofences HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_WaypointGeofencing_ListGeofences_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CollectionName](#API_WaypointGeofencing_ListGeofences_RequestSyntax) **   <a name="location-WaypointGeofencing_ListGeofences-request-uri-CollectionName"></a>
The name of the geofence collection storing the list of geofences.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_WaypointGeofencing_ListGeofences_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_WaypointGeofencing_ListGeofences_RequestSyntax) **   <a name="location-WaypointGeofencing_ListGeofences-request-MaxResults"></a>
An optional limit for the number of geofences returned in a single call.
Default value: `100`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_WaypointGeofencing_ListGeofences_RequestSyntax) **   <a name="location-WaypointGeofencing_ListGeofences-request-NextToken"></a>
The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.
Default value: `null`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60000.
Required: No

## Response Syntax
<a name="API_WaypointGeofencing_ListGeofences_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Entries": [
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_WaypointGeofencing_ListGeofences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entries](#API_WaypointGeofencing_ListGeofences_ResponseSyntax) **   <a name="location-WaypointGeofencing_ListGeofences-response-Entries"></a>
Contains a list of geofences stored in the geofence collection.
Type: Array of [ListGeofenceResponseEntry](API_WaypointGeofencing_ListGeofenceResponseEntry.md) objects

 ** [NextToken](#API_WaypointGeofencing_ListGeofences_ResponseSyntax) **   <a name="location-WaypointGeofencing_ListGeofences-response-NextToken"></a>
A pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60000.

## Errors
<a name="API_WaypointGeofencing_ListGeofences_Errors"></a>

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
<a name="API_WaypointGeofencing_ListGeofences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waypointgeofencing-2020-11-19/ListGeofences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waypointgeofencing-2020-11-19/ListGeofences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointgeofencing-2020-11-19/ListGeofences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waypointgeofencing-2020-11-19/ListGeofences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointgeofencing-2020-11-19/ListGeofences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waypointgeofencing-2020-11-19/ListGeofences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waypointgeofencing-2020-11-19/ListGeofences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waypointgeofencing-2020-11-19/ListGeofences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waypointgeofencing-2020-11-19/ListGeofences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointgeofencing-2020-11-19/ListGeofences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
