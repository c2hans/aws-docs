---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CursorConfiguration.html
---

# CursorConfiguration
<a name="API_CursorConfiguration"></a>

Cursor-based pagination configuration that defines how to handle pagination using cursor tokens or next page identifiers.

## Contents
<a name="API_CursorConfiguration_Contents"></a>

 ** NextPage **   <a name="Glue-Type-CursorConfiguration-NextPage"></a>
The parameter name or JSON path that contains the cursor or token for retrieving the next page of results.
Type: [ExtractedParameter](API_ExtractedParameter.md) object
Required: Yes

 ** LimitParameter **   <a name="Glue-Type-CursorConfiguration-LimitParameter"></a>
The parameter name used to specify the maximum number of results to return per page.
Type: [ExtractedParameter](API_ExtractedParameter.md) object
Required: No

## See Also
<a name="API_CursorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CursorConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CursorConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CursorConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
