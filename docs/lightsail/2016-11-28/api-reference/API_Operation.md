---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Operation.html
---

# Operation
<a name="API_Operation"></a>

Describes the API operation.

## Contents
<a name="API_Operation_Contents"></a>

 ** createdAt **   <a name="Lightsail-Type-Operation-createdAt"></a>
The timestamp when the operation was initialized (`1479816991.349`).
Type: Timestamp
Required: No

 ** errorCode **   <a name="Lightsail-Type-Operation-errorCode"></a>
The error code.
Type: String
Required: No

 ** errorDetails **   <a name="Lightsail-Type-Operation-errorDetails"></a>
The error details.
Type: String
Required: No

 ** id **   <a name="Lightsail-Type-Operation-id"></a>
The ID of the operation.
Type: String
Pattern: `.*\S.*`
Required: No

 ** isTerminal **   <a name="Lightsail-Type-Operation-isTerminal"></a>
A Boolean value indicating whether the operation is terminal.
Type: Boolean
Required: No

 ** location **   <a name="Lightsail-Type-Operation-location"></a>
The AWS Region and Availability Zone.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** operationDetails **   <a name="Lightsail-Type-Operation-operationDetails"></a>
Details about the operation (`Debian-1GB-Ohio-1`).
Type: String
Required: No

 ** operationType **   <a name="Lightsail-Type-Operation-operationType"></a>
The type of operation.
Type: String
Valid Values: `DeleteKnownHostKeys | DeleteInstance | CreateInstance | StopInstance | StartInstance | RebootInstance | OpenInstancePublicPorts | PutInstancePublicPorts | CloseInstancePublicPorts | AllocateStaticIp | ReleaseStaticIp | AttachStaticIp | DetachStaticIp | UpdateDomainEntry | DeleteDomainEntry | CreateDomain | DeleteDomain | CreateInstanceSnapshot | DeleteInstanceSnapshot | CreateInstancesFromSnapshot | CreateLoadBalancer | DeleteLoadBalancer | AttachInstancesToLoadBalancer | DetachInstancesFromLoadBalancer | UpdateLoadBalancerAttribute | CreateLoadBalancerTlsCertificate | DeleteLoadBalancerTlsCertificate | AttachLoadBalancerTlsCertificate | CreateDisk | DeleteDisk | AttachDisk | DetachDisk | CreateDiskSnapshot | DeleteDiskSnapshot | CreateDiskFromSnapshot | CreateRelationalDatabase | UpdateRelationalDatabase | DeleteRelationalDatabase | CreateRelationalDatabaseFromSnapshot | CreateRelationalDatabaseSnapshot | DeleteRelationalDatabaseSnapshot | UpdateRelationalDatabaseParameters | StartRelationalDatabase | RebootRelationalDatabase | StopRelationalDatabase | EnableAddOn | DisableAddOn | PutAlarm | GetAlarms | DeleteAlarm | TestAlarm | CreateContactMethod | GetContactMethods | SendContactMethodVerification | DeleteContactMethod | CreateDistribution | UpdateDistribution | DeleteDistribution | ResetDistributionCache | AttachCertificateToDistribution | DetachCertificateFromDistribution | UpdateDistributionBundle | SetIpAddressType | CreateCertificate | DeleteCertificate | CreateContainerService | UpdateContainerService | DeleteContainerService | CreateContainerServiceDeployment | CreateContainerServiceRegistryLogin | RegisterContainerImage | DeleteContainerImage | CreateBucket | DeleteBucket | CreateBucketAccessKey | DeleteBucketAccessKey | UpdateBucketBundle | UpdateBucket | SetResourceAccessForBucket | UpdateInstanceMetadataOptions | StartGUISession | StopGUISession | SetupInstanceHttps`
Required: No

 ** resourceName **   <a name="Lightsail-Type-Operation-resourceName"></a>
The resource name.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** resourceType **   <a name="Lightsail-Type-Operation-resourceType"></a>
The resource type.
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** status **   <a name="Lightsail-Type-Operation-status"></a>
The status of the operation.
Type: String
Valid Values: `NotStarted | Started | Failed | Completed | Succeeded`
Required: No

 ** statusChangedAt **   <a name="Lightsail-Type-Operation-statusChangedAt"></a>
The timestamp when the status was changed (`1479816991.349`).
Type: Timestamp
Required: No

## See Also
<a name="API_Operation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/Operation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/Operation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/Operation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
