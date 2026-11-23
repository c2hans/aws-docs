---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteAccountDataRetentionStorage.html
---

# DeleteAccountDataRetentionStorage

Deletes your account's retention storage configuration for a model provider. Deleting an absent configuration succeeds. You do not need to participate in the program to delete the configuration. You can delete it even if your account is ineligible or its eligibility is revoked.

## Request Syntax
<a name="API_DeleteAccountDataRetentionStorage_RequestSyntax"></a>

```
DELETE /v1/data_retention/storage/{{modelProvider}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAccountDataRetentionStorage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [modelProvider](#API_DeleteAccountDataRetentionStorage_RequestSyntax) **   <a name="bedrock-DeleteAccountDataRetentionStorage-request-uri-modelProvider"></a>
The model provider whose retention storage configuration is addressed by this request.
Valid Values: `anthropic | openai`
Required: Yes

## Request Body
<a name="API_DeleteAccountDataRetentionStorage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAccountDataRetentionStorage_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteAccountDataRetentionStorage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAccountDataRetentionStorage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is denied because of missing access permissions.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** ThrottlingException **
The number of requests exceeds the limit. Resubmit your request later.
HTTP Status Code: 429

 ** ValidationException **
Input validation failed. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_DeleteAccountDataRetentionStorage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/DeleteAccountDataRetentionStorage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/DeleteAccountDataRetentionStorage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/DeleteAccountDataRetentionStorage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/DeleteAccountDataRetentionStorage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/DeleteAccountDataRetentionStorage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/DeleteAccountDataRetentionStorage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/DeleteAccountDataRetentionStorage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/DeleteAccountDataRetentionStorage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/DeleteAccountDataRetentionStorage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/DeleteAccountDataRetentionStorage)
