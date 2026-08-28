---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/additional-resources.html
---

# Additional resources
<a name="additional-resources"></a>

## Upload SSL Certificate to IAM
<a name="upload-ssl-certificate-to-iam"></a>

 Upload the SSL certificate by running the AWS CLI command `upload-server-certificate` similar to the following:

```
aws iam upload-server-certificate --path /cloudfront/ \
--server-certificate-name YourCertificate \
--certificate-body file://Certificate.pem \
--certificate-chain file://CertificateChain.pem \
--private-key file://PrivateKey.pem
```

 Replace the file names and Your Certificate with the names for your uploaded files and certificate. You must specify the file:// prefix in the certificate-body, certificate-chain and private-key parameters in the API request. Otherwise, the request fails with a `MalformedCertificate: Unknown` error message.

**Note**
 You must specify a path using the --path option. The path must begin with /cloudfront and must include a trailing slash (for example, /cloudfront/test/).

 After the certificate is uploaded, the AWS command `upload-server-certificate` returns metadata for the uploaded certificate, including the certificate's Amazon Resource Name (ARN), friendly name, identifier (ID), and expiration date.

 To view the uploaded certificate, run the AWS CLI command `list-server-certificates`:

```
aws iam list-server-certificates
```

 For more information, see [uploading a server certificate](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html#upload-server-certificate) to IAM.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
