---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/managing-transitive-dependency-conflicts-package-migrations/faq.html
---

# FAQ
<a name="faq"></a>

## What is a transitive dependency conflict?
<a name="what-is-a-transitive-dependency-conflict-.f9005849-2994-57d8-aed3-152368e4eb96"></a>

A transitive dependency conflict occurs when your package depends on Package X, Package X depends on Package Y version 1.x, and your migration target requires Package Y version 2.x. You never declared a dependency on Package Y. It arrived through the package you do depend on. During migration, these hidden version requirements collide.

## What does the transitive dependency analyzer detect?
<a name="what-does-the-transitive-dependency-analyzer-detect-.586c005e-943a-5f1e-9eda-22621c3618fc"></a>

The analyzer reports occurrences, not verdicts. It runs a breadth-first traversal of the dependency tree of a Node.js project and records every package that depends on the target package. For each occurrence, it reports the parent package, the depth count, the breadth count, and the version in use. You compare the reported versions against your target version to identify the conflicts.

## When should I pin a transitive dependency version instead of upgrading it?
<a name="when-should-i-pin-a-transitive-dependency-version-instead-of-upgrading-it-.f48e6a84-1737-501e-a228-23a9072722a6"></a>

Pin the version when the following conditions apply:
+ The breaking change in the new version does not affect how you use the package.
+ You need a fast, low-risk fix to unblock a release.
+ The maintainer has announced a compatibility shim for the next minor release.

Upgrade the version when the following conditions apply:
+ The pinned version has known security vulnerabilities.
+ The test suite of your target package runs against the newer version.
+ Pinning would force you to fork or patch the dependency yourself.

Pinning is a short-term tactic. Treat every pin as technical debt with a revisit date.

## How do I scope a migration when many packages share the same dependency?
<a name="how-do-i-scope-a-migration-when-many-packages-share-the-same-dependency-.9da8f345-1b26-5e2a-a795-a8ea591879e9"></a>

Start with a breadth-first impact analysis:

1. Identify the direct consumers of the package you are migrating.

1. For each consumer, map its transitive dependents.

1. Score each path by risk. Consider the number of hops, test coverage, and deployment frequency.

1. Group the packages into migration waves. Start with the packages that have the highest test coverage and the fewest hops.

The Interpreting the report section shows this in practice. The depth count tells you which packages sit lowest in the tree, so you know which ones to migrate first.

## Can I use this approach with package managers other than npm?
<a name="can-i-use-this-approach-with-package-managers-other-than-npm-.f1c9eff1-7ce5-5fe3-a3e7-a33e4c8f6d1e"></a>

Yes. The method applies wherever packages declare dependencies on other packages, including Maven, NuGet, Go modules, and Cargo. Impact scoring, wave planning, and bottom-up sequencing do not depend on the ecosystem.

The sample script is specific to Node.js, because it reads `npm` dependency output. For other ecosystems, generate the tree with the native command, such as `mvn dependency:tree`, and apply the same traversal.

## How do I handle npm peer dependency warnings during a migration?
<a name="how-do-i-handle-npm-peer-dependency-warnings-during-a-migration-.3d2004f7-f290-500f-bd32-ff7915b111d1"></a>

When npm reports `ERESOLVE` or peer dependency warnings during migration, it signals that a transitive package requires a different version than the one you declared. Run `npm ls` to identify which paths pull in the conflicting version. Then decide whether to update the transitive consumer first (preferred) or use `--legacy-peer-deps` as a temporary workaround. Treat `--legacy-peer-deps` the same as a pinned version: record a revisit date and resolve the underlying conflict before your next release.
