---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BrandDetail.html
---

# BrandDetail
<a name="API_BrandDetail"></a>

The details of the brand.

## Contents
<a name="API_BrandDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BrandId **   <a name="QS-Type-BrandDetail-BrandId"></a>
The ID of the Quick brand.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Arn **   <a name="QS-Type-BrandDetail-Arn"></a>
The Amazon Resource Name (ARN) of the brand.
Type: String
Required: No

 ** BrandStatus **   <a name="QS-Type-BrandDetail-BrandStatus"></a>
The status of the brand.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_SUCCEEDED | CREATE_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED`
Required: No

 ** CreatedTime **   <a name="QS-Type-BrandDetail-CreatedTime"></a>
The time that the brand was created.
Type: Timestamp
Required: No

 ** Errors **   <a name="QS-Type-BrandDetail-Errors"></a>
A list of errors that occurred during the most recent brand operation.
Type: Array of strings
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-BrandDetail-LastUpdatedTime"></a>
The last time the brand was updated.
Type: Timestamp
Required: No

 ** Logo **   <a name="QS-Type-BrandDetail-Logo"></a>
The logo details.
Type: [Logo](API_Logo.md) object
Required: No

 ** VersionId **   <a name="QS-Type-BrandDetail-VersionId"></a>
The ID of the version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: No

 ** VersionStatus **   <a name="QS-Type-BrandDetail-VersionStatus"></a>
The status of the version.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_SUCCEEDED | CREATE_FAILED`
Required: No

## See Also
<a name="API_BrandDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BrandDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BrandDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BrandDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
