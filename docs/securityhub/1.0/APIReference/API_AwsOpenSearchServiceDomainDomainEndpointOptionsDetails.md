---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsOpenSearchServiceDomainDomainEndpointOptionsDetails.html
---

# AwsOpenSearchServiceDomainDomainEndpointOptionsDetails
<a name="API_AwsOpenSearchServiceDomainDomainEndpointOptionsDetails"></a>

Information about additional options for the domain endpoint.

## Contents
<a name="API_AwsOpenSearchServiceDomainDomainEndpointOptionsDetails_Contents"></a>

 ** CustomEndpoint **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDomainEndpointOptionsDetails-CustomEndpoint"></a>
The fully qualified URL for the custom endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CustomEndpointCertificateArn **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDomainEndpointOptionsDetails-CustomEndpointCertificateArn"></a>
The ARN for the security certificate. The certificate is managed in ACM.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CustomEndpointEnabled **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDomainEndpointOptionsDetails-CustomEndpointEnabled"></a>
Whether to enable a custom endpoint for the domain.
Type: Boolean
Required: No

 ** EnforceHTTPS **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDomainEndpointOptionsDetails-EnforceHTTPS"></a>
Whether to require that all traffic to the domain arrive over HTTPS.
Type: Boolean
Required: No

 ** TLSSecurityPolicy **   <a name="securityhub-Type-AwsOpenSearchServiceDomainDomainEndpointOptionsDetails-TLSSecurityPolicy"></a>
The TLS security policy to apply to the HTTPS endpoint of the OpenSearch domain.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsOpenSearchServiceDomainDomainEndpointOptionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsOpenSearchServiceDomainDomainEndpointOptionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsOpenSearchServiceDomainDomainEndpointOptionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsOpenSearchServiceDomainDomainEndpointOptionsDetails)
