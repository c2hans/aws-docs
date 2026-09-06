---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ContainerServiceDeployment.html
---

# ContainerServiceDeployment
<a name="API_ContainerServiceDeployment"></a>

Describes a container deployment configuration of an Amazon Lightsail container service.

A deployment specifies the settings, such as the ports and launch command, of containers that are deployed to your container service.

## Contents
<a name="API_ContainerServiceDeployment_Contents"></a>

 ** containers **   <a name="Lightsail-Type-ContainerServiceDeployment-containers"></a>
An object that describes the configuration for the containers of the deployment.
Type: String to [Container](API_Container.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 53.
Key Pattern: `^[a-z0-9]{1,2}|[a-z0-9][a-z0-9-]+[a-z0-9]$`
Required: No

 ** createdAt **   <a name="Lightsail-Type-ContainerServiceDeployment-createdAt"></a>
The timestamp when the deployment was created.
Type: Timestamp
Required: No

 ** publicEndpoint **   <a name="Lightsail-Type-ContainerServiceDeployment-publicEndpoint"></a>
An object that describes the endpoint of the deployment.
Type: [ContainerServiceEndpoint](API_ContainerServiceEndpoint.md) object
Required: No

 ** state **   <a name="Lightsail-Type-ContainerServiceDeployment-state"></a>
The state of the deployment.
A deployment can be in one of the following states:
+  `ACTIVATING` - The deployment is being created.
+  `ACTIVE` - The deployment was successfully created, and it's currently running on the container service. The container service can have only one deployment in an active state at a time.
+  `INACTIVE` - The deployment was previously successfully created, but it is not currently running on the container service.
+  `FAILED` - The deployment failed. Use the `GetContainerLog` action to view the log events for the containers in the deployment to try to determine the reason for the failure.
Type: String
Valid Values: `ACTIVATING | ACTIVE | INACTIVE | FAILED`
Required: No

 ** version **   <a name="Lightsail-Type-ContainerServiceDeployment-version"></a>
The version number of the deployment.
Type: Integer
Required: No

## See Also
<a name="API_ContainerServiceDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/ContainerServiceDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/ContainerServiceDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/ContainerServiceDeployment)
