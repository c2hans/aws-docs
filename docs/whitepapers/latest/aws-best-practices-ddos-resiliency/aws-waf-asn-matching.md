---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-waf-asn-matching.html
---

# AWS WAF – ASN matching feature
<a name="aws-waf-asn-matching"></a>

 By monitoring and restricting traffic from specific ASNs, you can mitigate risks associated with malicious actors, comply with regulatory requirements, and optimize the performance and availability of your web applications. [ASN-based matching](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-asn-match.html) simplifies WAF operations by reducing the need to use customer-maintained [IP sets](https://docs.aws.amazon.com/waf/latest/developerguide/waf-ip-set-managing.html) for similar purposes:
+  You can add your trusted partners' ASNs to an ALLOW rule, for example your additional CDN vendors' ASNs in case of multi-CDN setup behind CloudFront or working on top of your ALBs
+  You can improve control by introducing Captcha, Challenge, or Block of ASNs listed in the Spamhaus ASN-DROP list, which contains ASNs leased by professional SPAM or cyber-criminals
+  Limit connections from countries where you don't actively operate your business by using [Geographic match rule statement](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-geo-match.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
