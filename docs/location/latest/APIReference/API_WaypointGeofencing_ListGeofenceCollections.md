---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ListGeofenceCollections.html
---

# ListGeofenceCollections
<a name="API_WaypointGeofencing_ListGeofenceCollections"></a>

Lists geofence collections in your AWS account.

## Request Syntax
<a name="API_WaypointGeofencing_ListGeofenceCollections_RequestSyntax"></a>

```
POST /geofencing/v0/list-collections HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_WaypointGeofencing_ListGeofenceCollections_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_WaypointGeofencing_ListGeofenceCollections_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_WaypointGeofencing_ListGeofenceCollections_RequestSyntax) **   <a name="location-WaypointGeofencing_ListGeofenceCollections-request-MaxResults"></a>
An optional limit for the number of resources returned in a single call.
Default value: `100`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_WaypointGeofencing_ListGeofenceCollections_RequestSyntax) **   <a name="location-WaypointGeofencing_ListGeofenceCollections-request-NextToken"></a>
The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.
Default value: `null`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_WaypointGeofencing_ListGeofenceCollections_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Entries": [
      {
         "CollectionName": "string",
         "CreateTime": "string",
         "Description": "string",
         "PricingPlan": "string",
         "PricingPlanDataSource": "string",
         "UpdateTime": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_WaypointGeofencing_ListGeofenceCollections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entries](#API_WaypointGeofencing_ListGeofenceCollections_ResponseSyntax) **   <a name="location-WaypointGeofencing_ListGeofenceCollections-response-Entries"></a>
Lists the geofence collections that exist in your AWS account.
Type: Array of [ListGeofenceCollectionsResponseEntry](API_WaypointGeofencing_ListGeofenceCollectionsResponseEntry.md) objects

 ** [NextToken](#API_WaypointGeofencing_ListGeofenceCollections_ResponseSyntax) **   <a name="location-WaypointGeofencing_ListGeofenceCollections-response-NextToken"></a>
A pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_WaypointGeofencing_ListGeofenceCollections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

HTTP Status Code: 403

 ** InternalServerException **

HTTP Status Code: 500

 ** ThrottlingException **

HTTP Status Code: 429

 ** ValidationException **

HTTP Status Code: 400

## See Also
<a name="API_WaypointGeofencing_ListGeofenceCollections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waypointgeofencing-2020-11-19/ListGeofenceCollections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waypointgeofencing-2020-11-19/ListGeofenceCollections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointgeofencing-2020-11-19/ListGeofenceCollections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waypointgeofencing-2020-11-19/ListGeofenceCollections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointgeofencing-2020-11-19/ListGeofenceCollections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waypointgeofencing-2020-11-19/ListGeofenceCollections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waypointgeofencing-2020-11-19/ListGeofenceCollections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waypointgeofencing-2020-11-19/ListGeofenceCollections)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waypointgeofencing-2020-11-19/ListGeofenceCollections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointgeofencing-2020-11-19/ListGeofenceCollections)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
