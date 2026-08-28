---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_ClientCertificate.html
---

# ClientCertificate
<a name="API_ClientCertificate"></a>

Represents a client certificate used to configure client-side SSL authentication while sending requests to the integration endpoint.

## Contents
<a name="API_ClientCertificate_Contents"></a>

 ** clientCertificateId **   <a name="apigw-Type-ClientCertificate-clientCertificateId"></a>
The identifier of the client certificate.
Type: String
Required: No

 ** createdDate **   <a name="apigw-Type-ClientCertificate-createdDate"></a>
The timestamp when the client certificate was created.
Type: Timestamp
Required: No

 ** description **   <a name="apigw-Type-ClientCertificate-description"></a>
The description of the client certificate.
Type: String
Required: No

 ** expirationDate **   <a name="apigw-Type-ClientCertificate-expirationDate"></a>
The timestamp when the client certificate will expire.
Type: Timestamp
Required: No

 ** pemEncodedCertificate **   <a name="apigw-Type-ClientCertificate-pemEncodedCertificate"></a>
The PEM-encoded public key of the client certificate, which can be used to configure certificate authentication in the integration endpoint .
Type: String
Required: No

 ** tags **   <a name="apigw-Type-ClientCertificate-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map
Required: No

## See Also
<a name="API_ClientCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/ClientCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/ClientCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/ClientCertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
