---
source_url: https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_ListResources.html
---

# ListResources
<a name="API_ListResources"></a>

Returns information about the specified resources. For more information, see [Discovering resources](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-list.html) in the * AWS Cloud Control API User Guide*.

You can use this action to return information about existing resources in your account and AWS Region, whether those resources were provisioned using Cloud Control API.

## Request Syntax
<a name="API_ListResources_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceModel": "{{string}}",
   "RoleArn": "{{string}}",
   "TypeName": "{{string}}",
   "TypeVersionId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListResources_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListResources_RequestSyntax) **   <a name="ccapi-ListResources-request-MaxResults"></a>
Reserved.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListResources_RequestSyntax) **   <a name="ccapi-ListResources-request-NextToken"></a>
If the previous paginated request didn't return all of the remaining results, the response object's `NextToken` parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's `NextToken` parameter. If there are no remaining results, the previous response object's `NextToken` parameter is set to `null`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.+`
Required: No

 ** [ResourceModel](#API_ListResources_RequestSyntax) **   <a name="ccapi-ListResources-request-ResourceModel"></a>
The resource model to use to select the resources to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Pattern: `[\s\S]*`
Required: No

 ** [RoleArn](#API_ListResources_RequestSyntax) **   <a name="ccapi-ListResources-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions required for this operation. The necessary permissions for each event handler are defined in the ` [handlers](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers) ` section of the [resource type definition schema](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html).
If you do not specify a role, Cloud Control API uses a temporary session created using your AWS user credentials.
For more information, see [Specifying credentials](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-permissions) in the * AWS Cloud Control API User Guide*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.+:iam::[0-9]{12}:role/.+`
Required: No

 ** [TypeName](#API_ListResources_RequestSyntax) **   <a name="ccapi-ListResources-request-TypeName"></a>
The name of the resource type.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 196.
Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}`
Required: Yes

 ** [TypeVersionId](#API_ListResources_RequestSyntax) **   <a name="ccapi-ListResources-request-TypeVersionId"></a>
For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-]+`
Required: No

## Response Syntax
<a name="API_ListResources_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ResourceDescriptions": [
      {
         "Identifier": "string",
         "Properties": "string"
      }
   ],
   "TypeName": "string"
}
```

## Response Elements
<a name="API_ListResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListResources_ResponseSyntax) **   <a name="ccapi-ListResources-response-NextToken"></a>
If the request doesn't return all of the remaining results, `NextToken` is set to a token. To retrieve the next set of results, call `ListResources` again and assign that token to the request object's `NextToken` parameter. If the request returns all results, `NextToken` is set to null.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.+`

 ** [ResourceDescriptions](#API_ListResources_ResponseSyntax) **   <a name="ccapi-ListResources-response-ResourceDescriptions"></a>
Information about the specified resources, including primary identifier and resource model.
Type: Array of [ResourceDescription](API_ResourceDescription.md) objects

 ** [TypeName](#API_ListResources_ResponseSyntax) **   <a name="ccapi-ListResources-response-TypeName"></a>
The name of the resource type.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 196.
Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}`

## Errors
<a name="API_ListResources_Errors"></a>

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
<a name="API_ListResources_Examples"></a>

### ListResources
<a name="API_ListResources_Example_1"></a>

The following example lists all resources of type `AWS::Logs::LogGroup`.

#### Sample Request
<a name="API_ListResources_Example_1_Request"></a>

```
https://cloudcontrolapi.us-east-1.amazonaws.com/
 ?Action=ListResources
 &TypeName=AWS::Logs::LogGroup
 &Version=2021-09-30
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20250316T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response
<a name="API_ListResources_Example_1_Response"></a>

```
<ListResourcesResponse xmlns="http://cloudcontrol.amazonaws.com/doc/2021-09-30/">
  <ListResourcesResult>
    <TypeName>AWS::Logs::LogGroup</TypeName>
    <ResourceDescriptions>
      <member>
        <ResourceModel>{"LogGroupName":"/aws/mobilehub/reactnativestarter_676534569","Arn":"arn:aws:logs:us-west-2:090123456789:log-group:/aws/mobilehub/reactnativestarter_676534569:*"}</ResourceModel>
        <Identifier>/aws/mobilehub/reactnativestarter_0123456789</Identifier>
      </member>
      <member>
        <ResourceModel>{"RetentionInDays":90,"LogGroupName":"CloudApiLogGroup","Arn":"arn:aws:logs:us-west-2:090123456789:log-group:CloudApiLogGroup:*"}</ResourceModel>
        <Identifier>CloudApiLogGroup</Identifier>
      </member>
      <member>
        <ResourceModel>{"RetentionInDays":90,"LogGroupName":"LogGroupResourceExample","Arn":"arn:aws:logs:us-west-2:090123456789:log-group:LogGroupResourceExample:*"}</ResourceModel>
        <Identifier>LogGroupResourceExample</Identifier>
      </member>
    </ResourceDescriptions>
  </ListResourcesResult>
  <ResponseMetadata>
    <RequestId>9c4bf1f2-59b3-4231-b349-5f0123456789</RequestId>
  </ResponseMetadata>
</ListResourcesResponse>
```

## See Also
<a name="API_ListResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudcontrol-2021-09-30/ListResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudcontrol-2021-09-30/ListResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudcontrol-2021-09-30/ListResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudcontrol-2021-09-30/ListResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudcontrol-2021-09-30/ListResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudcontrol-2021-09-30/ListResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudcontrol-2021-09-30/ListResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudcontrol-2021-09-30/ListResources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudcontrol-2021-09-30/ListResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudcontrol-2021-09-30/ListResources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Control API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudcontrolapi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
