---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteProjectDataRetentionStorage.html
---

# DeleteProjectDataRetentionStorage

Deletes a project's retention storage configuration for a model provider. Deleting an absent configuration on an active project succeeds. If the project does not exist or your account does not own it, the operation returns `ResourceNotFoundException`. For an archived project, the operation returns `ValidationException`. You can read the archived project's stored configuration until Amazon Bedrock purges the project. You do not need to participate in the program to delete the configuration.

## Request Syntax
<a name="API_DeleteProjectDataRetentionStorage_RequestSyntax"></a>

```
DELETE /v1/projects/{{projectIdentifier}}/data_retention/storage/{{modelProvider}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteProjectDataRetentionStorage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [modelProvider](#API_DeleteProjectDataRetentionStorage_RequestSyntax) **   <a name="bedrock-DeleteProjectDataRetentionStorage-request-uri-modelProvider"></a>
The model provider whose retention storage configuration is addressed by this request.
Valid Values: `anthropic | openai`
Required: Yes

 ** [projectIdentifier](#API_DeleteProjectDataRetentionStorage_RequestSyntax) **   <a name="bedrock-DeleteProjectDataRetentionStorage-request-uri-projectIdentifier"></a>
The ID or ARN of a named project owned by the calling account in this AWS Region. The default project is not supported; use the account-level retention storage operations instead.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `([a-zA-Z0-9_-]+|arn:aws(-[^:]+)?:bedrock:[0-9a-z-]{1,20}:[0-9]{12}:project/[a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_DeleteProjectDataRetentionStorage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteProjectDataRetentionStorage_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteProjectDataRetentionStorage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteProjectDataRetentionStorage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is denied because of missing access permissions.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.
HTTP Status Code: 404

 ** ThrottlingException **
The number of requests exceeds the limit. Resubmit your request later.
HTTP Status Code: 429

 ** ValidationException **
Input validation failed. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_DeleteProjectDataRetentionStorage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/DeleteProjectDataRetentionStorage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/DeleteProjectDataRetentionStorage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/DeleteProjectDataRetentionStorage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/DeleteProjectDataRetentionStorage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/DeleteProjectDataRetentionStorage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/DeleteProjectDataRetentionStorage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/DeleteProjectDataRetentionStorage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/DeleteProjectDataRetentionStorage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/DeleteProjectDataRetentionStorage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/DeleteProjectDataRetentionStorage)
