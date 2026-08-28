---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_4_acm_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# ACM examples using Tools for PowerShell V4
<a name="powershell_4_acm_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with ACM.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Get-ACMCertificate`
<a name="acm_GetCertificate_powershell_4_topic"></a>

The following code example shows how to use `Get-ACMCertificate`.

**Tools for PowerShell V4**
**Example 1: This example shows how to return a certificate and its chain using the ARN of the certificate.**

```
Get-ACMCertificate -CertificateArn "arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012"
```
+  For API details, see [GetCertificate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-ACMCertificateDetail`
<a name="acm_DescribeCertificate_powershell_4_topic"></a>

The following code example shows how to use `Get-ACMCertificateDetail`.

**Tools for PowerShell V4**
**Example 1: Returns details of the specified certificate.**

```
Get-ACMCertificateDetail -CertificateArn "arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012"
```
**Output:**

```
CertificateArn          : arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012
CreatedAt               : 1/21/2016 5:55:59 PM
DomainName              : www.example.com
DomainValidationOptions : {www.example.com}
InUseBy                 : {}
IssuedAt                : 1/1/0001 12:00:00 AM
Issuer                  :
KeyAlgorithm            : RSA-2048
NotAfter                : 1/1/0001 12:00:00 AM
NotBefore               : 1/1/0001 12:00:00 AM
RevocationReason        :
RevokedAt               : 1/1/0001 12:00:00 AM
Serial                  :
SignatureAlgorithm      : SHA256WITHRSA
Status                  : PENDING_VALIDATION
Subject                 : CN=www.example.com
SubjectAlternativeNames : {www.example.net}
```
+  For API details, see [DescribeCertificate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-ACMCertificateList`
<a name="acm_ListCertificates_powershell_4_topic"></a>

The following code example shows how to use `Get-ACMCertificateList`.

**Tools for PowerShell V4**
**Example 1: Retrieves a list of all your certificate ARNs and the domain name for each. The cmdlet will automatically paginate to retrieve all the ARNs. To manually control pagination, use the -MaxItem parameter to control how many certificate ARNs are returned for each service call and the -NextToken parameter to indicate the starting point for each call.**

```
Get-ACMCertificateList
```
**Output:**

```
CertificateArn                                                                      DomainName
--------------                                                                      ----------
arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012 www.example.com
```
**Example 2: Retrieves a list of all your certificate ARNs where the certificate status matches on the supplied states.**

```
Get-ACMCertificateList -CertificateStatus "VALIDATION_TIMED_OUT","FAILED"
```
**Example 3: This example returns a list of all certificates in the us-east-1 region that have a key type of RSA\_2048, and an extended key usage, or purpose, of CODE\_SIGNING. You can find the values for these filtering parameters in the ListCertificates Filters API reference topic: https://docs.aws.amazon.com/acm/latest/APIReference/API\_Filters.html.**

```
Get-ACMCertificateList -Region us-east-1 -Includes_KeyType RSA_2048 -Includes_ExtendedKeyUsage CODE_SIGNING
```
**Output:**

```
CertificateArn                                                                      DomainName
--------------                                                                      ----------
arn:aws:acm:us-east-1:8xxxxxxxxxxx:certificate/xxxxxxxx-d7c0-48c1-af8d-2133d8f30zzz *.route53docs.com
arn:aws:acm:us-east-1:8xxxxxxxxxxx:certificate/xxxxxxxx-98a5-443d-a734-800430c80zzz nerdzizm.net
arn:aws:acm:us-east-1:8xxxxxxxxxxx:certificate/xxxxxxxx-2be6-4376-8fa7-bad559525zzz
arn:aws:acm:us-east-1:8xxxxxxxxxxx:certificate/xxxxxxxx-e7ca-44c5-803e-24d9f2f36zzz
arn:aws:acm:us-east-1:8xxxxxxxxxxx:certificate/xxxxxxxx-1241-4b71-80b1-090305a62zzz
arn:aws:acm:us-east-1:8xxxxxxxxxxx:certificate/xxxxxxxx-8709-4568-8c64-f94617c99zzz
arn:aws:acm:us-east-1:8xxxxxxxxxxx:certificate/xxxxxxxx-a8fa-4a61-98cf-e08ccc0eezzz
arn:aws:acm:us-east-1:8xxxxxxxxxxx:certificate/xxxxxxxx-fa47-40fe-a714-2d277d3eezzz *.route53docs.com
```
+  For API details, see [ListCertificates](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-ACMCertificate`
<a name="acm_RequestCertificate_powershell_4_topic"></a>

The following code example shows how to use `New-ACMCertificate`.

**Tools for PowerShell V4**
**Example 1: Creates a new certificate. The service returns the ARN of the new certificate.**

```
New-ACMCertificate -DomainName "www.example.com"
```
**Output:**

```
arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012
```
**Example 2: Creates a new certificate. The service returns the ARN of the new certificate.**

```
New-ACMCertificate -DomainName "www.example.com" -SubjectAlternativeName "example.com","www.example.net"
```
**Output:**

```
arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012
```
+  For API details, see [RequestCertificate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-ACMCertificate`
<a name="acm_DeleteCertificate_powershell_4_topic"></a>

The following code example shows how to use `Remove-ACMCertificate`.

**Tools for PowerShell V4**
**Example 1: Deletes the certificate identified by the supplied ARN and the associated private key. The cmdlet will prompt for confirmation before proceeding; add the -Force switch to suppress confirmation.**

```
Remove-ACMCertificate -CertificateArn "arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012"
```
+  For API details, see [DeleteCertificate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Send-ACMValidationEmail`
<a name="acm_ResendValidationEmail_powershell_4_topic"></a>

The following code example shows how to use `Send-ACMValidationEmail`.

**Tools for PowerShell V4**
**Example 1: Requests that the email to validate domain ownership for 'www.example.com' be sent. If your shell's $ConfirmPreference is set to 'Medium' or lower, the cmdlet will prompt for confirmation before proceeeding. Add the -Force switch to suppress confirmation prompts.**

```
$params = @{
    CertificateArn="arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012"
    Domain="www.example.com"
    ValidationDomain="example.com"
}
Send-ACMValidationEmail @params
```
+  For API details, see [ResendValidationEmail](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
