---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_AssociateCertificate.html
---

# AssociateCertificate

Associates an ACM certificate with the specified proxy.

## Request Parameters
<a name="API_AssociateCertificate_RequestParameters"></a>

 ** certificateIdentifier **
The Amazon Resource Name (ARN) of the ACM certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:[a-z0-9\-]+:acm:[a-z0-9\-]+:[0-9]{12}:certificate/.+`
Required: Yes

 ** proxyIdentifier **
The Amazon Resource Name (ARN) of the proxy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z-]+:elasticloadbalancing:[a-z0-9-]+:[0-9]{12}:proxy/[a-zA-Z0-9-]+:[a-zA-Z0-9]+`
Required: Yes

## Response Elements
<a name="API_AssociateCertificate_ResponseElements"></a>

The following element is returned by the service.

 ** certificateAssociation **
The certificate association.
Type: [CertificateAssociation](API_CertificateAssociation.md) object

## Errors
<a name="API_AssociateCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
 ** message **
The error message.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** message **
The error message.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** message **
The error message.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** message **
The error message.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** message **
The error message.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** resourceId **
The ID of the resource that caused the service quota to be exceeded.
 ** resourceType **
The type of the resource that caused the service quota to be exceeded.
 ** serviceCode **
The code of the service associated with the exceeded quota.
HTTP Status Code: 402

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** message **
The error message.
HTTP Status Code: 429

 ** ValidationError **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_AssociateCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elb-proxy-2026-11-20/AssociateCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elb-proxy-2026-11-20/AssociateCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elb-proxy-2026-11-20/AssociateCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elb-proxy-2026-11-20/AssociateCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elb-proxy-2026-11-20/AssociateCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elb-proxy-2026-11-20/AssociateCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elb-proxy-2026-11-20/AssociateCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elb-proxy-2026-11-20/AssociateCertificate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elb-proxy-2026-11-20/AssociateCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elb-proxy-2026-11-20/AssociateCertificate)
