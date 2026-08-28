---
source_url: https://docs.aws.amazon.com/codeartifact/latest/ug/swift-name-normalization.html
---

# Swift package name and namespace normalization
<a name="swift-name-normalization"></a>

CodeArtifact normalizes package names and namespaces before storing them, which means the names in CodeArtifact may be different than the ones provided when the package was published.

**Package name and namespace normalization: ** CodeArtifact normalizes Swift package names and namespaces by converting all letters to lowercase.

**Package version normalization: ** CodeArtifact does not normalize Swift package versions. Note that CodeArtifact only supports Semantic Versioning 2.0 version patterns, for more information about Semantic Versioning, see [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

The non-normalized package name and namespace can be used with API and CLI requests because CodeArtifact performs normalization on the inputs for those requests. For example, inputs of `--package myPackage` and `--namespace myScope` would be normalized and return a package that has a normalized package name of `mypackage` and namespace of `myscope`.

**You must use normalized names in ARNs, such as in IAM policies.**

To find the normalized name of a package, use the `aws codeartifact list-packages` command. For more information, see [List package names](list-packages.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
