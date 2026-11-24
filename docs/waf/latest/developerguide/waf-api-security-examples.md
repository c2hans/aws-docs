---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-examples.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# AWS WAF API Security examples

This section shows example configurations for common AWS WAF API Security use cases. Each example provides a description of the use case and the solution as a JSON rule configuration.

**Note**
The JSON listings shown in these examples were created in the console by configuring the rule and then editing it using the **Rule JSON editor**.

**Topics**
+ [Minimum viable configuration](waf-api-security-example-minimum.md)
+ [Counting everything for a first deployment](waf-api-security-example-count-first-deploy.md)
+ [Limiting evaluation to your API paths](waf-api-security-example-scope-down.md)
+ [Overriding the action on individual rules](waf-api-security-example-rule-overrides.md)
+ [Building custom mitigations from detection labels](waf-api-security-examples-detection-labels.md)
+ [Blocking one threat family at any confidence](waf-api-security-example-block-threat-family.md)
+ [Blocking every request where attack-stage activity was detected](waf-api-security-example-block-attack-stage.md)
+ [Rate-limiting reconnaissance instead of blocking it](waf-api-security-example-rate-limit-recon.md)
+ [Challenging clients that produced posture warnings](waf-api-security-example-challenge-posture.md)
+ [Building custom mitigations from identity labels](waf-api-security-examples-identity-labels.md)
+ [Blocking a client that has attacked anywhere on your protection pack (web ACL)](waf-api-security-example-block-attack-actors.md)
+ [Capping the combined request rate of clients flagged for reconnaissance](waf-api-security-example-rate-limit-recon-actors.md)
+ [Treating a known client more leniently than an unknown one](waf-api-security-example-allow-known-client.md)
