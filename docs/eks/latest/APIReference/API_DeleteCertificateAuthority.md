---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_DeleteCertificateAuthority.html
---

# DeleteCertificateAuthority
<a name="API_DeleteCertificateAuthority"></a>

Deletes a certificate authority (CA) from your cluster.

Deleting a certificate authority removes its public certificate from the cluster's trust bundle. You can't delete the certificate authority that's currently signing certificates for the cluster (its `signingStatus` is `IN_USE`) — to remove the outgoing CA, first activate the successor CA with [`ActivateCertificateAuthority`](https://docs.aws.amazon.com/eks/latest/APIReference/API_ActivateCertificateAuthority.html). Amazon EKS also protects a successor CA from deletion in certain cases to keep a valid rotation path — for example, a successor that Amazon EKS appended can't be deleted while it's the only successor on the cluster. This is an asynchronous operation that returns an `update` object.

## Request Syntax
<a name="API_DeleteCertificateAuthority_RequestSyntax"></a>

```
DELETE /clusters/{{name}}/certificate-authorities/{{certificateAuthorityId}}?clientRequestToken={{clientRequestToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteCertificateAuthority_RequestParameters"></a>

The request uses the following URI parameters.

 ** [certificateAuthorityId](#API_DeleteCertificateAuthority_RequestSyntax) **   <a name="AmazonEKS-DeleteCertificateAuthority-request-uri-certificateAuthorityId"></a>
The ID of the certificate authority to delete. You can't delete the certificate authority that's currently signing certificates for the cluster.
Required: Yes

 ** [clientRequestToken](#API_DeleteCertificateAuthority_RequestSyntax) **   <a name="AmazonEKS-DeleteCertificateAuthority-request-uri-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

 ** [name](#API_DeleteCertificateAuthority_RequestSyntax) **   <a name="AmazonEKS-DeleteCertificateAuthority-request-uri-clusterName"></a>
The name of your cluster.
Required: Yes

## Request Body
<a name="API_DeleteCertificateAuthority_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCertificateAuthority_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificateAuthority": {
      "activatedAt": number,
      "activatedBy": "string",
      "createdAt": number,
      "createdBy": "string",
      "distributionStatus": "string",
      "id": "string",
      "signingStatus": "string"
   },
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
<a name="API_DeleteCertificateAuthority_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateAuthority](#API_DeleteCertificateAuthority_ResponseSyntax) **   <a name="AmazonEKS-DeleteCertificateAuthority-response-certificateAuthority"></a>
Summary information about the certificate authority that is being deleted.
Type: [CertificateAuthoritySummary](API_CertificateAuthoritySummary.md) object

 ** [update](#API_DeleteCertificateAuthority_ResponseSyntax) **   <a name="AmazonEKS-DeleteCertificateAuthority-response-update"></a>
An object representing the asynchronous update that removes the certificate authority from the cluster's trust bundle.
Type: [Update](API_Update.md) object

## Errors
<a name="API_DeleteCertificateAuthority_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

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

 ** ServiceUnavailableException **
The service is unavailable. Back off and retry the operation.
 ** message **
The request has failed due to a temporary failure of the server.
HTTP Status Code: 503

## Examples
<a name="API_DeleteCertificateAuthority_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DeleteCertificateAuthority_Example_1"></a>

The following example deletes the trusted certificate authority with the ID `b2c3d4e5-6789-0abc-def0-1234567890ab` from the cluster named `my-cluster`.

#### Sample Request
<a name="API_DeleteCertificateAuthority_Example_1_Request"></a>

```
DELETE /clusters/my-cluster/certificate-authorities/b2c3d4e5-6789-0abc-def0-1234567890ab?clientRequestToken=5a8578bd-b6c1-4624-9e65-d0b70f857835 HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.9.0 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/eks.delete-certificate-authority
X-Amz-Date: 20260729T193227Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteCertificateAuthority_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 29 Jul 2026 19:32:43 GMT
Content-Type: application/json
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
	"certificateAuthority": {
		"id": "b2c3d4e5-6789-0abc-def0-1234567890ab",
		"createdAt": 1785312515.848,
		"createdBy": "CUSTOMER",
		"signingStatus": "NOT_USED",
		"distributionStatus": "DELETING"
	},
	"update": {
		"id": "3c4d5e6f-6789-90ab-cdef-EXAMPLE33333",
		"status": "InProgress",
		"type": "CertificateAuthorityUpdate",
		"params": [
			{
				"type": "CertificateAuthorityId",
				"value": "b2c3d4e5-6789-0abc-def0-1234567890ab"
			}
		],
		"createdAt": 1785312515.848,
		"errors": []
	}
}
```

## See Also
<a name="API_DeleteCertificateAuthority_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DeleteCertificateAuthority)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DeleteCertificateAuthority)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DeleteCertificateAuthority)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DeleteCertificateAuthority)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DeleteCertificateAuthority)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DeleteCertificateAuthority)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DeleteCertificateAuthority)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DeleteCertificateAuthority)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DeleteCertificateAuthority)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DeleteCertificateAuthority)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
