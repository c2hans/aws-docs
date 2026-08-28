---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ContainerServiceDeploymentRequest.html
---

# ContainerServiceDeploymentRequest
<a name="API_ContainerServiceDeploymentRequest"></a>

Describes a container deployment configuration of an Amazon Lightsail container service.

A deployment specifies the settings, such as the ports and launch command, of containers that are deployed to your container service.

## Contents
<a name="API_ContainerServiceDeploymentRequest_Contents"></a>

 ** containers **   <a name="Lightsail-Type-ContainerServiceDeploymentRequest-containers"></a>
An object that describes the configuration for the containers of the deployment.
Type: String to [Container](API_Container.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 53.
Key Pattern: `^[a-z0-9]{1,2}|[a-z0-9][a-z0-9-]+[a-z0-9]$`
Required: No

 ** publicEndpoint **   <a name="Lightsail-Type-ContainerServiceDeploymentRequest-publicEndpoint"></a>
An object that describes the endpoint of the deployment.
Type: [EndpointRequest](API_EndpointRequest.md) object
Required: No

## See Also
<a name="API_ContainerServiceDeploymentRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/ContainerServiceDeploymentRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/ContainerServiceDeploymentRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/ContainerServiceDeploymentRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
