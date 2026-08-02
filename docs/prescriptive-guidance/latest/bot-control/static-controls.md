---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/bot-control/static-controls.html
---

# Static controls for managing bots
<a name="static-controls"></a>

To take an action,* static controls* evaluate static information from the HTTP(S) request, such as its IP address or its headers. These controls can be useful for low-sophistication bad bot activity or for expected beneficial bot traffic that needs to be verified and managed. Static control techniques include: allow listing, IP-based controls, and intrinsic checks.

## Allow listing
<a name="allow-listing"></a>

Allow listing is a control that allows identified friendly traffic through existing bot mitigation controls. There are a variety of ways of accomplishing this. The simplest is to use a rule that [matches a set of IP addresses](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-forwarded-ip-address.html) or a similar match condition. When a request matches a rule that is set to an `Allow` action, it is not evaluated by subsequent rules. In some cases, you need to prevent only certain rules from being acted on; in other words, you need to allow list for one rule but not all rules. This is a common scenario for handling false positives for rules. Allow listing is considered a broad-scope rule. To reduce the potential for false negatives, we recommend that you pair it with another option that is more granular, such as a path or header match.

## IP-based controls
<a name="ip-based-controls"></a>

### Single IP address blocks
<a name="single-ip-address-blocks.6da1ce09-f207-5b86-9d9f-cd682d1d0e23"></a>

A commonly used tool to mitigate the impact of bots is to limit requests from a single requestor. The simplest example is to block the source IP address of the traffic if its requests are malicious or high in volume. This uses AWS WAF [IP set match rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-ipset-match.html) to implement IP-based blocks. These rules match on IP addresses and apply an action of `Block`, `Challenge`, or `CAPTCHA`. You can determine when too many requests are coming in from an IP address by looking at Content Delivery Network (CDN), a web application firewall (WAF), or application and service logs. However, in most cases, this control is impractical without automation.

Automating IP address block lists in AWS WAF is commonly done with rate-based rules. For more information, see *Rate-based rules* in this guide. You can also implement the [Security Automations for AWS WAF](https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/welcome.html) solution. This solution automatically updates a list of IP addresses to block, and an AWS WAF rule denies requests that match those IP addresses.

One way to recognize a bot attack is if a multitude of requests from the same IP address focus on a small number of web pages. This indicates that the bot is price scrapping or repeatedly attempting logins that fail at a high percentage. You can create automations that immediately recognize this pattern. The automations block the IP address, which reduces the efficacy of the attack by quickly identifying and mitigating it. Blocking specific IP addresses is less effective when an attacker has a large collection of IP addresses to launch attacks from or when the attacking behavior is difficult to recognize and separate from normal traffic.

### IP address reputation
<a name="ip-address-reputation.bb86613d-be8e-5b33-9510-77b6ba6e96cb"></a>

An *IP reputation service* provides intelligence that helps evaluate the trustworthiness of an IP address. This intelligence is commonly derived by aggregating IP-related information from past activity from that IP address. Prior activity helps indicate how likely an IP address is to generate malicious requests. The data is added to managed lists that track the IP address behavior.

Anonymous IP addresses are a specialized case of IP address reputation. The source IP address originates from known sources of easily acquired IP addresses, such as cloud-based virtual machines, or from proxies, such as known VPN providers or Tor nodes. The AWS WAF [Amazon IP reputation list](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-ip-rep.html#aws-managed-rule-groups-ip-rep-amazon) and [Anonymous IP list](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-ip-rep.html#aws-managed-rule-groups-ip-rep-anonymous) managed rule groups use Amazon internal threat intelligence to help identify these IP addresses.

The intelligence provided by these managed lists can help you act on activity identified from these sources. Based on this intelligence, you can create rules that directly block traffic or rules that limit the number of requests (such as rate-based rules). You can also use this intelligence to evaluate the source of the traffic by using the rules in `COUNT` mode. This examines the match criteria and applies labels that you can use to create custom rules.

### Rate-based rules
<a name="rate-based-rules.105676d8-a338-5ffa-bbc5-01bfa7e3c4d2"></a>

Rate-based rules can be a valuable tool for certain scenarios. For example, rate-based rules are effective when bot traffic reaches high volumes compared to users in sensitive uniform resource identifiers (URIs) or when the traffic volume begins to affect normal operations. Rate limiting can keep requests at manageable levels and limit and control access. AWS WAF can implement rate-limiting rule in a [web access control list (web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html) by using a [rate-based rule statement](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html). A recommended approach when using rate-based rules is to include a blanket rule that covers the whole site, URI-specific rules, and IP reputation rate-based rules. IP reputation rate-based rules combines the intelligence of IP address reputation with rate-limiting functionality.

For the whole site, a blanket IP reputation rate-based rule creates a ceiling that prevents unsophisticated bots from flooding a site from a small number of IPs. Rate limiting is especially recommended for protecting URIs that have high cost or impact, such as login or account-creation pages.

Rate-limiting rules can provide a cost-efficient first layer of defense. You can use more advanced rules to protect sensitive URIs. URI-specific rate-based rules can limit the impact on critical pages or on APIs that affect the backend, such as database access. Advanced mitigations to protect certain URIs, which are discussed later in this guide, often incur additional costs, and these URI-specific rate-based rules can help you control costs. For more information about commonly recommended rate-based rules, see [The three most important AWS WAF rate-based rules](https://aws.amazon.com/blogs/security/three-most-important-aws-waf-rate-based-rules/) in the AWS Security Blog. In some situations, it is useful to limit what type of request is evaluated by a rate-based rule. You can use [scope-down statements](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-scope-down-statements.html) to, for example, limit rate-based rules by the geographic area of the source IP address.

AWS WAF offers an advanced capability for rate-based rules through the use of [aggregation keys](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-aggregation-instances.html). With this functionality, you can configure a rate-based rule to use various other aggregation keys and key combinations, aside from the source IP address. For example, as a single combination, you can aggregate requests based on a forwarded IP address, the HTTP method, and a query argument. This helps you configure more fine-grained rules for sophisticated volumetric traffic mitigation.

## Intrinsic checks
<a name="intrinsic-checks"></a>

*Intrinsic checks* are various types of internal or inherent validations or verifications within a system or process. For bot control, AWS WAF performs an intrinsic check by validating that the information sent in the request matches the system signals. For example, it performs reverse DNS lookups and other system verifications. Some automated requests are necessary, such as SEO-related requests. Allow listing is a way to permit good, expected bots through. But sometimes, malicious bots emulate good bots, and it can be challenging to separate them. AWS WAF provides methods to accomplish this through the managed [AWS WAF Bot Control rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html). The rules in this group provide verification that self-identified bots are who they say they are. AWS WAF checks the details of the request against the known pattern of that bot, and it also performs reverse DNS lookups and other objective verifications.
