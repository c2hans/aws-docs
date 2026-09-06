---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/addf-security-and-operations/initial-setup.html
---

# Initial setup
<a name="initial-setup"></a>

Set up ADDF according to the [ADDF Deployment Guide](https://github.com/awslabs/autonomous-driving-data-framework/blob/main/docs/deployment_guide.md) (GitHub). The starting point for any deployment is the `/manifest` folder in the [autonomous-driving-data-framework](https://github.com/awslabs/autonomous-driving-data-framework) Git Hub repository. The `/manifest/example-dev` folder contains a sample deployment for demo purposes. Use this sample as a starting point for designing your own deployment. In that directory, there is an ADDF deployment manifest file called **deployment.yaml**. It contains all the information for SeedFarmer to manage, deploy, or delete ADDF and its resources in the AWS Cloud. You can create groups of ADDF modules in dedicated files. The **core-modules.yaml** is an example of the core module group, and it includes all core modules provided by ADDF. To summarize, the **deployment.yaml** file contains all references to the groups and modules that will be deployed to their target accounts and specifies the deployment order.

For a secure and compliant configuration, especially in an environment that isn't for proof of concept, we recommend that you review the source code of each module that you intend to deploy. According to security hardening best practices, you should deploy only modules that are required for your intended use case.

**Note**
ADDF modules in the `modules/demo-only/` folder aren't security hardened and shouldn't be deployed in production environments or in any environment with sensitive or protected data. These modules are included to showcase system capabilities, and you can use them as the base for creating your own customized, security-hardened modules.
