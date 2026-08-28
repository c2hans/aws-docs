---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/aws-explorer.html
---

# Working with AWS Services in the AWS Explorer
<a name="aws-explorer"></a>

The **AWS Explorer** gives you a view of some of the AWS services that you can work with when using the AWS Toolkit for Visual Studio Code.

 This section provides information about how to access and use the **AWS Explorer** in VS Code. It assumes that you've already [installed and configured](setting-up.md) the Toolkit for VS Code on your system.

Some important points:
+ If the toolkit is installed and conﬁgured correctly, you should see items in the **AWS Explorer**. To see the **AWS Explorer**, choose the **AWS** icon in the **Activity bar**.

  For example:
![AWS Explorer with credentials defined.](http://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/images/aws-explorer-with-more-resources.png)
+ Certain features require certain AWS permissions. For example, to see the AWS Lambda functions in your AWS account, the credentials you configured in [Authentication and access](establish-credentials.md) must include at least read-only Lambda permissions. See the following topics for more information about the permissions that each feature needs.
+ If you want to interact with AWS services that aren't immediately visible in the **AWS Explorer**, you can go to **More resources** and choose from hundreds of resources that can added to the interface.

  For example, you can choose **AWS Toolkit:CodeArtifact::Repository** from the selection of available resource types. After this resource type is added to **More resources**, you can expand the entry to view a list of resources that create different CodeArtifact repositories with their own properties and attributes. Moreover, you can describe the properties and attributes of resources in JSON-formatted templates, which can be saved to create new resources in the AWS Cloud.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
