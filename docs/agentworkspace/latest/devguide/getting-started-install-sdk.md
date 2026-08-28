---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/getting-started-install-sdk.html
---

# Install the Amazon Connect SDK for developing applications for Connect Customer agent workspace
<a name="getting-started-install-sdk"></a>

To develop applications for the Connect Customer agent workspace you must first install the Connect Customer SDK.

The [*Connect Customer Amazon Connect SDK*](https://github.com/amazon-connect/AmazonConnectSDK) can be installed from NPM. The Aamzon Connect SDK is made up of a set of modules that can be installed as separate packages, meaning that you should only pull in the packages that you need.

The *app* package provides core application features like logging, error handling, secure messaging, and lifecycle events, and must be installed by all applications at a minimum to integrate into the workspace.

 **Install from NPM**

Install the app package from NPM by installing ** @amazon-connect/app**.

```
% npm install --save @amazon-connect/app
```

**Note**
 If you do not use NPM, refer to [Using Amazon Connect SDK without pacakage manager](https://docs.aws.amazon.com/agentworkspace/latest/devguide/sdk-without-package-manager.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
