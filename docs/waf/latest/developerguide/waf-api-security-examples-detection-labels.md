---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-examples-detection-labels.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Building custom mitigations from detection labels

All labels begin with `awswaf:managed:aws:api-security:` and carry a stage first:
+ **recon** – The client is learning the shape of your API rather than using it, indicated by breadth without depth.
+ **attack** – The client is applying force against a control, indicated by targeted requests and persistence.
+ **warning** – A posture observation not attributable to an attacker.

The two halves of the rule group use different label shapes after the stage:

```text
behavioral     awswaf:managed:aws:api-security:<stage>:<finding>:<confidence>
deterministic  awswaf:managed:aws:api-security:<stage>:<check>[:<location>]
```

The behavioral findings are `object_level`, `enumeration`, `args_fuzzing`, `cred_stuffing`, `path_fuzzing`, and `actor_identity`, each at high, medium, or low. The confidence indicates how much benign traffic the combination of evidence ruled out. A deterministic label carries no confidence; it names the specific check and usually the part of the token that was inspected.

Place all of these rules after the API Security managed rule group. Labels are available only to rules that run later in the same protection pack (web ACL).
