---
source_url: https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.html
---

# GetResourceRequestStatus
<a name="API_GetResourceRequestStatus"></a>

Returns the current status of a resource operation request. For more information, see [Tracking the progress of resource operation requests](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html#resource-operations-manage-requests-track) in the * AWS Cloud Control API User Guide*.

## Request Syntax
<a name="API_GetResourceRequestStatus_RequestSyntax"></a>

```
{
   "RequestToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetResourceRequestStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RequestToken](#API_GetResourceRequestStatus_RequestSyntax) **   <a name="ccapi-GetResourceRequestStatus-request-RequestToken"></a>
A unique token used to track the progress of the resource operation request.
Request tokens are included in the `ProgressEvent` type returned by a resource operation request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-A-Za-z0-9+/=]+`
Required: Yes

## Response Syntax
<a name="API_GetResourceRequestStatus_ResponseSyntax"></a>

```
{
   "HooksProgressEvent": [
      {
         "FailureMode": "string",
         "HookEventTime": number,
         "HookStatus": "string",
         "HookStatusMessage": "string",
         "HookTypeArn": "string",
         "HookTypeName": "string",
         "HookTypeVersionId": "string",
         "InvocationPoint": "string"
      }
   ],
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
<a name="API_GetResourceRequestStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HooksProgressEvent](#API_GetResourceRequestStatus_ResponseSyntax) **   <a name="ccapi-GetResourceRequestStatus-response-HooksProgressEvent"></a>
Lists Hook invocations for the specified target in the request. This is a list since the same target can invoke multiple Hooks.
Type: Array of [HookProgressEvent](API_HookProgressEvent.md) objects

 ** [ProgressEvent](#API_GetResourceRequestStatus_ResponseSyntax) **   <a name="ccapi-GetResourceRequestStatus-response-ProgressEvent"></a>
Represents the current status of the resource operation request.
Type: [ProgressEvent](API_ProgressEvent.md) object

## Errors
<a name="API_GetResourceRequestStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** RequestTokenNotFoundException **
A resource operation with the specified request token can't be found.
HTTP Status Code: 400

## Examples
<a name="API_GetResourceRequestStatus_Examples"></a>

### GetResourceRequestStatus
<a name="API_GetResourceRequestStatus_Example_1"></a>

The following example returns the successful completion status of the specified resource creation operation.

#### Sample Request
<a name="API_GetResourceRequestStatus_Example_1_Request"></a>

```
https://cloudcontrolapi.us-east-1.amazonaws.com/
 ?Action=GetResourceRequestStatus
 &RequestToken=b4a1cc5a-a2ae-4dec-9e1e-150123456789
 &Version=2021-09-30
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20250316T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response
<a name="API_GetResourceRequestStatus_Example_1_Response"></a>

```
<GetResourceRequestStatusResponse xmlns="http://cloudcontrol.amazonaws.com/doc/2021-09-30/">
  <GetResourceRequestStatusResult>
    <ProgressEvent>
      <Identifier>LogGroupResourceExample</Identifier>
      <OperationStatus>SUCCESS</OperationStatus>
      <EventTime>2025-02-27T18:52:57.406Z</EventTime>
      <TypeName>AWS::Logs::LogGroup</TypeName>
      <RequestToken>b4a1cc5a-a2ae-4dec-9e1e-150123456789</RequestToken>
      <Operation>CREATE</Operation>
    </ProgressEvent>
  </GetResourceRequestStatusResult>
  <ResponseMetadata>
    <RequestId>620e5d19-0c03-4069-ae3b-9e0123456789</RequestId>
  </ResponseMetadata>
</GetResourceRequestStatusResponse>
```

## See Also
<a name="API_GetResourceRequestStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudcontrol-2021-09-30/GetResourceRequestStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudcontrol-2021-09-30/GetResourceRequestStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudcontrol-2021-09-30/GetResourceRequestStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudcontrol-2021-09-30/GetResourceRequestStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudcontrol-2021-09-30/GetResourceRequestStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudcontrol-2021-09-30/GetResourceRequestStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudcontrol-2021-09-30/GetResourceRequestStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudcontrol-2021-09-30/GetResourceRequestStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudcontrol-2021-09-30/GetResourceRequestStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudcontrol-2021-09-30/GetResourceRequestStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Control API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudcontrolapi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
