---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_SuccessfulAssociationResult.html
---

# SuccessfulAssociationResult
<a name="API_SuccessfulAssociationResult"></a>

Details about a successful association or disassociation between a code repository and a scan configuration.

## Contents
<a name="API_SuccessfulAssociationResult_Contents"></a>

 ** resource **   <a name="inspector2-Type-SuccessfulAssociationResult-resource"></a>
Identifies a specific resource in a code repository that will be scanned.
Type: [CodeSecurityResource](API_CodeSecurityResource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** scanConfigurationArn **   <a name="inspector2-Type-SuccessfulAssociationResult-scanConfigurationArn"></a>
The Amazon Resource Name (ARN) of the scan configuration that was successfully associated or disassociated.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:owner/(\d{12}|o-[a-z0-9]{10,32})/codesecurity-configuration/[a-f0-9-]{36}`
Required: No

## See Also
<a name="API_SuccessfulAssociationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/SuccessfulAssociationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/SuccessfulAssociationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/SuccessfulAssociationResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
