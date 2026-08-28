---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_DeleteEarthObservationJob.html
---

# DeleteEarthObservationJob
<a name="API_geospatial_DeleteEarthObservationJob"></a>

Use this operation to delete an Earth Observation job.

## Request Syntax
<a name="API_geospatial_DeleteEarthObservationJob_RequestSyntax"></a>

```
DELETE /earth-observation-jobs/{{Arn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_geospatial_DeleteEarthObservationJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Arn](#API_geospatial_DeleteEarthObservationJob_RequestSyntax) **   <a name="sagemaker-geospatial_DeleteEarthObservationJob-request-uri-Arn"></a>
The Amazon Resource Name (ARN) of the Earth Observation job being deleted.
Pattern: `arn:aws[a-z-]{0,12}:sagemaker-geospatial:[a-z0-9-]{1,25}:[0-9]{12}:earth-observation-job/[a-z0-9]{12,}`
Required: Yes

## Request Body
<a name="API_geospatial_DeleteEarthObservationJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_geospatial_DeleteEarthObservationJob_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_geospatial_DeleteEarthObservationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_geospatial_DeleteEarthObservationJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** ResourceId **
Identifier of the resource affected.
HTTP Status Code: 409

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
<a name="API_geospatial_DeleteEarthObservationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-geospatial-2020-05-27/DeleteEarthObservationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-geospatial-2020-05-27/DeleteEarthObservationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/DeleteEarthObservationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-geospatial-2020-05-27/DeleteEarthObservationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/DeleteEarthObservationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-geospatial-2020-05-27/DeleteEarthObservationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-geospatial-2020-05-27/DeleteEarthObservationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-geospatial-2020-05-27/DeleteEarthObservationJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-geospatial-2020-05-27/DeleteEarthObservationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/DeleteEarthObservationJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
