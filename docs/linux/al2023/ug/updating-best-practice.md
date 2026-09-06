---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/updating-best-practice.html
---

# Best practices for safely deploying updates
<a name="updating-best-practice"></a>

 Amazon Linux 2023 (AL2023) has several features designed to aid in safely deploying updates to the Operating System, and being able to know what changed between updates, and if necessary, easily revert to the older version. This section explores lessons learned by AWS from more than a decade of internal and external use of Amazon Linux.

**Warning**
 Running `dnf --releasever=latest update` is not best practice, and is likely to result in an OS update being first tested in production.
 Instead of using `latest`, use a specific AL2023 release version. This ensures you are deploying the same changes across production instances as you previously tested. For example, `dnf --releasever=2023.12.20260817 update` will always update to the 2023.12.20260817 release.
 For more information, see the [Updating AL2023](https://docs.aws.amazon.com/linux/al2023/ug/updating.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/).

 Without planning for deployment safety of OS updates, the impact of an unexpected negative interaction between your application/service and an OS update can be significantly greater, up to and including a total outage. As with any software issue, the earlier the issue is detected, the less impact it can have on end users.

 It is important to not fall into the trap of believing two things which are fundamentally not true:

1. The OS vendor will never make a mistake in an update to the OS.

1. The specific behavior of or interface to the OS that you rely on matches behavior and interfaces that the OS vendor would consider something to be relied upon.

   i.e. both the OS vendor and you would agree that there was a problem with the update.

 Do not rely on good intentions, put systems in place to ensure that deployment safety *includes* any update to the OS.

 It is not recommended to test new OS updates by deploying to production environments. It is best practice to consider the OS as another part of your deployment, and think about applying the same deployment safety mechanisms you consider suitable for any other change to a production environment.

 It is best practice to test any and all OS updates before deploying to production systems. When deploying, staged rollouts combined with good monitoring are recommended. Staged rollouts can ensure that if a problem occurs, even if not immediate, impact is restricted to a subset of a fleet, and further deployment of the update can be halted while further investigation and mitigation can occur.

 The mitigation of any negative impact of taking an update to the OS is often the first priority, followed by resolving the issue, wherever it may be. Where the introduction of an OS update is correlated to negative impact, the ability to revert to the previous known-good version of the OS is a powerful tool to have.

 Amazon Linux 2023 introduces [Deterministic upgrades through versioned repositories](deterministic-upgrades.md), a powerful new feature to ensure any change to the version of the OS (or individual packages) is repeatable. Thus, if a problem is encounted when moving from one OS version to the next, there are simple to use mechanisms available to stick to the known-working OS version while working out how to resolve the problem.

 With AL2023, whenever we release new package updates, there's a new version to lock to, and new AMIs that lock to that version. The [AL2023 Release Notes](https://docs.aws.amazon.com/linux/al2023/release-notes/) cover changes in each release, and [Amazon Linux Security advisories for AL2023](alas.md) covers security issues addressed in package updates.

 For example, if you were affected by the issue present in the [2023.6.20241028](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20241028.html) release, you could immediately revert to using the AMIs and container images of the prior release, [2023.6.20241010](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20241010.html). In this case, there was a bug in a package that was fixed in the subsequent [2023.6.20241031](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20241031.html) release, but with [Deterministic upgrades through versioned repositories](deterministic-upgrades.md) anyone affected could *immediately* take simple action to mitigate: just use the previous images.

 [Deterministic upgrades through versioned repositories](deterministic-upgrades.md) also gives assurance that any in-progress deployment of an OS update, either in place or by launching new AMIs or container images, are not affected by subsequently released OS updates.

 For our first example, fleet A is a large fleet which is halfway through deploying the update from [2023.5.20241001](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.5.20241001.html) to the [2023.6.20241010](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20241010.html) release when the [2023.6.20241028](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20241028.html) release comes out. [Deterministic upgrades through versioned repositories](deterministic-upgrades.md) means that the deployment for fleet A continues without any change to what updates it is applying.

 The purpose of wave based or phase based deployment strategies such as first deploying to 1% of a fleet, then 5%, 10%, 20%, 40%, until reaching 100%, is to be able to test a change in a limited fashion before rolling it out wider. This type of deployment strategy is commonly considered best practice for deploying any production change.

 With a wave based deployment strategy and the fleet A update to [2023.6.20241010](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20241010.html) being at a stage where it's being deployed to a lot of hosts at once, the fact that [2023.6.20241028](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20241028.html) was released has *no impact on the in-progress deployment* thanks to using [Deterministic upgrades through versioned repositories](deterministic-upgrades.md).

 If fleet B was running an older version, say [2023.5.20240708](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.5.20240708.html), and had started deploying the update to [2023.6.20241028](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20241028.html), and fleet B was affected by the issue in that version, this would be noticed early in the deployment. At that point, a decision can be made on if to pause any rollout until a fix for that issue is available, or if in the meantime to start a deployment of the same version fleet A was running, [2023.6.20241010](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20241010.html) so that fleet B gets all the updates between [2023.5.20240708](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.5.20240708.html) and [2023.6.20241010](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20241010.html).

 It is important to note that *not* taking OS updates promptly can cause issues. New updates likely contain bug and security fixes which may be relevant to your environment. For more information, see [Security and Compliance in Amazon Linux](security.md) and [Manage package and operating system updates in AL2023](managing-repos-os-updates.md).

 It is important to configure your deployment systems to be able to easily take new OS updates, test them before deploying to production, and use mechanisms such as wave based deployments to minimize any negative impact. In order to be able to mitigate any negative impact of an OS update, it is important to know how to make your deployment systems point to a previous known-good version of the OS, and once the issue is addressed, no longer be locked to the older known-good version but rather move to a new known-good version.

## Preparing for Minor Updates
<a name="prepare-for-minor-updates"></a>

 Preparing for smaller updates to the OS, such as a new point release of AL2023 is intended to be limited to zero effort. Be sure to read the [AL2023 Release Notes](https://docs.aws.amazon.com/linux/al2023/release-notes/) for any upcoming changes.

 The [support period of a package](https://docs.aws.amazon.com/linux/al2023/release-notes/all-packages-AL2023.12.html) coming to an end may involve moving to a newer version of the language runtime (such as with [PHP in AL2023](php.md)). It is best practice to prepare for this in advance by moving to new language run time versions comfortably in advance of the support period ending.

 For packages such as [`pcre` version 1](deprecated-al2023.md#deprecated-pcre), there is also the opportunity to plan in advance and migrate any of your code to its replacement, which in this case is `pcre` version 2. It is best practice to do so as soon as possible, to allow time for any setbacks.

 Where there is no direct replacement, such as with [Berkeley DB (`libdb`)](deprecated-al2023.md#deprecated-bdb), you may need to make a choice based on your use case.

## Preparing for Major Updates
<a name="prepare-for-major-updates"></a>

 Updating to a new major version of an Operating System is near universally viewed as something which requires planning, work to adapt to changed or deprecated functionality, and also testing prior to deployment. It is not uncommon to be able to prepare for the next major version of Amazon Linux 2023 more incrementally, such as addressing any use of deprecated or removed functionality before proceeding with moving to the next major version.

 For example, when moving from AL2 to AL2023, reading the [Functionality deprecated in AL2 and removed in AL2023](deprecated-al2.md) section can result in a number of safe and small steps which can happen while still using AL2 to prepare for AL2023. For example, any [Python 2.7 has been replaced with Python 3](python2.7-no-more.md) usage (outside of OS use such as in the `yum` package manager) can be migrated to Python 3 in preparation for using [Python in AL2023](python.md). If using [PHP](php.md), both AL2 (through the PHP 8.2 [AL2 Extra](https://docs.aws.amazon.com/linux/al2/ug/al2-extras.html)) and AL2023 ship PHP 8.2, and thus both PHP version migration and OS migration do not have to occur simultaneously.

 While using AL2023, it is also possible to prepare for the next major version of Amazon Linux 2023 today, while using AL2023. The [Deprecated in AL2023](deprecated-al2023.md) section covers features and packages which are deprecated in AL2023 and due to be removed.

 For example, migrating any remaining [System V init (`sysvinit`)](deprecated-al2023.md#deprecated-sysv-init) use, such as `init` scripts over to their `systemd` equivalent will prepare you for the future, as well as allow you to use the full set of `systemd` features to monitor the service, how and if to restart it, what other services it needs, and if any resource or permission constraints should be applied.

 For features such as 32-bit support, deprecation can span multiple major versions of the OS. For 32-bit, Amazon Linux 1 (AL1) deprecated [32-bit x86 (i686) AMIs](deprecated-al1.md#deprecated-32bit-amis), Amazon Linux 2 deprecated [32-bit x86 (i686) Packages](deprecated-al2.md#deprecated-32bit-rpms), and Amazon Linux 2023 deprecates [32bit x86 (i686) runtime support](deprecated-al2023.md#deprecated-32bit). The transition away from [IMDSv1](deprecated-al2023.md#deprecated-imdsv1) also spans multiple major versions of the OS. For these types of changes, it is understood that some customers require a longer time to adapt to them, thus there is a large amount of leeway before the functionality is no longer available in Amazon Linux 2023.

 The list of deprecated functionality is updated over the lifetime of the OS, and it is advisable to keep up to date with changes to it.
