---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AccessControl.html
---

# AccessControl
<a name="API_AccessControl"></a>

A list of principals. Each principal can be either a `USER` or a `GROUP` and can be designated document access permissions of either `ALLOW` or `DENY`.

## Contents
<a name="API_AccessControl_Contents"></a>

 ** principals **   <a name="qbusiness-Type-AccessControl-principals"></a>
Contains a list of principals, where a principal can be either a `USER` or a `GROUP`. Each principal can be have the following type of document access: `ALLOW` or `DENY`.
Type: Array of [Principal](API_Principal.md) objects
Required: Yes

 ** memberRelation **   <a name="qbusiness-Type-AccessControl-memberRelation"></a>
Describes the member relation within a principal list.
Type: String
Valid Values: `AND | OR`
Required: No

## See Also
<a name="API_AccessControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/AccessControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/AccessControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/AccessControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
