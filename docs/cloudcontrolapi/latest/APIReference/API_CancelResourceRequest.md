---
source_url: https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_CancelResourceRequest.html
---

# CancelResourceRequest
<a name="API_CancelResourceRequest"></a>

Cancels the specified resource operation request. For more information, see [Canceling resource operation requests](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html#resource-operations-manage-requests-cancel) in the * AWS Cloud Control API User Guide*.

Only resource operations requests with a status of `PENDING` or `IN_PROGRESS` can be canceled.

## Request Syntax
<a name="API_CancelResourceRequest_RequestSyntax"></a>

```
{
   "RequestToken": "{{string}}"
}
```

## Request Parameters
<a name="API_CancelResourceRequest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RequestToken](#API_CancelResourceRequest_RequestSyntax) **   <a name="ccapi-CancelResourceRequest-request-RequestToken"></a>
The `RequestToken` of the `ProgressEvent` object returned by the resource operation request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-A-Za-z0-9+/=]+`
Required: Yes

## Response Syntax
<a name="API_CancelResourceRequest_ResponseSyntax"></a>

```
{
   "ProgressEvent": {
      "ErrorCode": "string",
      "EventTime": number,
      "HooksRequestToken": "string",
      "Identifier": "string",
      "Operation": "string",
      "OperationStatus": "string",
      "RequestToken": "string",
      "ResourceModel": "string",
      "RetryAfter": number,
      "StatusMessage": "string",
      "TypeName": "string"
   }
}
```

## Response Elements
<a name="API_CancelResourceRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProgressEvent](#API_CancelResourceRequest_ResponseSyntax) **   <a name="ccapi-CancelResourceRequest-response-ProgressEvent"></a>
Represents the current status of a resource operation request.
Type: [ProgressEvent](API_ProgressEvent.md) object

## Errors
<a name="API_CancelResourceRequest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
The resource is currently being modified by another operation.
HTTP Status Code: 500

 ** RequestTokenNotFoundException **
A resource operation with the specified request token can't be found.
HTTP Status Code: 400

## See Also
<a name="API_CancelResourceRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudcontrol-2021-09-30/CancelResourceRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudcontrol-2021-09-30/CancelResourceRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudcontrol-2021-09-30/CancelResourceRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudcontrol-2021-09-30/CancelResourceRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudcontrol-2021-09-30/CancelResourceRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudcontrol-2021-09-30/CancelResourceRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudcontrol-2021-09-30/CancelResourceRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudcontrol-2021-09-30/CancelResourceRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudcontrol-2021-09-30/CancelResourceRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudcontrol-2021-09-30/CancelResourceRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Control API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudcontrolapi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
