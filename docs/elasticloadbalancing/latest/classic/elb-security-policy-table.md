---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html
---

# Predefined SSL security policies for Classic Load Balancers
<a name="elb-security-policy-table"></a>

You can choose one of the predefined security policies for your HTTPS/SSL listeners. You can use one of the `ELBSecurityPolicy-TLS` policies to meet compliance and security standards that require disabling certain TLS protocol versions. Alternatively, you can create a custom security policy. For more information, see [Update the SSL negotiation configuration](ssl-config-update.md).

The RSA- and DSA-based ciphers are specific to the signing algorithm used to create SSL certificate. Make sure to create an SSL certificate using the signing algorithm that is based on the ciphers that are enabled for your security policy.

If you select a policy that is enabled for Server Order Preference, the load balancer uses the ciphers in the order that they are specified here to negotiate connections between the client and load balancer. Otherwise, the load balancer uses the ciphers in the order that they are presented by the client.

The following sections describe the most recent predefined security policies for Classic Load Balancers, including their enabled SSL protocols and SSL ciphers. You can also describe the predefined policies using the [describe-load-balancer-policies](https://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancer-policies.html) command.

**Tip**
This information applies only to Classic Load Balancers. For information that applies to other load balancers, see [Security policies for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/describe-ssl-policies.html) and [Security policies for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/describe-ssl-policies.html).

**Topics**
+ [Protocols by policy](#tls-protocols)
+ [Ciphers by policy](#tls-policy-ciphers)
+ [Policies by cipher](#tls-cipher-policies)

## Protocols by policy
<a name="tls-protocols"></a>

The following table describes the TLS protocols that each security policy supports.

| Security policies | TLS 1.2 | TLS 1.1 | TLS 1.0 |
| --- | --- | --- | --- |
| ELBSecurityPolicy-TLS-1-2-2017-01 | ![](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/images/negative_icon.png) No |
| ELBSecurityPolicy-TLS-1-1-2017-01 | ![](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/images/negative_icon.png) No |
| ELBSecurityPolicy-2016-08 | ![](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/images/success_icon.png) Yes |
| ELBSecurityPolicy-2015-05 | ![](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/images/success_icon.png) Yes |
| ELBSecurityPolicy-2015-03 | ![](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/images/success_icon.png) Yes |
| ELBSecurityPolicy-2015-02 | ![](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/images/success_icon.png) Yes |

## Ciphers by policy
<a name="tls-policy-ciphers"></a>

The following table describes the ciphers that each security policy supports.

| Security policy | Ciphers |
| --- | --- |
| ELBSecurityPolicy-TLS-1-2-2017-01 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  |
| ELBSecurityPolicy-TLS-1-1-2017-01 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  |
| ELBSecurityPolicy-2016-08 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  |
| ELBSecurityPolicy-2015-05 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  |
| ELBSecurityPolicy-2015-03 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  |
| ELBSecurityPolicy-2015-02 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  |

## Policies by cipher
<a name="tls-cipher-policies"></a>

The following table describes the security policies that support each cipher.

| Cipher name | Security policies | Cipher suite |
| --- | --- | --- |
| **OpenSSL** – ECDHE-ECDSA-AES128-GCM-SHA256<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | c02b |
| **OpenSSL** – ECDHE-RSA-AES128-GCM-SHA256<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | c02f |
| **OpenSSL** – ECDHE-ECDSA-AES128-SHA256<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA256 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | c023 |
| **OpenSSL** – ECDHE-RSA-AES128-SHA256<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | c027 |
| **OpenSSL** – ECDHE-ECDSA-AES128-SHA<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | c009 |
| **OpenSSL** – ECDHE-RSA-AES128-SHA<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | c013 |
| **OpenSSL** – ECDHE-ECDSA-AES256-GCM-SHA384<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | c02c |
| **OpenSSL** – ECDHE-RSA-AES256-GCM-SHA384<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | c030 |
| **OpenSSL** – ECDHE-ECDSA-AES256-SHA384<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | c024 |
| **OpenSSL** – ECDHE-RSA-AES256-SHA384<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | c028 |
| **OpenSSL** – ECDHE-ECDSA-AES256-SHA<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | c014 |
| **OpenSSL** – ECDHE-RSA-AES256-SHA<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | c00a |
| **OpenSSL** – AES128-GCM-SHA256<br />**IANA** – TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | 9c |
| **OpenSSL** – AES128-SHA256<br />**IANA** – TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA256 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | 3c |
| **OpenSSL** – AES128-SHA<br />**IANA** – TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | 2f |
| **OpenSSL** – AES256-GCM-SHA384<br />**IANA** – TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | 9d |
| **OpenSSL** – AES256-SHA256<br />**IANA** – TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA256 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | 3d |
| **OpenSSL** – AES256-SHA<br />**IANA** – TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | 35 |
| **OpenSSL** – DHE-RSA-AES128-SHA<br />**IANA** – TLS\_DHE\_RSA\_WITH\_AES\_128\_CBC\_SHA |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | 33 |
| **OpenSSL** – DHE-DSS-AES128-SHA<br />**IANA** – TLS\_DHE\_DSS\_WITH\_AES\_128\_CBC\_SHA |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | 32 |
| **OpenSSL** – DES-CBC3-SHA<br />**IANA** – TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)  | 0a |
