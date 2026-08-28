---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_PhysicalResource.html
---

# PhysicalResource
<a name="API_PhysicalResource"></a>

Defines a physical resource. A physical resource is a resource that exists in your account. It can be identified using an Amazon Resource Name (ARN) or an AWS Resilience Hub-native identifier.

## Contents
<a name="API_PhysicalResource_Contents"></a>

 ** logicalResourceId **   <a name="resiliencehub-Type-PhysicalResource-logicalResourceId"></a>
Logical identifier of the resource.
Type: [LogicalResourceId](API_LogicalResourceId.md) object
Required: Yes

 ** physicalResourceId **   <a name="resiliencehub-Type-PhysicalResource-physicalResourceId"></a>
Identifier of the physical resource.
Type: [PhysicalResourceId](API_PhysicalResourceId.md) object
Required: Yes

 ** resourceType **   <a name="resiliencehub-Type-PhysicalResource-resourceType"></a>
Type of resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** additionalInfo **   <a name="resiliencehub-Type-PhysicalResource-additionalInfo"></a>
Additional configuration parameters for an AWS Resilience Hub application. If you want to implement `additionalInfo` through the AWS Resilience Hub console rather than using an API call, see [Configure the application configuration parameters](https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html).
Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account.
Key: `"failover-regions"`
Value: `"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"`
Type: String to array of strings map
Key Pattern: `\S{1,128}`
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** appComponents **   <a name="resiliencehub-Type-PhysicalResource-appComponents"></a>
The Application Components that belong to this resource.
Type: Array of [AppComponent](API_AppComponent.md) objects
Required: No

 ** excluded **   <a name="resiliencehub-Type-PhysicalResource-excluded"></a>
Indicates if a resource is included or excluded from the assessment.
Type: Boolean
Required: No

 ** parentResourceName **   <a name="resiliencehub-Type-PhysicalResource-parentResourceName"></a>
Name of the parent resource.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: No

 ** resourceName **   <a name="resiliencehub-Type-PhysicalResource-resourceName"></a>
The name of the resource.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: No

 ** sourceType **   <a name="resiliencehub-Type-PhysicalResource-sourceType"></a>
Type of input source.
Type: String
Valid Values: `AppTemplate | Discovered`
Required: No

## See Also
<a name="API_PhysicalResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/PhysicalResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/PhysicalResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/PhysicalResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
