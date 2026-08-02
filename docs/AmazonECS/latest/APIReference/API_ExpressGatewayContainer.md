---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ExpressGatewayContainer.html
---

# ExpressGatewayContainer
<a name="API_ExpressGatewayContainer"></a>

Defines the configuration for the primary container in an Express service. This container receives traffic from the Application Load Balancer and runs your application code.

The container configuration includes the container image, port mapping, logging settings, environment variables, and secrets. The container image is the only required parameter, with sensible defaults provided for other settings.

## Contents
<a name="API_ExpressGatewayContainer_Contents"></a>

 ** image **   <a name="ECS-Type-ExpressGatewayContainer-image"></a>
The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either `repository-url/image:tag` or `repository-url/image@digest`.
For Express services, the image typically contains a web application that listens on the specified container port. The image can be stored in Amazon ECR, Docker Hub, or any other container registry accessible to your execution role.
Type: String
Required: Yes

 ** awsLogsConfiguration **   <a name="ECS-Type-ExpressGatewayContainer-awsLogsConfiguration"></a>
The log configuration for the container.
Type: [ExpressGatewayServiceAwsLogsConfiguration](API_ExpressGatewayServiceAwsLogsConfiguration.md) object
Required: No

 ** command **   <a name="ECS-Type-ExpressGatewayContainer-command"></a>
The command that is passed to the container.
Type: Array of strings
Required: No

 ** containerPort **   <a name="ECS-Type-ExpressGatewayContainer-containerPort"></a>
The port number on the container that receives traffic from the load balancer. Default is 80.
Type: Integer
Required: No

 ** environment **   <a name="ECS-Type-ExpressGatewayContainer-environment"></a>
The environment variables to pass to the container.
Type: Array of [KeyValuePair](API_KeyValuePair.md) objects
Required: No

 ** repositoryCredentials **   <a name="ECS-Type-ExpressGatewayContainer-repositoryCredentials"></a>
The configuration for repository credentials for private registry authentication.
Type: [ExpressGatewayRepositoryCredentials](API_ExpressGatewayRepositoryCredentials.md) object
Required: No

 ** secrets **   <a name="ECS-Type-ExpressGatewayContainer-secrets"></a>
The secrets to pass to the container.
Type: Array of [Secret](API_Secret.md) objects
Required: No

## See Also
<a name="API_ExpressGatewayContainer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ExpressGatewayContainer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ExpressGatewayContainer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ExpressGatewayContainer)
