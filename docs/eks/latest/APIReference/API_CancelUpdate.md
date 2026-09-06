---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_CancelUpdate.html
---

# CancelUpdate
<a name="API_CancelUpdate"></a>

Cancels an in-progress update to an Amazon EKS cluster on a best-effort basis. Cancellation is only performed if the update can be cancelled. Currently, this is supported for `VersionRollback` update types on EKS Auto Mode clusters when nodes are rolling back.

A successful cancellation stops the node rollback. After cancellation, nodes converge to the current cluster version honoring configured disruption controls. If the control plane rollback has already begun, the cancellation request fails.

## Request Syntax
<a name="API_CancelUpdate_RequestSyntax"></a>

```
POST /clusters/{{name}}/updates/{{updateId}}/cancel-update HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CancelUpdate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_CancelUpdate_RequestSyntax) **   <a name="AmazonEKS-CancelUpdate-request-uri-name"></a>
The name of the Amazon EKS cluster associated with the update.
Required: Yes

 ** [updateId](#API_CancelUpdate_RequestSyntax) **   <a name="AmazonEKS-CancelUpdate-request-uri-updateId"></a>
The ID of the update to cancel.
Required: Yes

## Request Body
<a name="API_CancelUpdate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CancelUpdate_RequestSyntax) **   <a name="AmazonEKS-CancelUpdate-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Required: No

## Response Syntax
<a name="API_CancelUpdate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "update": {
      "cancellation": {
         "reason": "string",
         "status": "string"
      },
      "createdAt": number,
      "errors": [
         {
            "errorCode": "string",
            "errorMessage": "string",
            "resourceIds": [ "string" ]
         }
      ],
      "id": "string",
      "params": [
         {
            "type": "string",
            "value": "string"
         }
      ],
      "status": "string",
      "type": "string"
   }
}
```

## Response Elements
<a name="API_CancelUpdate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [update](#API_CancelUpdate_ResponseSyntax) **   <a name="AmazonEKS-CancelUpdate-response-update"></a>
The full description of the specified update.
Type: [Update](API_Update.md) object

## Errors
<a name="API_CancelUpdate_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** ClientException **
These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.
 ** addonName **
The Amazon EKS add-on name associated with the exception.
 ** clusterName **
The Amazon EKS cluster associated with the exception.
 ** message **
These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.
 ** nodegroupName **
The Amazon EKS managed node group associated with the exception.
 ** subscriptionId **
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** addonName **
The specified parameter for the add-on name is invalid. Review the available parameters for the API request
 ** clusterName **
The Amazon EKS cluster associated with the exception.
 ** fargateProfileName **
The Fargate profile associated with the exception.
 ** message **
The specified parameter is invalid. Review the available parameters for the API request.
 ** nodegroupName **
The Amazon EKS managed node group associated with the exception.
 ** subscriptionId **
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.
 ** addonName **
The request is invalid given the state of the add-on name. Check the state of the cluster and the associated operations.
 ** clusterName **
The Amazon EKS cluster associated with the exception.
 ** message **
The Amazon EKS add-on name associated with the exception.
 ** nodegroupName **
The Amazon EKS managed node group associated with the exception.
 ** subscriptionId **
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 400

 ** InvalidStateException **
Amazon EKS detected upgrade readiness issues. Call the [`ListInsights`](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListInsights.html) API to view detected upgrade blocking issues. Pass the [`force`](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateClusterVersion.html#API_UpdateClusterVersion_RequestBody) flag when updating to override upgrade readiness errors.
 ** clusterName **
The Amazon EKS cluster associated with the exception.
HTTP Status Code: 400

 ** ResourceInUseException **
The specified resource is in use.
 ** addonName **
The specified add-on name is in use.
 ** clusterName **
The Amazon EKS cluster associated with the exception.
 ** message **
The Amazon EKS message associated with the exception.
 ** nodegroupName **
The Amazon EKS managed node group associated with the exception.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource could not be found. You can view your available clusters with `ListClusters`. You can view your available managed node groups with `ListNodegroups`. Amazon EKS clusters and node groups are AWS Region specific.
 ** addonName **
The Amazon EKS add-on name associated with the exception.
 ** clusterName **
The Amazon EKS cluster associated with the exception.
 ** fargateProfileName **
The Fargate profile associated with the exception.
 ** message **
The Amazon EKS message associated with the exception.
 ** nodegroupName **
The Amazon EKS managed node group associated with the exception.
 ** subscriptionId **
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 404

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** addonName **
The Amazon EKS add-on name associated with the exception.
 ** clusterName **
The Amazon EKS cluster associated with the exception.
 ** message **
These errors are usually caused by a server-side issue.
 ** nodegroupName **
The Amazon EKS managed node group associated with the exception.
 ** subscriptionId **
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 500

 ** ThrottlingException **
The request or operation couldn't be performed because a service is throttling requests.
 ** clusterName **
The Amazon EKS cluster associated with the exception.
HTTP Status Code: 429

## Examples
<a name="API_CancelUpdate_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CancelUpdate_Example_1"></a>

The following example cancels an in-progress update with the ID `9f771284-9e30-4886-b5b1-3789b6bea4dc` for the `my-cluster` cluster.

#### Sample Request
<a name="API_CancelUpdate_Example_1_Request"></a>

```
POST /clusters/my-cluster/updates/9f771284-9e30-4886-b5b1-3789b6bea4dc/cancel-update HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.9.0 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/eks.cancel-update
X-Amz-Date: 20250601T120000Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_CancelUpdate_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Sun, 01 Jun 2025 12:00:01 GMT
Content-Type: application/json
Content-Length: 300
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
	"update": {
		"id": "9f771284-9e30-4886-b5b1-3789b6bea4dc",
		"status": "InProgress",
		"type": "VersionRollback",
		"params": [{
			"type": "Version",
			"value": "1.30"
		}],
		"createdAt": 1748764800.0,
		"errors": [],
		"cancellation": {
			"status": "InProgress"
		}
	}
}
```

## See Also
<a name="API_CancelUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/CancelUpdate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/CancelUpdate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CancelUpdate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/CancelUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CancelUpdate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/CancelUpdate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/CancelUpdate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/CancelUpdate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/CancelUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CancelUpdate)
