---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_UpdateTarget.html
---

# UpdateTarget
<a name="API_UpdateTarget"></a>

A maintenance track that you can switch the current track to.

## Contents
<a name="API_UpdateTarget_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DatabaseVersion **
The cluster version for the new maintenance track.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** MaintenanceTrackName **
The name of the new maintenance track.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** SupportedOperations.SupportedOperation.N **
A list of operations supported by the maintenance track.
Type: Array of [SupportedOperation](API_SupportedOperation.md) objects
Required: No

## See Also
<a name="API_UpdateTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/UpdateTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/UpdateTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/UpdateTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
