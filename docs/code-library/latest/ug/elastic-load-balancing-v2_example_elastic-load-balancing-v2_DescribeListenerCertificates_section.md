---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing-v2_example_elastic-load-balancing-v2_DescribeListenerCertificates_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeListenerCertificates` with a CLI
<a name="elastic-load-balancing-v2_example_elastic-load-balancing-v2_DescribeListenerCertificates_section"></a>

The following code examples show how to use `DescribeListenerCertificates`.

------
#### [ CLI ]

**AWS CLI**
**To describe the certificates for a secure listener**
The following `describe-listener-certificates` example describes the certificates for the specified secure listener.

```
aws elbv2 describe-listener-certificates \
    --listener-arn {{arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2}}
```
Output:

```
{
    "Certificates": [
        {
            "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "IsDefault": false
        },
        {
            "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "IsDefault": false
        },
        {
            "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "IsDefault": true
        }
    ]
}
```
For more information, see [SSL certificates for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/https-listener-certificates.html) in the *Application Load Balancers Guide*.
+  For API details, see [DescribeListenerCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-listener-certificates.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This examples describes the certificate for the specified listener.**

```
Get-ELB2ListenerCertificate -ListenerArn 'arn:aws:elasticloadbalancing:us-east-1:123456789012:listener/app/test-alb/3651b4394dd9a24f/66e10e3aaf5b6d9b'
```
**Output:**

```
CertificateArn                                                                      IsDefault
--------------                                                                      ---------
arn:aws:acm:us-east-1:123456789012:certificate/5fc7c092-68bf-4862-969c-22fd48b6e17c True
```
+  For API details, see [DescribeListenerCertificates](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This examples describes the certificate for the specified listener.**

```
Get-ELB2ListenerCertificate -ListenerArn 'arn:aws:elasticloadbalancing:us-east-1:123456789012:listener/app/test-alb/3651b4394dd9a24f/66e10e3aaf5b6d9b'
```
**Output:**

```
CertificateArn                                                                      IsDefault
--------------                                                                      ---------
arn:aws:acm:us-east-1:123456789012:certificate/5fc7c092-68bf-4862-969c-22fd48b6e17c True
```
+  For API details, see [DescribeListenerCertificates](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
