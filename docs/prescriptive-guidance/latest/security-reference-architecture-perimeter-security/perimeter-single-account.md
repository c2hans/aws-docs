---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-perimeter-security/perimeter-single-account.html
---

# Deploying perimeter services in a single Network account
<a name="perimeter-single-account"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

The following diagram builds on the baseline AWS SRA to illustrate the architecture where perimeter services are deployed into the Network account**.**

![Deploying perimeter services into Network account.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-perimeter-security/images/guide-img/36fc75a2-a16a-4cf6-bea6-724dfeddb825/images/2dfbda14-546d-4e33-acfc-90d010886640.png)

Deploying the perimeter services into a single Network account has several benefits:
+ This pattern supports use cases such as highly regulated industries, where you want to restrict the administration of perimeter services across your organization to a single specialized team.
+ It simplifies the configuration required to limit the creation, modification, and deletion of networking components.
+ It simplifies detection, because inspection happens in a single place, which leads to fewer log aggregation points.
+ You can create custom best practice resources such as CloudFront policies and edge functions, and share these across distributions in the same account.
+ It simplifies the management of business-critical resources that are sensitive to configuration errors, such as content delivery network (CDN) cache settings or DNS records, by reducing the locations where that change is implemented.

The following sections dive into each service and discuss architectural considerations.

## Amazon CloudFront
<a name="perimeter-single-cloudfront"></a>

[Amazon CloudFront](https://aws.amazon.com/cloudfront/) is a content delivery network (CDN) service that's built for high performance, security, and developer convenience. For public, internet-facing HTTP endpoints, we recommend that you use CloudFront to distribute your internet-facing content. CloudFront is a reverse proxy that serves as a single point of entry for your application globally. It can also be combined with AWS WAF and edge functions such as Lambda@Edge and CloudFront functions to help create secure and customizable solutions for content delivery.

In this deployment architecture, all CloudFront configurations, including edge functions, are deployed into the Network account** **and managed by a centralized networking team. Only authorized employees on the networking team should have access to this account. Application teams that want to make changes to their CloudFront configuration or web access control list (web ACL) for AWS WAF should request those changes from the networking team. We recommend that you establish a workflow such as a ticketing system for application teams to request configuration changes.

In this pattern, both dynamic and static origins are located in the individual Application accounts, so accessing these origins requires cross-account permissions and cross-account roles. Logs from CloudFront distributions are configured to be sent to the Log Archive account.

## AWS WAF
<a name="perimeter-single-waf"></a>

[AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html) is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to your protected web application resources. This service can help protect your resources against common web exploits and volumetric threats, as well as against more sophisticated threats such as account creation fraud, unauthorized access to user accounts, and bots that attempt to evade detection. AWS WAF can help protect the following resource types: CloudFront distributions, Amazon API Gateway REST APIs, Application Load Balancers, AWS AppSync GraphQL APIs, Amazon Cognito user pools, AWS App Runner services, and AWS Verified Access instances.

In this deployment architecture, AWS WAF is attached to the CloudFront distributions that are configured in the Network account. When you configure AWS WAF with CloudFront, the perimeter footprint is extended to CloudFront edge locations instead of the application VPC. This pushes the filtering of malicious traffic closer to the source of that traffic and helps restrict malicious traffic from entering your core network.

Although web ACLs are deployed in the Network account, we recommend that you use AWS Firewall Manager to centrally manage web ACLs and make sure that all resources are compliant. Set the Security Tooling account as the administrator account for Firewall Manager. Deploy Firewall Manager policies with auto-remediation to enforce that all (or selected) CloudFront distributions in your account have a web ACL attached.

You can send full AWS WAF logs to an Amazon Simple Storage Service (Amazon S3) bucket in the Log Archive account by configuring cross-account access to the S3 bucket. For more information, see the [AWS re:Post article](https://repost.aws/knowledge-center/waf-send-logs-centralized-account) on this topic.

## AWS Shield and Amazon Route 53 health checks
<a name="perimeter-single-shield-route53"></a>

[AWS Shield Standard](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-standard-summary.html) and [AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html) provide protections against distributed denial of service (DDoS) threats for AWS resources at the network and transport layers (layers 3 and 4) and the application layer (layer 7). Shield Standard is automatically included at no extra cost beyond what you already pay for AWS WAF and your other AWS services.  Shield Advanced provides expanded DDoS event protection for your Amazon Elastic Compute Cloud (Amazon EC2) instances, Elastic Load Balancing load balancers, CloudFront distributions, and Route 53 hosted zones. If you own high-visibility websites or your applications are prone to frequent DDoS events, consider the additional features that Shield Advanced provides.

This section focuses on Shield Advanced configurations, because Shield Standard isn't user configurable.

To configure Shield Advanced to protect your CloudFront distributions, subscribe the Network account to Shield Advanced. In the account, add [Shield Response Team (SRT) support](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-access.html) and provide the necessary permissions for the SRT team to access your web ACLs during a DDoS event. You can contact the SRT at any time to create and manage custom mitigations for your application during an active DDoS event. Configuring access in advance give the SRT the flexibility to debug and revise the web ACLs without having to manage permissions during an event.

Use Firewall Manager with auto-remediation to add your CloudFront distributions as protected resources. If you have other internet-facing resources such as Application Load Balancers, you might consider adding them as Shield Advanced protected resources. However, if you have multiple Shield Advanced protected resources in the data flow (for example, your Application Load Balancer is the origin to CloudFront), we recommend that you use only the entry point as a protected resource to reduce duplicate data transfer out (DTO) fees for Shield Advanced.

Enable the [proactive engagement feature](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-proactive-engagement.html) to allow the SRT to proactively monitor your protected resources and contact you as required. To configure the proactive engagement feature effectively, create Route 53 health checks for your application and associate them with CloudFront distributions. Shield Advanced uses the health checks as an additional data point when it evaluates an event. Health checks should be properly defined to reduce false positives with detection. For more information about identifying the correct metrics for health checks, see [Best practices for using health checks with Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/health-checks-best-practices.html) in the AWS documentation. If you detect a DDoS attempt, you can contact the SRT and choose the highest severity available for your support plan.

## AWS Certificate Manager and Amazon Route 53
<a name="perimeter-single-acm-route53"></a>

[AWS Certificate Manager (ACM)](https://aws.amazon.com/certificate-manager/) helps you provision, manage, and renew public and private SSL/TLS X.509 certificates. When you use ACM to manage certificates, certificate private keys are securely protected and stored by using strong encryption and key management best practices.

ACM is deployed in the Network account in order to generate a public TLS certificate for CloudFront distributions. TLS certificates are needed to establish a HTTPS connection between viewers and CloudFront. For more information, see the [CloudFront documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html). ACM provides DNS or email validation to validate domain ownership. We recommend that you use DNS validation instead of email validation, because by using Route 53 to manage your public DNS records, you can update your records through ACM directly. ACM automatically renews DNS-validated certificates for as long as a certificate remains in use and the DNS record is in place.

## CloudFront access logs and AWS WAF logs
<a name="perimeter-single-cloudfront-waf"></a>

By default, CloudFront access logs are stored in the Network account** **and AWS WAF logs are aggregated in the Security Tooling account by** **using the Firewall Manager logging option. We recommend that you replicate these logs in the Log Archive account so that centralized security teams can access them for monitoring purposes.

**Design considerations:**
+ In this architecture, the large number of dependencies on a single networking team can affect your ability to make changes quickly.
+ Monitor the service quotas for each account. Service quotas, also referred to as *limits*, are the maximum number of service resources or operations for your AWS account. For more information, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) in the AWS documentation.
+ Providing specific metrics to workload teams might introduce complexities.
+ Application teams have restricted access to configurations, which might result in an overhead of waiting for the networking teams to implement changes on their behalf.
+ Teams that share resources in a single account might compete for the same resources and budgets, which might lead to resource allocation challenges. We recommend that you put mechanisms in place to charge back from the application teams that use the perimeter services deployed in the Networking account.
