---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_DomainName.html
---

# DomainName
<a name="API_DomainName"></a>

Represents a custom domain name as a user-friendly host name of an API (RestApi).

## Contents
<a name="API_DomainName_Contents"></a>

 ** certificateArn **   <a name="apigw-Type-DomainName-certificateArn"></a>
The reference to an AWS-managed certificate that will be used by edge-optimized endpoint or private endpoint for this domain name. AWS Certificate Manager is the only supported source.
Type: String
Required: No

 ** certificateName **   <a name="apigw-Type-DomainName-certificateName"></a>
The name of the certificate that will be used by edge-optimized endpoint or private endpoint for this domain name.
Type: String
Required: No

 ** certificateUploadDate **   <a name="apigw-Type-DomainName-certificateUploadDate"></a>
The timestamp when the certificate that was used by edge-optimized endpoint or private endpoint for this domain name was uploaded.
Type: Timestamp
Required: No

 ** distributionDomainName **   <a name="apigw-Type-DomainName-distributionDomainName"></a>
The domain name of the Amazon CloudFront distribution associated with this custom domain name for an edge-optimized endpoint. You set up this association when adding a DNS record pointing the custom domain name to this distribution name. For more information about CloudFront distributions, see the Amazon CloudFront documentation.
Type: String
Required: No

 ** distributionHostedZoneId **   <a name="apigw-Type-DomainName-distributionHostedZoneId"></a>
The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint. The valid value is `Z2FDTNDATAQYW2` for all the regions. For more information, see Set up a Regional Custom Domain Name and AWS Regions and Endpoints for API Gateway.
Type: String
Required: No

 ** domainName **   <a name="apigw-Type-DomainName-domainName"></a>
The custom domain name as an API host name, for example, `my-api.example.com`.
Type: String
Required: No

 ** domainNameArn **   <a name="apigw-Type-DomainName-domainNameArn"></a>
The ARN of the domain name.
Type: String
Required: No

 ** domainNameId **   <a name="apigw-Type-DomainName-domainNameId"></a>
The identifier for the domain name resource. Supported only for private custom domain names.
Type: String
Required: No

 ** domainNameStatus **   <a name="apigw-Type-DomainName-domainNameStatus"></a>
The status of the DomainName migration. The valid values are `AVAILABLE` and `UPDATING`. If the status is `UPDATING`, the domain cannot be modified further until the existing operation is complete. If it is `AVAILABLE`, the domain can be updated.
Type: String
Valid Values: `AVAILABLE | UPDATING | PENDING | PENDING_CERTIFICATE_REIMPORT | PENDING_OWNERSHIP_VERIFICATION | FAILED`
Required: No

 ** domainNameStatusMessage **   <a name="apigw-Type-DomainName-domainNameStatusMessage"></a>
An optional text message containing detailed information about status of the DomainName migration.
Type: String
Required: No

 ** endpointAccessMode **   <a name="apigw-Type-DomainName-endpointAccessMode"></a>
 The endpoint access mode of the DomainName.
Type: String
Valid Values: `BASIC | STRICT`
Required: No

 ** endpointConfiguration **   <a name="apigw-Type-DomainName-endpointConfiguration"></a>
The endpoint configuration of this DomainName showing the endpoint types and IP address types of the domain name.
Type: [EndpointConfiguration](API_EndpointConfiguration.md) object
Required: No

 ** managementPolicy **   <a name="apigw-Type-DomainName-managementPolicy"></a>
A stringified JSON policy document that applies to the API Gateway Management service for this DomainName. This policy document controls access for access association sources to create domain name access associations with this DomainName. Supported only for private custom domain names.
Type: String
Required: No

 ** mutualTlsAuthentication **   <a name="apigw-Type-DomainName-mutualTlsAuthentication"></a>
The mutual TLS authentication configuration for a custom domain name. If specified, API Gateway performs two-way authentication between the client and the server. Clients must present a trusted certificate to access your API.
Type: [MutualTlsAuthentication](API_MutualTlsAuthentication.md) object
Required: No

 ** ownershipVerificationCertificateArn **   <a name="apigw-Type-DomainName-ownershipVerificationCertificateArn"></a>
The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the regionalCertificateArn.
Type: String
Required: No

 ** policy **   <a name="apigw-Type-DomainName-policy"></a>
A stringified JSON policy document that applies to the `execute-api` service for this DomainName regardless of the caller and Method configuration. Supported only for private custom domain names.
Type: String
Required: No

 ** regionalCertificateArn **   <a name="apigw-Type-DomainName-regionalCertificateArn"></a>
The reference to an AWS-managed certificate that will be used for validating the regional domain name. AWS Certificate Manager is the only supported source.
Type: String
Required: No

 ** regionalCertificateName **   <a name="apigw-Type-DomainName-regionalCertificateName"></a>
The name of the certificate that will be used for validating the regional domain name.
Type: String
Required: No

 ** regionalDomainName **   <a name="apigw-Type-DomainName-regionalDomainName"></a>
The domain name associated with the regional endpoint for this custom domain name. You set up this association by adding a DNS record that points the custom domain name to this regional domain name. The regional domain name is returned by API Gateway when you create a regional endpoint.
Type: String
Required: No

 ** regionalHostedZoneId **   <a name="apigw-Type-DomainName-regionalHostedZoneId"></a>
The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint. For more information, see Set up a Regional Custom Domain Name and AWS Regions and Endpoints for API Gateway.
Type: String
Required: No

 ** routingMode **   <a name="apigw-Type-DomainName-routingMode"></a>
The routing mode for this domain name. The routing mode determines how API Gateway sends traffic from your custom domain name to your APIs.
Type: String
Valid Values: `BASE_PATH_MAPPING_ONLY | ROUTING_RULE_ONLY | ROUTING_RULE_THEN_BASE_PATH_MAPPING`
Required: No

 ** securityPolicy **   <a name="apigw-Type-DomainName-securityPolicy"></a>
The Transport Layer Security (TLS) version \+ cipher suite for this DomainName.
Type: String
Valid Values: `TLS_1_0 | TLS_1_2 | SecurityPolicy_TLS13_1_3_2025_09 | SecurityPolicy_TLS13_1_3_FIPS_2025_09 | SecurityPolicy_TLS13_1_2_PFS_PQ_2025_09 | SecurityPolicy_TLS13_1_2_FIPS_PQ_2025_09 | SecurityPolicy_TLS13_1_2_PQ_2025_09 | SecurityPolicy_TLS13_1_2_2021_06 | SecurityPolicy_TLS13_2025_EDGE | SecurityPolicy_TLS12_PFS_2025_EDGE | SecurityPolicy_TLS12_2018_EDGE`
Required: No

 ** tags **   <a name="apigw-Type-DomainName-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map
Required: No

## See Also
<a name="API_DomainName_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/DomainName)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/DomainName)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/DomainName)
