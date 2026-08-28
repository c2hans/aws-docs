---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_BatchPermissionsFailureEntry.html
---

# BatchPermissionsFailureEntry
<a name="API_BatchPermissionsFailureEntry"></a>

A list of failures when performing a batch grant or batch revoke operation.

## Contents
<a name="API_BatchPermissionsFailureEntry_Contents"></a>

 ** Error **   <a name="lakeformation-Type-BatchPermissionsFailureEntry-Error"></a>
An error message that applies to the failure of the entry.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

 ** RequestEntry **   <a name="lakeformation-Type-BatchPermissionsFailureEntry-RequestEntry"></a>
An identifier for an entry of the batch request.
Type: [BatchPermissionsRequestEntry](API_BatchPermissionsRequestEntry.md) object
Required: No

## See Also
<a name="API_BatchPermissionsFailureEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/BatchPermissionsFailureEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/BatchPermissionsFailureEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/BatchPermissionsFailureEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
