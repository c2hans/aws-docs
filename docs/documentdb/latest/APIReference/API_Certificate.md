---
source_url: https://docs.aws.amazon.com/documentdb/latest/APIReference/API_Certificate.html
---

# Certificate
<a name="API_Certificate"></a>

A certificate authority (CA) certificate for an AWS account.

## Contents
<a name="API_Certificate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CertificateArn **
The Amazon Resource Name (ARN) for the certificate.
Example: `arn:aws:rds:us-east-1::cert:rds-ca-2019`
Type: String
Required: No

 ** CertificateIdentifier **
The unique key that identifies a certificate.
Example: `rds-ca-2019`
Type: String
Required: No

 ** CertificateType **
The type of the certificate.
Example: `CA`
Type: String
Required: No

 ** Thumbprint **
The thumbprint of the certificate.
Type: String
Required: No

 ** ValidFrom **
The starting date-time from which the certificate is valid.
Example: `2019-07-31T17:57:09Z`
Type: Timestamp
Required: No

 ** ValidTill **
The date-time after which the certificate is no longer valid.
Example: `2024-07-31T17:57:09Z`
Type: Timestamp
Required: No

## See Also
<a name="API_Certificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/Certificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/Certificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/Certificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
