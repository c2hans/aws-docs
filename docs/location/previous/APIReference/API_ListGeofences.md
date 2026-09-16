---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_ListGeofences.html
---

# ListGeofences
<a name="API_ListGeofences"></a>

Lists geofences stored in a given geofence collection.

## Request Syntax
<a name="API_ListGeofences_RequestSyntax"></a>

```
POST /geofencing/v0/collections/{{CollectionName}}/list-geofences HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListGeofences_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CollectionName](#API_ListGeofences_RequestSyntax) **   <a name="location-ListGeofences-request-uri-CollectionName"></a>
The name of the geofence collection storing the list of geofences.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_ListGeofences_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListGeofences_RequestSyntax) **   <a name="location-ListGeofences-request-MaxResults"></a>
An optional limit for the number of geofences returned in a single call.
Default value: `100`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListGeofences_RequestSyntax) **   <a name="location-ListGeofences-request-NextToken"></a>
The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.
Default value: `null`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60000.
Required: No

## Response Syntax
<a name="API_ListGeofences_ResponseSyntax"></a>

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
<a name="API_ListGeofences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entries](#API_ListGeofences_ResponseSyntax) **   <a name="location-ListGeofences-response-Entries"></a>
Contains a list of geofences stored in the geofence collection.
Type: Array of [ListGeofenceResponseEntry](API_ListGeofenceResponseEntry.md) objects

 ** [NextToken](#API_ListGeofences_ResponseSyntax) **   <a name="location-ListGeofences-response-NextToken"></a>
A pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60000.

## Errors
<a name="API_ListGeofences_Errors"></a>

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
<a name="API_ListGeofences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/ListGeofences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/ListGeofences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/ListGeofences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/ListGeofences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/ListGeofences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/ListGeofences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/ListGeofences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/ListGeofences)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/ListGeofences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/ListGeofences)
