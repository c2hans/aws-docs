---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CustomUpdateContent.html
---

# CustomUpdateContent
<a name="API_connect-cases_CustomUpdateContent"></a>

Represents the updated content of a `Custom` related item.

## Contents
<a name="API_connect-cases_CustomUpdateContent_Contents"></a>

 ** fields **   <a name="connect-Type-connect-cases_CustomUpdateContent-fields"></a>
List of updated field values for the `Custom` related item. All existing and new fields, and their associated values should be included. Fields not included as part of this request will be removed.
Type: Array of [FieldValue](API_connect-cases_FieldValue.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

## See Also
<a name="API_connect-cases_CustomUpdateContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/CustomUpdateContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/CustomUpdateContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/CustomUpdateContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
