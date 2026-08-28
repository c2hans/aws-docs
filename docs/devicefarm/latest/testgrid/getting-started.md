---
source_url: https://docs.aws.amazon.com/devicefarm/latest/testgrid/getting-started.html
---

# Getting started with Selenium testing on Device Farm
<a name="getting-started"></a>

Selenium is a popular open-source software testing framework used to test web applications on different devices, including desktops, laptops, tablets, and mobile phones. Selenium allows developers and QA (Quality Assurance) engineers to write scripts that can control a web browser, simulate user interactions, and verify that the application under test is behaving as expected. For more information about Selenium, see the [Selenium documentation](https://selenium.dev/documentation/).

For most Selenium users, using Device Farm desktop browser testing requires only minor changes to their testing configuration, specifically one API call to create a limited-time use URL for the Selenium `RemoteWebDriver`.

**Topics**
+ [Migrating to Device Farm desktop browser testing from Selenium Grid](getting-started-migration.md)
+ [Migrating to Device Farm desktop browser testing from local Selenium WebDrivers](getting-started-local.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
