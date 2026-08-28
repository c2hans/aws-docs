---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_WebExperience.html
---

# WebExperience
<a name="API_WebExperience"></a>

Provides information for an Amazon Q Business web experience.

## Contents
<a name="API_WebExperience_Contents"></a>

 ** createdAt **   <a name="qbusiness-Type-WebExperience-createdAt"></a>
The Unix timestamp when the Amazon Q Business application was last updated.
Type: Timestamp
Required: No

 ** defaultEndpoint **   <a name="qbusiness-Type-WebExperience-defaultEndpoint"></a>
The endpoint URLs for your Amazon Q Business web experience. The URLs are unique and fully hosted by AWS.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(https?|ftp|file)://([^\s]*)`
Required: No

 ** status **   <a name="qbusiness-Type-WebExperience-status"></a>
The status of your Amazon Q Business web experience.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED | PENDING_AUTH_CONFIG`
Required: No

 ** updatedAt **   <a name="qbusiness-Type-WebExperience-updatedAt"></a>
The Unix timestamp when your Amazon Q Business web experience was updated.
Type: Timestamp
Required: No

 ** webExperienceId **   <a name="qbusiness-Type-WebExperience-webExperienceId"></a>
The identifier of your Amazon Q Business web experience.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`
Required: No

## See Also
<a name="API_WebExperience_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/WebExperience)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/WebExperience)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/WebExperience)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
