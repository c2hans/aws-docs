---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ProjectSummary.html
---

# ProjectSummary
<a name="API_ProjectSummary"></a>

The details of a Amazon DataZone project.

## Contents
<a name="API_ProjectSummary_Contents"></a>

 ** createdBy **   <a name="datazone-Type-ProjectSummary-createdBy"></a>
The Amazon DataZone user who created the project.
Type: String
Required: Yes

 ** domainId **   <a name="datazone-Type-ProjectSummary-domainId"></a>
The identifier of a Amazon DataZone domain where the project exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** id **   <a name="datazone-Type-ProjectSummary-id"></a>
The identifier of a project.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** name **   <a name="datazone-Type-ProjectSummary-name"></a>
The name of a project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: Yes

 ** createdAt **   <a name="datazone-Type-ProjectSummary-createdAt"></a>
The timestamp of when a project was created.
Type: Timestamp
Required: No

 ** description **   <a name="datazone-Type-ProjectSummary-description"></a>
The description of a project.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** domainUnitId **   <a name="datazone-Type-ProjectSummary-domainUnitId"></a>
The ID of the domain unit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`
Required: No

 ** failureReasons **   <a name="datazone-Type-ProjectSummary-failureReasons"></a>
Specifies the error message that is returned if the operation cannot be successfully completed.
Type: Array of [ProjectDeletionError](API_ProjectDeletionError.md) objects
Required: No

 ** projectCategory **   <a name="datazone-Type-ProjectSummary-projectCategory"></a>
The category of the project.
Type: String
Required: No

 ** projectStatus **   <a name="datazone-Type-ProjectSummary-projectStatus"></a>
The status of the project.
Type: String
Valid Values: `ACTIVE | DELETING | DELETE_FAILED | UPDATING | UPDATE_FAILED | MOVING`
Required: No

 ** updatedAt **   <a name="datazone-Type-ProjectSummary-updatedAt"></a>
The timestamp of when the project was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ProjectSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ProjectSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ProjectSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ProjectSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
