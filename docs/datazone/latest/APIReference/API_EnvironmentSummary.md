---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_EnvironmentSummary.html
---

# EnvironmentSummary
<a name="API_EnvironmentSummary"></a>

The details of an environment.

## Contents
<a name="API_EnvironmentSummary_Contents"></a>

 ** createdBy **   <a name="datazone-Type-EnvironmentSummary-createdBy"></a>
The Amazon DataZone user who created the environment.
Type: String
Required: Yes

 ** domainId **   <a name="datazone-Type-EnvironmentSummary-domainId"></a>
The identifier of the Amazon DataZone domain in which the environment exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** name **   <a name="datazone-Type-EnvironmentSummary-name"></a>
The name of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: Yes

 ** projectId **   <a name="datazone-Type-EnvironmentSummary-projectId"></a>
The identifier of the project in which the environment exists.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** provider **   <a name="datazone-Type-EnvironmentSummary-provider"></a>
The provider of the environment.
Type: String
Required: Yes

 ** awsAccountId **   <a name="datazone-Type-EnvironmentSummary-awsAccountId"></a>
The identifier of the AWS account in which an environment exists.
Type: String
Pattern: `\d{12}`
Required: No

 ** awsAccountRegion **   <a name="datazone-Type-EnvironmentSummary-awsAccountRegion"></a>
The AWS Region in which an environment exists.
Type: String
Pattern: `[a-z]{2}-[a-z]{4,10}-\d`
Required: No

 ** createdAt **   <a name="datazone-Type-EnvironmentSummary-createdAt"></a>
The timestamp of when the environment was created.
Type: Timestamp
Required: No

 ** description **   <a name="datazone-Type-EnvironmentSummary-description"></a>
The description of the environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** environmentConfigurationId **   <a name="datazone-Type-EnvironmentSummary-environmentConfigurationId"></a>
The configuration ID with which the environment is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** environmentConfigurationName **   <a name="datazone-Type-EnvironmentSummary-environmentConfigurationName"></a>
The configuration name with which the environment is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: No

 ** environmentProfileId **   <a name="datazone-Type-EnvironmentSummary-environmentProfileId"></a>
The identifier of the environment profile with which the environment was created.
Type: String
Pattern: `[a-zA-Z0-9_-]{0,36}`
Required: No

 ** id **   <a name="datazone-Type-EnvironmentSummary-id"></a>
The identifier of the environment.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** status **   <a name="datazone-Type-EnvironmentSummary-status"></a>
The status of the environment.
Type: String
Valid Values: `ACTIVE | CREATING | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED | VALIDATION_FAILED | SUSPENDED | DISABLED | EXPIRED | DELETED | INACCESSIBLE`
Required: No

 ** updatedAt **   <a name="datazone-Type-EnvironmentSummary-updatedAt"></a>
The timestamp of when the environment was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_EnvironmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/EnvironmentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/EnvironmentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/EnvironmentSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
