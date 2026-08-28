---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/javascript-installation.html
---

# Installing the AWS Encryption SDK for JavaScript
<a name="javascript-installation"></a>

The AWS Encryption SDK for JavaScript consists of a collection of interdependent modules. Several of the modules are just collections of modules that are designed to work together. Some modules are designed to work independently. A few modules are required for all implementations; a few others are required only for special cases. For information about the modules in the AWS Encryption SDK for JavaScript, see [Modules in the AWS Encryption SDK for JavaScript](javascript-modules.md) and the `README.md` file in each of the modules in the [aws-encryption-sdk-javascript](https://github.com/aws/aws-encryption-sdk-javascript/tree/master/modules) repository on GitHub.

**Note**
All versions of the AWS Encryption SDK for JavaScript earlier than 2.0.0 are in the [end-of-support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle).
You can safely update from version 2.0.*x* and later to the latest version of the AWS Encryption SDK for JavaScript without any code or data changes. However, [ new security features](about-versions.md#version-2) introduced in version 2.0.*x* are not backward-compatible. To update from versions earlier than 1.7.*x* to version 2.0.*x* and later, you must first update to the latest 1.*x* version of the AWS Encryption SDK for JavaScript. For details, see [Migrating your AWS Encryption SDK](migration.md).

To install the modules, use the [npm package manager](https://www.npmjs.com/get-npm).

For example, to install the `client-node` module, which includes all of the modules you need to program with the AWS Encryption SDK for JavaScript in Node.js, use the following command.

```
npm install @aws-crypto/client-node
```

To install the `client-browser` module, which includes all of the modules you need to program with the AWS Encryption SDK for JavaScript in the browser, use the following command.

```
npm install @aws-crypto/client-browser
```

For working examples of how to use the AWS Encryption SDK for JavaScript, see the examples in the `example-node` and `example-browser` modules in the [aws-encryption-sdk-javascript](https://github.com/aws/aws-encryption-sdk-javascript/) repository on GitHub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
