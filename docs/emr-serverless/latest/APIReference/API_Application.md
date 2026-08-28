---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Application.html
---

# Application
<a name="API_Application"></a>

Information about an application. Amazon EMR Serverless uses applications to run jobs.

## Contents
<a name="API_Application_Contents"></a>

 ** applicationId **   <a name="emrserverless-Type-Application-applicationId"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** arn **   <a name="emrserverless-Type-Application-arn"></a>
The ARN of the application.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `arn:(aws[a-zA-Z0-9-]*):emr-serverless:.+:(\d{12}):\/applications\/[0-9a-zA-Z]+`
Required: Yes

 ** createdAt **   <a name="emrserverless-Type-Application-createdAt"></a>
The date and time when the application run was created.
Type: Timestamp
Required: Yes

 ** releaseLabel **   <a name="emrserverless-Type-Application-releaseLabel"></a>
The Amazon EMR release associated with the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._/-]+`
Required: Yes

 ** state **   <a name="emrserverless-Type-Application-state"></a>
The state of the application.
Type: String
Valid Values: `CREATING | CREATED | STARTING | STARTED | STOPPING | STOPPED | TERMINATED`
Required: Yes

 ** type **   <a name="emrserverless-Type-Application-type"></a>
The type of application, such as Spark or Hive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** updatedAt **   <a name="emrserverless-Type-Application-updatedAt"></a>
The date and time when the application run was last updated.
Type: Timestamp
Required: Yes

 ** architecture **   <a name="emrserverless-Type-Application-architecture"></a>
The CPU architecture of an application.
Type: String
Valid Values: `ARM64 | X86_64`
Required: No

 ** autoStartConfiguration **   <a name="emrserverless-Type-Application-autoStartConfiguration"></a>
The configuration for an application to automatically start on job submission.
Type: [AutoStartConfig](API_AutoStartConfig.md) object
Required: No

 ** autoStopConfiguration **   <a name="emrserverless-Type-Application-autoStopConfiguration"></a>
The configuration for an application to automatically stop after a certain amount of time being idle.
Type: [AutoStopConfig](API_AutoStopConfig.md) object
Required: No

 ** diskEncryptionConfiguration **   <a name="emrserverless-Type-Application-diskEncryptionConfiguration"></a>
The configuration object that allows encrypting local disks.
Type: [DiskEncryptionConfiguration](API_DiskEncryptionConfiguration.md) object
Required: No

 ** identityCenterConfiguration **   <a name="emrserverless-Type-Application-identityCenterConfiguration"></a>
The IAM Identity Center configuration applied to enable trusted identity propagation.
Type: [IdentityCenterConfiguration](API_IdentityCenterConfiguration.md) object
Required: No

 ** imageConfiguration **   <a name="emrserverless-Type-Application-imageConfiguration"></a>
The image configuration applied to all worker types.
Type: [ImageConfiguration](API_ImageConfiguration.md) object
Required: No

 ** initialCapacity **   <a name="emrserverless-Type-Application-initialCapacity"></a>
The initial capacity of the application.
Type: String to [InitialCapacityConfig](API_InitialCapacityConfig.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Key Pattern: `[a-zA-Z]+[-_]*[a-zA-Z]+`
Required: No

 ** interactiveConfiguration **   <a name="emrserverless-Type-Application-interactiveConfiguration"></a>
The interactive configuration object that enables the interactive use cases for an application.
Type: [InteractiveConfiguration](API_InteractiveConfiguration.md) object
Required: No

 ** jobLevelCostAllocationConfiguration **   <a name="emrserverless-Type-Application-jobLevelCostAllocationConfiguration"></a>
The configuration object that enables job level cost allocation.
Type: [JobLevelCostAllocationConfiguration](API_JobLevelCostAllocationConfiguration.md) object
Required: No

 ** maximumCapacity **   <a name="emrserverless-Type-Application-maximumCapacity"></a>
The maximum capacity of the application. This is cumulative across all workers at any given point in time during the lifespan of the application is created. No new resources will be created once any one of the defined limits is hit.
Type: [MaximumAllowedResources](API_MaximumAllowedResources.md) object
Required: No

 ** monitoringConfiguration **   <a name="emrserverless-Type-Application-monitoringConfiguration"></a>
The configuration setting for monitoring.
Type: [MonitoringConfiguration](API_MonitoringConfiguration.md) object
Required: No

 ** name **   <a name="emrserverless-Type-Application-name"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._/#-]+`
Required: No

 ** networkConfiguration **   <a name="emrserverless-Type-Application-networkConfiguration"></a>
The network configuration for customer VPC connectivity for the application.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** runtimeConfiguration **   <a name="emrserverless-Type-Application-runtimeConfiguration"></a>
The [Configuration](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html) specifications of an application. Each configuration consists of a classification and properties. You use this parameter when creating or updating an application. To see the runtimeConfiguration object of an application, run the [GetApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetApplication.html) API operation.
Type: Array of [Configuration](API_Configuration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** schedulerConfiguration **   <a name="emrserverless-Type-Application-schedulerConfiguration"></a>
The scheduler configuration for batch and streaming jobs running on this application. Supported with release labels emr-7.0.0 and above.
Type: [SchedulerConfiguration](API_SchedulerConfiguration.md) object
Required: No

 ** stateDetails **   <a name="emrserverless-Type-Application-stateDetails"></a>
The state details of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** tags **   <a name="emrserverless-Type-Application-tags"></a>
The tags assigned to the application.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[A-Za-z0-9 /_.:=+@-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[A-Za-z0-9 /_.:=+@-]*`
Required: No

 ** workerTypeSpecifications **   <a name="emrserverless-Type-Application-workerTypeSpecifications"></a>
The specification applied to each worker type.
Type: String to [WorkerTypeSpecification](API_WorkerTypeSpecification.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Key Pattern: `[a-zA-Z]+[-_]*[a-zA-Z]+`
Required: No

## See Also
<a name="API_Application_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/Application)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/Application)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/Application)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
