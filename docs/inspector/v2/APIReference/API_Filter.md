---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

Details about a filter.

## Contents
<a name="API_Filter_Contents"></a>

 ** action **   <a name="inspector2-Type-Filter-action"></a>
The action that is to be applied to the findings that match the filter.
Type: String
Valid Values: `NONE | SUPPRESS`
Required: Yes

 ** arn **   <a name="inspector2-Type-Filter-arn"></a>
The Amazon Resource Number (ARN) associated with this filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** createdAt **   <a name="inspector2-Type-Filter-createdAt"></a>
The date and time this filter was created at.
Type: Timestamp
Required: Yes

 ** criteria **   <a name="inspector2-Type-Filter-criteria"></a>
Details on the filter criteria associated with this filter.
Type: [FilterCriteria](API_FilterCriteria.md) object
Required: Yes

 ** name **   <a name="inspector2-Type-Filter-name"></a>
The name of the filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** ownerId **   <a name="inspector2-Type-Filter-ownerId"></a>
The AWS account ID of the account that created the filter.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 34.
Pattern: `.*(^\d{12}$)|(^o-[a-z0-9]{10,32}$).*`
Required: Yes

 ** updatedAt **   <a name="inspector2-Type-Filter-updatedAt"></a>
The date and time the filter was last updated at.
Type: Timestamp
Required: Yes

 ** description **   <a name="inspector2-Type-Filter-description"></a>
A description of the filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** reason **   <a name="inspector2-Type-Filter-reason"></a>
The reason for the filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** tags **   <a name="inspector2-Type-Filter-tags"></a>
The tags attached to the filter.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Filter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
