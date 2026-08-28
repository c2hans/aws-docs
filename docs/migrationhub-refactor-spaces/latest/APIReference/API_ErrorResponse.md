---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ErrorResponse.html
---

# ErrorResponse
<a name="API_ErrorResponse"></a>

Error associated with a resource returned for a Get or List resource response.

## Contents
<a name="API_ErrorResponse_Contents"></a>

 ** AccountId **   <a name="migrationhubrefactorspaces-Type-ErrorResponse-AccountId"></a>
The AWS account ID of the resource owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** AdditionalDetails **   <a name="migrationhubrefactorspaces-Type-ErrorResponse-AdditionalDetails"></a>
Additional details about the error.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Code **   <a name="migrationhubrefactorspaces-Type-ErrorResponse-Code"></a>
The error code associated with the error.
Type: String
Valid Values: `INVALID_RESOURCE_STATE | RESOURCE_LIMIT_EXCEEDED | RESOURCE_CREATION_FAILURE | RESOURCE_UPDATE_FAILURE | SERVICE_ENDPOINT_HEALTH_CHECK_FAILURE | RESOURCE_DELETION_FAILURE | RESOURCE_RETRIEVAL_FAILURE | RESOURCE_IN_USE | RESOURCE_NOT_FOUND | STATE_TRANSITION_FAILURE | REQUEST_LIMIT_EXCEEDED | NOT_AUTHORIZED`
Required: No

 ** Message **   <a name="migrationhubrefactorspaces-Type-ErrorResponse-Message"></a>
The message associated with the error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\p{Alnum}\p{Punct}\p{Blank}]*`
Required: No

 ** ResourceIdentifier **   <a name="migrationhubrefactorspaces-Type-ErrorResponse-ResourceIdentifier"></a>
The ID of the resource.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `.*(^(env|svc|pxy|rte|app)-([0-9A-Za-z]{10}$)).*`
Required: No

 ** ResourceType **   <a name="migrationhubrefactorspaces-Type-ErrorResponse-ResourceType"></a>
The type of resource.
Type: String
Valid Values: `ENVIRONMENT | APPLICATION | ROUTE | SERVICE | TRANSIT_GATEWAY | TRANSIT_GATEWAY_ATTACHMENT | API_GATEWAY | NLB | TARGET_GROUP | LOAD_BALANCER_LISTENER | VPC_LINK | LAMBDA | VPC | SUBNET | ROUTE_TABLE | SECURITY_GROUP | VPC_ENDPOINT_SERVICE_CONFIGURATION | RESOURCE_SHARE | IAM_ROLE`
Required: No

## See Also
<a name="API_ErrorResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/ErrorResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/ErrorResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/ErrorResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub Refactor Spaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-refactor-spaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
