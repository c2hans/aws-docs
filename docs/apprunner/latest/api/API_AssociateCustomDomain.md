---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_AssociateCustomDomain.html
---

# AssociateCustomDomain
<a name="API_AssociateCustomDomain"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Associate your own domain name with the AWS App Runner subdomain URL of your App Runner service.

After you call `AssociateCustomDomain` and receive a successful response, use the information in the [CustomDomain](API_CustomDomain.md) record that's returned to add CNAME records to your Domain Name System (DNS). For each mapped domain name, add a mapping to the target App Runner subdomain and one or more certificate validation records. App Runner then performs DNS validation to verify that you own or control the domain name that you associated. App Runner tracks domain validity in a certificate stored in [AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide).

## Request Syntax
<a name="API_AssociateCustomDomain_RequestSyntax"></a>

```
{
   "DomainName": "{{string}}",
   "EnableWWWSubdomain": {{boolean}},
   "ServiceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateCustomDomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainName](#API_AssociateCustomDomain_RequestSyntax) **   <a name="apprunner-AssociateCustomDomain-request-DomainName"></a>
A custom domain endpoint to associate. Specify a root domain (for example, `example.com`), a subdomain (for example, `login.example.com` or `admin.login.example.com`), or a wildcard (for example, `*.example.com`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9*.-]{1,255}`
Required: Yes

 ** [EnableWWWSubdomain](#API_AssociateCustomDomain_RequestSyntax) **   <a name="apprunner-AssociateCustomDomain-request-EnableWWWSubdomain"></a>
Set to `true` to associate the subdomain `www.DomainName ` with the App Runner service in addition to the base domain.
Default: `true`
Type: Boolean
Required: No

 ** [ServiceArn](#API_AssociateCustomDomain_RequestSyntax) **   <a name="apprunner-AssociateCustomDomain-request-ServiceArn"></a>
The Amazon Resource Name (ARN) of the App Runner service that you want to associate a custom domain name with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: Yes

## Response Syntax
<a name="API_AssociateCustomDomain_ResponseSyntax"></a>

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
<a name="API_AssociateCustomDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CustomDomain](#API_AssociateCustomDomain_ResponseSyntax) **   <a name="apprunner-AssociateCustomDomain-response-CustomDomain"></a>
A description of the domain name that's being associated.
Type: [CustomDomain](API_CustomDomain.md) object

 ** [DNSTarget](#API_AssociateCustomDomain_ResponseSyntax) **   <a name="apprunner-AssociateCustomDomain-response-DNSTarget"></a>
The App Runner subdomain of the App Runner service. The custom domain name is mapped to this target name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`

 ** [ServiceArn](#API_AssociateCustomDomain_ResponseSyntax) **   <a name="apprunner-AssociateCustomDomain-response-ServiceArn"></a>
The Amazon Resource Name (ARN) of the App Runner service with which a custom domain name is associated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`

 ** [VpcDNSTargets](#API_AssociateCustomDomain_ResponseSyntax) **   <a name="apprunner-AssociateCustomDomain-response-VpcDNSTargets"></a>
DNS Target records for the custom domains of this Amazon VPC.
Type: Array of [VpcDNSTarget](API_VpcDNSTarget.md) objects

## Errors
<a name="API_AssociateCustomDomain_Errors"></a>

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

## Examples
<a name="API_AssociateCustomDomain_Examples"></a>

### Associate a domain name and the www subdomain with a service
<a name="API_AssociateCustomDomain_Example_1"></a>

This example illustrates how to associate a custom domain name that you control with an App Runner service. The domain name is the root domain `example.com`, including the special-case subdomain `www.example.com`.

**Note**
 `CertificateValidationRecords` is an optional field and returns an empty response for `AssociateCustomDomain` APIs.

#### Sample Request
<a name="API_AssociateCustomDomain_Example_1_Request"></a>

```
$ aws apprunner associate-custom-domain --cli-input-json "`cat`"
{
  "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa",
  "DomainName": "example.com",
  "EnableWWWSubdomain": true
}
```

#### Sample Response
<a name="API_AssociateCustomDomain_Example_1_Response"></a>

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
<a name="API_AssociateCustomDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/AssociateCustomDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/AssociateCustomDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/AssociateCustomDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/AssociateCustomDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/AssociateCustomDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/AssociateCustomDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/AssociateCustomDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/AssociateCustomDomain)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/AssociateCustomDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/AssociateCustomDomain)
