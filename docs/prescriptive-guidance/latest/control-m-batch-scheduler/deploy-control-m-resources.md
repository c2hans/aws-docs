---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/deploy-control-m-resources.html
---

# Deploy Control-M resources
<a name="deploy-control-m-resources"></a>

The first two steps in integrating AWS Mainframe Modernization with Control-M are to deploy the plug-in and the job type.

## Deploy the AWS Mainframe Modernization Control-M plug-in
<a name="deploy-plug-in"></a>

Plug-ins provide integration and support for the applications and services that Control-M orchestrates. For the managed AWS Mainframe Modernization service, deploy the AWS Mainframe Modernization plug-in.

The plug-in deployment is an infrequent activity. If installing the plug-in for the first time, follow the steps in the [Control-M documentation](https://docs.bmc.com/docs/ctm_integrations/control-m-for-aws-mainframe-modernization-1244652367.html). If you have an existing plug-in that you want to use, skip this step, and create a connection profile.

## Deploy an AWS Mainframe Modernization job type in Control-M Application Integrator
<a name="deploy-job-type"></a>

The job type deployment is usually a one-time activity. If you already have an existing job type that you want to use, skip this step and move on to the next step of [creating a connection profile](connection-profile.md).

The example job type [AIJOB.ctmai](https://github.com/aws-samples/aws-mainframe-modernization-controlm-integration/blob/main/assets/AIJOB.ctmai)  is supplied in the git repository. To deploy a job type, you must perform the following steps using [Application Integrator](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Application_Integrator.htm):

1. Clone the [aws-mainframe-modernization-controlm-integration](https://github.com/aws-samples/aws-mainframe-modernization-controlm-integration) GitHub repository and download the `AIJOB.ctmai` file to a file system location that can be accessed by Application Integrator.

1. Log in to Application Integrator.

1. On the **Home** tab, select **Import job type from file**, and select the location of `AIJOB.ctmai`.

1. If you want to make any modifications to the supplied example, familiarize yourself with Application Integrator.

1. Deploy the job type by following the instructions in the [Control-M documentation](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Deploying_and_Publishing_a_Plug-in.htm).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
