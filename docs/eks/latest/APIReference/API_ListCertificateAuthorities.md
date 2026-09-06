---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_ListCertificateAuthorities.html
---

# ListCertificateAuthorities
<a name="API_ListCertificateAuthorities"></a>

Lists the certificate authorities (CAs) for your cluster. A cluster has at most two certificate authorities: the outgoing CA that's currently signing and, during a rotation, one successor CA.

## Request Syntax
<a name="API_ListCertificateAuthorities_RequestSyntax"></a>

```
GET /clusters/{{name}}/certificate-authorities?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCertificateAuthorities_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_ListCertificateAuthorities_RequestSyntax) **   <a name="AmazonEKS-ListCertificateAuthorities-request-uri-clusterName"></a>
The name of your cluster.
Required: Yes

 ** [maxResults](#API_ListCertificateAuthorities_RequestSyntax) **   <a name="AmazonEKS-ListCertificateAuthorities-request-uri-maxResults"></a>
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned `nextToken` value. If you don't specify a value, the default is 100 results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListCertificateAuthorities_RequestSyntax) **   <a name="AmazonEKS-ListCertificateAuthorities-request-uri-nextToken"></a>
The `nextToken` value returned from a previous paginated request, where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is null when there are no more results to return.
This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.

## Request Body
<a name="API_ListCertificateAuthorities_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCertificateAuthorities_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificateAuthorities": [
      {
         "activatedAt": number,
         "activatedBy": "string",
         "createdAt": number,
         "createdBy": "string",
         "distributionStatus": "string",
         "id": "string",
         "signingStatus": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCertificateAuthorities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateAuthorities](#API_ListCertificateAuthorities_ResponseSyntax) **   <a name="AmazonEKS-ListCertificateAuthorities-response-certificateAuthorities"></a>
A list of certificate authority summary objects, each containing basic information about a certificate authority, including its ID, signing status, and distribution status.
Type: Array of [CertificateAuthoritySummary](API_CertificateAuthoritySummary.md) objects

 ** [nextToken](#API_ListCertificateAuthorities_ResponseSyntax) **   <a name="AmazonEKS-ListCertificateAuthorities-response-nextToken"></a>
The `nextToken` value to include in a future `ListCertificateAuthorities` request. When the results of a `ListCertificateAuthorities` request exceed `maxResults`, you can use this value to retrieve the next page of results. This value is null when there are no more results to return.
This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.
Type: String

## Errors
<a name="API_ListCertificateAuthorities_Errors"></a>

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
<a name="API_ListCertificateAuthorities_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_ListCertificateAuthorities_Example_1"></a>

The following example lists the certificate authorities for the cluster named `my-cluster`.

#### Sample Request
<a name="API_ListCertificateAuthorities_Example_1_Request"></a>

```
GET /clusters/my-cluster/certificate-authorities HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.9.0 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/eks.list-certificate-authorities
X-Amz-Date: 20260729T193227Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_ListCertificateAuthorities_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 29 Jul 2026 19:32:43 GMT
Content-Type: application/json
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
	"certificateAuthorities": [
		{
			"id": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
			"createdAt": 1760284672.451,
			"createdBy": "EKS",
			"activatedAt": 1760284672.451,
			"activatedBy": "EKS",
			"signingStatus": "IN_USE",
			"distributionStatus": "COMPLETE"
		},
		{
			"id": "b2c3d4e5-6789-0abc-def0-1234567890ab",
			"createdAt": 1785312515.848,
			"createdBy": "CUSTOMER",
			"signingStatus": "NOT_USED",
			"distributionStatus": "COMPLETE"
		}
	]
}
```

## See Also
<a name="API_ListCertificateAuthorities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/ListCertificateAuthorities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/ListCertificateAuthorities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ListCertificateAuthorities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/ListCertificateAuthorities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ListCertificateAuthorities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/ListCertificateAuthorities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/ListCertificateAuthorities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/ListCertificateAuthorities)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/ListCertificateAuthorities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ListCertificateAuthorities)
