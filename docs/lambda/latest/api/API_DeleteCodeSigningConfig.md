---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_DeleteCodeSigningConfig.html
---

# DeleteCodeSigningConfig
<a name="API_DeleteCodeSigningConfig"></a>

Deletes the code signing configuration. You can delete the code signing configuration only if no function is using it.

## Request Syntax
<a name="API_DeleteCodeSigningConfig_RequestSyntax"></a>

```
DELETE /2020-04-22/code-signing-configs/{{CodeSigningConfigArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteCodeSigningConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CodeSigningConfigArn](#API_DeleteCodeSigningConfig_RequestSyntax) **   <a name="lambda-DeleteCodeSigningConfig-request-uri-CodeSigningConfigArn"></a>
The The Amazon Resource Name (ARN) of the code signing configuration.
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:code-signing-config:csc-[a-z0-9]{17}`
Required: Yes

## Request Body
<a name="API_DeleteCodeSigningConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCodeSigningConfig_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteCodeSigningConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteCodeSigningConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** ResourceConflictException **
The resource already exists, or another operation is in progress.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

## See Also
<a name="API_DeleteCodeSigningConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/DeleteCodeSigningConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/DeleteCodeSigningConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/DeleteCodeSigningConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/DeleteCodeSigningConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/DeleteCodeSigningConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/DeleteCodeSigningConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/DeleteCodeSigningConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/DeleteCodeSigningConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/DeleteCodeSigningConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/DeleteCodeSigningConfig)
