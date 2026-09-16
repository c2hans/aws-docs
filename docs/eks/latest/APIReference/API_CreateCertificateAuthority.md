---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateCertificateAuthority.html
---

# CreateCertificateAuthority
<a name="API_CreateCertificateAuthority"></a>

Appends a successor certificate authority (CA) to your cluster, beginning the CA rotation process.

A cluster certificate authority is the root of trust for your cluster's control plane. It signs the certificates that secure communication between the Kubernetes API server and its clients, and its public certificate is distributed to your cluster's trust bundle so that worker nodes and clients can verify the API server's identity. Each cluster can have at most two certificate authorities at a time: the outgoing CA that's currently signing (its `signingStatus` is `IN_USE`) and one successor CA (`signingStatus` of `NOT_USED`) that you can later activate to complete the rotation.

Appending a successor CA adds its public certificate to the cluster's trust bundle so that the cluster trusts both CAs simultaneously (the dual trust period), but it doesn't begin signing certificates. Amazon EKS then distributes the successor CA to the AWS managed components in your cluster; you can track this through the CA's `distributionStatus`. The successor CA can't be activated until its `distributionStatus` is `COMPLETE`. To activate it as the cluster's signer, use [`ActivateCertificateAuthority`](https://docs.aws.amazon.com/eks/latest/APIReference/API_ActivateCertificateAuthority.html). This is an asynchronous operation that returns an `update` object. If you don't append a successor CA yourself, Amazon EKS appends one automatically before the outgoing CA approaches expiration.

For more information, see [Rotate the Amazon EKS cluster certificate authority](https://docs.aws.amazon.com/eks/latest/userguide/certificate-authority-rotation.html) in the *Amazon EKS User Guide*.

## Request Syntax
<a name="API_CreateCertificateAuthority_RequestSyntax"></a>

```
POST /clusters/{{name}}/certificate-authorities HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateCertificateAuthority_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_CreateCertificateAuthority_RequestSyntax) **   <a name="AmazonEKS-CreateCertificateAuthority-request-uri-clusterName"></a>
The name of your cluster.
Required: Yes

## Request Body
<a name="API_CreateCertificateAuthority_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreateCertificateAuthority_RequestSyntax) **   <a name="AmazonEKS-CreateCertificateAuthority-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Required: No

## Response Syntax
<a name="API_CreateCertificateAuthority_ResponseSyntax"></a>

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
<a name="API_CreateCertificateAuthority_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateAuthority](#API_CreateCertificateAuthority_ResponseSyntax) **   <a name="AmazonEKS-CreateCertificateAuthority-response-certificateAuthority"></a>
Summary information about the certificate authority that was created, including its ID and initial signing and distribution status.
Type: [CertificateAuthoritySummary](API_CertificateAuthoritySummary.md) object

 ** [update](#API_CreateCertificateAuthority_ResponseSyntax) **   <a name="AmazonEKS-CreateCertificateAuthority-response-update"></a>
An object representing the asynchronous update that adds the certificate authority to the cluster's trust bundle.
Type: [Update](API_Update.md) object

## Errors
<a name="API_CreateCertificateAuthority_Errors"></a>

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

 ** ResourceLimitExceededException **
You have encountered a service limit on the specified resource.
 ** clusterName **
The Amazon EKS cluster associated with the exception.
 ** message **
The Amazon EKS message associated with the exception.
 ** nodegroupName **
The Amazon EKS managed node group associated with the exception.
 ** subscriptionId **
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 400

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
<a name="API_CreateCertificateAuthority_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreateCertificateAuthority_Example_1"></a>

The following example creates a certificate authority for the cluster named `my-cluster`.

#### Sample Request
<a name="API_CreateCertificateAuthority_Example_1_Request"></a>

```
POST /clusters/my-cluster/certificate-authorities HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.9.0 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/eks.create-certificate-authority
X-Amz-Date: 20260729T193227Z
Authorization: AUTHPARAMS
Content-Length: 62

{
	"clientRequestToken": "5a8578bd-b6c1-4624-9e65-d0b70f857835"
}
```

#### Sample Response
<a name="API_CreateCertificateAuthority_Example_1_Response"></a>

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
		"distributionStatus": "IN_PROGRESS"
	},
	"update": {
		"id": "1a2b3c4d-5678-90ab-cdef-EXAMPLE11111",
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
<a name="API_CreateCertificateAuthority_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/CreateCertificateAuthority)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/CreateCertificateAuthority)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CreateCertificateAuthority)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/CreateCertificateAuthority)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CreateCertificateAuthority)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/CreateCertificateAuthority)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/CreateCertificateAuthority)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/CreateCertificateAuthority)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/CreateCertificateAuthority)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CreateCertificateAuthority)
