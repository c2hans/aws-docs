---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/engage-srt-shield-advanced-subscribers-only.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Engage SRT (Shield Advanced subscribers only)
<a name="engage-srt-shield-advanced-subscribers-only"></a>

 In addition, when subscribed to Shield Advanced, you can engage the AWS SRT to help you create rules to mitigate an attack that is hurting your application’s availability. You can grant AWS SRT limited access to your account’s AWS Shield Advanced and AWS WAF APIs. AWS SRT accesses these APIs to place mitigations on your account only with your explicit authorization. For more information, refer to the [Support](support.md) section of this document.

 You can use AWS Firewall Manager to centrally configure and manage security rules, such as AWS Shield Advanced protections and AWS WAF rules, across your organization. Your AWS Organizations management account can designate an administrator account, which is authorized to create Firewall Manager policies. These policies allow you to define criteria, such as resource type and tags, which determine where rules are applied. This is useful when you have multiple accounts and want to standardize your protection.

 For more information about:
+  AWS Managed Rules for AWS WAF, refer to [AWS Managed Rules for AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups.html).
+  Using geographic restriction to limit access to your CloudFront distribution, refer to [Restricting the geographic distribution of your content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/georestrictions.html).
+  Using AWS WAF, refer to:
  +  [Getting started with AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html)
  +  [Logging web ACL traffic information](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html)
  +  [Viewing a sample of web requests](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing.html#web-acl-testing-view-sample)
+  Configuring rate-based rules, refer to [Protect Web Sites and Services Using Rate-Based Rules for AWS WAF](https://aws.amazon.com/blogs/aws/protect-web-sites-services-using-rate-based-rules-for-aws-waf/).
+  How to manage the deployment of rules across your AWS resources with Firewall Manager, see:
  +  [Getting started with Firewall Manager AWS WAF policies](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms.html).
  +  [Getting started with Firewall Manager Shield Advanced policies](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms-shield.html).
