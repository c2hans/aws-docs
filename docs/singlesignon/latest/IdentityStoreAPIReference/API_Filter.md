---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

A query filter used by `ListUsers` and `ListGroups`. This filter object provides the attribute name and attribute value to search users or groups.

## Contents
<a name="API_Filter_Contents"></a>

 ** AttributePath **   <a name="singlesignon-Type-Filter-AttributePath"></a>
The attribute path that is used to specify which attribute name to search. Length limit is 255 characters. For example, `UserName` is a valid attribute path for the ` ListUsers` API, and `DisplayName` is a valid attribute path for the ` ListGroups` API.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?:\p{L}+:\p{L}+:\p{L}+(?:\.\p{L}+){0,3}|\p{L}+(?:\.\p{L}+){0,2})`
Required: Yes

 ** AttributeValue **   <a name="singlesignon-Type-Filter-AttributeValue"></a>
Represents the data for an attribute. Each attribute value is described as a name-value pair.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: Yes

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/Filter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Identity Store. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
