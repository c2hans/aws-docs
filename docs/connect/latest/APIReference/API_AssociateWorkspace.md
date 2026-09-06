---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AssociateWorkspace.html
---

# AssociateWorkspace
<a name="API_AssociateWorkspace"></a>

Associates a workspace with one or more users or routing profiles, allowing them to access the workspace's configured views and pages.

## Request Syntax
<a name="API_AssociateWorkspace_RequestSyntax"></a>

```
POST /workspaces/{{InstanceId}}/{{WorkspaceId}}/associate HTTP/1.1
Content-type: application/json

{
   "ResourceArns": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_AssociateWorkspace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_AssociateWorkspace_RequestSyntax) **   <a name="connect-AssociateWorkspace-request-uri-InstanceId"></a>
The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [WorkspaceId](#API_AssociateWorkspace_RequestSyntax) **   <a name="connect-AssociateWorkspace-request-uri-WorkspaceId"></a>
The identifier of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_AssociateWorkspace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ResourceArns](#API_AssociateWorkspace_RequestSyntax) **   <a name="connect-AssociateWorkspace-request-ResourceArns"></a>
The Amazon Resource Names (ARNs) of the resources to associate with the workspace. Valid resource types are users and routing profiles.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

## Response Syntax
<a name="API_AssociateWorkspace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "FailedList": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "ResourceArn": "string"
      }
   ],
   "SuccessfulList": [
      {
         "ResourceArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_AssociateWorkspace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedList](#API_AssociateWorkspace_ResponseSyntax) **   <a name="connect-AssociateWorkspace-response-FailedList"></a>
A list of resources that failed to be associated with the workspace, including error details.
Type: Array of [FailedBatchAssociationSummary](API_FailedBatchAssociationSummary.md) objects

 ** [SuccessfulList](#API_AssociateWorkspace_ResponseSyntax) **   <a name="connect-AssociateWorkspace-response-SuccessfulList"></a>
A list of resources that were successfully associated with the workspace.
Type: Array of [SuccessfulBatchAssociationSummary](API_SuccessfulBatchAssociationSummary.md) objects

## Errors
<a name="API_AssociateWorkspace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_AssociateWorkspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/AssociateWorkspace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/AssociateWorkspace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AssociateWorkspace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/AssociateWorkspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AssociateWorkspace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/AssociateWorkspace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/AssociateWorkspace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/AssociateWorkspace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/AssociateWorkspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AssociateWorkspace)
