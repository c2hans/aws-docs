---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-example-count-first-deploy.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Counting everything for a first deployment

Override each rule that blocks by default to Count. Every rule then runs and adds its label, and no rule in the rule group blocks. This is the configuration to use while the behavioral baseline builds, over approximately the first one to two weeks.

Set the overrides on the individual rules rather than setting the rule group's override action (`OverrideAction`) to Count. A rule group override action of Count doesn't change how the rule group evaluates a request, so evaluation stops at the first rule that would block, and the rules after it don't add their labels.

The following list covers the rules that block by default in version 1.0. For the current rules and their default actions, see [AWS WAF API Security rule group](aws-managed-rule-groups-api-security.md).

```json
{
  "Name": "AWS-AWSManagedRulesAPISecurityRuleSet",
  "Priority": 100,
  "Statement": {
    "ManagedRuleGroupStatement": {
      "VendorName": "AWS",
      "Name": "AWSManagedRulesAPISecurityRuleSet",
      "RuleActionOverrides": [
        { "Name": "FixedAlgSignatureLengthMismatch_JWT_Signature", "ActionToUse": { "Count": {} } },
        { "Name": "AlgNone_JWT_Header", "ActionToUse": { "Count": {} } },
        { "Name": "MissingAlg_JWT_Header", "ActionToUse": { "Count": {} } },
        { "Name": "EmbeddedCertChain_JWT_Header", "ActionToUse": { "Count": {} } },
        { "Name": "EmbeddedJwk_JWT_Header", "ActionToUse": { "Count": {} } },
        { "Name": "CommandInjection_JWT", "ActionToUse": { "Count": {} } },
        { "Name": "PathTraversal_JWT_Header", "ActionToUse": { "Count": {} } },
        { "Name": "SQLInjection_JWT", "ActionToUse": { "Count": {} } },
        { "Name": "RemoteCertUrl_JWT_Header", "ActionToUse": { "Count": {} } },
        { "Name": "RemoteJwkUrl_JWT_Header", "ActionToUse": { "Count": {} } },
        { "Name": "UnsignedToken_JWT", "ActionToUse": { "Count": {} } },
        { "Name": "InvalidFourSegmentCompact_JWT", "ActionToUse": { "Count": {} } },
        { "Name": "Log4j_JWT_Payload", "ActionToUse": { "Count": {} } },
        { "Name": "AlgWhitespace_JWT_Header", "ActionToUse": { "Count": {} } },
        { "Name": "EcdsaPsychicSignature_JWT_Signature", "ActionToUse": { "Count": {} } },
        { "Name": "APISecurityObjectLevelHigh", "ActionToUse": { "Count": {} } },
        { "Name": "APISecurityCredStuffingHigh", "ActionToUse": { "Count": {} } },
        { "Name": "APISecurityPathFuzzingHigh", "ActionToUse": { "Count": {} } },
        { "Name": "APISecurityArgsFuzzingHigh", "ActionToUse": { "Count": {} } },
        { "Name": "APISecurityEnumerationHigh", "ActionToUse": { "Count": {} } },
        { "Name": "APISecurityActorIdentityHigh", "ActionToUse": { "Count": {} } }
      ]
    }
  },
  "OverrideAction": {
    "None": {}
  },
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "AWS-AWSManagedRulesAPISecurityRuleSet"
  }
}
```
