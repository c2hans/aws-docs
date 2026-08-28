---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_Service.html
---

# Service
<a name="API_Service"></a>

Describes an AWS App Runner service. It can describe a service in any state, including deleted services.

This type contains the full information about a service, including configuration details. It's returned by the [CreateService](https://docs.aws.amazon.com/apprunner/latest/api/API_CreateService.html), [DescribeService](https://docs.aws.amazon.com/apprunner/latest/api/API_DescribeService.html), and [DeleteService](https://docs.aws.amazon.com/apprunner/latest/api/API_DeleteService.html) actions. A subset of this information is returned by the [ListServices](https://docs.aws.amazon.com/apprunner/latest/api/API_ListServices.html) action using the [ServiceSummary](https://docs.aws.amazon.com/apprunner/latest/api/API_ServiceSummary.html) type.

## Contents
<a name="API_Service_Contents"></a>

 ** AutoScalingConfigurationSummary **   <a name="apprunner-Type-Service-AutoScalingConfigurationSummary"></a>
Summary information for the App Runner automatic scaling configuration resource that's associated with this service.
Type: [AutoScalingConfigurationSummary](API_AutoScalingConfigurationSummary.md) object
Required: Yes

 ** CreatedAt **   <a name="apprunner-Type-Service-CreatedAt"></a>
The time when the App Runner service was created. It's in the Unix time stamp format.
Type: Timestamp
Required: Yes

 ** InstanceConfiguration **   <a name="apprunner-Type-Service-InstanceConfiguration"></a>
The runtime configuration of instances (scaling units) of this service.
Type: [InstanceConfiguration](API_InstanceConfiguration.md) object
Required: Yes

 ** NetworkConfiguration **   <a name="apprunner-Type-Service-NetworkConfiguration"></a>
Configuration settings related to network traffic of the web application that this service runs.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: Yes

 ** ServiceArn **   <a name="apprunner-Type-Service-ServiceArn"></a>
The Amazon Resource Name (ARN) of this service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: Yes

 ** ServiceId **   <a name="apprunner-Type-Service-ServiceId"></a>
An ID that App Runner generated for this service. It's unique within the AWS Region.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`
Required: Yes

 ** ServiceName **   <a name="apprunner-Type-Service-ServiceName"></a>
The customer-provided service name.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Pattern: `[A-Za-z0-9][A-Za-z0-9-_]{3,39}`
Required: Yes

 ** SourceConfiguration **   <a name="apprunner-Type-Service-SourceConfiguration"></a>
The source deployed to the App Runner service. It can be a code or an image repository.
Type: [SourceConfiguration](API_SourceConfiguration.md) object
Required: Yes

 ** Status **   <a name="apprunner-Type-Service-Status"></a>
The current state of the App Runner service. These particular values mean the following.
+  `CREATE_FAILED` – The service failed to create. The failed service isn't usable, and still counts towards your service quota. To troubleshoot this failure, read the failure events and logs, change any parameters that need to be fixed, and rebuild your service using `UpdateService`.
+  `DELETE_FAILED` – The service failed to delete and can't be successfully recovered. Retry the service deletion call to ensure that all related resources are removed.
Type: String
Valid Values: `CREATE_FAILED | RUNNING | DELETED | DELETE_FAILED | PAUSED | OPERATION_IN_PROGRESS`
Required: Yes

 ** UpdatedAt **   <a name="apprunner-Type-Service-UpdatedAt"></a>
The time when the App Runner service was last updated at. It's in the Unix time stamp format.
Type: Timestamp
Required: Yes

 ** DeletedAt **   <a name="apprunner-Type-Service-DeletedAt"></a>
The time when the App Runner service was deleted. It's in the Unix time stamp format.
Type: Timestamp
Required: No

 ** EncryptionConfiguration **   <a name="apprunner-Type-Service-EncryptionConfiguration"></a>
The encryption key that App Runner uses to encrypt the service logs and the copy of the source repository that App Runner maintains for the service. It can be either a customer-provided encryption key or an AWS managed key.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** HealthCheckConfiguration **   <a name="apprunner-Type-Service-HealthCheckConfiguration"></a>
The settings for the health check that App Runner performs to monitor the health of this service.
Type: [HealthCheckConfiguration](API_HealthCheckConfiguration.md) object
Required: No

 ** ObservabilityConfiguration **   <a name="apprunner-Type-Service-ObservabilityConfiguration"></a>
The observability configuration of this service.
Type: [ServiceObservabilityConfiguration](API_ServiceObservabilityConfiguration.md) object
Required: No

 ** ServiceUrl **   <a name="apprunner-Type-Service-ServiceUrl"></a>
A subdomain URL that App Runner generated for this service. You can use this URL to access your service web application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`
Required: No

## See Also
<a name="API_Service_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/Service)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/Service)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/Service)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
