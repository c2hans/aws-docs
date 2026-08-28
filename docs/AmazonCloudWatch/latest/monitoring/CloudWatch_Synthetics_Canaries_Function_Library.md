---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Function_Library.html
---

# Library functions available for canary scripts
<a name="CloudWatch_Synthetics_Canaries_Function_Library"></a>

CloudWatch Synthetics includes several built-in classes and functions that you can call when writing Node.js scripts to use as canaries.

Some apply to both UI and API canaries. Others apply to UI canaries only. A UI canary is a canary that uses the `getPage()` function and uses Puppeteer as a web driver to navigate and interact with webpages.

**Note**
Whenever you upgrade a canary to use a new version of the the Synthetics runtime, all Synthetics library functions that your canary uses are also automatically upgraded to the same version of NodeJS that the Synthetics runtime supports.

**Topics**
+ [Library functions available for Node.js canary](Library_function_Nodejs.md)
+ [Library functions available for Java canary](CloudWatch_Synthetics_Canaries_Java.md)
+ [Library functions available for Node.js canary scripts using Playwright](CloudWatch_Synthetics_Canaries_Nodejs_Playwright.md)
+ [Library functions available for Node.js canary scripts using Puppeteer](CloudWatch_Synthetics_Canaries_Library_Nodejs.md)
+ [Library functions available for Python canary scripts using Selenium](CloudWatch_Synthetics_Canaries_Library_Python.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
