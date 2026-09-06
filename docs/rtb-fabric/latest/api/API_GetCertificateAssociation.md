---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetCertificateAssociation.html
---

# GetCertificateAssociation
<a name="API_GetCertificateAssociation"></a>

Retrieves the details of a certificate association with a responder gateway.

## Request Syntax
<a name="API_GetCertificateAssociation_RequestSyntax"></a>

```
GET /responder-gateway/{{gatewayId}}/certificate?acmCertificateArn={{acmCertificateArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCertificateAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [acmCertificateArn](#API_GetCertificateAssociation_RequestSyntax) **   <a name="rtbfabric-GetCertificateAssociation-request-uri-acmCertificateArn"></a>
The Amazon Resource Name (ARN) of the ACM certificate.
Length Constraints: Minimum length of 75. Maximum length of 256.
Pattern: `arn:(aws|aws-cn|aws-us-gov):acm:[a-z0-9-]+:[0-9]{12}:certificate/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [gatewayId](#API_GetCertificateAssociation_RequestSyntax) **   <a name="rtbfabric-GetCertificateAssociation-request-uri-gatewayId"></a>
The unique identifier of the gateway.
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`
Required: Yes

## Request Body
<a name="API_GetCertificateAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCertificateAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "acmCertificateArn": "string",
   "associatedAt": number,
   "gatewayId": "string",
   "status": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetCertificateAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [acmCertificateArn](#API_GetCertificateAssociation_ResponseSyntax) **   <a name="rtbfabric-GetCertificateAssociation-response-acmCertificateArn"></a>
The Amazon Resource Name (ARN) of the ACM certificate.
Type: String
Length Constraints: Minimum length of 75. Maximum length of 256.
Pattern: `arn:(aws|aws-cn|aws-us-gov):acm:[a-z0-9-]+:[0-9]{12}:certificate/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [associatedAt](#API_GetCertificateAssociation_ResponseSyntax) **   <a name="rtbfabric-GetCertificateAssociation-response-associatedAt"></a>
The timestamp of when the certificate was associated.
Type: Timestamp

 ** [gatewayId](#API_GetCertificateAssociation_ResponseSyntax) **   <a name="rtbfabric-GetCertificateAssociation-response-gatewayId"></a>
The unique identifier of the gateway.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`

 ** [status](#API_GetCertificateAssociation_ResponseSyntax) **   <a name="rtbfabric-GetCertificateAssociation-response-status"></a>
The status of the certificate association.
Type: String
Valid Values: `PENDING_ASSOCIATION | ASSOCIATED | PENDING_DISASSOCIATION | DISASSOCIATED | FAILED`

 ** [updatedAt](#API_GetCertificateAssociation_ResponseSyntax) **   <a name="rtbfabric-GetCertificateAssociation-response-updatedAt"></a>
The timestamp of when the certificate association was last updated.
Type: Timestamp

## Errors
<a name="API_GetCertificateAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request could not be completed because you do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request could not be completed because of an internal server error. Try your call again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request could not be completed because the resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request could not be completed because it fails satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_GetCertificateAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/GetCertificateAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/GetCertificateAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/GetCertificateAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/GetCertificateAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/GetCertificateAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/GetCertificateAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/GetCertificateAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/GetCertificateAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/GetCertificateAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/GetCertificateAssociation)
