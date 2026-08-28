---
source_url: https://docs.aws.amazon.com/m2/latest/userguide/assembler-conversion-concepts.html
---

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

# Code conversion concepts
<a name="assembler-conversion-concepts"></a>

To learn how code conversion happens, understanding some key concepts such as Macro handling, Code pages, and CodeBuild is important.

**Topics**
+ [Macro Handling](#conversion-concepts-macro-handling)
+ [Code pages (EBCDIC vs ASCII)](#conversion-concepts-code-pages)
+ [CodeBuild](#conversion-concepts-code-build)

## Macro Handling
<a name="conversion-concepts-macro-handling"></a>

Mainframe Assembler code frequently uses Macros to encapsulate functionality for reuse. Macro behavior is typically determined at application runtime based on parameters passed from an Assembler program. Code conversion provides several mechanisms for expanding Assembler Macros prior to conversion to COBOL.

## Code pages (EBCDIC vs ASCII)
<a name="conversion-concepts-code-pages"></a>

Mainframe Assembler often contain character literals expressed as hexadecimal values corresponding to EBCDIC characters. Code conversion provides a configurable capability to automatically manage character literals in ASCII when emitting COBOL for ASCII environments.

## CodeBuild
<a name="conversion-concepts-code-build"></a>

Code conversion is available through the AWS CodeBuild service. AWS CodeBuild is a build automation tool originally designed as a part of a CI/CD pipeline. In AWS Mainframe Modernization, AWS CodeBuild is used to automate the MCCAC Conversion tool and other tools such as the Rocket Software (formerly Micro Focus) COBOL compiler.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
