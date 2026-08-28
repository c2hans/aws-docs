---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeGeofenceCollection.html
---

# DescribeGeofenceCollection
<a name="API_DescribeGeofenceCollection"></a>

Retrieves the geofence collection details.

## Request Syntax
<a name="API_DescribeGeofenceCollection_RequestSyntax"></a>

```
GET /geofencing/v0/collections/{{CollectionName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeGeofenceCollection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CollectionName](#API_DescribeGeofenceCollection_RequestSyntax) **   <a name="location-DescribeGeofenceCollection-request-uri-CollectionName"></a>
The name of the geofence collection.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_DescribeGeofenceCollection_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeGeofenceCollection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CollectionArn": "string",
   "CollectionName": "string",
   "CreateTime": "string",
   "Description": "string",
   "GeofenceCount": number,
   "KmsKeyId": "string",
   "PricingPlan": "string",
   "PricingPlanDataSource": "string",
   "Tags": {
      "string" : "string"
   },
   "UpdateTime": "string"
}
```

## Response Elements
<a name="API_DescribeGeofenceCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CollectionArn](#API_DescribeGeofenceCollection_ResponseSyntax) **   <a name="location-DescribeGeofenceCollection-response-CollectionArn"></a>
The Amazon Resource Name (ARN) for the geofence collection resource. Used when you need to specify a resource across all AWS.
+ Format example: `arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollection`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`

 ** [CollectionName](#API_DescribeGeofenceCollection_ResponseSyntax) **   <a name="location-DescribeGeofenceCollection-response-CollectionName"></a>
The name of the geofence collection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`

 ** [CreateTime](#API_DescribeGeofenceCollection_ResponseSyntax) **   <a name="location-DescribeGeofenceCollection-response-CreateTime"></a>
The timestamp for when the geofence resource was created in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`
Type: Timestamp

 ** [Description](#API_DescribeGeofenceCollection_ResponseSyntax) **   <a name="location-DescribeGeofenceCollection-response-Description"></a>
The optional description for the geofence collection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [GeofenceCount](#API_DescribeGeofenceCollection_ResponseSyntax) **   <a name="location-DescribeGeofenceCollection-response-GeofenceCount"></a>
The number of geofences in the geofence collection.
Type: Integer
Valid Range: Minimum value of 0.

 ** [KmsKeyId](#API_DescribeGeofenceCollection_ResponseSyntax) **   <a name="location-DescribeGeofenceCollection-response-KmsKeyId"></a>
A key identifier for an [AWS KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) assigned to the Amazon Location resource
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [PricingPlan](#API_DescribeGeofenceCollection_ResponseSyntax) **   <a name="location-DescribeGeofenceCollection-response-PricingPlan"></a>
 *This parameter has been deprecated.*
No longer used. Always returns `RequestBasedUsage`.
Type: String
Valid Values: `RequestBasedUsage | MobileAssetTracking | MobileAssetManagement`

 ** [PricingPlanDataSource](#API_DescribeGeofenceCollection_ResponseSyntax) **   <a name="location-DescribeGeofenceCollection-response-PricingPlanDataSource"></a>
 *This parameter has been deprecated.*
No longer used. Always returns an empty string.
Type: String

 ** [Tags](#API_DescribeGeofenceCollection_ResponseSyntax) **   <a name="location-DescribeGeofenceCollection-response-Tags"></a>
Displays the key, value pairs of tags associated with this resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`

 ** [UpdateTime](#API_DescribeGeofenceCollection_ResponseSyntax) **   <a name="location-DescribeGeofenceCollection-response-UpdateTime"></a>
The timestamp for when the geofence collection was last updated in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`
Type: Timestamp

## Errors
<a name="API_DescribeGeofenceCollection_Errors"></a>

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
<a name="API_DescribeGeofenceCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/DescribeGeofenceCollection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/DescribeGeofenceCollection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/DescribeGeofenceCollection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/DescribeGeofenceCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/DescribeGeofenceCollection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/DescribeGeofenceCollection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/DescribeGeofenceCollection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/DescribeGeofenceCollection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/DescribeGeofenceCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/DescribeGeofenceCollection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
