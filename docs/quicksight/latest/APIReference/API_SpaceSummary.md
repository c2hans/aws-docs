---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SpaceSummary.html
---

# SpaceSummary
<a name="API_SpaceSummary"></a>

A summary of an Amazon QuickSight space.

## Contents
<a name="API_SpaceSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** spaceId **   <a name="QS-Type-SpaceSummary-spaceId"></a>
The ID of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9a-zA-Z-_=.+]+`
Required: Yes

 ** consumedSourceDocCount **   <a name="QS-Type-SpaceSummary-consumedSourceDocCount"></a>
The number of consumed source documents.
Type: Integer
Required: No

 ** consumedSourceSize **   <a name="QS-Type-SpaceSummary-consumedSourceSize"></a>
The total consumed source size in bytes.
Type: Long
Required: No

 ** createdAt **   <a name="QS-Type-SpaceSummary-createdAt"></a>
The date and time that the space was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="QS-Type-SpaceSummary-createdBy"></a>
The user who created the space.
Type: String
Required: No

 ** createdByArn **   <a name="QS-Type-SpaceSummary-createdByArn"></a>
The ARN of the user who created the space.
Type: String
Required: No

 ** description **   <a name="QS-Type-SpaceSummary-description"></a>
The description of the space.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `[\P{C}\n\r\t\f\v\p{Cf}]*`
Required: No

 ** name **   <a name="QS-Type-SpaceSummary-name"></a>
The display name of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[\P{C}\n\r\t\f\v\p{Cf}]*`
Required: No

 ** resourcesCount **   <a name="QS-Type-SpaceSummary-resourcesCount"></a>
The number of resources in the space.
Type: Integer
Required: No

 ** spaceArn **   <a name="QS-Type-SpaceSummary-spaceArn"></a>
The ARN of the space.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** updatedAt **   <a name="QS-Type-SpaceSummary-updatedAt"></a>
The date and time that the space was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_SpaceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SpaceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SpaceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SpaceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
