---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SnapshotUserConfiguration.html
---

# SnapshotUserConfiguration
<a name="API_SnapshotUserConfiguration"></a>

A structure that contains information about the users that the dashboard snapshot is generated for.

**Important**
When using identity-enhanced session credentials, set the UserConfiguration request attribute to null. Otherwise, the request will be invalid.

## Contents
<a name="API_SnapshotUserConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AnonymousUsers **   <a name="QS-Type-SnapshotUserConfiguration-AnonymousUsers"></a>
An array of records that describe the anonymous users that the dashboard snapshot is generated for.
Type: Array of [SnapshotAnonymousUser](API_SnapshotAnonymousUser.md) objects
Array Members: Fixed number of 1 item.
Required: No

## See Also
<a name="API_SnapshotUserConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SnapshotUserConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SnapshotUserConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SnapshotUserConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
