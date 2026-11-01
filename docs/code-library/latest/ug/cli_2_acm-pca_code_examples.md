---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_acm-pca_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS Private CA examples using AWS CLI
<a name="cli_2_acm-pca_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Private CA.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `create-certificate-authority-audit-report`
<a name="acm-pca_CreateCertificateAuthorityAuditReport_cli_2_topic"></a>

The following code example shows how to use `create-certificate-authority-audit-report`.

**AWS CLI**
**To create a certificate authority audit report**
The following `create-certificate-authority-audit-report` example creates an audit report for the private CA identified by the ARN.

```
aws acm-pca create-certificate-authority-audit-report \
    --certificate-authority-arn {{arn:aws:acm-pca:us-west-2:accountid:certificate-authority/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --s3-bucket-name {{your-bucket-name}} \
    --audit-report-response-format {{JSON}}
```
Output:

```
{
    "AuditReportId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "S3Key": "audit-report/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111.json"
}
```
For more information, see [Use audit reports with your private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaAuditReport.html) in the *AWS Private Certificate Authority User Guide*.
+  For API details, see [CreateCertificateAuthorityAuditReport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/create-certificate-authority-audit-report.html) in *AWS CLI Command Reference*.

### `create-certificate-authority`
<a name="acm-pca_CreateCertificateAuthority_cli_2_topic"></a>

The following code example shows how to use `create-certificate-authority`.

**AWS CLI**
**To create a private certificate authority**
The following `create-certificate-authority` example creates a private certificate authority in your AWS account.

```
aws acm-pca create-certificate-authority \
    --certificate-authority-configuration file://C:\ca_config.txt \
    --revocation-configuration file://C:\revoke_config.txt \
    --certificate-authority-type {{"SUBORDINATE"}} \
    --idempotency-token {{98256344}}
```
Contents of `C:\ca_config.txt`:

```
{
    "KeyAlgorithm": "RSA_2048",
    "SigningAlgorithm": "SHA256WITHRSA",
    "Subject": {
        "Country": "US",
        "Organization": "Example Corp",
        "OrganizationalUnit": "Sales",
        "State": "WA",
        "Locality": "Seattle",
        "CommonName": "www.example.com"
    }
}
```
Contents of `C:\revoke_config.txt`:

```
{
    "CrlConfiguration": {
        "Enabled": true,
        "ExpirationInDays": 7,
        "CustomCname": "crl.example.com",
        "S3BucketName": "amzn-s3-demo-bucket"
    }
}
```
Output:

```
{
    "CertificateAuthorityArn": "arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```
For more information, see [Create a private CA in AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/create-CA.html) in the *AWS Private Certificate Authority User Guide*.
+  For API details, see [CreateCertificateAuthority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/create-certificate-authority.html) in *AWS CLI Command Reference*.

### `delete-certificate-authority`
<a name="acm-pca_DeleteCertificateAuthority_cli_2_topic"></a>

The following code example shows how to use `delete-certificate-authority`.

**AWS CLI**
**To delete a private certificate authority**
The following `delete-certificate-authority` example deletes the certificate authority identified by the ARN.

```
aws acm-pca delete-certificate-authority \
    --certificate-authority-arn {{arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
This command produces no output.
For more information, see [Delete your private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PCADeleteCA.html) in the *AWS Private Certificate Authority User Guide*.
+  For API details, see [DeleteCertificateAuthority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/delete-certificate-authority.html) in *AWS CLI Command Reference*.

### `describe-certificate-authority-audit-report`
<a name="acm-pca_DescribeCertificateAuthorityAuditReport_cli_2_topic"></a>

The following code example shows how to use `describe-certificate-authority-audit-report`.

**AWS CLI**
**To describe an audit report for a certificate authority**
The following `describe-certificate-authority-audit-report` example lists information about the specified audit report for the CA identified by the ARN.

```
aws acm-pca describe-certificate-authority-audit-report \
    --certificate-authority-arn {{arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --audit-report-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}}
```
Output:

```
{
    "AuditReportStatus": "SUCCESS",
    "S3BucketName": "amzn-s3-demo-bucket",
    "S3Key": "audit-report/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222.json",
    "CreatedAt": "2023-08-21T20:30:15.123000+00:00"
}
```
For more information, see [Use audit reports with your private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaAuditReport.html) in the *AWS Private Certificate Authority User Guide*.
+  For API details, see [DescribeCertificateAuthorityAuditReport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/describe-certificate-authority-audit-report.html) in *AWS CLI Command Reference*.

### `describe-certificate-authority`
<a name="acm-pca_DescribeCertificateAuthority_cli_2_topic"></a>

The following code example shows how to use `describe-certificate-authority`.

**AWS CLI**
**To describe a private certificate authority**
The following `describe-certificate-authority` example lists information about the private CA identified by the ARN.

```
aws acm-pca describe-certificate-authority \
    --certificate-authority-arn {{arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
Output:

```
{
    "CertificateAuthority": {
        "Arn": "arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "OwnerAccount": "123456789012",
        "CreatedAt": "2023-08-21T20:30:15.123000+00:00",
        "LastStateChangeAt": "2023-08-21T20:45:47.456000+00:00",
        "Type": "SUBORDINATE",
        "Serial": "4109",
        "Status": "ACTIVE",
        "NotBefore": "2023-08-21T19:45:47+00:00",
        "NotAfter": "2033-08-21T20:45:47+00:00",
        "CertificateAuthorityConfiguration": {
            "KeyAlgorithm": "RSA_2048",
            "SigningAlgorithm": "SHA256WITHRSA",
            "Subject": {
                "Country": "US",
                "Organization": "Example Corp",
                "OrganizationalUnit": "Sales",
                "State": "WA",
                "CommonName": "www.example.com",
                "Locality": "Seattle"
            }
        },
        "RevocationConfiguration": {
            "CrlConfiguration": {
                "Enabled": true,
                "ExpirationInDays": 7,
                "CustomCname": "crl.example.com",
                "S3BucketName": "amzn-s3-demo-bucket",
                "S3ObjectAcl": "BUCKET_OWNER_FULL_CONTROL"
            },
            "OcspConfiguration": {
                "Enabled": false
            }
        },
        "KeyStorageSecurityStandard": "FIPS_140_2_LEVEL_3_OR_HIGHER",
        "UsageMode": "GENERAL_PURPOSE"
    }
}
```
For more information, see [View a private CA](https://docs.aws.amazon.com/privateca/latest/userguide/describe-CA.html) in the *AWS Private Certificate Authority User Guide*.
+  For API details, see [DescribeCertificateAuthority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/describe-certificate-authority.html) in *AWS CLI Command Reference*.

### `get-certificate-authority-certificate`
<a name="acm-pca_GetCertificateAuthorityCertificate_cli_2_topic"></a>

The following code example shows how to use `get-certificate-authority-certificate`.

**AWS CLI**
**To retrieve a certificate authority (CA) certificate**
The following `get-certificate-authority-certificate` example retrieves the certificate and certificate chain for the private CA specified by the ARN.

```
aws acm-pca get-certificate-authority-certificate \
    --certificate-authority-arn {{arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --output {{text}}
```
Output:

```
-----BEGIN CERTIFICATE-----
MIIDrzCCApegAwIBAgIRAOskdzLvcj1eShkoyEE693AwDQYJKoZIhvcNAQELBQAw
cTELMAkGA1UEBhMCVVMxEzARBgNVBAgMCldhc2hpbmd0b24xEDAOBgNVBAcMB1Nl
kdRGB6P2hpxstDOUIwAoCbhoaWwfA4ybJznf+jOQhAziNlRdKQRR8nODWpKt7H9w
dJ5nxsTk/fniJz86Ddtp6n8s82wYdkN3cVffeK72A9aTCOU=
-----END CERTIFICATE----- -----BEGIN CERTIFICATE-----
MIIDxjCCAq6gAwIBAgIQCv2jEXAMPLEi8l1pBwUNKjANBgkqhkiG9w0BAQsFADBx
MQswCQYDVQQGEwJVUzETMBEGA1UECAwKV2FzaGluZ3RvbjEQMA4GA1UEBwwHU2Vh
dHRsZTEVMBMGA1UECgwMRXhhbXBsZSBDb3JwMQ4wDAYDVQQLDAVTYWxlczEUMBIG
A1UEAwwLZXhhbXBsZS5jb20=
-----END CERTIFICATE-----
```
For more information, see [Installing the CA certificate](https://docs.aws.amazon.com/privateca/latest/userguide/PCACertInstall.html) in the *AWS Private Certificate Authority User Guide*.
+  For API details, see [GetCertificateAuthorityCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-certificate-authority-certificate.html) in *AWS CLI Command Reference*.

### `get-certificate-authority-csr`
<a name="acm-pca_GetCertificateAuthorityCsr_cli_2_topic"></a>

The following code example shows how to use `get-certificate-authority-csr`.

**AWS CLI**
**To retrieve the certificate signing request for a certificate authority**
The following `get-certificate-authority-csr` example retrieves the CSR for the private CA specified by the ARN.

```
aws acm-pca get-certificate-authority-csr \
    --certificate-authority-arn {{arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --output {{text}}
```
Output:

```
-----BEGIN CERTIFICATE REQUEST-----
MIICvjCCAaYCAQAweTELMAkGA1UEBhMCVVMxEzARBgNVBAgMCldhc2hpbmd0b24x
EDAOBgNVBAcMB1NlYXR0bGUxFTATBgNVBAoMDEV4YW1wbGUgQ29ycDEOMAwGA1UE
CwwFU2FsZXMxGDAWBgNVBAMMD3d3dy5leGFtcGxlLmNvbTCCASIwDQYJKoZIhvcN
AQEBBQADggEPADCCAQoCggEBAMEXAMPLEKEYBODYPLACEHOLDERVALUE0000000=
-----END CERTIFICATE REQUEST-----
```
For more information, see [Installing the CA certificate](https://docs.aws.amazon.com/privateca/latest/userguide/PCACertInstall.html) in the *AWS Private Certificate Authority User Guide*.
+  For API details, see [GetCertificateAuthorityCsr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-certificate-authority-csr.html) in *AWS CLI Command Reference*.

### `get-certificate`
<a name="acm-pca_GetCertificate_cli_2_topic"></a>

The following code example shows how to use `get-certificate`.

**AWS CLI**
**To retrieve an issued certificate**
The following `get-certificate` example retrieves a certificate from the specified private CA.

```
aws acm-pca get-certificate \
    --certificate-authority-arn {{arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --certificate-arn {{arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/certificate/6707447683a9b7f4055627ffd55cebcc}} \
    --output {{text}}
```
Output:

```
-----BEGIN CERTIFICATE-----
MIIEDzCCAvegAwIBAgIRAJuJ8f6ZVYL7gG/rS3qvrZMwDQYJKoZIhvcNAQELBQAw
cTELMAkGA1UEBhMCVVMxEzARBgNVBAgMCldhc2hpbmd0b24xEDAOBgNVBAcMB1Nl
    ....certificate body truncated for brevity....
tKCSglgZZrd4FdLw1EkGm+UVXnodwMtJEQyy3oTfZjURPIyyaqskTu/KSS7YDjK0
KQNy73D6LtmdOEbAyq10XiDxqY41lvKHJ1eZrPaBmYNABxU=
-----END CERTIFICATE---- -----BEGIN CERTIFICATE-----
MIIDrzCCApegAwIBAgIRAOskdzLvcj1eShkoyEE693AwDQYJKoZIhvcNAQELBQAw
cTELMAkGA1UEBhMCVVMxEzARBgNVBAgMCldhc2hpbmd0b24xEDAOBgNVBAcMB1Nl
    ...certificate body truncated for brevity....
kdRGB6P2hpxstDOUIwAoCbhoaWwfA4ybJznf+jOQhAziNlRdKQRR8nODWpKt7H9w
dJ5nxsTk/fniJz86Ddtp6n8s82wYdkN3cVffeK72A9aTCOU=
-----END CERTIFICATE-----
```
The first part of the output is the certificate itself. The second part is the certificate chain that chains to the root CA certificate. Note that when you use the `--output text` option, a `TAB` character is inserted between the two certificate pieces (that is the cause of the indented text). If you intend to take this output and parse the certificates with other tools, you might need to remove the `TAB` character so it is processed correctly.
For more information, see [Retrieve a private certificate](https://docs.aws.amazon.com/privateca/latest/userguide/PcaGetCert.html) in the *AWS Private Certificate Authority User Guide*.
+  For API details, see [GetCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-certificate.html) in *AWS CLI Command Reference*.

### `import-certificate-authority-certificate`
<a name="acm-pca_ImportCertificateAuthorityCertificate_cli_2_topic"></a>

The following code example shows how to use `import-certificate-authority-certificate`.

**AWS CLI**
**To import your certificate authority certificate into ACM PCA**
The following `import-certificate-authority-certificate` example imports the signed private CA certificate for the CA specified by the ARN into ACM PCA.

```
aws acm-pca import-certificate-authority-certificate \
    --certificate-authority-arn {{arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --certificate fileb://C:\ca_cert.pem \
    --certificate-chain fileb://C:\ca_cert_chain.pem
```
This command produces no output.
For more information, see [Installing the CA certificate](https://docs.aws.amazon.com/privateca/latest/userguide/PCACertInstall.html) in the *AWS Private Certificate Authority User Guide*.
+  For API details, see [ImportCertificateAuthorityCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/import-certificate-authority-certificate.html) in *AWS CLI Command Reference*.

### `issue-certificate`
<a name="acm-pca_IssueCertificate_cli_2_topic"></a>

The following code example shows how to use `issue-certificate`.

**AWS CLI**
**To issue a private certificate**
The following `issue-certificate` example uses the private CA specified by the ARN to issue a private certificate.

```
aws acm-pca issue-certificate \
    --certificate-authority-arn {{arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --csr fileb://C:\cert_1.csr \
    --signing-algorithm {{"SHA256WITHRSA"}} \
    --validity Value=365,Type="DAYS" \
    --idempotency-token {{1234}}
```
Output:

```
{
    "CertificateArn": "arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/certificate/6707447683a9b7f4055627ffd55cebcc"
}
```
For more information, see [Issue private end-entity certificates](https://docs.aws.amazon.com/privateca/latest/userguide/PcaIssueCert.html) in the *AWS Private Certificate Authority User Guide*.
+  For API details, see [IssueCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/issue-certificate.html) in *AWS CLI Command Reference*.

### `list-certificate-authorities`
<a name="acm-pca_ListCertificateAuthorities_cli_2_topic"></a>

The following code example shows how to use `list-certificate-authorities`.

**AWS CLI**
**To list your private certificate authorities**
The following `list-certificate-authorities` example lists information about all of the private CAs in your account.

```
aws acm-pca list-certificate-authorities \
    --max-results {{10}}
```
Output:

```
{
    "CertificateAuthorities": [
        {
            "Arn": "arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "OwnerAccount": "123456789012",
            "CreatedAt": "2023-08-21T20:30:15.123000+00:00",
            "LastStateChangeAt": "2023-08-21T20:45:47.456000+00:00",
            "Type": "SUBORDINATE",
            "Serial": "4109",
            "Status": "ACTIVE",
            "NotBefore": "2023-08-21T19:45:47+00:00",
            "NotAfter": "2033-08-21T20:45:47+00:00",
            "CertificateAuthorityConfiguration": {
                "KeyAlgorithm": "RSA_2048",
                "SigningAlgorithm": "SHA256WITHRSA",
                "Subject": {
                    "Country": "US",
                    "Organization": "Example Corp",
                    "OrganizationalUnit": "Sales",
                    "State": "WA",
                    "CommonName": "www.example.com",
                    "Locality": "Seattle"
                }
            },
            "RevocationConfiguration": {
                "CrlConfiguration": {
                    "Enabled": true,
                    "ExpirationInDays": 7,
                    "CustomCname": "crl.example.com",
                    "S3BucketName": "amzn-s3-demo-bucket",
                    "S3ObjectAcl": "BUCKET_OWNER_FULL_CONTROL"
                },
                "OcspConfiguration": {
                    "Enabled": false
                }
            },
            "KeyStorageSecurityStandard": "FIPS_140_2_LEVEL_3_OR_HIGHER",
            "UsageMode": "GENERAL_PURPOSE"
        }
    ]
}
```
For more information, see [List private CAs](https://docs.aws.amazon.com/privateca/latest/userguide/list-CAs.html) in the *AWS Private Certificate Authority User Guide*.
+  For API details, see [ListCertificateAuthorities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/list-certificate-authorities.html) in *AWS CLI Command Reference*.

### `list-tags`
<a name="acm-pca_ListTags_cli_2_topic"></a>

The following code example shows how to use `list-tags`.

**AWS CLI**
**To list the tags for your certificate authority**
The following `list-tags` example lists the tags associated with the private CA specified by the ARN.

```
aws acm-pca list-tags \
    --certificate-authority-arn {{arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/123455678-1234-1234-1234-123456789012}} \
    --max-results {{10}}
```
Output:

```
{
    "Tags": [
        {
            "Key": "Admin",
            "Value": "Alice"
        },
        {
            "Key": "Purpose",
            "Value": "Website"
        }
    ]
}
```
For more information, see [Add tags for your private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaCaTagging.html) in the *AWS Private Certificate Authority User Guide*.
+  For API details, see [ListTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/list-tags.html) in *AWS CLI Command Reference*.

### `revoke-certificate`
<a name="acm-pca_RevokeCertificate_cli_2_topic"></a>

The following code example shows how to use `revoke-certificate`.

**AWS CLI**
**To revoke a private certificate**
The following `revoke-certificate` example revokes a private certificate from the CA identified by the ARN.

```
aws acm-pca revoke-certificate \
    --certificate-authority-arn {{arn:aws:acm-pca:us-west-2:1234567890:certificate-authority/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --certificate-serial {{67:07:44:76:83:a9:b7:f4:05:56:27:ff:d5:5c:eb:cc}} \
    --revocation-reason {{"KEY_COMPROMISE"}}
```
This command produces no output.
For more information, see [Revoke a private certificate](https://docs.aws.amazon.com/privateca/latest/userguide/PcaRevokeCert.html) in the *AWS Private Certificate Authority User Guide*.
+  For API details, see [RevokeCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/revoke-certificate.html) in *AWS CLI Command Reference*.

### `tag-certificate-authority`
<a name="acm-pca_TagCertificateAuthority_cli_2_topic"></a>

The following code example shows how to use `tag-certificate-authority`.

**AWS CLI**
**To attach tags to a private certificate authority**
The following `tag-certificate-authority` example attaches one or more tags to your private CA.

```
aws acm-pca tag-certificate-authority \
    --certificate-authority-arn {{arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --tags {{Key=Admin,Value=Alice}}
```
This command produces no output.
For more information, see [Add tags for your private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaCaTagging.html) in the *AWS Private Certificate Authority User Guide*.
+  For API details, see [TagCertificateAuthority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/tag-certificate-authority.html) in *AWS CLI Command Reference*.

### `untag-certificate-authority`
<a name="acm-pca_UntagCertificateAuthority_cli_2_topic"></a>

The following code example shows how to use `untag-certificate-authority`.

**AWS CLI**
**To remove one or more tags from your private certificate authority**
The following `untag-certificate-authority` example removes tags from the private CA identified by the ARN.

```
aws acm-pca untag-certificate-authority \
    --certificate-authority-arn {{arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --tags {{Key=Purpose,Value=Website}}
```
This command produces no output.
For more information, see [Add tags for your private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaCaTagging.html) in the *AWS Private Certificate Authority User Guide*.
+  For API details, see [UntagCertificateAuthority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/untag-certificate-authority.html) in *AWS CLI Command Reference*.

### `update-certificate-authority`
<a name="acm-pca_UpdateCertificateAuthority_cli_2_topic"></a>

The following code example shows how to use `update-certificate-authority`.

**AWS CLI**
**To update the configuration of your private certificate authority**
The following `update-certificate-authority` example updates the status and configuration of the private CA identified by the ARN.

```
aws acm-pca update-certificate-authority \
    --certificate-authority-arn {{arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/12345678-1234-1234-1234-1232456789012}} \
    --revocation-configuration file://C:\revoke_config.txt \
    --status {{"DISABLED"}}
```
Contents of `C:\revoke_config.txt`:

```
{
    "CrlConfiguration": {
        "Enabled": true,
        "ExpirationInDays": 7,
        "CustomCname": "crl.example.com",
        "S3BucketName": "amzn-s3-demo-bucket"
    }
}
```
This command produces no output.
For more information, see [Update a private CA in AWS Private Certificate Authority](https://docs.aws.amazon.com/privateca/latest/userguide/PCAUpdateCA.html) in the *AWS Private Certificate Authority User Guide*.
+  For API details, see [UpdateCertificateAuthority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/update-certificate-authority.html) in *AWS CLI Command Reference*.
