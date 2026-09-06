---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_DisassociateCustomDomain.html
---

# DisassociateCustomDomain
<a name="API_DisassociateCustomDomain"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Disassociate a custom domain name from an AWS App Runner service.

Certificates tracking domain validity are associated with a custom domain and are stored in [AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide). These certificates aren't deleted as part of this action. App Runner delays certificate deletion for 30 days after a domain is disassociated from your service.

## Request Syntax
<a name="API_DisassociateCustomDomain_RequestSyntax"></a>

```
{
   "DomainName": "{{string}}",
   "ServiceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DisassociateCustomDomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainName](#API_DisassociateCustomDomain_RequestSyntax) **   <a name="apprunner-DisassociateCustomDomain-request-DomainName"></a>
The domain name that you want to disassociate from the App Runner service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9*.-]{1,255}`
Required: Yes

 ** [ServiceArn](#API_DisassociateCustomDomain_RequestSyntax) **   <a name="apprunner-DisassociateCustomDomain-request-ServiceArn"></a>
The Amazon Resource Name (ARN) of the App Runner service that you want to disassociate a custom domain name from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: Yes

## Response Syntax
<a name="API_DisassociateCustomDomain_ResponseSyntax"></a>

```
{
   "CustomDomain": {
      "CertificateValidationRecords": [
         {
            "Name": "string",
            "Status": "string",
            "Type": "string",
            "Value": "string"
         }
      ],
      "DomainName": "string",
      "EnableWWWSubdomain": boolean,
      "Status": "string"
   },
   "DNSTarget": "string",
   "ServiceArn": "string",
   "VpcDNSTargets": [
      {
         "DomainName": "string",
         "VpcId": "string",
         "VpcIngressConnectionArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DisassociateCustomDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CustomDomain](#API_DisassociateCustomDomain_ResponseSyntax) **   <a name="apprunner-DisassociateCustomDomain-response-CustomDomain"></a>
A description of the domain name that's being disassociated.
Type: [CustomDomain](API_CustomDomain.md) object

 ** [DNSTarget](#API_DisassociateCustomDomain_ResponseSyntax) **   <a name="apprunner-DisassociateCustomDomain-response-DNSTarget"></a>
The App Runner subdomain of the App Runner service. The disassociated custom domain name was mapped to this target name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`

 ** [ServiceArn](#API_DisassociateCustomDomain_ResponseSyntax) **   <a name="apprunner-DisassociateCustomDomain-response-ServiceArn"></a>
The Amazon Resource Name (ARN) of the App Runner service that a custom domain name is disassociated from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`

 ** [VpcDNSTargets](#API_DisassociateCustomDomain_ResponseSyntax) **   <a name="apprunner-DisassociateCustomDomain-response-VpcDNSTargets"></a>
DNS Target records for the custom domains of this Amazon VPC.
Type: Array of [VpcDNSTarget](API_VpcDNSTarget.md) objects

## Errors
<a name="API_DisassociateCustomDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **
An unexpected service exception occurred.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.
HTTP Status Code: 400

 ** InvalidStateException **
You can't perform this action when the resource is in its current state.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource doesn't exist for the specified Amazon Resource Name (ARN) in your AWS account.
HTTP Status Code: 400

## Examples
<a name="API_DisassociateCustomDomain_Examples"></a>

### Disassociate a domain name from a service
<a name="API_DisassociateCustomDomain_Example_1"></a>

This example illustrates how to disassociate the domain `example.com` from an App Runner service. The call also disassociates the subdomain `www.example.com` that was associated together with the root domain.

**Note**
 `CertificateValidationRecords` is an optional field and returns an empty response for `AssociateCustomDomain` APIs.

#### Sample Request
<a name="API_DisassociateCustomDomain_Example_1_Request"></a>

```
$ aws apprunner disassociate-custom-domain --cli-input-json "`cat`"
{
  "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa",
  "DomainName": "example.com"
}
```

#### Sample Response
<a name="API_DisassociateCustomDomain_Example_1_Response"></a>

```
{
  "DNSTarget": "zgz2t7wmhi.us-east-1.awsapprunner.com",
  "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa",
  "CustomDomain": {
    "DomainName": "example.com",
    "EnableWWWSubdomain": true,
    "Status": "creating"
  },
  "VpcDNSTargets": [
    {
      "DomainName": "psbqam834h.us-east-1.awsapprunner.com",
      "VpcId": "vpc-4a5b6c7d",
      "VpcIngressConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:vpcingressconnection/my-ingress-connection-name/3f2eb10e2c494674952026f646844e3d"
    }
  ]
}
```

## See Also
<a name="API_DisassociateCustomDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/DisassociateCustomDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/DisassociateCustomDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/DisassociateCustomDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/DisassociateCustomDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/DisassociateCustomDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/DisassociateCustomDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/DisassociateCustomDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/DisassociateCustomDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/DisassociateCustomDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/DisassociateCustomDomain)
