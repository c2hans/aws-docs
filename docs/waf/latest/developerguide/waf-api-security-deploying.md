---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-deploying.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Testing and deploying AWS WAF API Security

This section provides general guidance for configuring and testing an AWS WAF API Security implementation for your APIs. The specific steps that you choose to follow depend on your needs, resources, and the web requests that you receive. This information is in addition to the general information about testing and tuning provided at [Testing and tuning your AWS WAF protections](web-acl-testing.md).

**Note**
AWS Managed Rules are designed to protect you from common web threats. When used in accordance with the documentation, AWS Managed Rules rule groups add another layer of security for your applications. However, AWS Managed Rules rule groups aren't intended as a replacement for your security responsibilities, which are determined by the AWS resources that you select. Refer to the [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) to ensure that your resources in AWS are properly protected.

**Production traffic risk**
Before you deploy your API Security implementation for production traffic, test and tune it in a staging or testing environment until you are comfortable with the potential impact to your traffic. Then test and tune the rules in count mode with your production traffic before enabling them.

This guidance is intended for users who know generally how to create and manage AWS WAF protection packs (web ACLs), rules, and rule groups. Those topics are covered in earlier sections of this guide.

**To configure and test an API Security implementation**

Perform these steps first in a test environment, then in production.

1.

**Add the API Security managed rule group**
**Note**
You are charged additional fees when you use this managed rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/).

   Add the AWS managed rule group `AWSManagedRulesAPISecurityRuleSet` to a new or existing protection pack (web ACL) and configure it so that it doesn't alter current protection pack (web ACL) behavior.

   When you add the managed rule group, edit it and in the **Rules** pane, open the **Override all rule actions** dropdown and choose **Count**. This sets a Count override on each rule in the rule group (`RuleActionOverrides`), not the rule group's override action. With this configuration, AWS WAF evaluates requests against all of the rules in the rule group and only counts the matches that result, while still adding labels to requests. For more information, see [Overriding rule actions in a rule group](web-acl-rule-group-settings.md#web-acl-rule-group-rule-action-override).

   Overriding to count matters more for this rule group than for most. Many of its rules block by default: most of the deterministic rules, and the high-confidence behavioral rules (one for each behavioral detection, plus one for the identity labels). Without the override, adding the rule group changes how your traffic is handled immediately.

   Position the rule group so that it's evaluated last in the protection pack (web ACL), with a priority setting that's numerically higher than any other rules or rule groups that you're already using. For more information, see [Setting rule priority](web-acl-processing-order.md). This way, your current handling of traffic isn't disrupted.
**Note**
Keep the rule group in the same position after testing. The behavioral detections learn from the traffic that reaches them, so a rule group evaluated last learns from the traffic that survives your other rules. If you move the rule group earlier after its baseline has formed, you begin feeding it traffic it has never seen, and its detections are measured against a baseline that no longer describes what it is evaluating.

1.

**Enable logging and metrics for the protection pack (web ACL)**

   As needed, configure logging, Amazon Security Lake data collection, request sampling, and Amazon CloudWatch metrics for the protection pack (web ACL). You need all of these to tune this rule group: the metrics tell you whether a detection is firing cleanly, and the logs tell you what it fired on.

   For information about logging, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md). For Amazon Security Lake, see [What is Amazon Security Lake?](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html) For CloudWatch metrics, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md). For web request sampling, see [Viewing a sample of web requests](web-acl-testing-view-sample.md).

1.

**Associate the protection pack (web ACL) with a resource**

   If the protection pack (web ACL) isn't already associated with a resource, associate it. For information, see [Associating or disassociating protection with an AWS resource](web-acl-associating-aws-resource.md).

1. <a name="waf-api-security-deploying-baseline"></a>

**Let the behavioral baseline form**

   The deterministic rules in this rule group evaluate the contents of a single request and are accurate from the first one. The behavioral detections work differently: they compare a client's activity against the normal pattern of activity for the endpoints it is using, and that pattern must be learned before any comparison is possible.

   API Security establishes a baseline of normal traffic for each protected resource and refreshes it automatically as traffic arrives. Each refresh runs at least every 12 hours, or sooner on high-traffic resources, and uses up to the most recent 24 hours of traffic. After you enable the rule group, plan for approximately one day of typical traffic before the first baseline is available.

   Behavioral detections become more accurate over the first one to two weeks as the baseline builds. Each refresh merges into the existing baseline, with recent traffic weighted more heavily than older traffic. Older traffic loses influence day by day and drops out of the baseline after approximately two weeks.

   An endpoint gets its own baseline once it receives enough successful requests over the trailing two weeks. Endpoints with very little traffic, or that stop receiving traffic, aren't modeled individually.

   **What this means for your deployment:**
   + **Expect your first behavioral detections after approximately one day, not immediately.** The deterministic rules are working from the first request, so the rule group isn't idle in the meantime.
   + **Give it one to two weeks before you judge a behavioral detection.** A detection raised on the second day rests on a baseline built from approximately one day of traffic. The same detection two weeks later rests on a fuller picture of what your clients normally do.
   + **Don't tune in the first few days.** A detection that looks noisy early may be correct once the baseline fills. Overriding an action or narrowing the scope while the baseline is building removes the evidence you would need to tell the difference.
   + **There is no point at which the baseline is finished.** It refreshes continuously, and a refresh merges into what is already there rather than starting over. A change you make later doesn't reset it. The consequence is that a sustained change in your traffic becomes the new normal within approximately two weeks.
   + **Check your low-traffic endpoints separately.** An endpoint that doesn't get enough successful requests over the trailing two weeks isn't modeled on its own, so behavioral coverage isn't uniform across your API. If you have endpoints that matter more than their traffic volume suggests, don't assume a behavioral detection will appear there.

1.

**Monitor traffic and API Security rule matches**

   Make sure that traffic is flowing and that the rule group is adding labels to matching web requests. You can see the labels in the logs and in CloudWatch metrics. In the logs, the rules that you've overridden to count show up in the `ruleGroupList` with `action` set to count, and with `overriddenAction` indicating the configured rule action that you overrode.

   **Using metrics to evaluate whether a detection is firing cleanly**

   Matches appear in the standard `AWS/WAFV2` namespace, with the `LabelNamespace` and `LabelName` dimensions. The API Security namespace is `awswaf:managed:aws:api-security:`. Which metric counts a detection depends on the kind of rule:
   + **Deterministic rules** add their own labels, so their matches appear in the rule match metrics. A rule that counts, including one that you've overridden to Count, appears in `CountRuleMatch`. A rule that blocks appears in `BlockRuleMatch`.
   + **Behavioral detections** are labels that the behavioral analysis adds, not a rule, so AWS WAF doesn't publish rule match metrics for them. A request that carries one is counted under its final action: `AllowedRequests` if AWS WAF allows it, and `BlockedRequests` if AWS WAF blocks it. If other rules in your protection pack (web ACL) use a CAPTCHA or Challenge action, also add `CaptchaRequests` and `ChallengeRequests`.

   Rank detections by match rate over the baseline window:

   ```text
   deterministic_match_rate = CountRuleMatch / Requests
   behavioral_match_rate    = (FILL(AllowedRequests, 0) + FILL(BlockedRequests, 0)) / Requests
   ```

   `FILL` replaces a missing data point with 0, so the sum has a value when only one of the metrics is published. If other rules in your protection pack (web ACL) use a CAPTCHA or Challenge action, add `FILL(CaptchaRequests, 0)` and `FILL(ChallengeRequests, 0)` to the behavioral sum.

   Read the rate together with its shape over time. A detection holding a steady, traffic-proportional rate is the shape of a false positive, because your own clients are tripping it on every request. A detection near zero that bursts is the shape of something real, because an attack is time-bounded and your normal traffic is not. For the behavioral rules, compare each detection's confidence tiers against each other (for example, `APISecurityObjectLevelHigh`, `APISecurityObjectLevelMedium`, and `APISecurityObjectLevelLow`). Confidence tiers should thin out as confidence rises. A high tier firing as often as a low one means the tiering isn't separating your traffic.

   What the metrics can't tell you is how many distinct clients are behind a count, because every metric counts requests and matches rather than entities. That is the question that determines a behavioral detection, and it is answerable only from the logs: many matches from few clients is a campaign; one match each from many clients is your own traffic. Rank with the metrics, then confirm in the logs before you enforce.

   **Test with credentials your API accepts**

   AWS WAF identifies a client by source IP address plus a hash of the request's authentication header, and falls back to the IP address alone when there is no credential it can hash. A finding that would otherwise be high confidence is reported as medium for a client identified by IP address alone. Traffic you generate from a script or a test host without your application's credentials therefore never produces a high-confidence behavioral finding. Only the high-confidence behavioral rules block by default. If you test without credentials and see nothing at the high tier, that is the expected result, not evidence that the rule group is quiet.

   **Send test traffic to your API paths**

   Requests whose URI path ends in a static-file extension, such as .png, .js, or .html, aren't sent for behavioral analysis. They receive the `awswaf:managed:aws:api-security:not_supported` label instead, so a test against static files produces no behavioral finding.

   **Using the sampled requests view**

   Sampled requests show you individual requests the rule group labeled, which is the quickest way to confirm what a detection matched on. Some limitations are worth knowing. The view is a sample, so the absence of a request doesn't mean the rule group didn't evaluate it. For a behavioral detection, the meaningful unit is a client across many requests, so a sampled request shows you that a label was attached but not the activity that produced it. Use the logs and metrics for that.

   Carefully review the web request handling for any false positives that you might need to mitigate with custom handling. For examples, see [Example scenarios of false positives with AWS WAF API Security](waf-api-security-false-positives.md).

1.

**Tune the detections that need it**

   The rule group doesn't have a configuration of its own, so tuning means changing rule actions or changing what the rule group sees. Change one thing at a time, and prefer the change with the narrowest effect.

   1. **Override the action on the individual rule first.** Setting a noisy rule to Count stops it from acting while it keeps evaluating and adding its label, so you lose no visibility and you can reverse the change immediately. The effect is contained to that one rule. This is the right approach when one rule is noisy and the rest are behaving.

   1. **Narrow the scope with a scope-down statement second.** This has the wider effect. Excluded traffic isn't evaluated by any rule. Because the behavioral detections learn from what the rule group evaluates, excluded traffic is also removed from the baseline. That degrades detection quality for the traffic that remains, rather than simply reducing coverage.

   If your goal is reducing cost rather than reducing false positives, only the second option helps. A scope-down statement reduces the requests you are billed for; an action override doesn't.

1.

**Customize request handling where tuning isn't enough**

   As needed, add your own rules that explicitly allow or block requests to change how the API Security rules would otherwise handle them. Common approaches:
   + **Explicitly allow requests** with a rule that you add before the API Security managed rule group. The allowed requests never reach the rule group, which can help reduce cost. Note that those requests are also absent from the baseline.
   + **Exclude requests from evaluation** with a scope-down statement inside the managed rule group statement. For information, see [Using scope-down statements in AWS WAF](waf-rule-scope-down-statements.md).
   + **Use API Security labels in request handling.** Add a label match rule after the managed rule group to separate labeled requests you want to allow from those you want to block. After testing, keep the related rules in count mode and maintain the handling decision in your own rule. For information, see [Label match rule statement](waf-rule-statement-type-label-match.md).

   For additional examples, see [AWS WAF API Security examples](waf-api-security-examples.md).

1.

**Enable the API Security managed rule group settings**

   When you are satisfied with what the rule group is detecting, remove the Count overrides from the rules that you want to enforce, so that those rules run as they are configured inside the rule group.

   For most customers, this is the end state rather than a starting point for raising actions further. The rule group's own defaults already express the distinction between evidence of an attack and an observation about posture:
   + **Deterministic token attack rules** – Block by default, because a token carrying one of these techniques is evidence of an attack rather than of a misconfiguration.
   + **Deterministic posture and reconnaissance rules** – Count by default, because they aren't attributable to an attacker and blocking them would mean blocking your own integrations.
   + **High-confidence behavioral rules** (for example, `APISecurityObjectLevelHigh`) – Block by default. Each blocks the findings of its detection at high confidence. For path fuzzing and args fuzzing, these are reconnaissance findings only. For the other detections, they are both reconnaissance and attack findings. `APISecurityActorIdentityHigh` also blocks a caller's later requests anywhere on the protection pack (web ACL) once the caller has triggered a high-confidence detection.
   + **Medium and low-confidence behavioral rules** – Count by default.

   On the behavioral side, you can promote one detection at a time (for example, `APISecurityObjectLevelMedium`) from Count to Block. Do that only where your own metrics for that detection support it. Expect to stop at medium: low confidence means the evidence ruled out no common benign flow. If you decided during testing to keep some rules in count or with a different override, edit the rule group statement in your protection pack (web ACL) and make your changes in the **Rules** pane.
