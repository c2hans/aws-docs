---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeCertificateAuthority.html
---

# DescribeCertificateAuthority
<a name="API_DescribeCertificateAuthority"></a>

Returns detailed information about a certificate authority (CA) in your cluster, including its validity period, signing and distribution status, provenance, scheduled auto-activation events, and public certificate data.

## Request Syntax
<a name="API_DescribeCertificateAuthority_RequestSyntax"></a>

```
GET /clusters/{{name}}/certificate-authorities/{{certificateAuthorityId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeCertificateAuthority_RequestParameters"></a>

The request uses the following URI parameters.

 ** [certificateAuthorityId](#API_DescribeCertificateAuthority_RequestSyntax) **   <a name="AmazonEKS-DescribeCertificateAuthority-request-uri-certificateAuthorityId"></a>
The ID of the certificate authority to describe.
Required: Yes

 ** [name](#API_DescribeCertificateAuthority_RequestSyntax) **   <a name="AmazonEKS-DescribeCertificateAuthority-request-uri-clusterName"></a>
The name of your cluster.
Required: Yes

## Request Body
<a name="API_DescribeCertificateAuthority_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeCertificateAuthority_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificateAuthority": {
      "activatedAt": number,
      "activatedBy": "string",
      "createdAt": number,
      "createdBy": "string",
      "data": "string",
      "distributionStatus": "string",
      "id": "string",
      "rollbackAvailable": boolean,
      "scheduledEvents": {
         "finalAutoActivation": number,
         "firstAutoActivation": number
      },
      "signingStatus": "string",
      "validity": {
         "notAfter": number,
         "notBefore": number
      }
   }
}
```

## Response Elements
<a name="API_DescribeCertificateAuthority_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateAuthority](#API_DescribeCertificateAuthority_ResponseSyntax) **   <a name="AmazonEKS-DescribeCertificateAuthority-response-certificateAuthority"></a>
An object containing detailed information about the certificate authority.
Type: [CertificateAuthority](API_CertificateAuthority.md) object

## Errors
<a name="API_DescribeCertificateAuthority_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

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
<a name="API_DescribeCertificateAuthority_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DescribeCertificateAuthority_Example_1"></a>

The following example describes the certificate authority with the ID `b2c3d4e5-6789-0abc-def0-1234567890ab` for the cluster named `my-cluster`.

#### Sample Request
<a name="API_DescribeCertificateAuthority_Example_1_Request"></a>

```
GET /clusters/my-cluster/certificate-authorities/b2c3d4e5-6789-0abc-def0-1234567890ab HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.9.0 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/eks.describe-certificate-authority
X-Amz-Date: 20260729T193227Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeCertificateAuthority_Example_1_Response"></a>

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
		"distributionStatus": "COMPLETE",
		"validity": {
			"notBefore": 1785312515.848,
			"notAfter": 1816848515.848
		},
		"scheduledEvents": {
			"firstAutoActivation": 1801080515.848,
			"finalAutoActivation": 1812960515.848
		},
		"rollbackAvailable": false,
		"data": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0t...LS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQ=="
	}
}
```

## See Also
<a name="API_DescribeCertificateAuthority_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DescribeCertificateAuthority)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DescribeCertificateAuthority)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DescribeCertificateAuthority)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DescribeCertificateAuthority)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DescribeCertificateAuthority)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DescribeCertificateAuthority)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DescribeCertificateAuthority)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DescribeCertificateAuthority)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DescribeCertificateAuthority)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DescribeCertificateAuthority)
