---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/mcp-security-scanner-kiro.html
---

# Deploy real-time coding security validation by using an MCP server with Kiro
<a name="mcp-security-scanner-kiro"></a>

*Ivan Girardi and Iker Reina Fuente, Amazon Web Services*

## Summary
<a name="mcp-security-scanner-kiro-summary"></a>

This pattern describes how to implement a Model Context Protocol (MCP) server that integrates three widely used security scanning tools to provide code security analysis. The server enables AI coding assistants (such as Kiro, Amazon Q Developer, and Cline) to automatically scan code snippets and infrastructure as code (IaC) configurations. With these scans, the coding assistants can help identify security vulnerabilities, misconfigurations, and compliance violations.

AI code generators are trained on large volumes of code whose security quality can vary. This pattern provides real-time security validation during code generation, helping developers identify and understand potential security issues as they code. This approach also helps developers address both direct vulnerabilities and risks inherited from dependencies. By combining AI efficiency with security checks, this pattern supports the adoption of AI-powered development tools.

This pattern helps organizations enhance their development security practices through AI-assisted coding tools, providing on-demand security scanning across multiple programming languages and infrastructure definitions. The solution combines the capabilities of the following tools:
+ Checkov for scanning IaC files, including Terraform, AWS CloudFormation, and Kubernetes manifests
+ Semgrep for analyzing multiple programming languages such as Python, JavaScript, Java, and others
+ Bandit for specialized Python security scanning

Key features of this solution include the following:
+ Delta scanning of new code segments, reducing computational overhead
+ Isolated security tool environments, preventing cross-tool contamination
+ Seamless integration with AI coding assistants (Kiro, Amazon Q Developer, Cline, and others)
+ Real-time security feedback during code generation
+ Customizable scanning rules for organizational compliance

This pattern provides a unified interface for security scanning with standardized response formats, making it easier to integrate security checks into development workflows. It uses Python and the MCP framework to deliver automated security feedback. This approach helps developers identify and address security issues early in the development process while they learn about security best practices through detailed findings.

## Prerequisites and limitations
<a name="mcp-security-scanner-kiro-prereqs"></a>

**Prerequisites**
+ An active AWS account with access to use Kiro or Amazon Q Developer, if you want to use either of those coding assistants
+ Python version 3.10 or later [installed](https://www.python.org/downloads/)
+ `uv` package manager [installed](https://docs.astral.sh/uv/getting-started/installation/)
+ Familiarity with security scanning tools and concepts
+ Basic understanding of infrastructure as code (IaC) and application security

**Limitations**
+ Bandit scanning supports Python files only.
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
<a name="mcp-security-scanner-kiro-architecture"></a>

The following diagram shows the architecture for this solution.

![AI assistants send code to MCP security scanner server to route to specialized scanners; scan results sent to developer.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/fa623544-4d54-48af-a4e4-9b6a0624e776/images/9c881f95-76d0-40f6-983e-d987fd2097b8.png)

The diagram shows the following workflow:

1. The developer uses AI assistants (for example, Kiro, Cline, Amazon Q Developer, or Roo Code) to generate or analyze code. The AI assistant sends the code for security scanning.

1. The Model Context Protocol (MCP) security scanner server processes the request by routing it to the appropriate specialized scanner: Checkov for infrastructure as code (IaC) files, Semgrep for analysis of multiple programming languages, or Bandit for Python-specific security scanning.

1. The MCP security scanner server sends scanner results, including security findings, severity levels, detailed descriptions, and suggested fixes, back to the developer through the AI assistant.

1. The developer receives real-time security validation through a continuous feedback loop, which enables automated fixes through AI assistants and promotes security best practices during development.

The architecture mitigates the following common security risks:
+ Command injection
+ Prompt injection
+ Path traversal
+ Dependency attacks
+ Resource exhaustion

The architecture mitigates these common security risks by implementing the following best practices:
+ The server writes all user and AI model inputs to temporary files.
+ The server doesn't provide direct inputs to command line interface (CLI) commands.
+ The server restricts file system access to temporary directories and files only.
+ The server automatically cleans up temporary files.
+ The server sanitizes scanning responses.
+ The server enforces process isolation that restricts process capabilities.
+ The server logs all scanning activities.

**Automation and scale**

The pattern supports automation through the following capabilities:
+ Integration with AI coding assistants for automatic code scanning
+ Standardized API responses for automated processing
+ Configuration through MCP configuration files
+ Support for batch processing of multiple files
+ Scalable scanning across multiple programming languages and IaC formats

You can automate the scanning process through the following API endpoints:
+ `scan_with_checkov` for IaC scanning
+ `scan_with_semgrep` for multi-language code scanning
+ `scan_with_bandit` for Python-specific scanning
+ `get_supported_formats` for format validation

When extending the scanning tools, follow the design principles and best practices described earlier in this section. Also see [Best practices](#mcp-security-scanner-kiro-best-practices).

## Tools
<a name="mcp-security-scanner-kiro-tools"></a>

**AWS services**
+ [Kiro](https://aws.amazon.com/documentation-overview/kiro/) is an agentic coding service that works alongside developers to turn prompts into detailed specs, then into working code, docs, and tests. Kiro agents help developers solve challenging problems and automate tasks like generating documentation and unit tests.
+ [Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html) is a generative AI-powered conversational assistant that can help you understand, build, extend, and operate AWS applications.

**Other tools**
+ [Bandit](https://bandit.readthedocs.io/en/latest/) is a specialized Python security scanner tool. It detects common Python security issues like insecure functions, hardcoded secrets, and injection vulnerabilities. Bandit provides detailed confidence and severity ratings.
+ [Checkov](https://github.com/bridgecrewio/checkov) is a static code-analysis tool that checks infrastructure as code (IaC) for security and compliance misconfigurations.
+ [Cline](https://cline.bot/) is an AI-powered coding assistant that runs in Visual Studio Code.
+ [Loguru](https://loguru.readthedocs.io/en/stable/) is a logging library for Python.
+ [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) is an open source framework for building AI-assisted development tools.
+ [Pydantic](https://docs.pydantic.dev/latest/) is a data validation library for Python.
+ [Semgrep](https://semgrep.dev/docs/introduction) analyzes source code for security vulnerabilities and bugs. It supports multiple programming languages. Semgrep uses security-focused rulesets for analysis. It provides detailed confidence and severity ratings.

**Code repository**

The code for this pattern is available in the GitHub [MCP Security Scanner: Real-Time Protection for AI Code Assistants](https://github.com/aws-samples/sample-mcp-security-scanner) repository. The repository includes the MCP server implementation, details on the MCP configuration for Kiro, Amazon Q Developer, Cline and others, configuration examples, and testing utilities.

The repository structure includes:
+ `security_scanner_mcp_server/` - Main server implementation
+ `docs/` - Documentation and demo materials
+ `tests/` - Test files
+ `mcp-config-example.json` - Example MCP configuration
+ `requirements.txt` - Project dependencies

## Best practices
<a name="mcp-security-scanner-kiro-best-practices"></a>

**Security scanning implementation**
+ Review security findings to validate and prioritize issues.
+ Keep scanning tools (Checkov, Semgrep, and Bandit) updated to the latest versions.
+ Use this pattern’s Model Context Protocol (MCP) security tool with other security measures and tools.
+ Update security rule sets and policies regularly.

**Configuration management**
+ Store the MCP configuration files in your version control repository, and use them from there.
+ Document custom rules and configurations.

**Integration**
+ Integrate security scanning early in the development cycle.
+ Set up automated scanning in pre-commit hooks or continuous integration and continuous deployment (CI/CD) pipelines.
+ Configure severity thresholds that match your organization’s risk tolerance and environment.
+ Establish procedures for triaging and remediating security findings.

**Operational considerations**
+ Monitor scanning performance and resource usage.
+ Implement error handling and logging for scan failures.
+ Establish a process for reviewing and updating security rules.

Follow these additional best practices:
+ Validate security findings in your specific context.
+ Keep dependencies up to date.
+ Use multiple security tools to broaden coverage.
+ Incorporate secure coding practices into your development process.

## Epics
<a name="mcp-security-scanner-kiro-epics"></a>

### (Kiro users) Set up the MCP security scanner server
<a name="kiro-users-set-up-the-mcp-security-scanner-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure MCP settings. | You can edit the configuration files in Kiro either by (Option 1) manually locating the configuration files or (Option 2) by using the Kiro IDE.+ (Option 1) Locate and edit the configuration files manually as follows:Path: `.kiro/settings/mcp.json` (local) or `~/.kiro/settings/mcp.json` (global)<br />+ (Option 2) Modify the configuration files by using the Kiro IDE as follows:Choose the Kiro symbol in the left navigation menu.Navigate to the 'MCP SERVERS' section.Edit the configuration settings. Changes made with the Kiro IDE will be saved to one of these configuration files: `.kiro/settings/mcp.json` (local) or `~/.kiro/settings/mcp.json` (global)<br />+ (Both options) After you complete either Option 1 or Option 2, add the security-scanner configuration `.kiro/settings/mcp.json` (local) or `~/.kiro/settings/mcp.json` (global):<pre>{<br />  "mcpServers": {<br />    "security-scanner": {<br />      "command": "uvx",<br />      "args": [<br />        "--from",<br />        "git+https://github.com/aws-samples/sample-mcp-security-scanner.git@main",<br />        "security_scanner_mcp_server"<br />      ],<br />      "env": {<br />        "FASTMCP_LOG_LEVEL": "ERROR"<br />      },<br />      "disabled": false,<br />      "autoApprove": []<br />    }<br />  }<br />}</pre> | App developer |

### (Amazon Q Developer users) Set up the MCP security scanner server
<a name="qdevlong-users-set-up-the-mcp-security-scanner-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure MCP settings. | To configure the MCP settings manually, use the following steps:1. Edit the MCP configuration file at `~/.aws/amazonq/mcp.json` (global) or `.amazonq/mcp.json` (local).<br />2. Add the following security-scanner configuration `~/.aws/amazonq/mcp.json` (global) or `.amazonq/mcp.json` (local):<pre>{<br />  "mcpServers": {<br />    "security-scanner": {<br />      "command": "uvx",<br />      "args": [<br />        "--from",<br />        "git+https://github.com/aws-samples/sample-mcp-security-scanner.git@main",<br />        "security_scanner_mcp_server"<br />      ],<br />      "env": {<br />        "FASTMCP_LOG_LEVEL": "ERROR"<br />      }<br />    }<br />  }<br />}</pre> | App developer |

### (Cline users) Set up the MCP security scanner server
<a name="cline-users-set-up-the-mcp-security-scanner-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure MCP settings. | To configure the MCP settings manually, use the following steps:1. Choose the extension to open it and then select **MCP Servers**.<br />2. Choose the **Installed** tab and then choose **Configure MCP Servers** to open the `cline_mcp_settings.json` file.<br />3. Add the following security-scanner configuration `cline_mcp_settings.json`:<pre>{<br />  "mcpServers": {<br />    "security-scanner": {<br />      "command": "uvx",<br />      "args": [<br />        "--from",<br />        "git+https://github.com/aws-samples/sample-mcp-security-scanner.git@main",<br />        "security_scanner_mcp_server"<br />      ],<br />      "env": {<br />        "FASTMCP_LOG_LEVEL": "ERROR"<br />      },<br />      "disabled": false,<br />      "autoApprove": []<br />    }<br />  }<br />}</pre> | App developer |

### Example of code analysis using Python and Bandit
<a name="example-of-code-analysis-using-python-and-bandit"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Perform code analysis. | To perform code analysis by using Python and Bandit, use the following steps:1. Create a new Python file named `bandit_test.py` with the following content:<pre>import pickle<br />import yaml<br />import subprocess<br />from flask import Flask, request<br />import hashlib<br /><br />app = Flask(__name__)<br /><br />@app.route("/unsafe_pickle", methods=["POST"])<br />def unsafe_pickle_usage():<br />    data = request.get_data()<br />    return pickle.loads(data)<br /><br />@app.route("/command_injection", methods=["GET"])<br />def command_injection():<br />    command = request.args.get("cmd")<br />    return subprocess.Popen(command, shell=True)<br /><br />def weak_crypto():<br />    password = "secret_password"<br />    return hashlib.md5(password.encode()).hexdigest()<br /><br />PASSWORD = "super_secret_password123"<br /></pre><br />2. Open the coding assistant. Request the following actions in the chat: **Scan current script and tell me the results.** | App developer |

### Example of code analysis using Terraform and Checkov
<a name="example-of-code-analysis-using-terraform-and-checkov"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Perform code analysis. | To perform code analysis by using Terraform and Checkov, use the following steps:1. Create a new Terraform file named `terraform_test.tf` with the following content:<pre>    resource "aws_s3_bucket" "insecure_bucket" {<br />    bucket = "my-insecure-bucket"<br />    acl    = "public-read"<br />}<br /><br />resource "aws_security_group" "wide_open" {<br />    name        = "allow_all"<br />    description = "Allow all inbound traffic"<br /><br />    ingress {<br />        from_port   = 0<br />        to_port     = 0<br />        protocol    = "-1"<br />        cidr_blocks = ["0.0.0.0/0"]<br />    }<br />}<br /><br />    </pre><br />2. Open the coding assistant. Request the following actions in the chat: **Scan current script and tell me the results.** | App developer |

### Example of advanced scanning capabilities
<a name="example-of-advanced-scanning-capabilities"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Perform targeted scanning. | Following are examples of requests that you can use to perform a targeted scan:+ **Scan current project and tell me the results.**<br />+ **Scan lines 6-10 in the current script.** | App developer |
| Use security scanning with code generation. | To resolve security findings by using code generation loops, use the following steps (this example uses Kiro as the coding assistant):1. In Kiro, ask: **Create a DynamoDB table in Terraform and scan the code with the security scanner.**<br />2. In Kiro, ask: **Review the generated code and security scan results and follow the code generation loops resolving the security findings.** | App developer |

## Troubleshooting
<a name="mcp-security-scanner-kiro-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Environment setup issues | + Verify that Python version 3.10 or later is installed.<br />+ Make sure that `uv` package manager is installed. |
| Scanner issues | + Verify that file formats are supported.<br />+ Check that file syntax is valid.<br />+ Ensure that proper file extensions are used.<br />+ Review scan timeout settings. |
| Integration problems | + Verify that the MCP server is running.<br />+ Check that the configuration file is correct.<br />+ Validate API endpoints.<br />+ Ensure that the response format is valid. |
| Additional support | + Review logs for detailed error messages.<br />+ Check tool-specific documentation.<br />+ Create an issue in the repository. |

## Related resources
<a name="mcp-security-scanner-kiro-resources"></a>

**AWS documentation**
+ [Infrastructure as code](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html) (AWS Whitepaper *Introduction to DevOps on AWS*)

**Other AWS resources**
+ [Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/)

**Other resources**
+ [Bandit documentation](https://bandit.readthedocs.io/)
+ [Checkov documentation](https://www.checkov.io/)
+ [Model Context Protocol (MCP) documentation](https://modelcontextprotocol.io/)
+ [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) (OWASP Foundation website)
+ [Semgrep documentation](https://semgrep.dev/docs/)

## Additional information
<a name="mcp-security-scanner-kiro-additional"></a>

**Example MCP configuration with auto approved enabled**

Without `autoApprove` configured, you must grant approval to send the code to the MCP security server for scanning. When `autoApprove` is configured, the code assistant can invoke the tools without your approval. These tools run locally on your machine. No data is sent out, and only a code scan is performed.

The following configuration automatically runs all security scanning functions:

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
+ GitLab CI – .yml, .yaml
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
+ "Generate a CloudFormation template for an Amazon S3 bucket with encryption and public access blocking enabled, and verify it passes security checks."
+ "Write a Python script to query DynamoDB with pagination and scan for security best practices."
+ "Create a Kubernetes deployment manifest for a microservice with security hardening and validate it."

For more information, see this [code generation with security scanning](https://github.com/aws-samples/sample-mcp-security-scanner/blob/main/docs/demo_code_generation.gif) demo in this pattern’s GitHub repository.
