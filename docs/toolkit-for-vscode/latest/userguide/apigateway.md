---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/apigateway.html
---

# Working with Amazon API Gateway
<a name="apigateway"></a>

You can browse and run remote API Gateway resources in your connected AWS account using the AWS Toolkit for Visual Studio Code.

**Note**
This feature does not support debugging.

**To browse and run remote API Gateway resources**

1.  In the **AWS Explorer**, choose **API Gateway** to expand the menu. The remote API Gateway resources are listed.

1.  Locate the API Gateway resource you want to invoke, open its context (right-click) menu, and then choose **Invoke on AWS**.

1.  In the parameters form, specify the invoke parameters.

1.  To run the remote API Gateway resource, choose **Invoke**. The results are deplayed in the **VS Code Output** view.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
