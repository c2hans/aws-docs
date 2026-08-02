---
source_url: https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_UpdateResource.html
---

# UpdateResource
<a name="API_UpdateResource"></a>

Updates the specified property values in the resource.

You specify your resource property updates as a list of patch operations contained in a JSON patch document that adheres to the [https://datatracker.ietf.org/doc/html/rfc6902](https://datatracker.ietf.org/doc/html/rfc6902) standard.

For details on how Cloud Control API performs resource update operations, see [Updating a resource](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-update.html) in the * AWS Cloud Control API User Guide*.

After you have initiated a resource update request, you can monitor the progress of your request by calling [GetResourceRequestStatus](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.html) using the `RequestToken` of the `ProgressEvent` returned by `UpdateResource`.

For more information about the properties of a specific resource, refer to the related topic for the resource in the [Resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-template-resource-type-ref.html) in the * AWS CloudFormation Template Reference*.

## Request Syntax
<a name="API_UpdateResource_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "Identifier": "{{string}}",
   "PatchDocument": "{{string}}",
   "RoleArn": "{{string}}",
   "TypeName": "{{string}}",
   "TypeVersionId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_UpdateResource_RequestSyntax) **   <a name="ccapi-UpdateResource-request-ClientToken"></a>
A unique identifier to ensure the idempotency of the resource request. As a best practice, specify this token to ensure idempotency, so that AWS Cloud Control API can accurately distinguish between request retries and new resource requests. You might retry a resource request to ensure that it was successfully received.
A client token is valid for 36 hours once used. After that, a resource request with the same client token is treated as a new request.
If you do not specify a client token, one is generated for inclusion in the request.
For more information, see [Ensuring resource operation requests are unique](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-idempotency) in the * AWS Cloud Control API User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-A-Za-z0-9+/=]+`
Required: No

 ** [Identifier](#API_UpdateResource_RequestSyntax) **   <a name="ccapi-UpdateResource-request-Identifier"></a>
The identifier for the resource.
You can specify the primary identifier, or any secondary identifier defined for the resource type in its resource schema. You can only specify one identifier. Primary identifiers can be specified as a string or JSON; secondary identifiers must be specified as JSON.
For compound primary identifiers (that is, one that consists of multiple resource properties strung together), to specify the primary identifier as a string, list the property values *in the order they are specified* in the primary identifier definition, separated by `|`.
For more information, see [Identifying resources](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-identifier.html) in the * AWS Cloud Control API User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: Yes

 ** [PatchDocument](#API_UpdateResource_RequestSyntax) **   <a name="ccapi-UpdateResource-request-PatchDocument"></a>
A JavaScript Object Notation (JSON) document listing the patch operations that represent the updates to apply to the current resource properties. For more information, see [Composing the patch document](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-update.html#resource-operations-update-patch) in the * AWS Cloud Control API User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Pattern: `[\s\S]*`
Required: Yes

 ** [RoleArn](#API_UpdateResource_RequestSyntax) **   <a name="ccapi-UpdateResource-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions required for this operation. The necessary permissions for each event handler are defined in the ` [handlers](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers) ` section of the [resource type definition schema](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html).
If you do not specify a role, Cloud Control API uses a temporary session created using your AWS user credentials.
For more information, see [Specifying credentials](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-permissions) in the * AWS Cloud Control API User Guide*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.+:iam::[0-9]{12}:role/.+`
Required: No

 ** [TypeName](#API_UpdateResource_RequestSyntax) **   <a name="ccapi-UpdateResource-request-TypeName"></a>
The name of the resource type.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 196.
Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}`
Required: Yes

 ** [TypeVersionId](#API_UpdateResource_RequestSyntax) **   <a name="ccapi-UpdateResource-request-TypeVersionId"></a>
For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-]+`
Required: No

## Response Syntax
<a name="API_UpdateResource_ResponseSyntax"></a>

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
<a name="API_UpdateResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProgressEvent](#API_UpdateResource_ResponseSyntax) **   <a name="ccapi-UpdateResource-response-ProgressEvent"></a>
Represents the current status of the resource update request.
Use the `RequestToken` of the `ProgressEvent` with [GetResourceRequestStatus](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.html) to return the current status of a resource operation request.
Type: [ProgressEvent](API_ProgressEvent.md) object

## Errors
<a name="API_UpdateResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
The resource with the name requested already exists.
HTTP Status Code: 400

 ** ClientTokenConflictException **
The specified client token has already been used in another resource request.
It's best practice for client tokens to be unique for each resource operation request. However, client token expire after 36 hours.
HTTP Status Code: 400

 ** ConcurrentOperationException **
Another resource operation is currently being performed on this resource.
HTTP Status Code: 400

 ** GeneralServiceException **
The resource handler has returned that the downstream service generated an error that doesn't map to any other handler error code.
HTTP Status Code: 400

 ** HandlerFailureException **
The resource handler has failed without a returning a more specific error code. This can include timeouts.
HTTP Status Code: 500

 ** HandlerInternalFailureException **
The resource handler has returned that an unexpected error occurred within the resource handler.
HTTP Status Code: 500

 ** InvalidCredentialsException **
The resource handler has returned that the credentials provided by the user are invalid.
HTTP Status Code: 400

 ** InvalidRequestException **
The resource handler has returned that invalid input from the user has generated a generic exception.
HTTP Status Code: 400

 ** NetworkFailureException **
The resource handler has returned that the request couldn't be completed due to networking issues, such as a failure to receive a response from the server.
HTTP Status Code: 500

 ** NotStabilizedException **
The resource handler has returned that the downstream resource failed to complete all of its ready-state checks.
HTTP Status Code: 400

 ** NotUpdatableException **
One or more properties included in this resource operation are defined as create-only, and therefore can't be updated.
HTTP Status Code: 400

 ** PrivateTypeException **
Cloud Control API hasn't received a valid response from the resource handler, due to a configuration error. This includes issues such as the resource handler returning an invalid response, or timing out.
HTTP Status Code: 400

 ** ResourceConflictException **
The resource is temporarily unavailable to be acted upon. For example, if the resource is currently undergoing an operation and can't be acted upon until that operation is finished.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource with the specified identifier can't be found.
HTTP Status Code: 400

 ** ServiceInternalErrorException **
The resource handler has returned that the downstream service returned an internal error, typically with a `5XX HTTP` status code.
HTTP Status Code: 500

 ** ServiceLimitExceededException **
The resource handler has returned that a non-transient resource limit was reached on the service side.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** TypeNotFoundException **
The specified extension doesn't exist in the CloudFormation registry.
HTTP Status Code: 400

 ** UnsupportedActionException **
The specified resource doesn't support this resource operation.
HTTP Status Code: 400

## Examples
<a name="API_UpdateResource_Examples"></a>

### UpdateResource
<a name="API_UpdateResource_Example_1"></a>

The following example performs two patch operations on the specified resource. The first operation tests to see if the retention policy is set to 3653 days. If this is the case, the second operation updates the retention policy to 90 days.

#### Sample Request
<a name="API_UpdateResource_Example_1_Request"></a>

```
https://cloudcontrolapi.us-east-1.amazonaws.com/
 ?Action=GetResource
 &TypeName=AWS::Logs::LogGroup
 &Identifier=LogGroupResourceExample
 &PatchDocument=[{"op": "test", "path": "RetentionInDays", "value":3653},{"op": "replace","path": "RetentionInDays", "value": 90}]
 &Version=2021-09-30
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20250316T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response
<a name="API_UpdateResource_Example_1_Response"></a>

```
<UpdateResourceResponse xmlns="http://cloudcontrol.amazonaws.com/doc/2021-09-30/">
  <UpdateResourceResult>
    <ProgressEvent>
      <Identifier>CloudApiLogGroup</Identifier>
      <OperationStatus>IN_PROGRESS</OperationStatus>
      <TypeName>AWS::Logs::LogGroup</TypeName>
      <EventTime>2025-02-27T19:50:29.241Z</EventTime>
      <ResourceModel>{"RetentionInDays":90,"LogGroupName":"CloudApiLogGroup"}</ResourceModel>
      <RequestToken>332e531e-3435-434e-82e0-de841ff13b25</RequestToken>
      <Operation>UPDATE</Operation>
    </ProgressEvent>
  </UpdateResourceResult>
  <ResponseMetadata>
    <RequestId>f75ec393-dd7c-4ad4-a3e3-d7b9c8468d86</RequestId>
  </ResponseMetadata>
</UpdateResourceResponse>
```

## See Also
<a name="API_UpdateResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudcontrol-2021-09-30/UpdateResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudcontrol-2021-09-30/UpdateResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudcontrol-2021-09-30/UpdateResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudcontrol-2021-09-30/UpdateResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudcontrol-2021-09-30/UpdateResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudcontrol-2021-09-30/UpdateResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudcontrol-2021-09-30/UpdateResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudcontrol-2021-09-30/UpdateResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudcontrol-2021-09-30/UpdateResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudcontrol-2021-09-30/UpdateResource)
