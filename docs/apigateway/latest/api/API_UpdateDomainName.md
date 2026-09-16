---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_UpdateDomainName.html
---

# UpdateDomainName
<a name="API_UpdateDomainName"></a>

Changes information about the DomainName resource.

## Request Syntax
<a name="API_UpdateDomainName_RequestSyntax"></a>

```
PATCH /domainnames/{{domain_name}}?domainNameId={{domainNameId}} HTTP/1.1
Content-type: application/json

{
   "patchOperations": [
      {
         "from": "{{string}}",
         "op": "{{string}}",
         "path": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateDomainName_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain\_name](#API_UpdateDomainName_RequestSyntax) **   <a name="apigw-UpdateDomainName-request-uri-domainName"></a>
The name of the DomainName resource to be changed.
Required: Yes

 ** [domainNameId](#API_UpdateDomainName_RequestSyntax) **   <a name="apigw-UpdateDomainName-request-uri-domainNameId"></a>
 The identifier for the domain name resource. Supported only for private custom domain names.

## Request Body
<a name="API_UpdateDomainName_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [patchOperations](#API_UpdateDomainName_RequestSyntax) **   <a name="apigw-UpdateDomainName-request-patchOperations"></a>
For more information about supported patch operations, see [Patch Operations](patch-operations.md).
Type: Array of [PatchOperation](API_PatchOperation.md) objects
Required: No

## Response Syntax
<a name="API_UpdateDomainName_ResponseSyntax"></a>

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
<a name="API_UpdateDomainName_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateArn](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-certificateArn"></a>
The reference to an AWS-managed certificate that will be used by edge-optimized endpoint or private endpoint for this domain name. AWS Certificate Manager is the only supported source.
Type: String

 ** [certificateName](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-certificateName"></a>
The name of the certificate that will be used by edge-optimized endpoint or private endpoint for this domain name.
Type: String

 ** [certificateUploadDate](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-certificateUploadDate"></a>
The timestamp when the certificate that was used by edge-optimized endpoint or private endpoint for this domain name was uploaded.
Type: Timestamp

 ** [distributionDomainName](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-distributionDomainName"></a>
The domain name of the Amazon CloudFront distribution associated with this custom domain name for an edge-optimized endpoint. You set up this association when adding a DNS record pointing the custom domain name to this distribution name. For more information about CloudFront distributions, see the Amazon CloudFront documentation.
Type: String

 ** [distributionHostedZoneId](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-distributionHostedZoneId"></a>
The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint. The valid value is `Z2FDTNDATAQYW2` for all the regions. For more information, see Set up a Regional Custom Domain Name and AWS Regions and Endpoints for API Gateway.
Type: String

 ** [domainName](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-domainName"></a>
The custom domain name as an API host name, for example, `my-api.example.com`.
Type: String

 ** [domainNameArn](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-domainNameArn"></a>
The ARN of the domain name.
Type: String

 ** [domainNameId](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-domainNameId"></a>
The identifier for the domain name resource. Supported only for private custom domain names.
Type: String

 ** [domainNameStatus](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-domainNameStatus"></a>
The status of the DomainName migration. The valid values are `AVAILABLE` and `UPDATING`. If the status is `UPDATING`, the domain cannot be modified further until the existing operation is complete. If it is `AVAILABLE`, the domain can be updated.
Type: String
Valid Values: `AVAILABLE | UPDATING | PENDING | PENDING_CERTIFICATE_REIMPORT | PENDING_OWNERSHIP_VERIFICATION | FAILED`

 ** [domainNameStatusMessage](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-domainNameStatusMessage"></a>
An optional text message containing detailed information about status of the DomainName migration.
Type: String

 ** [endpointAccessMode](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-endpointAccessMode"></a>
 The endpoint access mode of the DomainName.
Type: String
Valid Values: `BASIC | STRICT`

 ** [endpointConfiguration](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-endpointConfiguration"></a>
The endpoint configuration of this DomainName showing the endpoint types and IP address types of the domain name.
Type: [EndpointConfiguration](API_EndpointConfiguration.md) object

 ** [managementPolicy](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-managementPolicy"></a>
A stringified JSON policy document that applies to the API Gateway Management service for this DomainName. This policy document controls access for access association sources to create domain name access associations with this DomainName. Supported only for private custom domain names.
Type: String

 ** [mutualTlsAuthentication](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-mutualTlsAuthentication"></a>
The mutual TLS authentication configuration for a custom domain name. If specified, API Gateway performs two-way authentication between the client and the server. Clients must present a trusted certificate to access your API.
Type: [MutualTlsAuthentication](API_MutualTlsAuthentication.md) object

 ** [ownershipVerificationCertificateArn](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-ownershipVerificationCertificateArn"></a>
The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the regionalCertificateArn.
Type: String

 ** [policy](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-policy"></a>
A stringified JSON policy document that applies to the `execute-api` service for this DomainName regardless of the caller and Method configuration. Supported only for private custom domain names.
Type: String

 ** [regionalCertificateArn](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-regionalCertificateArn"></a>
The reference to an AWS-managed certificate that will be used for validating the regional domain name. AWS Certificate Manager is the only supported source.
Type: String

 ** [regionalCertificateName](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-regionalCertificateName"></a>
The name of the certificate that will be used for validating the regional domain name.
Type: String

 ** [regionalDomainName](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-regionalDomainName"></a>
The domain name associated with the regional endpoint for this custom domain name. You set up this association by adding a DNS record that points the custom domain name to this regional domain name. The regional domain name is returned by API Gateway when you create a regional endpoint.
Type: String

 ** [regionalHostedZoneId](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-regionalHostedZoneId"></a>
The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint. For more information, see Set up a Regional Custom Domain Name and AWS Regions and Endpoints for API Gateway.
Type: String

 ** [routingMode](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-routingMode"></a>
The routing mode for this domain name. The routing mode determines how API Gateway sends traffic from your custom domain name to your APIs.
Type: String
Valid Values: `BASE_PATH_MAPPING_ONLY | ROUTING_RULE_ONLY | ROUTING_RULE_THEN_BASE_PATH_MAPPING`

 ** [securityPolicy](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-securityPolicy"></a>
The Transport Layer Security (TLS) version \+ cipher suite for this DomainName.
Type: String
Valid Values: `TLS_1_0 | TLS_1_2 | SecurityPolicy_TLS13_1_3_2025_09 | SecurityPolicy_TLS13_1_3_FIPS_2025_09 | SecurityPolicy_TLS13_1_2_PFS_PQ_2025_09 | SecurityPolicy_TLS13_1_2_FIPS_PQ_2025_09 | SecurityPolicy_TLS13_1_2_PQ_2025_09 | SecurityPolicy_TLS13_1_2_2021_06 | SecurityPolicy_TLS13_2025_EDGE | SecurityPolicy_TLS12_PFS_2025_EDGE | SecurityPolicy_TLS12_2018_EDGE`

 ** [tags](#API_UpdateDomainName_ResponseSyntax) **   <a name="apigw-UpdateDomainName-response-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map

## Errors
<a name="API_UpdateDomainName_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.
HTTP Status Code: 400

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 409

 ** LimitExceededException **
The request exceeded the rate limit. Retry after the specified time period.
HTTP Status Code: 429

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
<a name="API_UpdateDomainName_Examples"></a>

### Rotate the certificate name of an edge-optimized custom domain name
<a name="API_UpdateDomainName_Example_1"></a>

This example illustrates one usage of UpdateDomainName.

#### Sample Request
<a name="API_UpdateDomainName_Example_1_Request"></a>

```
PATCH /domainnames/mon-api.com HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160615T214257Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160615/us-east-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sig4_hash}

{
  "patchOperations" : [ {
    "op" : "replace",
    "path" : "/certificateName",
    "value" : "mon-api.com-cert-rotated-today"
    },{
    "op" : "replace",
    "path" : "/certificateArn",
    "value" : "arn:aws:acm:us-east-1:012345678910:certificate/34a95aa1-77fa-427c-aa07-3a88bd9f3c0a"
  }]
}
```

#### Sample Response
<a name="API_UpdateDomainName_Example_1_Response"></a>

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
      "href": "/domainnames/mon-api.com"
    },
    "basepathmapping:by-base-path": {
      "href": "/domainnames/mon-api.com/basepathmappings/{base_path}",
      "templated": true
    },
    "basepathmapping:create": {
      "href": "/domainnames/mon-api.com/basepathmappings"
    },
    "domainname:basepathmappings": {
      "href": "/domainnames/mon-api.com/basepathmappings{?limit}",
      "templated": true
    },
    "domainname:delete": {
      "href": "/domainnames/mon-api.com"
    },
    "domainname:update": {
      "href": "/domainnames/mon-api.com"
    }
  },
  "certificateArn": "arn:aws:acm:us-east-1:012345678910:certificate/34a95aa1-77fa-427c-aa07-3a88bd9f3c0a",
  "certificateName": "mon-api.com-cert-rotated-today",
  "certificateUploadDate": "2016-06-15T21:14:43Z",
  "distributionDomainName": "d2ck2x1vuc8qzh.cloudfront.net",
  "domainName": "mon-api.com"
}
```

## See Also
<a name="API_UpdateDomainName_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/UpdateDomainName)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/UpdateDomainName)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/UpdateDomainName)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/UpdateDomainName)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/UpdateDomainName)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/UpdateDomainName)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/UpdateDomainName)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/UpdateDomainName)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/UpdateDomainName)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/UpdateDomainName)
