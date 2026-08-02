---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/testing.html
---

# Testing
<a name="testing"></a>

The telecom-specific test automation framework can be integrated in the code pipeline. The code pipeline is integrated with step functions to orchestrate the integration with a test automation framework. AWS step functions use multiple Lambda functions to invoke the test automation framework (third-party tools) via API calls. The step function will initially get the test ID, run the test, and get the results from the test automation framework. The step function then analyzes the results and passes them to the code pipeline for approval of the application for production deployment. The approval can be automated or maintained manual in the code pipeline as needed. This is an important step for CSPs to promote the deployment from test environment to production. High level APIs required for integration are categorized into the following manner:
+ Get context
+ Run specific test case
+ Stop test case
+ Get results

The complexity of calling external REST APIs is modeled using AWS step functions, which allow standard constructs to invoke parallel flows, wait for results, branch based on conditions, and integrate REST API with AWS CodePipeline.

![A diagram depicting testing flow.](http://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/images/cicd_5g15.png)

*Testing flow*
