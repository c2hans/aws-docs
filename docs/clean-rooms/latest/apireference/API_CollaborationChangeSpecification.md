---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CollaborationChangeSpecification.html
---

# CollaborationChangeSpecification
<a name="API_CollaborationChangeSpecification"></a>

Defines the specific changes being requested for a collaboration, including configuration modifications and approval requirements.

## Contents
<a name="API_CollaborationChangeSpecification_Contents"></a>

 ** autoApprovedChangeTypes **   <a name="API-Type-CollaborationChangeSpecification-autoApprovedChangeTypes"></a>
Defines requested updates to properties of the collaboration. Currently, this only supports modifying which change types are auto-approved for the collaboration.
Type: Array of strings
Valid Values: `ADD_MEMBER | GRANT_RECEIVE_RESULTS_ABILITY | REVOKE_RECEIVE_RESULTS_ABILITY | GRANT_EXPORT_QUERY_ANALYSIS_LOG_ABILITY | REVOKE_EXPORT_QUERY_ANALYSIS_LOG_ABILITY`
Required: No

## See Also
<a name="API_CollaborationChangeSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/CollaborationChangeSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/CollaborationChangeSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/CollaborationChangeSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
