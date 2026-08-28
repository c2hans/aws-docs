---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_StatusDetails.html
---

# StatusDetails
<a name="API_StatusDetails"></a>

Details about the status of a resource.

## Contents
<a name="API_StatusDetails_Contents"></a>

 ** message **   <a name="API-Type-StatusDetails-message"></a>
The error message that was returned. The message is intended for human consumption and can change at any time. Use the `statusCode` for programmatic error handling.
Type: String
Required: No

 ** statusCode **   <a name="API-Type-StatusDetails-statusCode"></a>
The status code that was returned. The status code is intended for programmatic error handling. Clean Rooms ML will not change the status code for existing error conditions.
Type: String
Required: No

## See Also
<a name="API_StatusDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/StatusDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/StatusDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/StatusDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
