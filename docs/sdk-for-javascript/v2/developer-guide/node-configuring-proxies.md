---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/node-configuring-proxies.html
---

The AWS SDK for JavaScript v2 has reached end-of-support. We recommend that you migrate to [AWS SDK for JavaScript v3](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-javascript-v2/).

# Configuring Proxies for Node.js
<a name="node-configuring-proxies"></a>

If you can't directly connect to the internet, the SDK for JavaScript supports use of HTTP or HTTPS proxies through a third-party HTTP agent, such as [proxy-agent](https://github.com/TooTallNate/proxy-agents/tree/main/packages/proxy-agent). To install proxy-agent, type the following at the command line.

```
npm install proxy-agent --save
```

If you decide to use a different proxy, first follow the installation and configuration instructions for that proxy. To use this or another third-party proxy in your application, you must set the `httpOptions` property of ` AWS.Config` to specify the proxy you choose. This example shows ` proxy-agent`.

```
var AWS = require("aws-sdk");
var ProxyAgent = require('proxy-agent').ProxyAgent;
AWS.config.update({
  httpOptions: { agent: new ProxyAgent('http://internal.proxy.com') }
});
```

For more information about other proxy libraries, see [npm, the Node.js package manager](https://www.npmjs.com/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for JavaScript SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-javascript` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
