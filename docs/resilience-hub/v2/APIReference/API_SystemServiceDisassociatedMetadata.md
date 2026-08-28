---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_SystemServiceDisassociatedMetadata.html
---

# SystemServiceDisassociatedMetadata
<a name="API_SystemServiceDisassociatedMetadata"></a>

Metadata for a system service disassociated event.

## Contents
<a name="API_SystemServiceDisassociatedMetadata_Contents"></a>

 ** comment **   <a name="ngresiliencehub-Type-SystemServiceDisassociatedMetadata-comment"></a>
A comment about the disassociation.
Type: String
Required: No

 ** serviceArn **   <a name="ngresiliencehub-Type-SystemServiceDisassociatedMetadata-serviceArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** serviceName **   <a name="ngresiliencehub-Type-SystemServiceDisassociatedMetadata-serviceName"></a>
The name of the disassociated service.
Type: String
Required: No

 ** userJourneysAffected **   <a name="ngresiliencehub-Type-SystemServiceDisassociatedMetadata-userJourneysAffected"></a>
The user journeys affected by the disassociation.
Type: Array of strings
Required: No

## See Also
<a name="API_SystemServiceDisassociatedMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/SystemServiceDisassociatedMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/SystemServiceDisassociatedMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/SystemServiceDisassociatedMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
