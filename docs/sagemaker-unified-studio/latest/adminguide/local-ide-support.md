---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/local-ide-support.html
---

# Connect your local Visual Studio Code to Amazon SageMaker Unified Studio spaces with remote access
<a name="local-ide-support"></a>

You can connect remotely from Visual Studio Code (VS Code) to Amazon SageMaker Unified Studio Spaces. You can use your customized local VS Code setup, including AI-assisted development tools and custom extensions, with the scalable compute resources in Amazon SageMaker Unified Studio.

## Key Concepts
<a name="local-ide-key-concepts"></a>

**VPC**
Amazon Virtual Private Cloud (VPC) is a fundamental building block, allowing you to provision a logically isolated virtual network within the AWS Cloud.

**Amazon SageMaker Unified Studio Space**
Amazon SageMaker Unified Studio provides compute Spaces for integrated development environments (IDEs) that you can use to author code. There are two IDE applications available in Amazon SageMaker Unified Studio: JupyterLab and Code Editor. A JupyterLab Space is created in your project by default, and you can create additional Spaces as desired.

**Remote Connection**
A secure SSH-over-SSM tunnel between your local VS Code and a SageMaker Unified Studio Space. This connection enables interactive development and code execution in VS Code using Amazon SageMaker Unified Studio compute resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
