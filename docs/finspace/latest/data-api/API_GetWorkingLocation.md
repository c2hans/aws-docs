---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_GetWorkingLocation.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# GetWorkingLocation
<a name="API_GetWorkingLocation"></a>

A temporary Amazon S3 location, where you can copy your files from a source location to stage or use as a scratch space in FinSpace notebook.

## Request Syntax
<a name="API_GetWorkingLocation_RequestSyntax"></a>

```
POST /workingLocationV1 HTTP/1.1
Content-type: application/json

{
   "locationType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetWorkingLocation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetWorkingLocation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [locationType](#API_GetWorkingLocation_RequestSyntax) **   <a name="finspace-GetWorkingLocation-request-locationType"></a>
Specify the type of the working location.
+  `SAGEMAKER` – Use the Amazon S3 location as a temporary location to store data content when working with FinSpace Notebooks that run on SageMaker studio.
+  `INGESTION` – Use the Amazon S3 location as a staging location to copy your data content and then use the location with the Changeset creation operation.
Type: String
Valid Values: `INGESTION | SAGEMAKER`
Required: No

## Response Syntax
<a name="API_GetWorkingLocation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "s3Bucket": "string",
   "s3Path": "string",
   "s3Uri": "string"
}
```

## Response Elements
<a name="API_GetWorkingLocation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [s3Bucket](#API_GetWorkingLocation_ResponseSyntax) **   <a name="finspace-GetWorkingLocation-response-s3Bucket"></a>
Returns the Amazon S3 bucket name for the working location.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `.*\S.*`

 ** [s3Path](#API_GetWorkingLocation_ResponseSyntax) **   <a name="finspace-GetWorkingLocation-response-s3Path"></a>
Returns the Amazon S3 Path for the working location.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [s3Uri](#API_GetWorkingLocation_ResponseSyntax) **   <a name="finspace-GetWorkingLocation-response-s3Uri"></a>
Returns the Amazon S3 URI for the working location.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

## Errors
<a name="API_GetWorkingLocation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetWorkingLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2020-07-13/GetWorkingLocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2020-07-13/GetWorkingLocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/GetWorkingLocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2020-07-13/GetWorkingLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/GetWorkingLocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2020-07-13/GetWorkingLocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2020-07-13/GetWorkingLocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2020-07-13/GetWorkingLocation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2020-07-13/GetWorkingLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/GetWorkingLocation)
