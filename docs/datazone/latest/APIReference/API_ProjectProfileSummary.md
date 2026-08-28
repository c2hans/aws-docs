---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ProjectProfileSummary.html
---

# ProjectProfileSummary
<a name="API_ProjectProfileSummary"></a>

The summary of a project profile.

## Contents
<a name="API_ProjectProfileSummary_Contents"></a>

 ** createdBy **   <a name="datazone-Type-ProjectProfileSummary-createdBy"></a>
The user who created the project profile.
Type: String
Required: Yes

 ** domainId **   <a name="datazone-Type-ProjectProfileSummary-domainId"></a>
The domain ID of the project profile.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** id **   <a name="datazone-Type-ProjectProfileSummary-id"></a>
The ID of the project profile.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** name **   <a name="datazone-Type-ProjectProfileSummary-name"></a>
The name of a project profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: Yes

 ** createdAt **   <a name="datazone-Type-ProjectProfileSummary-createdAt"></a>
The timestamp of when the project profile was created.
Type: Timestamp
Required: No

 ** description **   <a name="datazone-Type-ProjectProfileSummary-description"></a>
The description of the project profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** domainUnitId **   <a name="datazone-Type-ProjectProfileSummary-domainUnitId"></a>
The domain unit ID of the project profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`
Required: No

 ** lastUpdatedAt **   <a name="datazone-Type-ProjectProfileSummary-lastUpdatedAt"></a>
The timestamp at which a project profile was last updated.
Type: Timestamp
Required: No

 ** status **   <a name="datazone-Type-ProjectProfileSummary-status"></a>
The status of a project profile.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_ProjectProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ProjectProfileSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ProjectProfileSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ProjectProfileSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
