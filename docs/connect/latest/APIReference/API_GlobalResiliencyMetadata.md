---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_GlobalResiliencyMetadata.html
---

# GlobalResiliencyMetadata
<a name="API_GlobalResiliencyMetadata"></a>

Information about the global resiliency configuration for the contact, including traffic distribution details.

## Contents
<a name="API_GlobalResiliencyMetadata_Contents"></a>

 ** ActiveRegion **   <a name="connect-Type-GlobalResiliencyMetadata-ActiveRegion"></a>
The current AWS region in which the contact is active. This indicates where the contact is being processed in real-time.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** OriginRegion **   <a name="connect-Type-GlobalResiliencyMetadata-OriginRegion"></a>
The AWS region where the contact was originally created and initiated. This may differ from the ActiveRegion if the contact has been transferred across regions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** TrafficDistributionGroupId **   <a name="connect-Type-GlobalResiliencyMetadata-TrafficDistributionGroupId"></a>
The identifier of the traffic distribution group.
Type: String
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

## See Also
<a name="API_GlobalResiliencyMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/GlobalResiliencyMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/GlobalResiliencyMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/GlobalResiliencyMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
