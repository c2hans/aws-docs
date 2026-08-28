---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_SetLoadBalancerListenerSslCertificate_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `SetLoadBalancerListenerSslCertificate` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_SetLoadBalancerListenerSslCertificate_section"></a>

The following code examples show how to use `SetLoadBalancerListenerSslCertificate`.

------
#### [ CLI ]

**AWS CLI**
**To update the SSL certificate for an HTTPS load balancer**
This example replaces the existing SSL certificate for the specified HTTPS load balancer.
Command:

```
aws elb set-load-balancer-listener-ssl-certificate --load-balancer-name {{my-load-balancer}} --load-balancer-port {{443}} --ssl-certificate-id {{arn:aws:iam::123456789012:server-certificate/new-server-cert}}
```
+  For API details, see [SetLoadBalancerListenerSslCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/set-load-balancer-listener-ssl-certificate.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example replaces the certificate that terminates the SSL connections for the specified listener.**

```
Set-ELBLoadBalancerListenerSSLCertificate -LoadBalancerName my-load-balancer `
>> -LoadBalancerPort 443 `
>> -SSLCertificateId "arn:aws:iam::123456789012:server-certificate/new-server-cert"
```
+  For API details, see [SetLoadBalancerListenerSslCertificate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example replaces the certificate that terminates the SSL connections for the specified listener.**

```
Set-ELBLoadBalancerListenerSSLCertificate -LoadBalancerName my-load-balancer `
>> -LoadBalancerPort 443 `
>> -SSLCertificateId "arn:aws:iam::123456789012:server-certificate/new-server-cert"
```
+  For API details, see [SetLoadBalancerListenerSslCertificate](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
