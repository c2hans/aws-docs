---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_GcpCapabilityScopeInput.html
---

# GcpCapabilityScopeInput
<a name="API_GcpCapabilityScopeInput"></a>

The scope of Google Cloud Platform (GCP) resources to scan for a single scanning type. Provide this as part of a `GcpScopeConfigurationInput` when you create or update a connector.

## Contents
<a name="API_GcpCapabilityScopeInput_Contents"></a>

 ** scopeType **   <a name="inspector2-Type-GcpCapabilityScopeInput-scopeType"></a>
The type of scope: `ORGANIZATION`, which scans all projects in the GCP organization, or `PROJECT`, which scans only the specified GCP projects.
Type: String
Valid Values: `TENANT | SUBSCRIPTION | ORGANIZATION | PROJECT`
Required: Yes

 ** scopeValues **   <a name="inspector2-Type-GcpCapabilityScopeInput-scopeValues"></a>
The GCP project IDs to scan. Required when `scopeType` is `PROJECT`. Don't specify scope values when `scopeType` is `ORGANIZATION`. Amazon Inspector scans the organization of the AWS Config connector.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `([a-z][a-z0-9-]{4,28}[a-z0-9]|[0-9]{6,30})`
Required: No

## See Also
<a name="API_GcpCapabilityScopeInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/GcpCapabilityScopeInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/GcpCapabilityScopeInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/GcpCapabilityScopeInput)
