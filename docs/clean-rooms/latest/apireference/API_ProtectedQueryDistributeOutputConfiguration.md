---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ProtectedQueryDistributeOutputConfiguration.html
---

# ProtectedQueryDistributeOutputConfiguration
<a name="API_ProtectedQueryDistributeOutputConfiguration"></a>

 Specifies the configuration for distributing protected query results to multiple receivers, including S3 and collaboration members.

## Contents
<a name="API_ProtectedQueryDistributeOutputConfiguration_Contents"></a>

 ** locations **   <a name="API-Type-ProtectedQueryDistributeOutputConfiguration-locations"></a>
 A list of locations where you want to distribute the protected query results. Each location must specify either an S3 destination or a collaboration member destination.
You can't specify more than one S3 location.
You can't specify the query runner's account as a member location.
You must include either an S3 or member output configuration for each location, but not both.
Type: Array of [ProtectedQueryDistributeOutputConfigurationLocation](API_ProtectedQueryDistributeOutputConfigurationLocation.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## See Also
<a name="API_ProtectedQueryDistributeOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ProtectedQueryDistributeOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ProtectedQueryDistributeOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ProtectedQueryDistributeOutputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
