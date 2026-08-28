---
source_url: https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-supported-languages.html
---

# Supported languages for Amazon Inspector code security
<a name="code-security-assessments-supported-languages"></a>

 This topic includes the supported languages for Amazon Inspector Code Security.

**Supported languages for SAST**
+  C\# (all versions but .Net 6.0 and later is recommended)
+  C (C11 or earlier)
+  C\+\+ (C\+\+ 17 or earlier)
+  Go (Go 1.18 only)
+  Java (Java 25 or earlier)
+  JavaScript (EMCMAScript 2021 or earlier)
+  JSX (React 17 or earlier)
+  Kotlin (Kotlin 2.0 or earlier)
+  PHP (PHP 8.2 or earlier)
+  Python (Python 3.13 or earlier within the Python 3 series)
+  Ruby (Ruby 2.7 and 3.2 only)
+  Rust
+  Scala (Scala 3.2.2 or earlier)
+  Shell
+  TSX
+  TypeScript (all versions)

**Supported languages for software composition analysis**
+  Go (Go 1.18 only)
+  Java (Java 25 or earlier)
+  JavaScript (EMCMAScript 2021 or earlier)
+  PHP (PHP 8.2 or earlier)
+  Python (Python 3.13 or earlier within the Python 3 series)
+  .Net
+  Ruby (Ruby 2.7 and 3.2 only)
+  Rust

**Note**
 For npm (Node.js) projects, Amazon Inspector code security software composition analysis identifies dependencies from the `package.json` manifest and excludes the `package-lock.json` lockfile from analysis. Dependencies that appear only in `package-lock.json`, including transitive dependencies and the exact versions that it pins, are not evaluated.

**Languages for Infrastructure as Code**
+  AWS CDK (Python and TypeScript)
+  CloudFormation (2010–09–09)
+  Terraform (1.6.2 or earlier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
