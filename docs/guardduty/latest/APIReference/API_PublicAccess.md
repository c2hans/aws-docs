---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_PublicAccess.html
---

# PublicAccess
<a name="API_PublicAccess"></a>

Describes the public access policies that apply to the S3 bucket.

## Contents
<a name="API_PublicAccess_Contents"></a>

 ** effectivePermission **   <a name="guardduty-Type-PublicAccess-effectivePermission"></a>
Describes the effective permission on this bucket after factoring all attached policies.
Type: String
Required: No

 ** permissionConfiguration **   <a name="guardduty-Type-PublicAccess-permissionConfiguration"></a>
Contains information about how permissions are configured for the S3 bucket.
Type: [PermissionConfiguration](API_PermissionConfiguration.md) object
Required: No

## See Also
<a name="API_PublicAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/PublicAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/PublicAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/PublicAccess)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
