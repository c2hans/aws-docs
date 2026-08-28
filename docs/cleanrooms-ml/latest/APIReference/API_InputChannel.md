---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_InputChannel.html
---

# InputChannel
<a name="API_InputChannel"></a>

Provides information about the data source that is used to create an ML input channel.

## Contents
<a name="API_InputChannel_Contents"></a>

 ** dataSource **   <a name="API-Type-InputChannel-dataSource"></a>
The data source that is used to create the ML input channel.
Type: [InputChannelDataSource](API_InputChannelDataSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** roleArn **   <a name="API-Type-InputChannel-roleArn"></a>
The Amazon Resource Name (ARN) of the role used to run the query specified in the `dataSource` field of the input channel.
Passing a role across AWS accounts is not allowed. If you pass a role that isn't in your account, you get an `AccessDeniedException` error.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:iam::[0-9]{12}:role/.+`
Required: Yes

## See Also
<a name="API_InputChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/InputChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/InputChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/InputChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
