---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/security-instance-replacement.html
---

# Deterministic updates via instance replacement
<a name="security-instance-replacement"></a>

 The [Deterministic upgrades through versioned repositories on AL2023](deterministic-upgrades.md) feature of Amazon Linux 2023 makes instance replacement an easy way to deterministically and safely roll out updated versions of AL2023. Deterministic updates mean that as a new version is progressively rolled out, if any issue is found, it's simple to revert to the previous AMI while determining the cause of the issue.

 Using instance replacement rather than patching in-place means that updates are more deterministic and predictable as launching new capacity can be a well tested code-path with clear A and B states. Each of the before and after states can be well tested in a CI/CD system before deployment starts.

 When doing in-place patching, there are a lot of intermediary states between before and after applying updates, which is harder to test for all combinations of states.

 An OS update strategy of using instance replacement with deterministic updates fits well into blue/green, wave, and phase based deployment models.
