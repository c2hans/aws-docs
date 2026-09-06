---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RegisteredService.html
---

# RegisteredService
<a name="API_RegisteredService"></a>

Represents a registered service with its configuration and accessible resources.

## Contents
<a name="API_RegisteredService_Contents"></a>

 ** createdAt **   <a name="devopsagent-Type-RegisteredService-createdAt"></a>
The timestamp when the service was registered.
Type: Timestamp
Required: Yes

 ** serviceId **   <a name="devopsagent-Type-RegisteredService-serviceId"></a>
The unique identifier of a service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** serviceType **   <a name="devopsagent-Type-RegisteredService-serviceType"></a>
The service type e.g github or dynatrace
Type: String
Valid Values: `github | slack | azure | azuredevops | dynatrace | servicenow | pagerduty | gitlab | eventChannel | mcpservernewrelic | mcpservergrafana | mcpserverdatadog | mcpserver | mcpserversplunk | azureidentity | mcpserversigv4 | remoteagent | remoteagentsigv4`
Required: Yes

 ** updatedAt **   <a name="devopsagent-Type-RegisteredService-updatedAt"></a>
The timestamp when the service was last updated.
Type: Timestamp
Required: Yes

 ** accessibleResources **   <a name="devopsagent-Type-RegisteredService-accessibleResources"></a>
List of accessible resources for this service.
Type: Array of JSON values
Required: No

 ** additionalServiceDetails **   <a name="devopsagent-Type-RegisteredService-additionalServiceDetails"></a>
Additional details specific to the service type.
Type: [AdditionalServiceDetails](API_AdditionalServiceDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** kmsKeyArn **   <a name="devopsagent-Type-RegisteredService-kmsKeyArn"></a>
The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.
Type: String
Length Constraints: Minimum length of 20.
Pattern: `arn:aws[a-zA-Z-]*:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** name **   <a name="devopsagent-Type-RegisteredService-name"></a>
The display name of the registered service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}\p{S}\p{Z}]+`
Required: No

 ** privateConnectionName **   <a name="devopsagent-Type-RegisteredService-privateConnectionName"></a>
The name of the private connection used for VPC connectivity.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `[a-z0-9]([a-z0-9-]*[a-z0-9])?`
Required: No

## See Also
<a name="API_RegisteredService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/RegisteredService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/RegisteredService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/RegisteredService)
