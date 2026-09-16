---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_PostTimeSeriesDataPoints.html
---

# PostTimeSeriesDataPoints
<a name="API_PostTimeSeriesDataPoints"></a>

Posts time series data points to Amazon DataZone for the specified asset.

## Request Syntax
<a name="API_PostTimeSeriesDataPoints_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/entities/{{entityType}}/{{entityIdentifier}}/time-series-data-points HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "forms": [
      {
         "content": "{{string}}",
         "formName": "{{string}}",
         "timestamp": {{number}},
         "typeIdentifier": "{{string}}",
         "typeRevision": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_PostTimeSeriesDataPoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_PostTimeSeriesDataPoints_RequestSyntax) **   <a name="datazone-PostTimeSeriesDataPoints-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which you want to post time series data points.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [entityIdentifier](#API_PostTimeSeriesDataPoints_RequestSyntax) **   <a name="datazone-PostTimeSeriesDataPoints-request-uri-entityIdentifier"></a>
The ID of the asset for which you want to post time series data points.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [entityType](#API_PostTimeSeriesDataPoints_RequestSyntax) **   <a name="datazone-PostTimeSeriesDataPoints-request-uri-entityType"></a>
The type of the asset for which you want to post data points.
Valid Values: `ASSET | LISTING`
Required: Yes

## Request Body
<a name="API_PostTimeSeriesDataPoints_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_PostTimeSeriesDataPoints_RequestSyntax) **   <a name="datazone-PostTimeSeriesDataPoints-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [forms](#API_PostTimeSeriesDataPoints_RequestSyntax) **   <a name="datazone-PostTimeSeriesDataPoints-request-forms"></a>
The forms that contain the data points that you want to post.
Type: Array of [TimeSeriesDataPointFormInput](API_TimeSeriesDataPointFormInput.md) objects
Required: Yes

## Response Syntax
<a name="API_PostTimeSeriesDataPoints_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "domainId": "string",
   "entityId": "string",
   "entityType": "string",
   "forms": [
      {
         "content": "string",
         "formName": "string",
         "id": "string",
         "timestamp": number,
         "typeIdentifier": "string",
         "typeRevision": "string"
      }
   ]
}
```

## Response Elements
<a name="API_PostTimeSeriesDataPoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [domainId](#API_PostTimeSeriesDataPoints_ResponseSyntax) **   <a name="datazone-PostTimeSeriesDataPoints-response-domainId"></a>
The ID of the Amazon DataZone domain in which you want to post time series data points.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [entityId](#API_PostTimeSeriesDataPoints_ResponseSyntax) **   <a name="datazone-PostTimeSeriesDataPoints-response-entityId"></a>
The ID of the asset for which you want to post time series data points.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [entityType](#API_PostTimeSeriesDataPoints_ResponseSyntax) **   <a name="datazone-PostTimeSeriesDataPoints-response-entityType"></a>
The type of the asset for which you want to post data points.
Type: String
Valid Values: `ASSET | LISTING`

 ** [forms](#API_PostTimeSeriesDataPoints_ResponseSyntax) **   <a name="datazone-PostTimeSeriesDataPoints-response-forms"></a>
The forms that contain the data points that you have posted.
Type: Array of [TimeSeriesDataPointFormOutput](API_TimeSeriesDataPointFormOutput.md) objects

## Errors
<a name="API_PostTimeSeriesDataPoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request has exceeded the specified service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_PostTimeSeriesDataPoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/PostTimeSeriesDataPoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/PostTimeSeriesDataPoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/PostTimeSeriesDataPoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/PostTimeSeriesDataPoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/PostTimeSeriesDataPoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/PostTimeSeriesDataPoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/PostTimeSeriesDataPoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/PostTimeSeriesDataPoints)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/PostTimeSeriesDataPoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/PostTimeSeriesDataPoints)
