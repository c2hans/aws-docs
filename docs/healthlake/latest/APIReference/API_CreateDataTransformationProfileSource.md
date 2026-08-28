---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_CreateDataTransformationProfileSource.html
---

# CreateDataTransformationProfileSource
<a name="API_CreateDataTransformationProfileSource"></a>

The source for initial content when creating a data transformation profile. Specify exactly one variant: a built-in starter profile, an existing profile version to clone, raw profile content, or a sample data file.

## Contents
<a name="API_CreateDataTransformationProfileSource_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ExistingVersionedProfileId **   <a name="HealthLake-Type-CreateDataTransformationProfileSource-ExistingVersionedProfileId"></a>
Creates the profile by cloning an existing profile at a specific version.
Type: [ExistingVersionedProfileSource](API_ExistingVersionedProfileSource.md) object
Required: No

 ** ProfileMapping **   <a name="HealthLake-Type-CreateDataTransformationProfileSource-ProfileMapping"></a>
Creates the profile from raw profile content that you provide directly. Use this variant for continuous integration and continuous delivery (CI/CD) workflows.
Type: [ProfileMappingSource](API_ProfileMappingSource.md) object
Required: No

 ** SampleData **   <a name="HealthLake-Type-CreateDataTransformationProfileSource-SampleData"></a>
Creates the profile from a sample data file stored in Amazon S3. Valid only when the source format is Comma-separated values (CSV).
Type: [SampleDataSource](API_SampleDataSource.md) object
Required: No

 ** StarterProfile **   <a name="HealthLake-Type-CreateDataTransformationProfileSource-StarterProfile"></a>
Creates the profile from a built-in starter profile. Valid only when the source format is Consolidated Clinical Document Architecture (C-CDA).
Type: [StarterProfileSource](API_StarterProfileSource.md) object
Required: No

## See Also
<a name="API_CreateDataTransformationProfileSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/CreateDataTransformationProfileSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/CreateDataTransformationProfileSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/CreateDataTransformationProfileSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
