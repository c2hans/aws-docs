---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ProtectedQueryDistributeOutputConfigurationLocation.html
---

# ProtectedQueryDistributeOutputConfigurationLocation
<a name="API_ProtectedQueryDistributeOutputConfigurationLocation"></a>

 Specifies where you'll distribute the results of your protected query. You must configure either an S3 destination or a collaboration member destination.

## Contents
<a name="API_ProtectedQueryDistributeOutputConfigurationLocation_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** member **   <a name="API-Type-ProtectedQueryDistributeOutputConfigurationLocation-member"></a>
 Contains configuration details for the protected query member output.
Type: [ProtectedQueryMemberOutputConfiguration](API_ProtectedQueryMemberOutputConfiguration.md) object
Required: No

 ** s3 **   <a name="API-Type-ProtectedQueryDistributeOutputConfigurationLocation-s3"></a>
Contains the configuration to write the query results to S3.
Type: [ProtectedQueryS3OutputConfiguration](API_ProtectedQueryS3OutputConfiguration.md) object
Required: No

## See Also
<a name="API_ProtectedQueryDistributeOutputConfigurationLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ProtectedQueryDistributeOutputConfigurationLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ProtectedQueryDistributeOutputConfigurationLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ProtectedQueryDistributeOutputConfigurationLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
