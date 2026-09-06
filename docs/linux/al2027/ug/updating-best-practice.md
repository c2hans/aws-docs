---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/updating-best-practice.html
---

# Best practices for safely deploying updates
<a name="updating-best-practice"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

AL2027 has several features designed to help you deploy operating system updates safely, know what changed between updates, and, if necessary, revert to the previous version. This section reflects lessons we learned from more than a decade of internal and external use of Amazon Linux.

**Warning**
 Running `sudo dnf upgrade --releasever=latest` is not best practice, and is likely to result in an OS update being first tested in production.
 Instead of `latest`, use a specific AL2027 release version. This ensures that you deploy the same changes across production instances that you previously tested. For example, `sudo dnf upgrade --releasever=2027.0.20260817` always updates to the 2027.0.20260817 release.

Plan for the deployment safety of OS updates. An unexpected negative interaction between your application and an OS update can cause impact up to a total outage. As with any software issue, the earlier an issue is detected, the less impact it has on end users.

Do not rely on two assumptions that are fundamentally not true:

1. The OS vendor will never make a mistake in an update to the OS.

1. The specific behavior of, or interface to, the OS that you rely on matches what the OS vendor considers something to be relied upon. In other words, both the OS vendor and you would agree that an update introduced a problem.

Treat the OS as another part of your deployment. Apply the same deployment safety mechanisms that you use for any other change to a production environment:
+ Test all OS updates before deploying to production systems. Do not test new OS updates by deploying them to production.
+ Use staged rollouts, such as wave or phase based deployments (for example 1%, 5%, 10%, 20%, 40%, 100% of a fleet), combined with monitoring. If a problem occurs, impact is restricted to a subset of the fleet and the rollout can be halted while you investigate.
+ Know how to point your deployment systems at a previous known-good version of the OS. Mitigating impact is usually the first priority; reverting to a known-good version is a powerful tool. After the issue is resolved, move to a new known-good version rather than staying locked to the old one.

[Deterministic upgrades through versioned repositories on AL2027](deterministic-upgrades.md) makes every change to the OS version repeatable. Each AL2027 release is a version you can lock to, with AMIs and container images that lock to that version. If a release causes a problem for your workload, you can immediately go back to the images of the prior release while you work out how to resolve it. Deterministic upgrades also protect in-progress deployments. A release that comes out mid-deployment does not affect the fleet: it keeps applying the exact release version the deployment started with.

The changes in each release are documented in the [AL2027 Release Notes](https://docs.aws.amazon.com/linux/al2027/release-notes/relnotes.html). Security issues addressed in package updates are covered by [Amazon Linux Security advisories for AL2027](alas.md).

Not taking OS updates promptly also causes issues. New releases contain bug and security fixes that are likely relevant to your environment. Configure your deployment systems so that taking a new release, testing it, and rolling it out is routine. For more information, see [Security and Compliance in AL2027](security.md) and [Manage package and operating system updates in AL2027](manage-updates.md).

**Topics**
+ [Preparing for minor updates](#prepare-for-minor-updates)
+ [Preparing for major updates](#prepare-for-major-updates)

## Preparing for minor updates
<a name="prepare-for-minor-updates"></a>

Preparing for smaller updates, such as a new point release of AL2027, is intended to require minimal effort. Read the [AL2027 Release Notes](https://docs.aws.amazon.com/linux/al2027/release-notes/relnotes.html) for upcoming changes, and check package support timelines with the `dnf supportinfo` command. For more information, see [Getting package support information](manage-updates.md#dnf-support-info-plugin).

## Preparing for major updates
<a name="prepare-for-major-updates"></a>

Updating to a new major version of an operating system requires planning, work to adapt to changed or removed functionality, and testing before deployment. You can prepare incrementally while still on the previous version by addressing deprecated functionality first.

For example, AL2023 documented System V init scripts as deprecated, and AL2027 removes support for them. Workloads that migrated to `systemd` unit files while still on AL2023 move to AL2027 without that change. The same applies to the other items in [Deprecated functionality in AL2027](deprecated.md): addressing them early turns a major version upgrade into a series of small, safe steps.

The list of deprecated functionality is updated over the lifetime of the OS. Check it regularly to prepare for the next major version of Amazon Linux.
