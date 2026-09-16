---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetDomainName.html
---

# GetDomainName
<a name="API_GetDomainName"></a>

Represents a domain name that is contained in a simpler, more intuitive URL that can be called.

## Request Syntax
<a name="API_GetDomainName_RequestSyntax"></a>

```
GET /domainnames/{{domain_name}}?domainNameId={{domainNameId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDomainName_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain\_name](#API_GetDomainName_RequestSyntax) **   <a name="apigw-GetDomainName-request-uri-domainName"></a>
The name of the DomainName resource.
Required: Yes

 ** [domainNameId](#API_GetDomainName_RequestSyntax) **   <a name="apigw-GetDomainName-request-uri-domainNameId"></a>
 The identifier for the domain name resource. Required for private custom domain names.

## Request Body
<a name="API_GetDomainName_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDomainName_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificateArn": "string",
   "certificateName": "string",
   "certificateUploadDate": number,
   "distributionDomainName": "string",
   "distributionHostedZoneId": "string",
   "domainName": "string",
   "domainNameArn": "string",
   "domainNameId": "string",
   "domainNameStatus": "string",
   "domainNameStatusMessage": "string",
   "endpointAccessMode": "string",
   "endpointConfiguration": {
      "ipAddressType": "string",
      "types": [ "string" ],
      "vpcEndpointIds": [ "string" ]
   },
   "managementPolicy": "string",
   "mutualTlsAuthentication": {
      "truststoreUri": "string",
      "truststoreVersion": "string",
      "truststoreWarnings": [ "string" ]
   },
   "ownershipVerificationCertificateArn": "string",
   "policy": "string",
   "regionalCertificateArn": "string",
   "regionalCertificateName": "string",
   "regionalDomainName": "string",
   "regionalHostedZoneId": "string",
   "routingMode": "string",
   "securityPolicy": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetDomainName_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateArn](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-certificateArn"></a>
The reference to an AWS-managed certificate that will be used by edge-optimized endpoint or private endpoint for this domain name. AWS Certificate Manager is the only supported source.
Type: String

 ** [certificateName](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-certificateName"></a>
The name of the certificate that will be used by edge-optimized endpoint or private endpoint for this domain name.
Type: String

 ** [certificateUploadDate](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-certificateUploadDate"></a>
The timestamp when the certificate that was used by edge-optimized endpoint or private endpoint for this domain name was uploaded.
Type: Timestamp

 ** [distributionDomainName](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-distributionDomainName"></a>
The domain name of the Amazon CloudFront distribution associated with this custom domain name for an edge-optimized endpoint. You set up this association when adding a DNS record pointing the custom domain name to this distribution name. For more information about CloudFront distributions, see the Amazon CloudFront documentation.
Type: String

 ** [distributionHostedZoneId](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-distributionHostedZoneId"></a>
The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint. The valid value is `Z2FDTNDATAQYW2` for all the regions. For more information, see Set up a Regional Custom Domain Name and AWS Regions and Endpoints for API Gateway.
Type: String

 ** [domainName](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-domainName"></a>
The custom domain name as an API host name, for example, `my-api.example.com`.
Type: String

 ** [domainNameArn](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-domainNameArn"></a>
The ARN of the domain name.
Type: String

 ** [domainNameId](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-domainNameId"></a>
The identifier for the domain name resource. Supported only for private custom domain names.
Type: String

 ** [domainNameStatus](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-domainNameStatus"></a>
The status of the DomainName migration. The valid values are `AVAILABLE` and `UPDATING`. If the status is `UPDATING`, the domain cannot be modified further until the existing operation is complete. If it is `AVAILABLE`, the domain can be updated.
Type: String
Valid Values: `AVAILABLE | UPDATING | PENDING | PENDING_CERTIFICATE_REIMPORT | PENDING_OWNERSHIP_VERIFICATION | FAILED`

 ** [domainNameStatusMessage](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-domainNameStatusMessage"></a>
An optional text message containing detailed information about status of the DomainName migration.
Type: String

 ** [endpointAccessMode](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-endpointAccessMode"></a>
 The endpoint access mode of the DomainName.
Type: String
Valid Values: `BASIC | STRICT`

 ** [endpointConfiguration](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-endpointConfiguration"></a>
The endpoint configuration of this DomainName showing the endpoint types and IP address types of the domain name.
Type: [EndpointConfiguration](API_EndpointConfiguration.md) object

 ** [managementPolicy](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-managementPolicy"></a>
A stringified JSON policy document that applies to the API Gateway Management service for this DomainName. This policy document controls access for access association sources to create domain name access associations with this DomainName. Supported only for private custom domain names.
Type: String

 ** [mutualTlsAuthentication](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-mutualTlsAuthentication"></a>
The mutual TLS authentication configuration for a custom domain name. If specified, API Gateway performs two-way authentication between the client and the server. Clients must present a trusted certificate to access your API.
Type: [MutualTlsAuthentication](API_MutualTlsAuthentication.md) object

 ** [ownershipVerificationCertificateArn](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-ownershipVerificationCertificateArn"></a>
The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the regionalCertificateArn.
Type: String

 ** [policy](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-policy"></a>
A stringified JSON policy document that applies to the `execute-api` service for this DomainName regardless of the caller and Method configuration. Supported only for private custom domain names.
Type: String

 ** [regionalCertificateArn](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-regionalCertificateArn"></a>
The reference to an AWS-managed certificate that will be used for validating the regional domain name. AWS Certificate Manager is the only supported source.
Type: String

 ** [regionalCertificateName](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-regionalCertificateName"></a>
The name of the certificate that will be used for validating the regional domain name.
Type: String

 ** [regionalDomainName](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-regionalDomainName"></a>
The domain name associated with the regional endpoint for this custom domain name. You set up this association by adding a DNS record that points the custom domain name to this regional domain name. The regional domain name is returned by API Gateway when you create a regional endpoint.
Type: String

 ** [regionalHostedZoneId](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-regionalHostedZoneId"></a>
The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint. For more information, see Set up a Regional Custom Domain Name and AWS Regions and Endpoints for API Gateway.
Type: String

 ** [routingMode](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-routingMode"></a>
The routing mode for this domain name. The routing mode determines how API Gateway sends traffic from your custom domain name to your APIs.
Type: String
Valid Values: `BASE_PATH_MAPPING_ONLY | ROUTING_RULE_ONLY | ROUTING_RULE_THEN_BASE_PATH_MAPPING`

 ** [securityPolicy](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-securityPolicy"></a>
The Transport Layer Security (TLS) version \+ cipher suite for this DomainName.
Type: String
Valid Values: `TLS_1_0 | TLS_1_2 | SecurityPolicy_TLS13_1_3_2025_09 | SecurityPolicy_TLS13_1_3_FIPS_2025_09 | SecurityPolicy_TLS13_1_2_PFS_PQ_2025_09 | SecurityPolicy_TLS13_1_2_FIPS_PQ_2025_09 | SecurityPolicy_TLS13_1_2_PQ_2025_09 | SecurityPolicy_TLS13_1_2_2021_06 | SecurityPolicy_TLS13_2025_EDGE | SecurityPolicy_TLS12_PFS_2025_EDGE | SecurityPolicy_TLS12_2018_EDGE`

 ** [tags](#API_GetDomainName_ResponseSyntax) **   <a name="apigw-GetDomainName-response-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map

## Errors
<a name="API_GetDomainName_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource is not found. Make sure that the request URI is correct.
HTTP Status Code: 404

 ** TooManyRequestsException **
The request has reached its throttling limit. Retry after the specified time period.
HTTP Status Code: 429

 ** UnauthorizedException **
The request is denied because the caller has insufficient permissions.
HTTP Status Code: 401

## Examples
<a name="API_GetDomainName_Examples"></a>

### Get a information about a DomainName
<a name="API_GetDomainName_Example_1"></a>

This example illustrates one usage of GetDomainName.

#### Sample Request
<a name="API_GetDomainName_Example_1_Request"></a>

```
GET /domainnames/a.b.c.com HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160602T000654Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160602/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}
```

#### Sample Response
<a name="API_GetDomainName_Example_1_Response"></a>

```
{
  "_links": {
    "curies": [
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-basepathmapping-{rel}.html",
        "name": "basepathmapping",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-domainname-{rel}.html",
        "name": "domainname",
        "templated": true
      }
    ],
    "self": {
      "href": "/domainnames/a.b.c.com"
    },
    "basepathmapping:by-base-path": {
      "href": "/domainnames/a.b.c.com/basepathmappings/{base_path}",
      "templated": true
    },
    "basepathmapping:create": {
      "href": "/domainnames/a.b.c.com/basepathmappings"
    },
    "domainname:basepathmappings": {
      "href": "/domainnames/a.b.c.com/basepathmappings{?limit}",
      "templated": true
    },
    "domainname:delete": {
      "href": "/domainnames/a.b.c.com"
    },
    "domainname:update": {
      "href": "/domainnames/a.b.c.com"
    }
  },
  "certificateName": "test",
  "certificateArn": "arn:aws:acm:us-east-1:012345678910:certificate/certificate_id",
  "certificateUploadDate": "2016-04-18T22:16:04Z",
  "distributionDomainName": "d3ih7ecqtec0mt.cloudfront.net",
  "domainName": "a.b.c.com"
}
```

### Get a information about a DomainName with an endpoint type of private
<a name="API_GetDomainName_Example_2"></a>

This example illustrates one usage of GetDomainName.

#### Sample Request
<a name="API_GetDomainName_Example_2_Request"></a>

```
GET /domainnames/private.a.b.c.com?domainNameId=abcd1234 HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160602T000654Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160602/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}
```

#### Sample Response
<a name="API_GetDomainName_Example_2_Response"></a>

```
{
  "_links": {
      "curies": [
          {
              "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-basepathmapping-{rel}.html",
              "name": "basepathmapping",
              "templated": true
          },
          {
              "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-domainname-{rel}.html",
              "name": "domainname",
              "templated": true
          }
      ],
      "self": {
          "href": "/domainnames/private.a.b.c.com?domainNameId=abcd1234"
      },
     "basepathmapping:by-base-path": {
          "href": "/domainnames/private.a.b.c.com/basepathmappings/{base_path}?domainNameId=abcd1234",
          "templated": true
      },
      "basepathmapping:create": {
          "href": "/domainnames/private.a.b.c.com/basepathmappings?domainNameId=abcd1234"
      },
      "domainname:basepathmappings": {
          "href": "/domainnames/private.a.b.c.com/basepathmappings?domainNameId=abcd1234{&limit}",
          "templated": true
      },
      "domainname:delete": {
          "href": "/domainnames/private.a.b.c.com?domainNameId=abcd1234"
      },
      "domainname:update": {
          "href": "/domainnames/private.a.b.c.com?domainNameId=abcd1234"
      }
  },
  "certificateArn": "arn:aws:acm:us-east-1:012345678910:certificate/certificate_id",
  "certificateUploadDate": "2024-10-28T17:57:00Z",
  "domainName": "private.a.b.c.com",
  "domainNameArn": "arn:aws:apigateway:us-east-1:012345678910:/domainnames/a.b.c.com+abcd1234",
  "domainNameId": "abcd1234",
  "domainNameStatus": "AVAILABLE",
  "endpointConfiguration": {
      "vpcEndpointIds": null,
      "types": "PRIVATE",
  },
  "policy": "..."
  "securityPolicy": "TLS_1_2",
  "tags": {}
}
```

## See Also
<a name="API_GetDomainName_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetDomainName)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetDomainName)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetDomainName)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetDomainName)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetDomainName)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetDomainName)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetDomainName)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetDomainName)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetDomainName)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetDomainName)
