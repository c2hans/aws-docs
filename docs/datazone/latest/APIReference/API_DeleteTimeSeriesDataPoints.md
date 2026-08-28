---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DeleteTimeSeriesDataPoints.html
---

# DeleteTimeSeriesDataPoints
<a name="API_DeleteTimeSeriesDataPoints"></a>

Deletes the specified time series form for the specified asset.

## Request Syntax
<a name="API_DeleteTimeSeriesDataPoints_RequestSyntax"></a>

```
DELETE /v2/domains/{{domainIdentifier}}/entities/{{entityType}}/{{entityIdentifier}}/time-series-data-points?clientToken={{clientToken}}&formName={{formName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteTimeSeriesDataPoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_DeleteTimeSeriesDataPoints_RequestSyntax) **   <a name="datazone-DeleteTimeSeriesDataPoints-request-uri-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`

 ** [domainIdentifier](#API_DeleteTimeSeriesDataPoints_RequestSyntax) **   <a name="datazone-DeleteTimeSeriesDataPoints-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain that houses the asset for which you want to delete a time series form.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [entityIdentifier](#API_DeleteTimeSeriesDataPoints_RequestSyntax) **   <a name="datazone-DeleteTimeSeriesDataPoints-request-uri-entityIdentifier"></a>
The ID of the asset for which you want to delete a time series form.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [entityType](#API_DeleteTimeSeriesDataPoints_RequestSyntax) **   <a name="datazone-DeleteTimeSeriesDataPoints-request-uri-entityType"></a>
The type of the asset for which you want to delete a time series form.
Valid Values: `ASSET | LISTING`
Required: Yes

 ** [formName](#API_DeleteTimeSeriesDataPoints_RequestSyntax) **   <a name="datazone-DeleteTimeSeriesDataPoints-request-uri-formName"></a>
The name of the time series form that you want to delete.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_DeleteTimeSeriesDataPoints_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteTimeSeriesDataPoints_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteTimeSeriesDataPoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteTimeSeriesDataPoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

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
<a name="API_DeleteTimeSeriesDataPoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/DeleteTimeSeriesDataPoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/DeleteTimeSeriesDataPoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DeleteTimeSeriesDataPoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/DeleteTimeSeriesDataPoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DeleteTimeSeriesDataPoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/DeleteTimeSeriesDataPoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/DeleteTimeSeriesDataPoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/DeleteTimeSeriesDataPoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/DeleteTimeSeriesDataPoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DeleteTimeSeriesDataPoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
