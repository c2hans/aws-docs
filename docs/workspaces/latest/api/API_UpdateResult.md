---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateResult.html
---

# UpdateResult
<a name="API_UpdateResult"></a>

Describes whether a WorkSpace image needs to be updated with the latest drivers and other components required by Amazon WorkSpaces.

**Note**
Only Windows 10 WorkSpace images can be programmatically updated at this time.

## Contents
<a name="API_UpdateResult_Contents"></a>

 ** Description **   <a name="WorkSpaces-Type-UpdateResult-Description"></a>
A description of whether updates for the WorkSpace image are pending or available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_./() -]+$`
Required: No

 ** UpdateAvailable **   <a name="WorkSpaces-Type-UpdateResult-UpdateAvailable"></a>
Indicates whether updated drivers or other components are available for the specified WorkSpace image.
Type: Boolean
Required: No

## See Also
<a name="API_UpdateResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/UpdateResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/UpdateResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/UpdateResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
