---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_StopJobRun.html
---

# StopJobRun
<a name="API_StopJobRun"></a>

Stops a particular run of a job.

## Request Syntax
<a name="API_StopJobRun_RequestSyntax"></a>

```
POST /jobs/{{name}}/jobRun/{{runId}}/stopJobRun HTTP/1.1
```

## URI Request Parameters
<a name="API_StopJobRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_StopJobRun_RequestSyntax) **   <a name="databrew-StopJobRun-request-uri-Name"></a>
The name of the job to be stopped.
Length Constraints: Minimum length of 1. Maximum length of 240.
Required: Yes

 ** [runId](#API_StopJobRun_RequestSyntax) **   <a name="databrew-StopJobRun-request-uri-RunId"></a>
The ID of the job run to be stopped.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_StopJobRun_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StopJobRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RunId": "string"
}
```

## Response Elements
<a name="API_StopJobRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RunId](#API_StopJobRun_ResponseSyntax) **   <a name="databrew-StopJobRun-response-RunId"></a>
The ID of the job run that you stopped.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_StopJobRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_StopJobRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/StopJobRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/StopJobRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/StopJobRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/StopJobRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/StopJobRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/StopJobRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/StopJobRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/StopJobRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/StopJobRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/StopJobRun)
