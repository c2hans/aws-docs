---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_FailedAssociationResult.html
---

# FailedAssociationResult
<a name="API_FailedAssociationResult"></a>

Details about a failed attempt to associate or disassociate a code repository with a scan configuration.

## Contents
<a name="API_FailedAssociationResult_Contents"></a>

 ** resource **   <a name="inspector2-Type-FailedAssociationResult-resource"></a>
Identifies a specific resource in a code repository that will be scanned.
Type: [CodeSecurityResource](API_CodeSecurityResource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** scanConfigurationArn **   <a name="inspector2-Type-FailedAssociationResult-scanConfigurationArn"></a>
The Amazon Resource Name (ARN) of the scan configuration that failed to be associated or disassociated.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:owner/(\d{12}|o-[a-z0-9]{10,32})/codesecurity-configuration/[a-f0-9-]{36}`
Required: No

 ** statusCode **   <a name="inspector2-Type-FailedAssociationResult-statusCode"></a>
The status code indicating why the association or disassociation failed.
Type: String
Valid Values: `INTERNAL_ERROR | ACCESS_DENIED | SCAN_CONFIGURATION_NOT_FOUND | INVALID_INPUT | RESOURCE_NOT_FOUND | QUOTA_EXCEEDED`
Required: No

 ** statusMessage **   <a name="inspector2-Type-FailedAssociationResult-statusMessage"></a>
A message explaining why the association or disassociation failed.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_FailedAssociationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/FailedAssociationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/FailedAssociationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/FailedAssociationResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
