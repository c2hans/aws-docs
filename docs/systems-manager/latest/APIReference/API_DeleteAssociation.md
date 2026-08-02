---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteAssociation.html
---

# DeleteAssociation
<a name="API_DeleteAssociation"></a>

Disassociates the specified AWS Systems Manager document (SSM document) from the specified managed node. If you created the association by using the `Targets` parameter, then you must delete the association by using the association ID.

When you disassociate a document from a managed node, it doesn't change the configuration of the node. To change the configuration state of a managed node after you disassociate a document, you must create a new document with the desired configuration and associate it with the node.

## Request Syntax
<a name="API_DeleteAssociation_RequestSyntax"></a>

```
{
   "AssociationId": "{{string}}",
   "InstanceId": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociationId](#API_DeleteAssociation_RequestSyntax) **   <a name="systemsmanager-DeleteAssociation-request-AssociationId"></a>
The association ID that you want to delete.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: No

 ** [InstanceId](#API_DeleteAssociation_RequestSyntax) **   <a name="systemsmanager-DeleteAssociation-request-InstanceId"></a>
The managed node ID.
 `InstanceId` has been deprecated. To specify a managed node ID for an association, use the `Targets` parameter. Requests that include the parameter `InstanceID` with Systems Manager documents (SSM documents) that use schema version 2.0 or later will fail. In addition, if you use the parameter `InstanceId`, you can't use the parameters `AssociationName`, `DocumentVersion`, `MaxErrors`, `MaxConcurrency`, `OutputLocation`, or `ScheduleExpression`. To use these parameters, you must use the `Targets` parameter.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: No

 ** [Name](#API_DeleteAssociation_RequestSyntax) **   <a name="systemsmanager-DeleteAssociation-request-Name"></a>
The name of the SSM document.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: No

## Response Elements
<a name="API_DeleteAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AssociationDoesNotExist **
The specified association doesn't exist.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidDocument **
The specified SSM document doesn't exist.
 ** Message **
The SSM document doesn't exist or the document isn't available to the user. This exception can be issued by various API operations.
HTTP Status Code: 400

 ** InvalidInstanceId **
The following problems can cause this exception:
+ You don't have permission to access the managed node.
+  AWS Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.
+ SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.
+ The managed node isn't in a valid state. Valid states are: `Running`, `Pending`, `Stopped`, and `Stopping`. Invalid states are: `Shutting-down` and `Terminated`.
HTTP Status Code: 400

 ** TooManyUpdates **
There are concurrent updates for a resource that supports one update at a time.
HTTP Status Code: 400

## Examples
<a name="API_DeleteAssociation_Examples"></a>

### Example
<a name="API_DeleteAssociation_Example_1"></a>

This example illustrates one usage of DeleteAssociation.

#### Sample Request
<a name="API_DeleteAssociation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DeleteAssociation
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240324T150348Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240324/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 57

{
    "AssociationId": "33858bec-0c55-4547-a054-eb5fcEXAMPLE"
}
```

#### Sample Response
<a name="API_DeleteAssociation_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_DeleteAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DeleteAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DeleteAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DeleteAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DeleteAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DeleteAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DeleteAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DeleteAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DeleteAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DeleteAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DeleteAssociation)
