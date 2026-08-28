---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_TagFilter.html
---

# TagFilter
<a name="API_amazon-q-connect_TagFilter"></a>

An object that can be used to specify Tag conditions.

## Contents
<a name="API_amazon-q-connect_TagFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** andConditions **   <a name="connect-Type-amazon-q-connect_TagFilter-andConditions"></a>
A list of conditions which would be applied together with an `AND` condition.
Type: Array of [TagCondition](API_amazon-q-connect_TagCondition.md) objects
Required: No

 ** orConditions **   <a name="connect-Type-amazon-q-connect_TagFilter-orConditions"></a>
A list of conditions which would be applied together with an `OR` condition.
Type: Array of [OrCondition](API_amazon-q-connect_OrCondition.md) objects
Required: No

 ** tagCondition **   <a name="connect-Type-amazon-q-connect_TagFilter-tagCondition"></a>
A leaf node condition which can be used to specify a tag condition.
Type: [TagCondition](API_amazon-q-connect_TagCondition.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_TagFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/TagFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/TagFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/TagFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
