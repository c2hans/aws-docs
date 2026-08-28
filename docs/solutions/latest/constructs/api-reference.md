---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/api-reference.html
---

# API Reference
<a name="api-reference"></a>

AWS Solutions Constructs (Constructs) is an open-source extension of the AWS Cloud Development Kit (AWS CDK) that provides multi-service, well-architected patterns for quickly defining solutions in code to create predictable and repeatable infrastructure. Constructs’s goal is to accelerates the experience for developers to build solutions of any size using pattern-based definitions for their architecture.

The patterns defined in Constructs are high level, multi-service abstractions of AWS CDK constructs that have default configurations based on well-architected best practices. The library is organized into logical modules using object-oriented techniques to create each architectural pattern model.

The CDK is available in the following languages:
+ JavaScript, TypeScript (Node.js ≥ 10.3.0)
+ Python (Python ≥ 3.6)
+ Java (Java ≥ 1.8)

## Modules
<a name="modules"></a>

AWS Solutions Constructs is organized into several modules. They are named like this:
+  **aws-xxx**: Well-architected pattern package for the indicated services. This package will contain constructs that contain multiple AWS CDK service modules to configure the given pattern.
+  **xxx**: Packages that don’t start "**aws-**" are Constructs core modules that are used to configure best practice defaults for services used within the pattern library. Any function in these modules is internal and not intended to be called by clients directly - changes in implementation may result in the breaking changes to the interfaces on these functions. Some of this functionality has been exposed for safe client use in the aws-constructs-factories.

## Module Contents
<a name="module-contents"></a>

Modules contain the following types:
+  **Patterns** - All higher-level, multi-services constructs in this library.
+  **Other Types** - All non-construct classes, interfaces, structs and enums that exist to support the patterns.

Patterns take a set of (input) properties in their constructor; the set of properties (and which ones are required) can be seen on a pattern’s documentation page.

The pattern’s documentation page also lists the available methods to call and the properties which can be used to retrieve information about the pattern after it has been instantiated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
