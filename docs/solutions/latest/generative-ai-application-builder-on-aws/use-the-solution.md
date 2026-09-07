---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/use-the-solution.html
---

# Use the solution
<a name="use-the-solution"></a>

## Accessing the UI
<a name="accessing-the-ui"></a>

During the stack deployment process (for both the Deployment dashboard and use cases) an email is sent to the configured email address. The email contains the user’s temporary credentials they can use to sign up and access the web interface.

**Note**
The DevOps user with access to the AWS Management Console must provide the admin user with the CloudFront URL of the Deployment dashboard UI when the stack completes.

For the use cases, the admin user with access to the Deployment dashboard UI must provide the business user with the CloudFront URL of the use case UI when the deployment completes.

Once logged in, the user can interact with the solution UIs, either the Deployment dashboard in the case of admins, or the use case in the case of business users.

## How to update a deployment
<a name="how-to-update-a-deployment"></a>

When on the Deployment dashboard home page (or the details page of a deployment) you can edit the configuration used by a deployment. You can only edit deployments that are in the CREATE\_COMPLETE or UPDATE\_COMPLETE statuses.

Except for the use case name, all other options are editable for a deployment. Just change the values you want to edit and redeploy.

Depending on the scope of edits made, the redeployment time will vary. It might take a few seconds if simple settings have changed (example, model parameters), to more than 30 minutes if larger infrastructure related options have changed (example, request to create the Amazon Kendra index for the Text use case RAG).

Once the edit has completed successfully, the application status will report an UPDATE\_COMPLETE status. At this time, you can access the deployed UI through the CloudFront URL and interact with the modified deployment.

**Note**
It might be easier to run multiple deployments side-by-side if you want to compare different settings or LLMs. Use the **Clone** feature to quickly use an existing configuration to launch a new deployment.

## How to clone a deployment
<a name="how-to-clone-a-deployment"></a>

When on the Deployments dashboard home page (or the details page of a deployment) you can clone the configuration used by a deployment. Cloning a deployment launches the **Deploy new use case** wizard, but with most fields pre-filled with the same values.

This is a convenience operation to help you quickly duplicate deployments with changed settings, revive a deleted deployment, or compare multiple LLMs in otherwise identical deployments.

## How to delete a deployment
<a name="how-to-delete-a-deployment"></a>

When on the Deployments dashboard home page (or the details page of a deployment) you can delete it once you no longer need the deployment. Deleting a deployment invokes a CloudFormation stack delete operation and deprovisions the resources for the deployment.

By default, a deleted deployment still remains on the dashboard to enable the clone functionality. To completely remove a deployment from the dashboard so that it stops being tracked in the UI, choose **Permanently delete** on the delete confirmation window.

**Important**
Some resources are left behind during stack deletion and must be manually deleted. Refer to the [Manual uninstall](uninstall-the-solution.md#manual-uninstall-sub-topics) section for details on what resources are retained and how to clean them up.

## Using Amazon SageMaker AI as an LLM Provider
<a name="using-amazon-sagemaker-ai-as-an-llm-provider"></a>

As of v1.3.0, [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) is available as a model provider for Text use cases. This feature allows you to use a SageMaker AI inference endpoint already existing within the AWS account in the solution. Here are some ways to get started.

**Important**
The solution does not manage the lifecycle of your SageMaker AI endpoints. You are responsible for deleting the SageMaker AI endpoints once they are no longer needed to stop incurring additional charges.

### Creating a SageMaker AI endpoint
<a name="creating-a-sagemaker-endpoint"></a>

You can use [Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/) to quickly deploy an endpoint.

You can also use a text-generation based SageMaker AI endpoint and deploy using the base SageMaker AI service. Refer to the [SageMaker AI JumpStart documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) for a step by step guide on [how to deploy a model](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-deploy.html) for inference.

**Note**
Foundation models/LLMs are typically quite large and can often require the use of large accelerated compute instances. Many of these larger instances might not be available by default in your AWS account. Refer to the default [SageMaker AI quotas](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html#limits_sagemaker) and be sure to [request a quota increase](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) before deploying to avoid common deployment failures.

#### Use SageMaker AI endpoint to create a Text use case deployment
<a name="use-endpoint-to-create-a-text-use-case-deployment"></a>

To deploy a new Text use case using a SageMaker AI endpoint for inference:

1.  [Create a new use case](step-2-deploy-use-case.md) through the Deployment dashboard wizard and complete the forms until you reach the Models selection page.

1. On the Models page, select **SageMaker AI** as the model provider. This will generate a custom form requiring three key pieces of user input:
   + The name of the SageMaker AI endpoint you want to use. DevOps users can obtain this from the AWS console. Note that the endpoint must be in the same account and Region as the solution is deployed in.

      **Location of the endpoint name on the AWS console**
![image15](https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/image15.png)
   + The schema of the input payload expected by the endpoint. To support the widest set of endpoints, admin users are required to tell the solution how their endpoint expects the input to be formatted. In the model selection wizard, provide the JSON schema for the solution to send to the endpoint. You can add placeholders to inject static and dynamic values into the request payload. The available options are:
     + Mandatory placeholders: \\<\\<prompt\\>\\> will be dynamically replaced with the full input (for example, history, context, and user input as per the prompt template) to be sent to the SageMaker AI endpoint at runtime.
     + Optional placeholders: \\<\\<temperature\\>\\> \*,\\\* as well as any parameters defined in advanced model parameters can be provided to the endpoint. Any string containing a placeholder enclosed in \\<\\< and \\>\\> (for example, \\<\\<max\_new\_tokens\\>\\>) will be replaced by the value of the advanced model parameter of the same name.

        **Example input schema - setting mandatory fields, prompt and temperature, along with a custom advanced parameter, max\_new\_tokens. Output path must be supplied as a valid JSONPath string**
![image16](https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/image16.png)

1. The location of the LLMs generated string response within the output payload. This must be supplied as a JSONPath expression to indicate where the final text response shown to users is expected to be accessed from within the endpoint’s return object and response.

    **Example of adding Advanced model parameters to use within SageMaker AI input schema (see Figure 2 for previous options/settings)**
![image17](https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/image17.png)

**Note**
SageMaker AI now supports hosting multiple models behind the same endpoint, and this is the default configuration when deploying an endpoint in the current version of SageMaker AI Studio (not Studio Classic).
If your endpoint is configured in this way, you will be required to add **InferenceComponentName** to the advanced model parameters section, with a value corresponding to the name of the model you want to use.
