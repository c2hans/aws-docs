---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/iam_example_iam_UpdateSigningCertificate_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `UpdateSigningCertificate` with a CLI
<a name="iam_example_iam_UpdateSigningCertificate_section"></a>

The following code examples show how to use `UpdateSigningCertificate`.

------
#### [ CLI ]

**AWS CLI**
**To activate or deactivate a signing certificate for an IAM user**
The following `update-signing-certificate` command deactivates the specified signing certificate for the IAM user named `Bob`.

```
aws iam update-signing-certificate \
    --certificate-id {{TA7SMP42TDN5Z26OBPJE7EXAMPLE}} \
    --status {{Inactive}} \
    --user-name {{Bob}}
```
To get the ID for a signing certificate, use the `list-signing-certificates` command.
For more information, see [Manage signing certificates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-up-ami-tools.html#ami-tools-managing-certs) in the *Amazon EC2 User Guide*.
+  For API details, see [UpdateSigningCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-signing-certificate.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example updates the certificate that is associated with the IAM user named `Bob` and whose certificate ID si `Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU` to mark it as inactive.**

```
Update-IAMSigningCertificate -CertificateId Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU -UserName Bob -Status Inactive
```
+  For API details, see [UpdateSigningCertificate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example updates the certificate that is associated with the IAM user named `Bob` and whose certificate ID si `Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU` to mark it as inactive.**

```
Update-IAMSigningCertificate -CertificateId Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU -UserName Bob -Status Inactive
```
+  For API details, see [UpdateSigningCertificate](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
