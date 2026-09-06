---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/addf-security-and-operations/customizing-the-addf-deployment-framework-code.html
---

# Customizing the ADDF deployment framework code
<a name="customizing-the-addf-deployment-framework-code"></a>

The ADDF deployment framework and its orchestration and deployment logic can be fully customized to meet any requirements. However, we suggest you either refrain from customizing or minimize your changes for the following reasons:
+ **Keep upstream compatibility** – Upstream compatibility makes it easier to update ADDF for the latest features and security updates. Changing the framework breaks native backwards compatibility with SeedFarmer, CodeSeeder, and any ADDF core modules.
+ **Security consequences** – Changing the ADDF deployment framework can be a complex task that can have unintended security consequences. In the worst-case scenario, framework changes can create security vulnerabilities.

When possible, build and customize your own module code instead of modifying the ADDF deployment framework and ADDF core module code.

**Note**
If you feel that specific parts of the ADDF deployment framework need improvement or further security hardening, please contribute your changes to the ADDF repository through a pull request. For more information, see [Open-source security reviews and contributions](addf-security-review-process.md#open-source-sec-reviews).
