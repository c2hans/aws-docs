---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_RejectDomainNameAccessAssociation.html
---

# RejectDomainNameAccessAssociation
<a name="API_RejectDomainNameAccessAssociation"></a>

Rejects a domain name access association with a private custom domain name.

To reject a domain name access association with an access association source in another AWS account, use this operation. To remove a domain name access association with an access association source in your own account, use the DeleteDomainNameAccessAssociation operation.

## Request Syntax
<a name="API_RejectDomainNameAccessAssociation_RequestSyntax"></a>

```
POST /rejectdomainnameaccessassociations?domainNameAccessAssociationArn={{domainNameAccessAssociationArn}}&domainNameArn={{domainNameArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_RejectDomainNameAccessAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainNameAccessAssociationArn](#API_RejectDomainNameAccessAssociation_RequestSyntax) **   <a name="apigw-RejectDomainNameAccessAssociation-request-uri-domainNameAccessAssociationArn"></a>
The ARN of the domain name access association resource.
Required: Yes

 ** [domainNameArn](#API_RejectDomainNameAccessAssociation_RequestSyntax) **   <a name="apigw-RejectDomainNameAccessAssociation-request-uri-domainNameArn"></a>
 The ARN of the domain name.
Required: Yes

## Request Body
<a name="API_RejectDomainNameAccessAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_RejectDomainNameAccessAssociation_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_RejectDomainNameAccessAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_RejectDomainNameAccessAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.
HTTP Status Code: 400

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 409

 ** NotFoundException **
The requested resource is not found. Make sure that the request URI is correct.
HTTP Status Code: 404

 ** TooManyRequestsException **
The request has reached its throttling limit. Retry after the specified time period.
HTTP Status Code: 429

 ** UnauthorizedException **
The request is denied because the caller has insufficient permissions.
HTTP Status Code: 401

## See Also
<a name="API_RejectDomainNameAccessAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/RejectDomainNameAccessAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/RejectDomainNameAccessAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/RejectDomainNameAccessAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/RejectDomainNameAccessAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/RejectDomainNameAccessAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/RejectDomainNameAccessAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/RejectDomainNameAccessAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/RejectDomainNameAccessAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/RejectDomainNameAccessAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/RejectDomainNameAccessAssociation)
