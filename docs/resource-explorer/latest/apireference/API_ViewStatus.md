---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ViewStatus.html
---

# ViewStatus
<a name="API_ViewStatus"></a>

Contains information about the status of a Resource Explorer view operation in a specific Region.

## Contents
<a name="API_ViewStatus_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ErrorDetails **   <a name="resourceexplorer-Type-ViewStatus-ErrorDetails"></a>
Details about any error that occurred during the view operation.
Type: [ErrorDetails](API_ErrorDetails.md) object
Required: No

 ** Status **   <a name="resourceexplorer-Type-ViewStatus-Status"></a>
The current status of the view operation. Valid values are `SUCCEEDED`, `FAILED`, `IN_PROGRESS`, or `SKIPPED`.
Type: String
Valid Values: `SUCCEEDED | FAILED | IN_PROGRESS | SKIPPED`
Required: No

 ** View **   <a name="resourceexplorer-Type-ViewStatus-View"></a>
A view is a structure that defines a set of filters that provide a view into the information in the AWS Resource Explorer index. The filters specify which information from the index is visible to the users of the view. For example, you can specify filters that include only resources that are tagged with the key "ENV" and the value "DEVELOPMENT" in the results returned by this view. You could also create a second view that includes only resources that are tagged with "ENV" and "PRODUCTION".
Type: [View](API_View.md) object
Required: No

## See Also
<a name="API_ViewStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/ViewStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/ViewStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/ViewStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resource Explorer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resource-explorer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
