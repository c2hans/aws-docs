---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/security_iam_unauthenticated-users.html
---

# How Amazon Location Service works with unauthenticated users
<a name="security_iam_unauthenticated-users"></a>

Many scenarios for using Amazon Location Service, including showing maps on the web or in a mobile application, require allowing access to users who haven't signed in with IAM. For these unauthenticated scenarios, you have two options.
+ **Use API keys** – To grant access to unauthenticated users, you can create API Keys that give read-only access to your Amazon Location Service resources. This is useful in a case where you do not want to authenticate every user. For example, a web application. For more information about API keys, see [Allow unauthenticated guest access to your application using API keys](using-apikeys.md).
+ **Use Amazon Cognito** – An alternative to API keys is to use Amazon Cognito to grant anonymous access. Amazon Cognito allows you to create a richer authorization with IAM policy to define what can be done by the unauthenticated users. For more information about using Amazon Cognito, see [Allow unauthenticated guest access to your application using Amazon Cognito](authenticating-using-cognito.md).

For an overview of providing access to unauthenticated users, see [Grant access to Amazon Location Service](how-to-access.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
