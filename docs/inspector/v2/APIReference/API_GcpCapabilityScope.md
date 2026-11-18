---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_GcpCapabilityScope.html
---

# GcpCapabilityScope
<a name="API_GcpCapabilityScope"></a>

The scope of Google Cloud Platform (GCP) resources that Amazon Inspector scans for a single scanning type, including the scope level, the targeted resources, and the current state.

## Contents
<a name="API_GcpCapabilityScope_Contents"></a>

 ** scopeType **   <a name="inspector2-Type-GcpCapabilityScope-scopeType"></a>
The type of scope: `ORGANIZATION`, which scans all projects in the GCP organization, or `PROJECT`, which scans only the specified GCP projects.
Type: String
Valid Values: `TENANT | SUBSCRIPTION | ORGANIZATION | PROJECT`
Required: Yes

 ** scopeValues **   <a name="inspector2-Type-GcpCapabilityScope-scopeValues"></a>
The GCP project IDs to scan when `scopeType` is `PROJECT`. Not used when `scopeType` is `ORGANIZATION`. Amazon Inspector scans the organization of the AWS Config connector.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `([a-z][a-z0-9-]{4,28}[a-z0-9]|[0-9]{6,30})`
Required: No

 ** state **   <a name="inspector2-Type-GcpCapabilityScope-state"></a>
The current state of the scope configuration.
Type: String
Valid Values: `ACTIVE | PENDING | ERROR | DISABLED`
Required: No

 ** stateReason **   <a name="inspector2-Type-GcpCapabilityScope-stateReason"></a>
The reason for the current state of the scope configuration.
Type: String
Required: No

## See Also
<a name="API_GcpCapabilityScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/GcpCapabilityScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/GcpCapabilityScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/GcpCapabilityScope)
