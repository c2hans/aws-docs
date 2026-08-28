---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_GetTile.html
---

# GetTile
<a name="API_geospatial_GetTile"></a>

Gets a web mercator tile for the given Earth Observation job.

## Request Syntax
<a name="API_geospatial_GetTile_RequestSyntax"></a>

```
GET /tile/{{z}}/{{x}}/{{y}}?Arn={{Arn}}&ExecutionRoleArn={{ExecutionRoleArn}}&ImageAssets={{ImageAssets}}&ImageMask={{ImageMask}}&OutputDataType={{OutputDataType}}&OutputFormat={{OutputFormat}}&PropertyFilters={{PropertyFilters}}&Target={{Target}}&TimeRangeFilter={{TimeRangeFilter}} HTTP/1.1
```

## URI Request Parameters
<a name="API_geospatial_GetTile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Arn](#API_geospatial_GetTile_RequestSyntax) **   <a name="sagemaker-geospatial_GetTile-request-uri-Arn"></a>
The Amazon Resource Name (ARN) of the tile operation.
Pattern: `arn:aws[a-z-]{0,12}:sagemaker-geospatial:[a-z0-9-]{1,25}:[0-9]{12}:earth-observation-job/[a-z0-9]{12,}`
Required: Yes

 ** [ExecutionRoleArn](#API_geospatial_GetTile_RequestSyntax) **   <a name="sagemaker-geospatial_GetTile-request-uri-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that you specify.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-z-]*):iam::([0-9]{12}):role/[a-zA-Z0-9+=,.@_/-]+`

 ** [ImageAssets](#API_geospatial_GetTile_RequestSyntax) **   <a name="sagemaker-geospatial_GetTile-request-uri-ImageAssets"></a>
The particular assets or bands to tile.
Array Members: Minimum number of 1 item.
Required: Yes

 ** [ImageMask](#API_geospatial_GetTile_RequestSyntax) **   <a name="sagemaker-geospatial_GetTile-request-uri-ImageMask"></a>
Determines whether or not to return a valid data mask.

 ** [OutputDataType](#API_geospatial_GetTile_RequestSyntax) **   <a name="sagemaker-geospatial_GetTile-request-uri-OutputDataType"></a>
The output data type of the tile operation.
Valid Values: `INT32 | FLOAT32 | INT16 | FLOAT64 | UINT16`

 ** [OutputFormat](#API_geospatial_GetTile_RequestSyntax) **   <a name="sagemaker-geospatial_GetTile-request-uri-OutputFormat"></a>
The data format of the output tile. The formats include .npy, .png and .jpg.

 ** [PropertyFilters](#API_geospatial_GetTile_RequestSyntax) **   <a name="sagemaker-geospatial_GetTile-request-uri-PropertyFilters"></a>
Property filters for the imagery to tile.

 ** [Target](#API_geospatial_GetTile_RequestSyntax) **   <a name="sagemaker-geospatial_GetTile-request-uri-Target"></a>
Determines what part of the Earth Observation job to tile. 'INPUT' or 'OUTPUT' are the valid options.
Valid Values: `INPUT | OUTPUT`
Required: Yes

 ** [TimeRangeFilter](#API_geospatial_GetTile_RequestSyntax) **   <a name="sagemaker-geospatial_GetTile-request-uri-TimeRangeFilter"></a>
Time range filter applied to imagery to find the images to tile.

 ** [x](#API_geospatial_GetTile_RequestSyntax) **   <a name="sagemaker-geospatial_GetTile-request-uri-x"></a>
The x coordinate of the tile input.
Required: Yes

 ** [y](#API_geospatial_GetTile_RequestSyntax) **   <a name="sagemaker-geospatial_GetTile-request-uri-y"></a>
The y coordinate of the tile input.
Required: Yes

 ** [z](#API_geospatial_GetTile_RequestSyntax) **   <a name="sagemaker-geospatial_GetTile-request-uri-z"></a>
The z coordinate of the tile input.
Required: Yes

## Request Body
<a name="API_geospatial_GetTile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_geospatial_GetTile_ResponseSyntax"></a>

```
HTTP/1.1 200

{{BinaryFile}}
```

## Response Elements
<a name="API_geospatial_GetTile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following as the HTTP body.

 ** [BinaryFile](#API_geospatial_GetTile_ResponseSyntax) **   <a name="sagemaker-geospatial_GetTile-response-BinaryFile"></a>
The output binary file.

## Errors
<a name="API_geospatial_GetTile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
 ** ResourceId **

HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource which does not exist.
 ** ResourceId **
Identifier of the resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** ResourceId **

HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** ResourceId **

HTTP Status Code: 400

## See Also
<a name="API_geospatial_GetTile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-geospatial-2020-05-27/GetTile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-geospatial-2020-05-27/GetTile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/GetTile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-geospatial-2020-05-27/GetTile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/GetTile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-geospatial-2020-05-27/GetTile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-geospatial-2020-05-27/GetTile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-geospatial-2020-05-27/GetTile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-geospatial-2020-05-27/GetTile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/GetTile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
