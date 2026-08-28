---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_ListMaps.html
---

# ListMaps
<a name="API_ListMaps"></a>

**Important**
This operation is no longer current and may be deprecated in the future. We recommend upgrading to the Maps API V2 unless you require `Grab` data.
 `ListMaps` is part of a previous Amazon Location Service Maps API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).
The Maps API version 2 has a simplified interface that can be used without creating or managing map resources.
If you are using an AWS SDK or the AWS CLI, note that the Maps API version 2 is found under `geo-maps` or `geo_maps`, not under `location`.
Since `Grab` is not yet fully supported in Maps API version 2, we recommend you continue using API version 1 when using `Grab`.
Start your version 2 API journey with the [Maps V2 API Reference](https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Maps_V2.html) or the [Developer Guide](https://docs.aws.amazon.com/location/latest/developerguide/maps.html).

Lists map resources in your AWS account.

## Request Syntax
<a name="API_ListMaps_RequestSyntax"></a>

```
POST /maps/v0/list-maps HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListMaps_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListMaps_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListMaps_RequestSyntax) **   <a name="location-ListMaps-request-MaxResults"></a>
An optional limit for the number of resources returned in a single call.
Default value: `100`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListMaps_RequestSyntax) **   <a name="location-ListMaps-request-NextToken"></a>
The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.
Default value: `null`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_ListMaps_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Entries": [
      {
         "CreateTime": "string",
         "DataSource": "string",
         "Description": "string",
         "MapName": "string",
         "PricingPlan": "string",
         "UpdateTime": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMaps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entries](#API_ListMaps_ResponseSyntax) **   <a name="location-ListMaps-response-Entries"></a>
Contains a list of maps in your AWS account
Type: Array of [ListMapsResponseEntry](API_ListMapsResponseEntry.md) objects

 ** [NextToken](#API_ListMaps_ResponseSyntax) **   <a name="location-ListMaps-response-NextToken"></a>
A pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_ListMaps_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed to process because of an unknown server error, exception, or failure.
HTTP Status Code: 500

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
<a name="API_ListMaps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/ListMaps)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/ListMaps)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/ListMaps)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/ListMaps)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/ListMaps)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/ListMaps)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/ListMaps)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/ListMaps)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/ListMaps)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/ListMaps)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
