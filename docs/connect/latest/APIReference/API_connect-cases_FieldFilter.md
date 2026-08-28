---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_FieldFilter.html
---

# FieldFilter
<a name="API_connect-cases_FieldFilter"></a>

A filter for fields. Only one value can be provided.

## Contents
<a name="API_connect-cases_FieldFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** contains **   <a name="connect-Type-connect-cases_FieldFilter-contains"></a>
Object containing field identifier and value information.
Type: [FieldValue](API_connect-cases_FieldValue.md) object
Required: No

 ** equalTo **   <a name="connect-Type-connect-cases_FieldFilter-equalTo"></a>
Object containing field identifier and value information.
Type: [FieldValue](API_connect-cases_FieldValue.md) object
Required: No

 ** greaterThan **   <a name="connect-Type-connect-cases_FieldFilter-greaterThan"></a>
Object containing field identifier and value information.
Type: [FieldValue](API_connect-cases_FieldValue.md) object
Required: No

 ** greaterThanOrEqualTo **   <a name="connect-Type-connect-cases_FieldFilter-greaterThanOrEqualTo"></a>
Object containing field identifier and value information.
Type: [FieldValue](API_connect-cases_FieldValue.md) object
Required: No

 ** lessThan **   <a name="connect-Type-connect-cases_FieldFilter-lessThan"></a>
Object containing field identifier and value information.
Type: [FieldValue](API_connect-cases_FieldValue.md) object
Required: No

 ** lessThanOrEqualTo **   <a name="connect-Type-connect-cases_FieldFilter-lessThanOrEqualTo"></a>
Object containing field identifier and value information.
Type: [FieldValue](API_connect-cases_FieldValue.md) object
Required: No

## See Also
<a name="API_connect-cases_FieldFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/FieldFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/FieldFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/FieldFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
