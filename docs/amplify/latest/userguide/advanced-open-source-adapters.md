---
source_url: https://docs.aws.amazon.com/amplify/latest/userguide/advanced-open-source-adapters.html
---

# Advanced: Open source adapters
<a name="advanced-open-source-adapters"></a>

Framework authors can use the file system based deployment specification to develop open source build adapters customized for their specific frameworks. These adapters will transform an app's build output into a deployment bundle that conforms to Amplify Hosting’s expected directory structure. This deployment bundle will include all the necessary files and assets to host an app, including runtime configuration, such as routing rules.

If you aren't using a framework, you can develop your own solution to generate a build output that Amplify expects.

**Topics**
+ [Using the Amplify Hosting deployment specification to configure build output](ssr-deployment-specification.md)
+ [Deploying an Express server using the deployment manifest](deploy-express-server.md)
+ [Image optimization integration for framework authors](integrate-image-optimization-framework.md)
+ [Using open source adapters for any SSR framework](using-framework-adapter.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Amplify. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplify` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
