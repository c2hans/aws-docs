---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/troubleshooting-ad-skipping-overview.html
---

# MediaTailor ad skipping troubleshooting guide
<a name="troubleshooting-ad-skipping-overview"></a>

Ad skipping is one of the most common issues that MediaTailor customers report. This guide helps you identify ad skipping issues and provides step-by-step troubleshooting procedures.

## Symptoms and impact
<a name="ad-skipping-symptoms"></a>

When ad skipping occurs, you might observe the following symptoms:
+ Ads don't appear during expected ad breaks
+ Ad breaks show content instead of advertisements
+ Inconsistent ad playback across different viewing sessions
+ CloudWatch logs showing `AdSkipped` events with various skip reasons

Ad skipping directly impacts revenue and can create poor viewer experiences. Address these issues promptly to maintain optimal performance.

## Identifying skip reasons
<a name="identifying-skip-reasons"></a>

Use CloudWatch Logs Insights to query the `MediaTailor/AdDecisionServerInteractions` log group for skipped ads:

```
fields @timestamp, avail.availId, skippedAds.0.skippedReason, skippedAds.0.creativeUniqueId
| filter eventType = "FILLED_AVAIL" and ispresent(skippedAds.0.skippedReason)
| sort @timestamp desc
```

This query returns the most recent ad skip events with their specific reasons to help you identify patterns.

**Topics**
+ [Symptoms](#ad-skipping-symptoms)
+ [Skip reasons](#identifying-skip-reasons)
+ [NEW\_CREATIVE skipping](troubleshooting-new-creative-skipping.md)
+ [ADS timeout skipping](troubleshooting-ads-timeout-skipping.md)
+ [VAST parsing skipping](troubleshooting-vast-parsing-skipping.md)
+ [Duration mismatch skipping](troubleshooting-duration-mismatch-skipping.md)
+ [Session variable skipping](troubleshooting-session-variables-skipping.md)
+ [Monitoring ad skipping](monitoring-ad-skipping-issues.md)
+ [Prevention best practices](preventing-ad-skipping-best-practices.md)
+ [Reference materials](ad-skipping-reference-materials.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
