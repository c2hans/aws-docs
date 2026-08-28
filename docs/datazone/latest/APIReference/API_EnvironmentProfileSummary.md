---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_EnvironmentProfileSummary.html
---

# EnvironmentProfileSummary
<a name="API_EnvironmentProfileSummary"></a>

The details of an environment profile.

## Contents
<a name="API_EnvironmentProfileSummary_Contents"></a>

 ** createdBy **   <a name="datazone-Type-EnvironmentProfileSummary-createdBy"></a>
The Amazon DataZone user who created the environment profile.
Type: String
Required: Yes

 ** domainId **   <a name="datazone-Type-EnvironmentProfileSummary-domainId"></a>
The identifier of the Amazon DataZone domain in which the environment profile exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** environmentBlueprintId **   <a name="datazone-Type-EnvironmentProfileSummary-environmentBlueprintId"></a>
The identifier of a blueprint with which an environment profile is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** id **   <a name="datazone-Type-EnvironmentProfileSummary-id"></a>
The identifier of the environment profile.
Type: String
Pattern: `[a-zA-Z0-9_-]{0,36}`
Required: Yes

 ** name **   <a name="datazone-Type-EnvironmentProfileSummary-name"></a>
The name of the environment profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: Yes

 ** awsAccountId **   <a name="datazone-Type-EnvironmentProfileSummary-awsAccountId"></a>
The identifier of an AWS account in which an environment profile exists.
Type: String
Pattern: `\d{12}`
Required: No

 ** awsAccountRegion **   <a name="datazone-Type-EnvironmentProfileSummary-awsAccountRegion"></a>
The AWS Region in which an environment profile exists.
Type: String
Pattern: `[a-z]{2}-[a-z]{4,10}-\d`
Required: No

 ** createdAt **   <a name="datazone-Type-EnvironmentProfileSummary-createdAt"></a>
The timestamp of when an environment profile was created.
Type: Timestamp
Required: No

 ** description **   <a name="datazone-Type-EnvironmentProfileSummary-description"></a>
The description of the environment profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** projectId **   <a name="datazone-Type-EnvironmentProfileSummary-projectId"></a>
The identifier of a project in which an environment profile exists.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** updatedAt **   <a name="datazone-Type-EnvironmentProfileSummary-updatedAt"></a>
The timestamp of when the environment profile was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_EnvironmentProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/EnvironmentProfileSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/EnvironmentProfileSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/EnvironmentProfileSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
