---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_StartApplication.html
---

# StartApplication
<a name="API_StartApplication"></a>

Starts a specified application and initializes initial capacity if configured.

## Request Syntax
<a name="API_StartApplication_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/start HTTP/1.1
```

## URI Request Parameters
<a name="API_StartApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_StartApplication_RequestSyntax) **   <a name="emrserverless-StartApplication-request-uri-applicationId"></a>
The ID of the application to start.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_StartApplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StartApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_StartApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StartApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Request processing failed because of an error or failure with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The maximum number of resources per account has been reached.
HTTP Status Code: 402

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_StartApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-serverless-2021-07-13/StartApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-serverless-2021-07-13/StartApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/StartApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-serverless-2021-07-13/StartApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/StartApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-serverless-2021-07-13/StartApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-serverless-2021-07-13/StartApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-serverless-2021-07-13/StartApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-serverless-2021-07-13/StartApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/StartApplication)
