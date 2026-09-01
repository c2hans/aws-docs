---
source_url: https://docs.aws.amazon.com/agent-registry/latest/APIReference/API_BatchGetDiscoverableRegistryRecordError.html
---

# BatchGetDiscoverableRegistryRecordError
<a name="API_BatchGetDiscoverableRegistryRecordError"></a>

 Describes why a requested record could not be retrieved.

## Contents
<a name="API_BatchGetDiscoverableRegistryRecordError_Contents"></a>

 ** errorCode **   <a name="agentregistry-Type-BatchGetDiscoverableRegistryRecordError-errorCode"></a>
 The machine-readable reason that the record could not be retrieved.
Type: String
Valid Values: `RESOURCE_NOT_FOUND | ACCESS_DENIED | INTERNAL_ERROR`
Required: Yes

 ** recordId **   <a name="agentregistry-Type-BatchGetDiscoverableRegistryRecordError-recordId"></a>
 The identifier of the record that could not be retrieved, echoed from the request in the same format that you supplied (ARN or record ID).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/)?[a-zA-Z0-9]{12}`
Required: Yes

 ** registryId **   <a name="agentregistry-Type-BatchGetDiscoverableRegistryRecordError-registryId"></a>
 The identifier of the registry the record was requested from, echoed from the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`
Required: Yes

 ** message **   <a name="agentregistry-Type-BatchGetDiscoverableRegistryRecordError-message"></a>
 An optional human-readable detail about the error. Do not parse this value programmatically.
Type: String
Required: No

## See Also
<a name="API_BatchGetDiscoverableRegistryRecordError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/BatchGetDiscoverableRegistryRecordError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/BatchGetDiscoverableRegistryRecordError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/BatchGetDiscoverableRegistryRecordError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Agent Registry Data Plane API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agent-registry` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
