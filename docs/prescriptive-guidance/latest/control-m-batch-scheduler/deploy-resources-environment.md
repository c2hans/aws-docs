---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/deploy-resources-environment.html
---

# Deploy Control-M and Micro Focus resources
<a name="deploy-resources-environment"></a>

The first two steps in integrating AWS Mainframe Modernization with Control-M are to deploy a Control-M Agent and then deploy a plug-in on the Agent. The third step is to deploy the job type in Control-M Application Integrator.

## Deploy a Control-M Agent on an EC2 instance
<a name="deploy-agent"></a>

When using a custom AWS Replatform with Micro Focus on Amazon EC2 runtime environment, the `MFBSIFJCL` utility is invoked. The utility operates on the host that was launched using the Micro Focus Enterprise Server offer from the AWS Marketplace. To run the `MFBSIFJCL` utility, you must also deploy a Control-M Agent on that host. For instructions, see the [Control-M documentation](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Agent_Installation.htm).

**Note**
You can download required installation media from the [BMC Electronic Product Download site](https://www.bmc.com/support/resources/product-downloads.html).

## Deploy the Micro Focus plug-in on the Control-M Agent
<a name="deploy-plug-in"></a>

Plug-ins provide integration and support for the applications and services that Control-M orchestrates.

The plug-in deployment is an infrequent activity. If you already have an existing plug-in that you want to use, skip this step, and create a connection profile.

On Amazon EC2, the AWS Mainframe Modernization Replatform with Micro Focus service exposes the Micro Focus engine. To integrate AWS Mainframe Modernization, Control-M uses the Micro Focus plug-in. For more information, see the [Control-M documentation](https://docs.bmc.com/docs/ctm_integrations/control-m-for-micro-focus-1193641959.html).

You must deploy this plug-in to an Agent that is installed on a host where Micro Focus Enterprise Server is running.

## Deploy an AWS Mainframe Modernization job type in Control-M Application Integrator
<a name="application-integrator"></a>

The job type deployment is usually a one-time activity. If you already have an existing job type that you want to use, skip this step and move on to the next step of [creating a connection profile](create-control-m-connection-profile.md).

The example job type [AIJOB.ctmai ](https://github.com/aws-samples/aws-mainframe-modernization-controlm-integration/blob/main/assets/AIJOB.ctmai)is supplied in the git repository. To deploy a job type, you must perform the following steps using [Application Integrator](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Application_Integrator.htm):
+ Clone the [aws-mainframe-modernization-controlm-integration](https://github.com/aws-samples/aws-mainframe-modernization-controlm-integration) GitHub repository and download the `AIJOB.ctmai`  file to a file system location that can be accessed by Application Integrator.
+ Log in to Application Integrator.
+ On the **Home** tab, select **Import job type from file**, and select the location of `AIM2JOB.ctmai`.
+ If you want to make any modifications to the supplied example, familiarize yourself with Application Integrator.
+ Deploy the job type by following the instructions in the [Control-M documentation](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Deploying_and_Publishing_a_Plug-in.htm).
