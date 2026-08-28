---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ActivityType.html
---

# ActivityType
<a name="API_ActivityType"></a>

Represents an activity type.

## Contents
<a name="API_ActivityType_Contents"></a>

 ** name **   <a name="SWF-Type-ActivityType-name"></a>
The name of this activity.
The combination of activity type name and version must be unique within a domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** version **   <a name="SWF-Type-ActivityType-version"></a>
The version of this activity.
The combination of activity type name and version must be unique with in a domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## See Also
<a name="API_ActivityType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ActivityType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ActivityType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ActivityType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
