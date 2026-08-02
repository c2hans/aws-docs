---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/versioning.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# AWS CDK versioning
<a name="versioning"></a>

This topic provides reference information on how the AWS Cloud Development Kit (AWS CDK) handles versioning.

Version numbers consist of three numeric version parts: *major*.*minor*.*patch*, and broadly follow [semantic versioning](https://semver.org) principles with a few caveats described in [AWS Construct Library semantic versioning clarifications](https://docs.aws.amazon.com/cdk/v2/guide/versioning.html#aws-construct-lib-semver). This means that breaking changes to APIs we consider stable are limited to major releases.

Minor and patch releases are backward compatible. The code written in a previous version with the same major version can be upgraded to a newer version within the same major version. It will continue to build and run, producing a functionally equivalent result. For some advanced use cases, small changes to your code will be required as noted in the next topic.

## AWS CDK Toolkit compatibility
<a name="cdk-toolkit-versioning"></a>

Each version of the main AWS Construct Library (`aws-cdk-lib`) is compatible with the AWS CDK Toolkit CLI (`aws-cdk-cli`) and Toolkit Library (`@aws-cdk/toolkit-lib`) version that was current at the time of the AWS Construct Library’s release. It is also compatible with any newer version of the AWS CDK Toolkit. Each version of the AWS Construct Library maintains this compatibility until the library’s *End of Life* date. Therefore, as long as you’re using a supported AWS Construct Library version, it is always safe to upgrade your AWS CDK Toolkit version.

Each version of the AWS Construct Library might also work with AWS CDK Toolkit versions older than the version that was current at the time of the AWS Construct Library’s release. However, this is not guaranteed. Compatibility depends on the AWS Construct Library’s cloud assembly schema version. The AWS CDK generates a cloud assembly during synthesis and the AWS CDK Toolkit consumes it for deployment. The schema that defines the format of the cloud assembly is strictly specified and versioned. Therefore, an older version of the AWS CDK Toolkit would need to support the cloud assembly schema version of the AWS Construct Library for them to be compatible.

When the cloud assembly version required by the AWS Construct Library is not compatible with the version supported by the AWS CDK Toolkit, you receive an error message like the following:

```
Cloud assembly schema version mismatch: Maximum schema version supported is 3.0.0, but found 4.0.0.
    Please upgrade your CLI in order to interact with this app.
```

To resolve this error, update the AWS CDK Toolkit to a version compatible with the required cloud assembly version, or to the latest available version. The alternative (downgrading the AWS Construct Library modules your app uses) is generally not recommended.

**Note**
For more information on the exact combinations of versions that work together, see the [compatibility table](https://github.com/aws/aws-cdk-cli/blob/main/COMPATIBILITY.md) in the *aws-cdk-cli GitHub repository*.

## AWS Construct Library versioning
<a name="aws-construct-lib-stability"></a>

The modules in the AWS Construct Library move through various stages as they are developed from concept to mature API. Different stages offer varying degrees of API stability in subsequent versions of the AWS CDK.

Except for scenarios where the caveats documented in the next topic apply, APIs in the main AWS Construct Library (`aws-cdk-lib`) are stable, and the library broadly follows semantic versioning principles. The library includes AWS CloudFormation (L1) constructs for all AWS services, which are auto-generated from [CloudFormation resource provider schemas](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/resource-type-schemas.html) and might sometimes include backward incompatible updates. It also includes higher-level (L2 and L3) constructs and the core CDK classes like `App` and `Stack`, which are all stable. APIs will not be removed from this package (though they might be deprecated) until the next major release of the CDK. When a breaking change is required to a stable API, an entirely new API will be added.

New APIs under development for a service already incorporated in `aws-cdk-lib` are identified using a `Beta<N>` suffix, where `N` starts at 1 and is incremented with each breaking change to the new API. `Beta<N>` APIs are never removed, only deprecated, so your existing app continues to work with newer versions of `aws-cdk-lib`. When the API is deemed stable, a new API without the `Beta<N>` suffix is added.

When higher-level (L2 or L3) APIs begin to be developed for an AWS service that previously had only L1 APIs, those APIs are initially distributed in a separate package. The name of such a package has an "Alpha" suffix, and its version matches the first version of `aws-cdk-lib` it is compatible with, with an `alpha` sub-version. When the module supports the intended use cases, its APIs are added to `aws-cdk-lib`.

## AWS Construct Library semantic versioning clarifications
<a name="aws-construct-lib-semver"></a>

While the AWS Construct Library broadly follows semantic versioning principles, there are some important caveats specific to our implementation. In general the AWS Construct Library maintains stability for API consumers, but sometimes adds additional burdens to construct authors to enable the necessary evolution of the framework.
+  **Security impacting changes**

  To meet our security bar, we might be required to change APIs in backward incompatible ways or remove them entirely. This prevents affected APIs from being used and forces implementations to be updated.
+  **Features are described by intent**

  We aim to minimize unexpected changes, but will favor *intent over implementation stability*. The AWS Construct Library does not guarantee that constructs always synthesize to the exact same CloudFormation template or use the exact same set of resources. This especially applies to higher-level constructs, where the same goal can often be achieved in different ways.
+  **Implementing Interfaces and Abstract Classes**

  Interfaces and abstract classes in the AWS Construct Library are stable for **consumers**, but not for **implementors**. This means that you can safely rely on interfaces like `s3.IBucket` to provide at least the same functionality as at the time (AWS Construct Library version) that you started consuming the interface or abstract class. However, periodically, new (abstract) members will be added to interfaces and abstract classes. For anyone **implementing** them, this creates an additional implementation burden to consider when upgrading, since the implementation wouldn’t be implementing the new members yet. Strictly treating additions to interfaces and abstract classes for implementors as breaking changes would unduly limit the evolvability of the AWS Construct Library. In most cases, implementors should prefer to extend concrete classes like `s3.Bucket`.
+  **L1 constructs, generated code, and other APIs marked as external**

  Parts of the AWS Construct Library are generated from data sources coming directly from AWS services. To keep these APIs aligned with reality, generated code might contain backward incompatible changes. Most of the time, data sources are updated to correctly reflect reality and rectify incorrect representation. *Your IDE’s IntelliSense will display external APIs with the `@stability — external` annotation.*
+  **Semantically correct programs only**

  We ensure that correct programs continue to work with newer versions. Programs that are formally incorrect but happen to work due to implementation details are not covered. For example, if your program relies on [TypeScript’s structural typing rules](https://www.typescriptlang.org/docs/handbook/type-compatibility.html) to pass unexpected object types, or synthesizes successfully but produces a CloudFormation template that fails to deploy, we may introduce changes that cause these programs to fail without considering them breaking changes.
+  **Specific language bindings**

  Language bindings can contain backward incompatible changes in a very limited number of situations. These are caused by upstream type changes that are backward compatible in other supported languages. These types changes are allowed, as doing otherwise would severely limit the evolvability of the library.

  The following list describes all known instances:
  +  **Golang - Changing from typed slice to any slice: ** A list of a single type is changing to a list of multiple types (union types in TypeScript). In `Go`, these are typed as a slice of any (`*[]any`). Due to Go’s typing assignment rules, changing from `*[]string ` to `` is not an automatic conversion. Therefore, this type widening requires consumer code to change. See [Working with any slice](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-go.html#go-cdk-idioms) for strategies.

## Language binding stability
<a name="aws-construct-lib-versioning-binding"></a>

Over time, we might add support to the AWS CDK for additional programming languages. Although the API described in all the languages is the same, the way that API is expressed varies by language and might change as the language support evolves. For this reason, language bindings are deemed experimental for a time until they are considered ready for production use.

| Language | Stability |
| --- | --- |
| TypeScript | Stable |
| JavaScript | Stable |
| Python | Stable |
| Java | Stable |
| C\#/.NET | Stable |
| Go | Stable |
