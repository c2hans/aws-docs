---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/how-to-access.html
---

# Grant access to Amazon Location Service
<a name="how-to-access"></a>

To use Amazon Location Service, a user must be granted access to the resources and APIs that make up Amazon Location. There are three strategies you can use to grant access to your resources.
+ **Use IAM** – To grant access to users authenticated with AWS IAM Identity Center or AWS Identity and Access Management (IAM), create an IAM policy that allows access to the resources that you want. For more information about IAM and Amazon Location, see [Identity and Access Management for Amazon Location Service](security-iam.md).
+ **Use API keys** – To grant access to unauthenticated users, you can create API Keys that give read-only access to your Amazon Location Service resources. This is useful in a case where you do not want to authenticate every user. For example, a web application. For more information about API keys, see [Allow unauthenticated guest access to your application using API keys](using-apikeys.md).
+ **Use Amazon Cognito** – An alternative to API keys is to use Amazon Cognito to grant anonymous access. Amazon Cognito allows you to create a richer authorization with policy to define what can be done by the unauthenticated users. For more information about using Amazon Cognito, see [Allow unauthenticated guest access to your application using Amazon Cognito](authenticating-using-cognito.md).
**Note**
You can also use Amazon Cognito to use your own authentication process or to combine multiple authentication methods, using Amazon Cognito Federated Identities. For more information, see [Getting Started with Federated Identities](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-with-identity-pools.html) in the *Amazon Cognito Developer Guide*.

**Topics**
+ [Use API keys](using-apikeys.md)
+ [Use Amazon Cognito](authenticating-using-cognito.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
