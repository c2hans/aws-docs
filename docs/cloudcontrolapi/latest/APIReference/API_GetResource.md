---
source_url: https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResource.html
---

# GetResource
<a name="API_GetResource"></a>

Returns information about the current state of the specified resource. For details, see [Reading a resource's current state](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-read.html).

You can use this action to return information about an existing resource in your account and AWS Region, whether those resources were provisioned using Cloud Control API.

## Request Syntax
<a name="API_GetResource_RequestSyntax"></a>

```
{
   "Identifier": "{{string}}",
   "RoleArn": "{{string}}",
   "TypeName": "{{string}}",
   "TypeVersionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Identifier](#API_GetResource_RequestSyntax) **   <a name="ccapi-GetResource-request-Identifier"></a>
The identifier for the resource.
You can specify the primary identifier, or any secondary identifier defined for the resource type in its resource schema. You can only specify one identifier. Primary identifiers can be specified as a string or JSON; secondary identifiers must be specified as JSON.
For compound primary identifiers (that is, one that consists of multiple resource properties strung together), to specify the primary identifier as a string, list the property values *in the order they are specified* in the primary identifier definition, separated by `|`.
For more information, see [Identifying resources](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-identifier.html) in the * AWS Cloud Control API User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: Yes

 ** [RoleArn](#API_GetResource_RequestSyntax) **   <a name="ccapi-GetResource-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions required for this operation. The necessary permissions for each event handler are defined in the ` [handlers](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers) ` section of the [resource type definition schema](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html).
If you do not specify a role, Cloud Control API uses a temporary session created using your AWS user credentials.
For more information, see [Specifying credentials](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-permissions) in the * AWS Cloud Control API User Guide*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.+:iam::[0-9]{12}:role/.+`
Required: No

 ** [TypeName](#API_GetResource_RequestSyntax) **   <a name="ccapi-GetResource-request-TypeName"></a>
The name of the resource type.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 196.
Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}`
Required: Yes

 ** [TypeVersionId](#API_GetResource_RequestSyntax) **   <a name="ccapi-GetResource-request-TypeVersionId"></a>
For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-]+`
Required: No

## Response Syntax
<a name="API_GetResource_ResponseSyntax"></a>

```
{
   "ResourceDescription": {
      "Identifier": "string",
      "Properties": "string"
   },
   "TypeName": "string"
}
```

## Response Elements
<a name="API_GetResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceDescription](#API_GetResource_ResponseSyntax) **   <a name="ccapi-GetResource-response-ResourceDescription"></a>
Represents information about a provisioned resource.
Type: [ResourceDescription](API_ResourceDescription.md) object

 ** [TypeName](#API_GetResource_ResponseSyntax) **   <a name="ccapi-GetResource-response-TypeName"></a>
The name of the resource type.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 196.
Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}`

## Errors
<a name="API_GetResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
The resource with the name requested already exists.
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
<a name="API_GetResource_Examples"></a>

### GetResource
<a name="API_GetResource_Example_1"></a>

The following example uses the type name and primary identifier of a resource to return summary information about the resource.

#### Sample Request
<a name="API_GetResource_Example_1_Request"></a>

```
https://cloudcontrolapi.us-east-1.amazonaws.com/
 ?Action=GetResource
 &TypeName=AWS::Logs::LogGroup
 &Identifier=LogGroupResourceExample
 &Version=2021-09-30
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20250316T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response
<a name="API_GetResource_Example_1_Response"></a>

```
<GetResourceResponse xmlns="http://cloudcontrol.amazonaws.com/doc/2021-09-30/">
  <GetResourceResult>
    <TypeName>AWS::Logs::LogGroup</TypeName>
    <ResourceDescription>
      <ResourceModel>{"RetentionInDays":90,"LogGroupName":"LogGroupResourceExample","Arn":"arn:aws:logs:us-west-2:090123456789:log-group:LogGroupResourceExample:*"}</ResourceModel>
      <Identifier>LogGroupResourceExample</Identifier>
    </ResourceDescription>
  </GetResourceResult>
  <ResponseMetadata>
    <RequestId>9277ff54-d56e-4a29-95af-b10123456789</RequestId>
  </ResponseMetadata>
</GetResourceResponse>
```

## See Also
<a name="API_GetResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudcontrol-2021-09-30/GetResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudcontrol-2021-09-30/GetResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudcontrol-2021-09-30/GetResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudcontrol-2021-09-30/GetResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudcontrol-2021-09-30/GetResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudcontrol-2021-09-30/GetResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudcontrol-2021-09-30/GetResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudcontrol-2021-09-30/GetResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudcontrol-2021-09-30/GetResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudcontrol-2021-09-30/GetResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Control API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudcontrolapi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
