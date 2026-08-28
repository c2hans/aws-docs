---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ContainerService.html
---

# ContainerService
<a name="API_ContainerService"></a>

Describes an Amazon Lightsail container service.

## Contents
<a name="API_ContainerService_Contents"></a>

 ** arn **   <a name="Lightsail-Type-ContainerService-arn"></a>
The Amazon Resource Name (ARN) of the container service.
Type: String
Pattern: `.*\S.*`
Required: No

 ** containerServiceName **   <a name="Lightsail-Type-ContainerService-containerServiceName"></a>
The name of the container service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9]{1,2}|[a-z0-9][a-z0-9-]+[a-z0-9]$`
Required: No

 ** createdAt **   <a name="Lightsail-Type-ContainerService-createdAt"></a>
The timestamp when the container service was created.
Type: Timestamp
Required: No

 ** currentDeployment **   <a name="Lightsail-Type-ContainerService-currentDeployment"></a>
An object that describes the current container deployment of the container service.
Type: [ContainerServiceDeployment](API_ContainerServiceDeployment.md) object
Required: No

 ** isDisabled **   <a name="Lightsail-Type-ContainerService-isDisabled"></a>
A Boolean value indicating whether the container service is disabled.
Type: Boolean
Required: No

 ** location **   <a name="Lightsail-Type-ContainerService-location"></a>
An object that describes the location of the container service, such as the AWS Region and Availability Zone.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** nextDeployment **   <a name="Lightsail-Type-ContainerService-nextDeployment"></a>
An object that describes the next deployment of the container service.
This value is `null` when there is no deployment in a `pending` state.
Type: [ContainerServiceDeployment](API_ContainerServiceDeployment.md) object
Required: No

 ** power **   <a name="Lightsail-Type-ContainerService-power"></a>
The power specification of the container service.
The power specifies the amount of RAM, the number of vCPUs, and the base price of the container service.
Type: String
Valid Values: `nano | micro | small | medium | large | xlarge`
Required: No

 ** powerId **   <a name="Lightsail-Type-ContainerService-powerId"></a>
The ID of the power of the container service.
Type: String
Required: No

 ** principalArn **   <a name="Lightsail-Type-ContainerService-principalArn"></a>
The principal ARN of the container service.
The principal ARN can be used to create a trust relationship between your standard AWS account and your Lightsail container service. This allows you to give your service permission to access resources in your standard AWS account.
Type: String
Required: No

 ** privateDomainName **   <a name="Lightsail-Type-ContainerService-privateDomainName"></a>
The private domain name of the container service.
The private domain name is accessible only by other resources within the default virtual private cloud (VPC) of your Lightsail account.
Type: String
Required: No

 ** privateRegistryAccess **   <a name="Lightsail-Type-ContainerService-privateRegistryAccess"></a>
An object that describes the configuration for the container service to access private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.
For more information, see [Configuring access to an Amazon ECR private repository for an Amazon Lightsail container service](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-service-ecr-private-repo-access) in the *Amazon Lightsail Developer Guide*.
Type: [PrivateRegistryAccess](API_PrivateRegistryAccess.md) object
Required: No

 ** publicDomainNames **   <a name="Lightsail-Type-ContainerService-publicDomainNames"></a>
The public domain name of the container service, such as `example.com` and `www.example.com`.
You can specify up to four public domain names for a container service. The domain names that you specify are used when you create a deployment with a container configured as the public endpoint of your container service.
If you don't specify public domain names, then you can use the default domain of the container service.
You must create and validate an SSL/TLS certificate before you can use public domain names with your container service. Use the `CreateCertificate` action to create a certificate for the public domain names you want to use with your container service.
See `CreateContainerService` or `UpdateContainerService` for information about how to specify public domain names for your Lightsail container service.
Type: String to array of strings map
Required: No

 ** resourceType **   <a name="Lightsail-Type-ContainerService-resourceType"></a>
The Lightsail resource type of the container service.
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** scale **   <a name="Lightsail-Type-ContainerService-scale"></a>
The scale specification of the container service.
The scale specifies the allocated compute nodes of the container service.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** state **   <a name="Lightsail-Type-ContainerService-state"></a>
The current state of the container service.
The following container service states are possible:
+  `PENDING` - The container service is being created.
+  `READY` - The container service is running but it does not have an active container deployment.
+  `DEPLOYING` - The container service is launching a container deployment.
+  `RUNNING` - The container service is running and it has an active container deployment.
+  `UPDATING` - The container service capacity or its custom domains are being updated.
+  `DELETING` - The container service is being deleted.
+  `DISABLED` - The container service is disabled, and its active deployment and containers, if any, are shut down.
Type: String
Valid Values: `PENDING | READY | RUNNING | UPDATING | DELETING | DISABLED | DEPLOYING`
Required: No

 ** stateDetail **   <a name="Lightsail-Type-ContainerService-stateDetail"></a>
An object that describes the current state of the container service.
The state detail is populated only when a container service is in a `PENDING`, `DEPLOYING`, or `UPDATING` state.
Type: [ContainerServiceStateDetail](API_ContainerServiceStateDetail.md) object
Required: No

 ** tags **   <a name="Lightsail-Type-ContainerService-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** url **   <a name="Lightsail-Type-ContainerService-url"></a>
The publicly accessible URL of the container service.
If no public endpoint is specified in the `currentDeployment`, this URL returns a 404 response.
Type: String
Required: No

## See Also
<a name="API_ContainerService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/ContainerService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/ContainerService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/ContainerService)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
