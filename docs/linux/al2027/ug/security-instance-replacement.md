---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/security-instance-replacement.html
---

# Deterministic updates through instance replacement
<a name="security-instance-replacement"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

With [Deterministic upgrades through versioned repositories on AL2027](deterministic-upgrades.md) in AL2027, you can use instance replacement as a deterministic and safe way to roll out updated versions of AL2027. As you progressively roll out a new version, you can revert to the previous AMI at any point while you determine the cause of an issue.

Using instance replacement rather than patching in-place makes updates more deterministic and predictable. Launching new capacity is a well-tested code path with clear A and B states. You can fully test both states in a CI/CD system before deployment starts. In-place patching passes through many intermediary states between before and after applying updates, which is harder to test for all combinations.

An OS update strategy of instance replacement with deterministic updates fits well into blue/green, wave, and phase based deployment models.
