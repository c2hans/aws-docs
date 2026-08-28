---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_ActivateCertificateAuthority.html
---

# ActivateCertificateAuthority
<a name="API_ActivateCertificateAuthority"></a>

Activates a successor certificate authority (CA) as the signing certificate authority for your cluster, completing a CA rotation.

When you activate a successor CA, Amazon EKS promotes it to be the cluster's signer (its `signingStatus` becomes `IN_USE`) and the outgoing CA is retired (`NOT_USED`). The outgoing CA remains in the cluster's trust bundle but no longer signs certificates. The successor CA you activate must already be present on the cluster and fully distributed (its `distributionStatus` must be `COMPLETE`). This is an asynchronous operation that returns an `update` object you can track with [`DescribeUpdate`](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeUpdate.html).

Before you activate the successor CA, make sure the worker nodes you manage and your external clients have been updated to trust it, so they maintain connectivity to the API server after activation. For a limited period after activation, CA rollback is available to revert to the outgoing CA if needed. If you don't activate the successor CA yourself, Amazon EKS activates it automatically as the expiration deadline approaches. For more information, see [Rotate the Amazon EKS cluster certificate authority](https://docs.aws.amazon.com/eks/latest/userguide/certificate-authority-rotation.html) in the *Amazon EKS User Guide*.

## Request Syntax
<a name="API_ActivateCertificateAuthority_RequestSyntax"></a>

```
POST /clusters/{{name}}/certificate-authorities/{{certificateAuthorityId}}/activate HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ActivateCertificateAuthority_RequestParameters"></a>

The request uses the following URI parameters.

 ** [certificateAuthorityId](#API_ActivateCertificateAuthority_RequestSyntax) **   <a name="AmazonEKS-ActivateCertificateAuthority-request-uri-certificateAuthorityId"></a>
The ID of the certificate authority to activate as the cluster's signing certificate authority. This certificate authority must already exist on the cluster and have a `distributionStatus` of `COMPLETE`.
Required: Yes

 ** [name](#API_ActivateCertificateAuthority_RequestSyntax) **   <a name="AmazonEKS-ActivateCertificateAuthority-request-uri-clusterName"></a>
The name of your cluster.
Required: Yes

## Request Body
<a name="API_ActivateCertificateAuthority_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_ActivateCertificateAuthority_RequestSyntax) **   <a name="AmazonEKS-ActivateCertificateAuthority-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Required: No

## Response Syntax
<a name="API_ActivateCertificateAuthority_ResponseSyntax"></a>

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
<a name="API_ActivateCertificateAuthority_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateAuthority](#API_ActivateCertificateAuthority_ResponseSyntax) **   <a name="AmazonEKS-ActivateCertificateAuthority-response-certificateAuthority"></a>
Summary information about the certificate authority that is being activated.
Type: [CertificateAuthoritySummary](API_CertificateAuthoritySummary.md) object

 ** [update](#API_ActivateCertificateAuthority_ResponseSyntax) **   <a name="AmazonEKS-ActivateCertificateAuthority-response-update"></a>
An object representing the asynchronous update that promotes the certificate authority to be the cluster's signer.
Type: [Update](API_Update.md) object

## Errors
<a name="API_ActivateCertificateAuthority_Errors"></a>

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
<a name="API_ActivateCertificateAuthority_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_ActivateCertificateAuthority_Example_1"></a>

The following example activates the certificate authority with the ID `b2c3d4e5-6789-0abc-def0-1234567890ab` as the signing certificate authority for the cluster named `my-cluster`.

#### Sample Request
<a name="API_ActivateCertificateAuthority_Example_1_Request"></a>

```
POST /clusters/my-cluster/certificate-authorities/b2c3d4e5-6789-0abc-def0-1234567890ab/activate HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.9.0 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/eks.activate-certificate-authority
X-Amz-Date: 20260729T193227Z
Authorization: AUTHPARAMS
Content-Length: 62

{
	"clientRequestToken": "5a8578bd-b6c1-4624-9e65-d0b70f857835"
}
```

#### Sample Response
<a name="API_ActivateCertificateAuthority_Example_1_Response"></a>

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
		"signingStatus": "ACTIVATING",
		"distributionStatus": "COMPLETE"
	},
	"update": {
		"id": "2b3c4d5e-6789-90ab-cdef-EXAMPLE22222",
		"status": "InProgress",
		"type": "CertificateAuthorityUpdate",
		"params": [
			{
				"type": "ActiveCertificateAuthority",
				"value": "b2c3d4e5-6789-0abc-def0-1234567890ab"
			}
		],
		"createdAt": 1785312515.848,
		"errors": []
	}
}
```

## See Also
<a name="API_ActivateCertificateAuthority_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/ActivateCertificateAuthority)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/ActivateCertificateAuthority)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ActivateCertificateAuthority)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/ActivateCertificateAuthority)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ActivateCertificateAuthority)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/ActivateCertificateAuthority)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/ActivateCertificateAuthority)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/ActivateCertificateAuthority)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/ActivateCertificateAuthority)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ActivateCertificateAuthority)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
