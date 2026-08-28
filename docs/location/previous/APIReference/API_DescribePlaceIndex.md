---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_DescribePlaceIndex.html
---

# DescribePlaceIndex
<a name="API_DescribePlaceIndex"></a>

**Important**
This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Places API V2 unless you require Grab data.
 `DescribePlaceIndex` is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).
The Places API version 2 has a simplified interface that can be used without creating or managing place index resources.
If you are using an AWS SDK or the AWS CLI, note that the Places API version 2 is found under `geo-places` or `geo_places`, not under `location`.
Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.
Start your version 2 API journey with the Places V2 [API Reference](/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html) or the [Developer Guide](/location/latest/developerguide/places.html).

Retrieves the place index resource details.

## Request Syntax
<a name="API_DescribePlaceIndex_RequestSyntax"></a>

```
GET /places/v0/indexes/{{IndexName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribePlaceIndex_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IndexName](#API_DescribePlaceIndex_RequestSyntax) **   <a name="location-DescribePlaceIndex-request-uri-IndexName"></a>
The name of the place index resource.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_DescribePlaceIndex_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribePlaceIndex_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreateTime": "string",
   "DataSource": "string",
   "DataSourceConfiguration": {
      "IntendedUse": "string"
   },
   "Description": "string",
   "IndexArn": "string",
   "IndexName": "string",
   "PricingPlan": "string",
   "Tags": {
      "string" : "string"
   },
   "UpdateTime": "string"
}
```

## Response Elements
<a name="API_DescribePlaceIndex_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreateTime](#API_DescribePlaceIndex_ResponseSyntax) **   <a name="location-DescribePlaceIndex-response-CreateTime"></a>
The timestamp for when the place index resource was created in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp

 ** [DataSource](#API_DescribePlaceIndex_ResponseSyntax) **   <a name="location-DescribePlaceIndex-response-DataSource"></a>
The data provider of geospatial data. Values can be one of the following:
+  `Esri`
+  `Grab`
+  `Here`
For more information about data providers, see [Amazon Location Service data providers](https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html).
Type: String

 ** [DataSourceConfiguration](#API_DescribePlaceIndex_ResponseSyntax) **   <a name="location-DescribePlaceIndex-response-DataSourceConfiguration"></a>
The specified data storage option for requesting Places.
Type: [DataSourceConfiguration](API_DataSourceConfiguration.md) object

 ** [Description](#API_DescribePlaceIndex_ResponseSyntax) **   <a name="location-DescribePlaceIndex-response-Description"></a>
The optional description for the place index resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [IndexArn](#API_DescribePlaceIndex_ResponseSyntax) **   <a name="location-DescribePlaceIndex-response-IndexArn"></a>
The Amazon Resource Name (ARN) for the place index resource. Used to specify a resource across AWS.
+ Format example: `arn:aws:geo:region:account-id:place-index/ExamplePlaceIndex`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*):geo(:([a-z0-9]+([.-][a-z0-9]+)*))(:[0-9]+):((\*)|([-a-z]+[/][*-._\w]+))`

 ** [IndexName](#API_DescribePlaceIndex_ResponseSyntax) **   <a name="location-DescribePlaceIndex-response-IndexName"></a>
The name of the place index resource being described.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`

 ** [PricingPlan](#API_DescribePlaceIndex_ResponseSyntax) **   <a name="location-DescribePlaceIndex-response-PricingPlan"></a>
 *This parameter has been deprecated.*
No longer used. Always returns `RequestBasedUsage`.
Type: String
Valid Values: `RequestBasedUsage | MobileAssetTracking | MobileAssetManagement`

 ** [Tags](#API_DescribePlaceIndex_ResponseSyntax) **   <a name="location-DescribePlaceIndex-response-Tags"></a>
Tags associated with place index resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`

 ** [UpdateTime](#API_DescribePlaceIndex_ResponseSyntax) **   <a name="location-DescribePlaceIndex-response-UpdateTime"></a>
The timestamp for when the place index resource was last updated in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp

## Errors
<a name="API_DescribePlaceIndex_Errors"></a>

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
<a name="API_DescribePlaceIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/DescribePlaceIndex)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/DescribePlaceIndex)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/DescribePlaceIndex)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/DescribePlaceIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/DescribePlaceIndex)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/DescribePlaceIndex)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/DescribePlaceIndex)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/DescribePlaceIndex)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/DescribePlaceIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/DescribePlaceIndex)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
