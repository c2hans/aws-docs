---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ProjectSummary.html
---

# ProjectSummary
<a name="API_ProjectSummary"></a>

Contains project summary information.

## Contents
<a name="API_ProjectSummary_Contents"></a>

 ** id **   <a name="iotsitewise-Type-ProjectSummary-id"></a>
The ID of the project.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** name **   <a name="iotsitewise-Type-ProjectSummary-name"></a>
The name of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** creationDate **   <a name="iotsitewise-Type-ProjectSummary-creationDate"></a>
The date the project was created, in Unix epoch time.
Type: Timestamp
Required: No

 ** description **   <a name="iotsitewise-Type-ProjectSummary-description"></a>
The project's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** lastUpdateDate **   <a name="iotsitewise-Type-ProjectSummary-lastUpdateDate"></a>
The date the project was last updated, in Unix epoch time.
Type: Timestamp
Required: No

## See Also
<a name="API_ProjectSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ProjectSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ProjectSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ProjectSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
