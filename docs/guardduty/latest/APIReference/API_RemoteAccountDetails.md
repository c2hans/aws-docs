---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_RemoteAccountDetails.html
---

# RemoteAccountDetails
<a name="API_RemoteAccountDetails"></a>

Contains details about the remote AWS account that made the API call.

## Contents
<a name="API_RemoteAccountDetails_Contents"></a>

 ** accountId **   <a name="guardduty-Type-RemoteAccountDetails-accountId"></a>
The AWS account ID of the remote API caller.
Type: String
Required: No

 ** affiliated **   <a name="guardduty-Type-RemoteAccountDetails-affiliated"></a>
Details on whether the AWS account of the remote API caller is related to your GuardDuty environment. If this value is `True` the API caller is affiliated to your account in some way. If it is `False` the API caller is from outside your environment.
Type: Boolean
Required: No

## See Also
<a name="API_RemoteAccountDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/RemoteAccountDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/RemoteAccountDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/RemoteAccountDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
