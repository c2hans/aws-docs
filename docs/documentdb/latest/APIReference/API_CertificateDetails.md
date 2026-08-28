---
source_url: https://docs.aws.amazon.com/documentdb/latest/APIReference/API_CertificateDetails.html
---

# CertificateDetails
<a name="API_CertificateDetails"></a>

Returns the details of the DB instance’s server certificate.

For more information, see [Updating Your Amazon DocumentDB TLS Certificates](https://docs.aws.amazon.com/documentdb/latest/devguide/ca_cert_rotation.html) and [ Encrypting Data in Transit](https://docs.aws.amazon.com/documentdb/latest/devguide/security.encryption.ssl.html) in the *Amazon DocumentDB Developer Guide*.

## Contents
<a name="API_CertificateDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CAIdentifier **
The CA identifier of the CA certificate used for the DB instance's server certificate.
Type: String
Required: No

 ** ValidTill **
The expiration date of the DB instance’s server certificate.
Type: Timestamp
Required: No

## See Also
<a name="API_CertificateDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/CertificateDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/CertificateDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/CertificateDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
