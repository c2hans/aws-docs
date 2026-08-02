---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-no-findings.html
---

# Assessment produces no failure mode findings
<a name="next-gen-troubleshoot-no-findings"></a>

**Symptom:** Assessment completes successfully but returns zero failure mode findings.

**Possible causes:**
+ Service has very few resources (assessment needs sufficient architecture to analyze).
+ No policy is applied (assessments without policies produce fewer findings).
+ Architecture already meets all requirements.
