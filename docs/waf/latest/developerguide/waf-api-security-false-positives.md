---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-false-positives.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Example scenarios of false positives with AWS WAF API Security

A false positive is traffic that you expect and want to serve, matched by a rule that is working as designed. The API Security managed rule group can produce false positives for a specific reason: its behavioral detections compare a client's activity against the pattern it has learned for your endpoints, and some legitimate clients genuinely don't behave like your typical users.

Before you change anything, note what you can't change. This rule group doesn't have a configuration of its own. There is no sensitivity setting and no way to disable an individual detection. Your options are to override a rule's action, to narrow what the rule group evaluates with a scope-down statement, or to add your own rule before or after the rule group. Those options appear throughout this page. For how to apply them, see [Testing and deploying AWS WAF API Security](waf-api-security-deploying.md).

## A scheduled job is detected as enumeration
<a name="waf-api-security-false-positives-scheduled-job"></a>

**What you see**

A nightly export, a reconciliation job, or a cache warmer receives an `object_level` or `enumeration` finding, often at low or medium confidence, on the endpoints it reads in bulk.

**Why it happens**

The job reads many object identifiers in a short window with machine-regular timing, which is the pattern the object-breadth and timing-regularity signals look for. The confidence model is designed to discount this, because the breadth and the regularity describe the same scheduled job rather than two independent pieces of evidence. However, the detection can still surface when the job hasn't yet been learned as normal.

**What to do**

Confirm the client from the sampled requests or the logs first, because a credential-stuffing campaign and a batch job look similar in a metric and quite different in a log line. Then either allow the job ahead of the rule group (if you can identify it reliably by a header or a path) or exclude its path with a scope-down statement. Both choices remove the job's traffic from the behavioral baseline as well, which is what you want here: the baseline should describe your real clients.

## Your own security scanner is detected as reconnaissance
<a name="waf-api-security-false-positives-scanner"></a>

**What you see**

An internal scanner, an inventory tool, or a penetration test receives `path_fuzzing`, `object_level`, or `args_fuzzing` findings, often at high confidence.

**Why it happens**

This isn't a false positive in the traditional sense. Enumerating endpoints and object identifiers is what those tools do, and the rule group is identifying it correctly. What is wrong is only that you authorized the activity.

**What to do**

Allow the scanner ahead of the rule group, identified as specifically as you can. A scanner is also the cleanest way to confirm that the rule group is working before you trust it on real traffic, so consider leaving one unauthorized scan unallowed in a test environment.

## A client lagging an API version is detected as path probing
<a name="waf-api-security-false-positives-stale-client"></a>

**What you see**

`path_fuzzing` findings, and an elevated error-rate contribution, from a client calling paths that no longer exist.

**Why it happens**

A client requesting removed routes produces the same off-schema requests and the same 404 pattern as a client mapping your surface deliberately. The rule group can't distinguish a stale client from a probing one.

**What to do**

Fix the client, which is the real defect. If the old version is still served deliberately, make sure its paths are in the schema the rule group has learned, or exclude them with a scope-down statement.

For more ways to express these mitigations, see [AWS WAF API Security examples](waf-api-security-examples.md).
