---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_DeletePublisher.html
---

# DeletePublisher

Deletes a publisher. You can't delete a publisher that has registry record associations. Call `DisassociatePublisher` for each associated registry record first. The request fails with `ConflictException` while the publisher has associations or while another delete of the publisher is in progress. Association removals can take a few seconds to take effect, so a delete that follows a disassociation can briefly fail with `ConflictException`. Retry after a short wait. If the publisher ARN is in your account and the publisher doesn't exist, the request fails with `ResourceNotFoundException`.

## Request Syntax
<a name="API_DeletePublisher_RequestSyntax"></a>

```
DELETE /publishers/{{publisherArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeletePublisher_RequestParameters"></a>

The request uses the following URI parameters.

 ** [publisherArn](#API_DeletePublisher_RequestSyntax) **   <a name="agentregistrycontrol-DeletePublisher-request-uri-publisherArn"></a>
The Amazon Resource Name (ARN) of the publisher to delete.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-z0-9-]+::[0-9]{12}:[a-zA-Z0-9._/-]+`
Required: Yes

## Request Body
<a name="API_DeletePublisher_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeletePublisher_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeletePublisher_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeletePublisher_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform the requested action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request failed due to an unexpected internal error; the caller may retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling; the caller may retry after a delay.
HTTP Status Code: 429

 ** ValidationException **
The request failed validation of one or more input fields.
 ** fieldList **
The list of input fields that failed validation.
 ** reason **
The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_DeletePublisher_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/DeletePublisher)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/DeletePublisher)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/DeletePublisher)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/DeletePublisher)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/DeletePublisher)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/DeletePublisher)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/DeletePublisher)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/DeletePublisher)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/DeletePublisher)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/DeletePublisher)
