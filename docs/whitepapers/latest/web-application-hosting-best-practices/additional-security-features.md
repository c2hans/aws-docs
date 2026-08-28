---
source_url: https://docs.aws.amazon.com/whitepapers/latest/web-application-hosting-best-practices/additional-security-features.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Additional security features
<a name="additional-security-features"></a>

The number and sophistication of Distributed Denial of Service (DDoS) attacks are rising. Traditionally, these attacks are difficult to fend off. They often end up being costly in both mitigation time and power spent, as well as the opportunity cost from lost visits to your website during the attack. There are a number of AWS factors and services that can help you defend against such attacks. One of them is the scale of the AWS network. The AWS infrastructure is quite large, and enables you to leverage our scale to optimize your defense. Several services, including [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/), [Amazon CloudFront](https://aws.amazon.com/cloudfront/), and [Amazon Route 53](https://aws.amazon.com/route53/), are effective at scaling your web application in response to a large increase in traffic.

The infrastructure protection services in particular help with your defense strategy:
+ [**AWS Shield**](https://aws.amazon.com/shield/) is a managed DDoS protection service that helps safeguard against various forms of DDoS attack vectors. The standard offering of AWS Shield is free and automatically active throughout your account. This standard offering helps to defend against the most common network and transportation layer attacks. In addition to this level, the advanced offering grants higher levels of protection against your web application by providing you with near real-time visibility into an ongoing attack, as well as integrating at higher levels with the services mentioned earlier. Additionally, you get access to the AWS DDoS Response Team (DRT) to help mitigate large-scale and sophisticated attacks against your resources.
+ [** AWS WAF**](https://aws.amazon.com/waf/) (Web Application Firewall) is designed to protect your web applications from attacks that can compromise availability or security, or otherwise consume excessive resources. AWS WAF works in line with CloudFront or Application Load Balancer, along with your custom rules, to defend against attacks such as cross-site scripting, SQL injection, and DDoS. As with most AWS services, AWS WAF comes with a fully featured API that can help automate the creation and editing of rules for your AWS WAF instance as your security needs change.
+ [**AWS Firewall Manager**](https://aws.amazon.com/firewall-manager/) is a security management service which enables you to centrally configure and manage firewall rules across your accounts and applications in [AWS Organizations](https://aws.amazon.com/organizations/). As new applications are created, AWS Firewall Manager makes it easy to bring new applications and resources into compliance by enforcing a common set of security rules.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
