---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/docker-custom-images-managed-endpoint.html
---

# Customize Docker images for interactive endpoints
<a name="docker-custom-images-managed-endpoint"></a>

You can also customize Docker images for interactive endpoints so that you can run customized base kernel images. This helps you ensure that you have the dependencies you need when you run interactive workloads from EMR Studio.

1. Follow the [Steps 1-4](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/docker-custom-images-steps.html#docker-custom-images-retrieve) outlined above to customize a Docker image. For Amazon EMR 6.9.0 releases and later, you can get the base image URI from Amazon ECR Public Gallery. For releases before Amazon EMR 6.9.0, you can get the image in Amazon ECR Registry accounts in each AWS Region, and the only difference is the base image URI in your Dockerfile. The base image URI follows the format:

   ```
   {{ECR-registry-account}}.dkr.ecr.{{Region}}.amazonaws.com/notebook-spark/{{container-image-tag}}
   ```

   You need to use `notebook-spark` in the base image URI, instead of `spark`. The base image contains the Spark runtime and the notebook kernels that run with it. For more information about selecting Regions and container image tags, see [Details for selecting a base image URI](docker-custom-images-tag.md).
**Note**
Currently only overrides of base images are supported and introducing completely new kernels of other types than the base images AWS provides is not supported.

1. Create an interactive endpoint that can be used with the custom image.

   First, create a JSON file called `custom-image-managed-endpoint.json` with the following contents.

   ```
   {
       "name": "endpoint-name",
       "virtualClusterId": "{{virtual-cluster-id}}",
       "type": "JUPYTER_ENTERPRISE_GATEWAY",
       "releaseLabel": "{{emr-6.6.0-latest}}",
       "executionRoleArn": "{{execution-role-arn}}",
       "certificateArn": "{{certificate-arn}}",
       "configurationOverrides": {
           "applicationConfiguration": [
               {
                   "classification": "jupyter-kernel-overrides",
                   "configurations": [
                       {
                           "classification": "python3",
                           "properties": {
                               "container-image": "{{123456789012.dkr.ecr.us-west-2.amazonaws.com/custom-notebook-python:latest}}"
                           }
                       },
                       {
                           "classification": "spark-python-kubernetes",
                           "properties": {
                               "container-image": "{{123456789012.dkr.ecr.us-west-2.amazonaws.com/custom-notebook-spark:latest}}"
                           }
                       }
                   ]
               }
           ]
       }
   }
   ```

   Next, create an interactive endpoint using the configurations specified in the JSON file, as the following example demonstrates.

   ```
   aws emr-containers create-managed-endpoint --cli-input-json custom-image-managed-endpoint.json
   ```

   For more information, see [Create an interactive endpoint for your virtual cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-create-eks-cluster.html#emr-studio-create-managed-endpoint).

1. Connect to the interactive endpoint via EMR Studio. For more information, see [Connecting from Studio](https://emr-on-eks.workshop.aws/advanced/emr-studio/connecting-from-studio.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
