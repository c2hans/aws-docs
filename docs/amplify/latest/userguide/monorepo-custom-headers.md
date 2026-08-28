---
source_url: https://docs.aws.amazon.com/amplify/latest/userguide/monorepo-custom-headers.html
---

# Monorepo custom header requirements
<a name="monorepo-custom-headers"></a>

When you specify custom headers for an app in a monorepo, be aware of the following setup requirements:
+ There is a specific YAML format for a monorepo. For the correct syntax, see [Custom header YAML reference](custom-header-YAML-format.md).
+ You can specify custom headers for an application in a monorepo using the **Custom headers** section of the Amplify console. You must redeploy your application to apply the new custom headers.
+ As an alternative to using the console, you can specify custom headers for an app in a monorepo in a `customHttp.yml` file. You must save the `customHttp.yml` file in the root of your repo and then redeploy the application to apply the new custom headers. Custom headers specified in the `customHttp.yml` file override any custom headers specified using the **Custom headers** section of the Amplify console.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Amplify. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplify` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
