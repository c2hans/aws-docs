---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/bot-control/advanced-analysis-controls.html
---

# Advanced analysis controls for managing bots
<a name="advanced-analysis-controls"></a>

Some bots employ advanced deception tools to actively evade detection. These bots mimic human behavior in order to perform a specific activity, such as scalping. These bots have a purpose, and it is usually linked to a big monetary reward.

These advanced, persistent bots use a mix of technologies to evade detection or blend in with regular traffic. In turn, this also requires a mix of different detection technologies to accurately identify and mitigate the malicious traffic.

## Targeted use cases
<a name="targeted-use-cases"></a>

Use-case data can provide bot-detection opportunities. *Fraud detections* are special use cases where special mitigation is warranted. For example, to help prevent account takeovers, you can compare a list of compromised account usernames and passwords against login or account creation requests. This helps website owners to detect login attempts that use compromised credentials. Use of compromised credentials can indicate bots trying take over an account, or it could be users who are unaware their credentials are compromised. In this use case, website owners can take additional steps to verify the user and then help them change their password. AWS WAF provides the [Fraud Control account takeover prevention (ATP)](https://docs.aws.amazon.com/waf/latest/developerguide/waf-atp.html) managed rule for this use case.

## Application-level or aggregated bot detection
<a name="aggregated-bot-detection"></a>

Some use cases require combining data about requests from the content delivery network (CDN), AWS WAF, and the backend of the application or service. Sometimes, you even need to integrate third-party intelligence to be able to make high-confidence decisions about bots.

Features in [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) and AWS WAF can send signals to the backend infrastructure, or they can subsequently aggregate rules through headers and [labels](https://docs.aws.amazon.com/waf/latest/developerguide/waf-labels.html). CloudFront exposes JA3 fingerprint headers, as previously mentioned. This is an example of CloudFront providing such data through a header. AWS WAF can send labels when it matches on a rule. Subsequent rules can use these labels to make better decisions about bots. When multiple rules are combined, you can implement highly granular controls. A common use case is to match on parts of a managed rule through a label and then combine it with other request data. For more information, see [Label match examples](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-label-match-examples.html) in the AWS WAF documentation.

## Machine learning analysis
<a name="machine-learning-analysis"></a>

Machine leaning (ML) is a powerful technique for dealing with bots. ML can adapt to changing details, and when combined with other tools, provides the most robust and complete way to mitigate bots with minimal false positives. The two most common ML techniques are *behavioral analysis* and *anomaly detection*. With behavioral analysis, a system (in the client, server, or both) monitors how a user interacts with the application or website. It monitors mouse movement patterns or frequency of click and touch interactions. The behavior is then analyzed with a ML model to recognize bots. Anomaly detection is similar. It focuses on detecting behavior or patterns that are significantly different from a baseline that is defined for the application or website.

AWS WAF targeted controls for bots provides predictive ML technology. This technology helps defend against distributed, proxy-based attacks that are made by bots designed to evade detection. The managed [AWS WAF Bot Control rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html) uses automated, ML analysis of website traffic statistics to detect anomalous behavior that is indicative of distributed, coordinated bot activity.
