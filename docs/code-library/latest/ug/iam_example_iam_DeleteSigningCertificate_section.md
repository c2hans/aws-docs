---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/iam_example_iam_DeleteSigningCertificate_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteSigningCertificate` with a CLI
<a name="iam_example_iam_DeleteSigningCertificate_section"></a>

The following code examples show how to use `DeleteSigningCertificate`.

------
#### [ CLI ]

**AWS CLI**
**To delete a signing certificate for an IAM user**
The following `delete-signing-certificate` command deletes the specified signing certificate for the IAM user named `Bob`.

```
aws iam delete-signing-certificate \
    --user-name {{Bob}} \
    --certificate-id {{TA7SMP42TDN5Z26OBPJE7EXAMPLE}}
```
This command produces no output.
To get the ID for a signing certificate, use the `list-signing-certificates` command.
For more information, see [Manage signing certificates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-up-ami-tools.html#ami-tools-managing-certs) in the *Amazon EC2 User Guide*.
+  For API details, see [DeleteSigningCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-signing-certificate.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes the signing certificate with the ID `Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU` from the IAM user named `Bob`.**

```
Remove-IAMSigningCertificate -UserName Bob -CertificateId Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU
```
+  For API details, see [DeleteSigningCertificate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes the signing certificate with the ID `Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU` from the IAM user named `Bob`.**

```
Remove-IAMSigningCertificate -UserName Bob -CertificateId Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU
```
+  For API details, see [DeleteSigningCertificate](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
