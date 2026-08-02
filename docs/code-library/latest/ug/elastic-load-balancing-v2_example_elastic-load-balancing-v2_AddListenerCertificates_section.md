---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing-v2_example_elastic-load-balancing-v2_AddListenerCertificates_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `AddListenerCertificates` with a CLI
<a name="elastic-load-balancing-v2_example_elastic-load-balancing-v2_AddListenerCertificates_section"></a>

The following code examples show how to use `AddListenerCertificates`.

------
#### [ CLI ]

**AWS CLI**
**To add a certificate to a secure listener**
This example adds the specified certificate to the specified secure listener.
Command:

```
aws elbv2 add-listener-certificates --listener-arn {{arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2}} --certificates {{CertificateArn=arn:aws:acm:us-west-2:123456789012:certificate/5cc54884-f4a3-4072-80be-05b9ba72f705}}
```
Output:

```
{
  "Certificates": [
      {
          "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/5cc54884-f4a3-4072-80be-05b9ba72f705",
          "IsDefault": false
      }
  ]
}
```
+  For API details, see [AddListenerCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/add-listener-certificates.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example adds additional certificate to the specified Listener.**

```
Add-ELB2ListenerCertificate -ListenerArn 'arn:aws:elasticloadbalancing:us-east-1:123456789012:listener/app/test-alb/3651b4394dd9a24f/3873f123b98f7618' -Certificate @{CertificateArn = 'arn:aws:acm:us-east-1:123456789012:certificate/19478bd5-491d-47d4-b1d7-5217feba1d97'}
```
**Output:**

```
CertificateArn                                                                      IsDefault
--------------                                                                      ---------
arn:aws:acm:us-east-1:123456789012:certificate/19478bd5-491d-47d4-b1d7-5217feba1d97 False
```
+  For API details, see [AddListenerCertificates](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example adds additional certificate to the specified Listener.**

```
Add-ELB2ListenerCertificate -ListenerArn 'arn:aws:elasticloadbalancing:us-east-1:123456789012:listener/app/test-alb/3651b4394dd9a24f/3873f123b98f7618' -Certificate @{CertificateArn = 'arn:aws:acm:us-east-1:123456789012:certificate/19478bd5-491d-47d4-b1d7-5217feba1d97'}
```
**Output:**

```
CertificateArn                                                                      IsDefault
--------------                                                                      ---------
arn:aws:acm:us-east-1:123456789012:certificate/19478bd5-491d-47d4-b1d7-5217feba1d97 False
```
+  For API details, see [AddListenerCertificates](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
