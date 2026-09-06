---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_ListTrackerConsumers.html
---

# ListTrackerConsumers
<a name="API_WaypointTracking_ListTrackerConsumers"></a>

Lists geofence collections currently associated to the given tracker resource.

## Request Syntax
<a name="API_WaypointTracking_ListTrackerConsumers_RequestSyntax"></a>

```
POST /tracking/v0/trackers/{{TrackerName}}/list-consumers HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_WaypointTracking_ListTrackerConsumers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TrackerName](#API_WaypointTracking_ListTrackerConsumers_RequestSyntax) **   <a name="location-WaypointTracking_ListTrackerConsumers-request-uri-TrackerName"></a>
The tracker resource whose associated geofence collections you want to list.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_WaypointTracking_ListTrackerConsumers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_WaypointTracking_ListTrackerConsumers_RequestSyntax) **   <a name="location-WaypointTracking_ListTrackerConsumers-request-MaxResults"></a>
An optional limit for the number of resources returned in a single call.
Default value: `100`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_WaypointTracking_ListTrackerConsumers_RequestSyntax) **   <a name="location-WaypointTracking_ListTrackerConsumers-request-NextToken"></a>
The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.
Default value: `null`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_WaypointTracking_ListTrackerConsumers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConsumerArns": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_WaypointTracking_ListTrackerConsumers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConsumerArns](#API_WaypointTracking_ListTrackerConsumers_ResponseSyntax) **   <a name="location-WaypointTracking_ListTrackerConsumers-response-ConsumerArns"></a>
Contains the list of geofence collection ARNs associated to the tracker resource.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`

 ** [NextToken](#API_WaypointTracking_ListTrackerConsumers_ResponseSyntax) **   <a name="location-WaypointTracking_ListTrackerConsumers-response-NextToken"></a>
A pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_WaypointTracking_ListTrackerConsumers_Errors"></a>

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
<a name="API_WaypointTracking_ListTrackerConsumers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waypointtracking-2020-11-19/ListTrackerConsumers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waypointtracking-2020-11-19/ListTrackerConsumers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointtracking-2020-11-19/ListTrackerConsumers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waypointtracking-2020-11-19/ListTrackerConsumers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointtracking-2020-11-19/ListTrackerConsumers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waypointtracking-2020-11-19/ListTrackerConsumers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waypointtracking-2020-11-19/ListTrackerConsumers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waypointtracking-2020-11-19/ListTrackerConsumers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waypointtracking-2020-11-19/ListTrackerConsumers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointtracking-2020-11-19/ListTrackerConsumers)
