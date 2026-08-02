---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants.html
---

# Deploy real-time coding security validation by using an MCP server with Kiro and other coding assistants
<a name="deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants"></a>

*Ivan Girardi and Iker Reina Fuente, Amazon Web Services*

## Summary
<a name="deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants-summary"></a>

This pattern describes how to implement a Model Context Protocol (MCP) server that integrates three industry-standard security scanning tools to provide comprehensive code security analysis. The server enables AI coding assistants (such as Kiro, Amazon Q Developer, and Cline) to automatically scan code snippets and infrastructure as code (IaC) configurations. With these scans, the coding assistants can help identify security vulnerabilities, misconfigurations, and compliance violations.

AI code generators trained on millions of code snippets create a security blind spot—how secure was that training data? This pattern provides real-time security validation during code generation, helping developers identify and understand potential security issues as they code. This approach helps developers address both direct vulnerabilities and inherited risks from dependencies. By bridging the gap between AI efficiency and security compliance, this pattern helps to enable safe adoption of AI-powered development tools.

This pattern helps organizations enhance their development security practices through AI-assisted coding tools, providing continuous security scanning capabilities across multiple programming languages and infrastructure definitions. The solution combines the capabilities of the following tools:
+ Checkov for scanning IaC files, including Terraform, AWS CloudFormation, and Kubernetes manifests
+ Semgrep for analyzing multiple programming languages such as Python, JavaScript, Java, and others
+ Bandit for specialized Python security scanning

Key features of this solution include the following:
+ Delta scanning of new code segments, reducing computational overhead
+ Isolated security tool environments, preventing cross-tool contamination
+ Seamless integration with AI coding assistants (Kiro, Amazon Q Developer, Cline, and others)
+ Real-time security feedback during code generation
+ Customizable scanning rules for organizational compliance

The pattern provides a unified interface for security scanning with standardized response formats, making it easier to integrate security checks into development workflows. The pattern uses Python and the MCP framework to deliver automated security feedback. This approach helps developers identify and address security issues early in the development process while learning about security best practices through detailed findings.

## Prerequisites and limitations
<a name="deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants-prereqs"></a>

**Prerequisites**
+ An active AWS account with access to use Kiro or Amazon Q Developer, if you want to use either of those coding assistants
+ Python version 3.10 or later [installed](https://www.python.org/downloads/)
+ `uv` package manager [installed](https://docs.astral.sh/uv/getting-started/installation/)
+ Familiarity with security scanning tools and concepts
+ Basic understanding of IaC and application security

**Limitations**
+ Bandit scanning is limited to Python files only.
+ Real-time scanning might impact performance for large code bases.
+ Tool-specific limitations are based on supported file formats and languages.
+ Manual review is required to validate security findings.
+ Security scanning results require security expertise for proper interpretation.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**
+ Python version 3.10 or later
+ Checkov version 3.0.0 or later
+ Semgrep version 1.45.0 or later
+ Bandit version 1.7.5 or later
+ MCP[cli] version 1.11.0 or later
+ Pydantic version 1.10.0 or later
+ Loguru version 0.6.0 or later

## Architecture
<a name="deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants-architecture"></a>

The following diagram shows the architecture for this solution.

![AI assistants send code to MCP security scanner server to route to specialized scanners; scan results sent to developer.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/fa623544-4d54-48af-a4e4-9b6a0624e776/images/9c881f95-76d0-40f6-983e-d987fd2097b8.png)

The diagram shows the following workflow:

1. The developer uses AI assistants (for example, Kiro, Cline, Amazon Q Developer, or Roo Code) to generate or analyze code. The AI assistant sends the code for security scanning.

1. The MCP security scanner server processes the request by routing it to the appropriate specialized scanner: Checkov for IaC files, Semgrep for multiple programming languages analysis, or Bandit for Python-specific security scanning.

1. Scanner results with security findings, severity levels, detailed descriptions, and suggested fixes are sent back to the developer through the AI assistant.

1. A continuous feedback loop is established where the developer receives real-time security validation, enabling automated fixes through AI assistants and promoting security best practices during development.

The architecture mitigates the following common security risks:
+ Command injection
+ Prompt injection
+ Path traversal
+ Dependency attacks
+ Resource exhaustion

The architecture mitigates these common security risks by implementing the following best practices:
+ All user and AI model inputs are written to temporary files.
+ No direct inputs are provided to command line interface (CLI) commands.
+ File system access is restricted to temporary directories and files only.
+ Temporary files are automatically cleaned up.
+ Scanning responses are sanitized.
+ Process isolation that restricts process capabilities is enforced.
+ All scanning activities are logged.

**Automation and scale**

The pattern supports automation through the following capabilities:
+ Integration with AI coding assistants for automatic code scanning
+ Standardized API responses for automated processing
+ Configuration through MCP configuration files
+ Support for batch processing of multiple files
+ Scalable scanning across multiple programming languages and IaC formats

The scanning process can be automated through the provided API endpoints:
+ `scan_with_checkov` for IaC scanning
+ `scan_with_semgrep` for multi-language code scanning
+ `scan_with_bandit` for Python-specific scanning
+ `get_supported_formats` for format validation

When extending the scanning tools, follow the design principles and best practices described earlier in this section. Also see [Best practices](#deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants-best-practices).

## Tools
<a name="deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants-tools"></a>

**AWS services**
+ [Kiro](https://aws.amazon.com/documentation-overview/kiro/) is an agentic coding service that works alongside developers to turn prompts into detailed specs, then into working code, docs, and tests. Kiro agents help developers solve challenging problems and automate tasks like generating documentation and unit tests.
+ [Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html) is a generative AI-powered conversational assistant that can help you understand, build, extend, and operate AWS applications.

**Other tools**
+ [Bandit](https://bandit.readthedocs.io/en/latest/) is a specialized Python security scanner tool. It detects common Python security issues like insecure functions, hardcoded secrets, and injection vulnerabilities. Bandit provides detailed confidence and severity ratings.
+ [Checkov](https://github.com/bridgecrewio/checkov) is a static code-analysis tool that checks IaC for security and compliance misconfigurations. In addition, Checkov detects compliance violations and security best practices.
+ [Cline](https://cline.bot/) is an AI-powered coding assistant that runs in VS Code.
+ [Loguru](https://loguru.readthedocs.io/en/stable/) is a data validation library for Python.
+ [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) is an open source framework for building AI-assisted development tools.
+ [Pydantic](https://docs.pydantic.dev/latest/) is a data validation library for Python.
+ [Semgrep](https://semgrep.dev/docs/introduction) analyzes source code for security vulnerabilities and bugs. It supports multiple programming languages. Semgrep uses security-focused rulesets for comprehensive analysis. It provides detailed confidence and severity ratings.

**Code repository**

The code for this pattern is available in the GitHub [MCP Security Scanner: Real-Time Protection for AI Code Assistants](https://github.com/aws-samples/sample-mcp-security-scanner) repository. The repository includes the MCP server implementation, details on the MCP configuration for Kiro, Amazon Q Developer, Cline and others, configuration examples, and testing utilities.

The repository structure includes:
+ `security_scanner_mcp_server/` - Main server implementation
+ `docs/` - Documentation and demo materials
+ `tests/` - Test files
+ `mcp-config-example.json` - Example MCP configuration
+ `requirements.txt` - Project dependencies

## Best practices
<a name="deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants-best-practices"></a>

**Security scanning implementation**
+ Review security findings to validate and prioritize issues.
+ Keep scanning tools (Checkov, Semgrep, and Bandit) updated to latest versions.
+ Use this pattern’s MCP security tool in conjunction with other security measures and tools.
+ Update security rule sets and policies regularly.

**Configuration management**
+ Use the MCP configuration files in the official version control source.
+ Document custom rules and configurations.

**Integration**
+ Integrate security scanning early in the development cycle.
+ Set up automated scanning in pre-commit hooks or continuous integration and continuous deployment (CI/CD) pipelines.
+ Configure appropriate severity thresholds for your environment.
+ Establish clear procedures for handling security findings.

**Operational considerations**
+ Monitor scanning performance and resource usage.
+ Implement proper error handling and logging.
+ Maintain documentation of custom configurations.
+ Establish a process for reviewing and updating security rules.

Also, keep in mind the following best practices:
+ Always validate security findings in your specific context.
+ Keep security tools and dependencies up to date.
+ Use multiple security tools for comprehensive coverage.
+ Follow security best practices in your development process.

## Epics
<a name="deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants-epics"></a>

### (Kiro users) Set up the MCP security scanner server
<a name="kiro-users-set-up-the-mcp-security-scanner-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure MCP settings. | You can edit the configuration files in Kiro either by (Option 1) manually locating the configuration files or (Option 2) by using the Kiro IDE.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants.html)<pre>{<br />  "mcpServers": {<br />    "security-scanner": {<br />      "command": "uvx",<br />      "args": [<br />        "--from",<br />        "git+https://github.com/aws-samples/sample-mcp-security-scanner.git@main",<br />        "security_scanner_mcp_server"<br />      ],<br />      "env": {<br />        "FASTMCP_LOG_LEVEL": "ERROR"<br />      },<br />      "disabled": false,<br />      "autoApprove": []<br />    }<br />  }<br />}</pre> | App developer |

### (Amazon Q Developer users) Set up the MCP security scanner server
<a name="qdevlong-users-set-up-the-mcp-security-scanner-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure MCP settings. | To configure the MCP settings manually, use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants.html)<pre>{<br />  "mcpServers": {<br />    "security-scanner": {<br />      "command": "uvx",<br />      "args": [<br />        "--from",<br />        "git+https://github.com/aws-samples/sample-mcp-security-scanner.git@main",<br />        "security_scanner_mcp_server"<br />      ],<br />      "env": {<br />        "FASTMCP_LOG_LEVEL": "ERROR"<br />      }<br />    }<br />  }<br />}</pre> | App developer |

### (Cline users) Set up the MCP security scanner server
<a name="cline-users-set-up-the-mcp-security-scanner-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure MCP settings. | To configure the MCP settings manually, use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants.html)<pre>{<br />  "mcpServers": {<br />    "security-scanner": {<br />      "command": "uvx",<br />      "args": [<br />        "--from",<br />        "git+https://github.com/aws-samples/sample-mcp-security-scanner.git@main",<br />        "security_scanner_mcp_server"<br />      ],<br />      "env": {<br />        "FASTMCP_LOG_LEVEL": "ERROR"<br />      },<br />      "disabled": false,<br />      "autoApprove": []<br />    }<br />  }<br />}</pre> | App developer |

### Example of code analysis using Python and Bandit
<a name="example-of-code-analysis-using-python-and-bandit"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Perform code analysis. | To perform code analysis by using Python and Bandit, use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants.html) | App developer |

### Example of code analysis using Terraform and Checkov
<a name="example-of-code-analysis-using-terraform-and-checkov"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Perform code analysis. | To perform code analysis by using Terraform and Checkov, use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants.html) | App developer |

### Example of advanced scanning capabilities
<a name="example-of-advanced-scanning-capabilities"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Perform targeted scanning. | Following are examples of requests that you can use to perform a targeted scan:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants.html) | App developer |
| Use security scanning with code generation. | To resolve security findings by using code generation loops, use the following steps (this example uses Kiro as the coding assistant):[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants.html) | App developer |

## Troubleshooting
<a name="deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Environment setup issues | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants.html) |
| Scanner issues | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants.html) |
| Integration problems | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants.html) |
| Additional support | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants.html) |

## Related resources
<a name="deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants-resources"></a>

**AWS documentation**
+ [Infrastructure as code](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html) (AWS Whitepaper *Introduction to DevOps on AWS*)

**Other AWS resources**
+ [Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/)

**Other resources**
+ [Bandit documentation](https://aws.amazon.com/architecture/security-identity-compliance/)
+ [Checkov documentation](https://aws.amazon.com/architecture/security-identity-compliance/)
+ [Model Context Protocol (MCP) documentation](https://aws.amazon.com/architecture/security-identity-compliance/)
+ [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) (OWASP Foundation website)
+ [Semgrep documentation](https://aws.amazon.com/architecture/security-identity-compliance/)

## Additional information
<a name="deploy-real-time-coding-security-validation-by-using-an-mcp-server-with-kiro-and-other-coding-assistants-additional"></a>

**Example MCP configuration with auto approved enabled**

Without `autoApprove` configured, the user must grant approval to send the code to the MCP security server for scanning. When `autoApprove` is configured, the code assistant is allowed to invoke the tools without user approval. These tools run locally on the machine, no data is sent out, and only a code scan is performed.

The following configuration enables automatic execution of all security scanning functions:

```
{
  "mcpServers": {
    "security-scanner": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/aws-samples/sample-mcp-security-scanner.git@main",
        "security_scanner_mcp_server"
      ],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": [
        "scan_with_checkov",
        "scan_with_semgrep",
        "scan_with_bandit",
        "get_supported_formats"
      ]
    }
  }
}
```

To enable debug logging, set `"FASTMCP_LOG_LEVEL"` to `"DEBUG"`.

**File formats supported by security scanning tools**

Each security scanning tool in this solution supports the following file formats:

*Checkov (IaC)*
+ Terraform – .tf, .tfvars, .tfstate
+ CloudFormation – .yaml, .yml, .json, .template
+ Kubernetes – .yaml, .yml
+ Dockerfile – Dockerfile
+ ARM – .json (Azure Resource Manager)
+ Bicep – .bicep
+ Serverless – .yml, .yaml
+ Helm – .yaml, .yml, .tpl
+ GitHub Actions – .yml, .yaml
+ GitLab\_ci – .yml, .yaml
+ Ansible – .yml, .yaml

*Semgrep (Source code)*
+ Python – .py
+ JavaScript – .js
+ TypeScript – .ts
+ Java – .java
+ Go – .go
+ C – .c
+ C\+\+ – .cpp
+ C\# – .cs
+ Ruby – .rb
+ PHP – .php
+ Scala – .scala
+ Kotlin – .kt
+ Rust – .rs

*Bandit (Python only)*
+ Python – .py

**Demos**

For code scanning, try the following sample prompts with your AI assistant:
+ "Scan the current script and tell me the results."
+ "Scan lines 20–60 and tell me the results."
+ "Scan this Amazon DynamoDB table resource and tell me the result."

For more information, see this [code scanning demo](https://github.com/aws-samples/sample-mcp-security-scanner/blob/main/docs/demo_code_scan.gif) in this pattern’s GitHub repository.

To generate secure code, try the following sample prompts:
+ "Generate a Terraform configuration to create a DynamoDB table with encryption enabled and scan it for security issues."
+ "Create a Python Lambda function that writes to DynamoDB and scan it for vulnerabilities."
+ "Generate a CloudFormation template for an S3 bucket with proper security settings and verify it passes security checks."
+ "Write a Python script to query DynamoDB with pagination and scan for security best practices."
+ "Create a Kubernetes deployment manifest for a microservice with security hardening and validate it."

For more information, see this [code generation with security scanning](https://github.com/aws-samples/sample-mcp-security-scanner/blob/main/docs/demo_code_generation.gif) demo in this pattern’s GitHub repository.
