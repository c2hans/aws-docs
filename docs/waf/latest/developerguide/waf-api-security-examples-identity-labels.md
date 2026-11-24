---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-examples-identity-labels.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Building custom mitigations from identity labels

The `actor_identity` labels attribute a conclusion to the client rather than to the request it sent. This is what makes them the right basis for a rule that should follow an actor across your endpoints. Every other label in this rule group describes one request against one endpoint.

A label attaches to the identity when that identity triggers any endpoint-scoped detection. The label carries the tier of the detection that triggered it and stays on every later request from that identity for a sliding window of approximately five minutes that resets on further detections. One label is added per stage, at that stage's strongest tier, so an identity carries at most two.

```text
awswaf:managed:aws:api-security:<attack|recon>:actor_identity:<high|medium|low>
```

The rule group acts on these labels itself: `APISecurityActorIdentityHigh` blocks a request carrying either identity label at high confidence, and `APISecurityActorIdentityMedium` and `APISecurityActorIdentityLow` count. Your own rules extend that behavior, for example to block at medium confidence or to rate-limit.
