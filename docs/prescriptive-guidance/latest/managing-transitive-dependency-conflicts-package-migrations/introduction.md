---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/managing-transitive-dependency-conflicts-package-migrations/introduction.html
---

# Managing transitive dependency conflicts during package migrations
<a name="introduction"></a>

*Tom Ron, David Guardiola, Mike Kight, and Anisha Salunkhe, Amazon Web Services*

Dependency migration in distributed systems requires careful sequencing. When a foundational package undergoes a major version change that breaks backward compatibility, all packages in the dependency tree must be updated in the correct order. If transitive dependencies are not updated in the proper sequence, applications fail to build. This guide provides a systematic approach to identifying and resolving these conflicts using breadth-first search (BFS) methodology.

## Intended audience
<a name="intended-audience"></a>

This guide targets software engineers, technical leads, and engineering managers who plan package migrations in distributed systems.

Readers should have the following skills:
+ Working knowledge of how a build system resolves direct and transitive dependencies
+ Experience with a package manager such as `npm`, Maven, NuGet, Go modules, or Cargo
+ Comfort running command line tools and reading their output

## Objectives
<a name="objectives"></a>

This guide contributes to the following outcomes:
+ **Reduced migration planning time**: Teams derive a migration sequence from tool output instead of inspecting dependency trees by hand. Planning time drops without sacrificing productivity or quality.
+ **Fewer version migration errors**: Teams migrate shared dependencies before the packages that consume them. This removes the most common cause of failed migration builds.

## Overview
<a name="overview"></a>

Transitive dependencies, indirect dependencies inherited through other packages, create complex relationship chains that are not always visible in project configuration files. During a major version migration, these hidden relationships can block progress when lower-level packages have not yet been updated to support the new version.

Build systems manage two fundamental categories of dependencies that determine how packages interact and compile together.

### Dependency types
<a name="dependency-types.648781d9-b436-5a7c-8bef-e77988af9da6"></a>
+ **Direct dependency**: When Package A relies on Package B, Package B is a direct dependency of Package A. Direct dependencies are declared explicitly in project configuration files such as `package.json` or `pom.xml`.
+ **Transitive dependency**: When Package B relies on Package C, and Package A relies on Package B, Package C becomes a dependency of Package A. This indirect relationship makes Package C a transitive dependency of Package A.

![Package A depends directly on Package B and transitively on Package C through Package B.](http://docs.aws.amazon.com/prescriptive-guidance/latest/managing-transitive-dependency-conflicts-package-migrations/images/guide-img/e09a1ad7-c54f-4a20-b180-a86ef69032e6/images/c11ff0af-6a90-49f4-903a-60f3efa2831b.png)

## Transitive dependency conflicts
<a name="transitive-dependency-conflicts"></a>

In distributed software systems, shared components frequently rely on third-party core packages. Using reusable components and third-party packages accelerates innovation and reduces development time, but introduces complexity in dependency management.

### Shared dependencies in distributed systems
<a name="shared-dependencies-in-distributed-systems.fda112e9-89c7-555c-a040-fbc47016b009"></a>

It is common to encounter shared dependencies between top-level components and reusable components within a system. Consider the following example:

Your organization has adopted a third-party UI/UX library called Party-UI. Party-UI is a direct dependency for a UI/UX component named Top-Level-Module, which you are developing to introduce a new feature.

As part of implementing this feature, you use a commonly employed package called Shared-Module, which also relies on Party-UI. Party-UI now becomes both a direct dependency of Top-Level-Module and a transitive dependency through Shared-Module.

### Dependency structure
<a name="dependency-structure.09ca2b14-0a21-5e24-96e3-c20b5fe0534e"></a>

The following diagram shows Party-UI as both a direct dependency of Top-Level-Module and a transitive dependency through Shared-Module.

![Top-Level-Module depends on Party-UI directly and on Shared-Module, which also depends on Party-UI.](http://docs.aws.amazon.com/prescriptive-guidance/latest/managing-transitive-dependency-conflicts-package-migrations/images/guide-img/e09a1ad7-c54f-4a20-b180-a86ef69032e6/images/b1298fc0-1911-446e-8b46-fa4e2c7735d0.png)

### When version conflicts arise
<a name="when-version-conflicts-arise.aa14b617-1f4d-5989-9a35-bad9fed8d070"></a>

When the version of a direct dependency is incompatible with the version of a transitive dependency, the build fails. In npm, this class of mismatch often surfaces as a peer dependency conflict.

### The migration attempt
<a name="the-migration-attempt.2ec24c77-28cf-5ac8-8e37-0be80aafe8dd"></a>

Party-UI releases version 3.0.0. It deprecates components, changes namespaces, and drops compatibility with the 2.x line. Your team updates Top-Level-Module for the new APIs. The build still fails, and the errors come from files in Shared-Module.

### Why the build fails
<a name="why-the-build-fails.0dafb6a9-98e3-57d8-8e35-1b27123bc30b"></a>

When Top-Level-Module declares Party-UI 3.0.0, the build system resolves that version for the whole project. Shared-Module sits in the same dependency tree, so the build system compiles it against 3.0.0 as well.

Shared-Module was written for Party-UI 2.5.8. Compiling it against 3.0.0 produces API mismatches, missing components, and changed method signatures. The compilation fails.

Top-Level-Module cannot move to Party-UI 3.0.0 until Shared-Module moves first.

### The solution
<a name="the-solution.c7c1d516-a84e-5e54-b941-04940f784d34"></a>

Map the relationships between packages before you migrate anything. A breadth-first search of the dependency tree produces that map. It identifies which packages sit below your target, so you update lower-level dependencies first and avoid the build failure above.

## When conflicts do not cause errors
<a name="transitive-dependency-conflicts-issues"></a>

Transitive dependency conflicts do not always result in errors. Differences between patch versions or minor iterations are often minimal enough to avoid triggering conflicts. For example, Party-UI 2.5.0 and Party-UI 2.5.8 exhibit only slight alterations between them and maintain backward compatibility.

Errors from transitive dependency conflicts typically occur during major version transitions. Party-UI 2.0 might feature components that are deprecated in Party-UI 3.0. Packages built on Party-UI 2.0 may encounter compatibility issues when forced to operate on Party-UI 3.0.

![Packages built on Party-UI 2.0 fail against Party-UI 3.0 because components are deprecated.](http://docs.aws.amazon.com/prescriptive-guidance/latest/managing-transitive-dependency-conflicts-package-migrations/images/guide-img/e09a1ad7-c54f-4a20-b180-a86ef69032e6/images/7003a7b9-1e62-476c-bfae-0ce57b7a9fe9.png)

## How transitive dependency conflicts cause build errors
<a name="how-transitive-dependency-conflicts-cause-build-errors"></a>

Transitive dependency conflicts can cause build errors through both configured dependencies and build-time dependencies.

### Configured dependencies
<a name="configured-dependencies.5b27c98b-8164-5a32-97a9-b6b80ffe5979"></a>

Configured dependencies are those you explicitly specify in your project's configuration files or build scripts.

**Version mismatch**: You pin a direct dependency to a specific version, and that dependency requires a conflicting version of a transitive dependency. For example, you declare Dependency A version 1.0, and Dependency A requires Transitive Dependency X version 2.0.

**Incompatibility**: You select a direct dependency that does not work with the resolved versions of its transitive dependencies. The result is compilation errors, runtime errors, or unexpected behavior.

### Build-time dependencies
<a name="build-time-dependencies.28036e8e-eb01-5d20-9207-107c0494d5f7"></a>

Build-time dependencies are those your build tool relies on during compilation.

**Conflict resolution**: Different parts of your project require different versions of the same transitive dependency. The build tool must pick one version. If it picks an incompatible version, or cannot resolve the conflict, the build fails.

**Build process failures**: The build tool fails to download, install, or link a required dependency because of the conflict. The project never compiles.

![Configured dependencies and build-time dependencies both produce build errors when transitive versions conflict.](http://docs.aws.amazon.com/prescriptive-guidance/latest/managing-transitive-dependency-conflicts-package-migrations/images/guide-img/e09a1ad7-c54f-4a20-b180-a86ef69032e6/images/c2f43728-87cf-47a5-884a-6e722e9f99c5.png)

## Using breadth-first search to sequence a migration
<a name="breadth-first-search-roadmap-to-avoid-dependency-conflicts-in-a-migration"></a>

Avoiding dependency conflicts during a migration using breadth-first search (BFS) is a systematic approach to identify and address potential issues in your project's dependencies. BFS helps you traverse the dependency tree layer by layer, starting from the root package being migrated and expanding outward.

### Step 1: Understand your project's dependency graph
<a name="step-1--understand-your-project9999999999999999apos-s-dependency-graph.f1d40dbc-06c5-5b24-bca9-402308b9750a"></a>

Identify every direct and transitive dependency, its version, and its relationships. Use `npm ls`, `mvn dependency:tree`, or the equivalent inspection command for your package manager.

### Step 2: Define your migration goal
<a name="step-2--define-your-migration-goal.9f0a3280-0a2f-5ca7-afab-cca2756d7ae3"></a>

State the goal precisely. Record the target package, the version you are moving from, and the version you are moving to.

### Step 3: Start from a known good state
<a name="step-3--start-from-a-known-good-state.61d69e5e-3085-5491-bf01-2a95b8aafd65"></a>

Confirm that the project builds before you change anything. Create a branch or snapshot so you can return to the working state.

### Step 4: Traverse the graph with breadth-first search
<a name="step-4--traverse-the-graph-with-breadth-first-search.70bffc6b-ed83-506f-8dca-7e036a90e970"></a>

Apply the following traversal:

1. Start with your project's direct dependencies.

1. For each direct dependency, read its own dependencies.

1. Add those dependencies to a queue for processing.

1. Process the queue, and record every package that depends on the target package and the version it uses.

### Step 5: Detect and resolve conflicts
<a name="step-5--detect-and-resolve-conflicts.4b676234-7892-5194-88c6-36a2cdf9de39"></a>

Look for these conflicts during the traversal:
+ **Version conflicts**: A package depends on a version of the target that your goal version replaces.
+ **Compatibility issues**: The new version of the target introduces breaking changes.
+ **Deprecated dependencies**: A package in the path is no longer maintained or supported.

For each conflict, take one of these actions:
+ Update the dependency to a compatible version.
+ Replace the dependency with an alternative that meets your requirements.
+ Change your code to work with the updated dependency.

### Step 6: Automate conflict detection
<a name="step-6--automate-conflict-detection.85097712-7e60-5e9f-9e2d-f6b19b709554"></a>

Run a script or dependency analysis tool instead of reading trees by hand. Automation removes transcription errors and makes the traversal repeatable.

### Step 7: Iterate and test
<a name="step-7--iterate-and-test.5a0ea25e-2aee-5eac-83a4-d29bdee93203"></a>

After you resolve conflicts, test the affected packages. Run unit tests, integration tests, and targeted manual checks to confirm the migration introduced no regressions.

### Step 8: Document and communicate
<a name="step-8--document-and-communicate.7df7c881-f636-5965-9f83-cf8ef5085878"></a>

Record the dependency updates you made and the order you made them in. Share the roadmap with the teams that own packages in the tree.

### Step 9: Prepare a rollback plan
<a name="step-9--prepare-a-rollback-plan.eb9a4abb-8b11-5840-9861-347cbd2dd2cc"></a>

Define how to return to the previous working state. You need this if a migrated package exposes a defect you cannot fix quickly.

### Step 10: Monitor and maintain
<a name="step-10--monitor-and-maintain.c2f38ea5-cb3a-5c21-869f-2c1f393d824e"></a>

Review the dependency graph after the migration. Repeat the analysis when the target package publishes its next major version.

### Migration example
<a name="migration-example.d6b98369-47cf-520f-a592-21725edf1abc"></a>

![Migrating Top-Level-Module to Party-UI 3.0.0 requires migrating Shared-Module first.](http://docs.aws.amazon.com/prescriptive-guidance/latest/managing-transitive-dependency-conflicts-package-migrations/images/guide-img/e09a1ad7-c54f-4a20-b180-a86ef69032e6/images/59b5bb15-5c11-4d09-b836-4db8fee5eff4.png)

**Goal**: Migrate Top-Level-Module 1.0 to a 2.0 version that uses Party-UI 3.0.0.

1. Starting at the lowest level of the dependency tree, migrate the Party-UI usage in Shared-Module 1.0 to Party-UI 3.0.0.

1. Publish Shared-Module 2.0 to mark the version that uses Party-UI 3.0.0.

1. In Top-Level-Module, replace Party-UI 2.5.8 with Party-UI 3.0.0, and Shared-Module 1.0 with Shared-Module 2.0.

## Transitive dependency analyzer
<a name="transitive-dependency-analyzer"></a>

The [Transitive Dependency Analyzer for Node.js Projects](https://github.com/aws-samples/sample-transitive-dependency-analyzer) is a Python command line script that applies the breadth-first traversal described earlier. It reads the dependency tree of a Node.js project and reports every package that depends on a target package, along with the version each one uses.

### What the tool reports
<a name="what-the-tool-reports.5ed537ca-fd54-513a-b850-851b8c96d116"></a>

The script writes a text report. Each occurrence in the report contains the following fields.

|
|
| Field | Meaning |
| --- |--- |
| Parent Package | The package that depends on the target package |
| Depth Count | How far the parent package sits from the root of the tree. A higher count means the package sits lower in the tree. |
| Breadth Count | The order in which the traversal discovered the package |
| Version | The version of the target package that the parent package depends on |

Use the depth count to build the migration sequence. The script reports occurrences and versions. You compare those versions against your target version to decide which packages need work.

### Prerequisites and setup
<a name="prerequisites-and-setup.551166fa-15cc-5d05-b8fe-873ddc0b05c1"></a>

The script requires Python 3.8 or later, Node.js and `npm` on your `PATH`, and a Node.js project that contains a `package.json` file. It uses only the Python standard library, so no package installation is needed. Clone the repository and follow the installation instructions in the [repository README](https://github.com/aws-samples/sample-transitive-dependency-analyzer).

### Running the script
<a name="running-the-script.937cb65c-d9f5-5073-8a12-b5e4ee03e6c4"></a>

Run the script with two required arguments. Set `--target` to the dependency you are searching for in the dependency tree. Set `--path` to the directory of the project you are analyzing.

```
python tree_traverse.py --target [TARGET_NAME] --path [PROJECT_PATH]
```

The script writes the report to `<target>_dependency_analysis.txt` unless you set an output path with `--output`. Add `--verbose` for detailed logging. Because the script has no third-party dependencies, you can also run it as a step in a build pipeline.

### Interpreting the report
<a name="interpreting-the-report.07885888-9093-5db3-85db-91dcbff25234"></a>

The report identifies every package in the dependency tree that depends on the target package. Those parent packages are the candidates for your migration roadmap.

The following output comes from a customer migration, with package names obscured. The customer needed to move a top-level component to Transitive-Dependency-Component v4.0.0. The analysis shows which packages still depended on v3.0.0.

```
Dependency occurrences

Parent Package: node
Depth Count : 1
    currently depends on version 3.0.0 of Transitive-Dependency-Component

Parent Package: UI-Module-Card
Depth Count : 2
    currently depends on version 3.0.0 of Transitive-Dependency-Component

Parent Package: UI-Components-Card
Depth Count : 2
    currently depends on version 3.0.0 of Transitive-Dependency-Component

Parent Package: UI-Module-Container
Depth Count : 2
    currently depends on version 3.0.0 of Transitive-Dependency-Component

Parent Package: UI-Components-Order
Depth Count : 2
    currently depends on version 3.0.0 of Transitive-Dependency-Component

Parent Package: UI-Module-Shell
Depth Count : 2
    currently depends on version 3.0.0 of Transitive-Dependency-Component

Parent Package: UI-Components-Dependency
Depth Count : 3
    currently depends on version 3.0.0 of Transitive-Dependency-Component

Parent Package: UI-Components-Workflow
Depth Count : 2
    currently depends on version 3.0.0 of Transitive-Dependency-Component

Parent Package: UI-Widget-Common
Depth Count : 2
    currently depends on version 3.0.0 of Transitive-Dependency-Component
```

**Note**
The analyzed package appears as its own entry at depth 0, labeled `root`. The earlier release that produced the example above labeled it `node`.

Build the roadmap from the report as follows:

1. Identify the parent packages that depend on the version you are replacing.

1. Sort those packages by depth count, highest first. Packages lower in the tree have a higher depth count.

1. Migrate from the bottom of the tree upward. Place the packages at the greatest depth first in the roadmap, and the packages at depth 1 last.

1. Migrate the package you ran the analysis against after every package in the report is migrated.

### Reanalyze after each pass
<a name="reanalyze-after-each-pass.c3e3a914-4b16-53c7-bcbe-7f9632e47a26"></a>

Dependency analysis is iterative on large projects. Rerun the script after each migration wave. A clean report confirms that no package in the tree still depends on the version you are replacing.
