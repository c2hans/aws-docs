---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/installing-storagebrowser.html
---

# Installing Storage Browser for S3
<a name="installing-storagebrowser"></a>

The fastest way to get started with Storage Browser is to clone one of the sample projects on GitHub. These sample projects can help you deploy production ready web apps for Storage Browser with preset integrations of AWS services for AWS Identity and Access Management so you can quickly connect authorized end users to data in S3.

For more information, see [Quick start](https://ui.docs.amplify.aws/react/connected-components/storage/storage-browser#quick-start) in the *Amplify Dev Center*.

## Installing Storage Browser for S3 from GitHub
<a name="install-storagebrowser-dependencies"></a>

Alternatively, you can install Storage Browser for S3 from the latest version of `aws-amplify/ui-react-storage` and `aws-amplify` packages in the [`aws-amplify`](https://github.com/aws-amplify) GitHub repository to start integrating Storage Browser into your existing application. When installing Storage Browser for S3, make sure to add the following dependencies to your `package.json` file:

```
"dependencies": {
    "aws-amplify/ui-react-storage": "latest",
    "aws-amplify": "latest",
  }
```

Alternatively, you can add the dependencies using Node Package Manager (NPM):

```
npm i --save @aws-amplify/ui-react-storage aws-amplify
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
