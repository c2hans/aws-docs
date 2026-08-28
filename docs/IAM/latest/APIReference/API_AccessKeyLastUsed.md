---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_AccessKeyLastUsed.html
---

# AccessKeyLastUsed
<a name="API_AccessKeyLastUsed"></a>

Contains information about the last time an AWS access key was used since IAM began tracking this information on April 22, 2015.

This data type is used as a response element in the [GetAccessKeyLastUsed](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccessKeyLastUsed.html) operation.

## Contents
<a name="API_AccessKeyLastUsed_Contents"></a>

 ** Region **
The AWS Region where this access key was most recently used. The value for this field is "N/A" in the following situations:
+ The user does not have an access key.
+ An access key exists but has not been used since IAM began tracking this information.
+ There is no sign-in data associated with the user.
For more information about AWS Regions, see [Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the Amazon Web Services General Reference.
Type: String
Required: Yes

 ** ServiceName **
The name of the AWS service with which this access key was most recently used. The value of this field is "N/A" in the following situations:
+ The user does not have an access key.
+ An access key exists but has not been used since IAM started tracking this information.
+ There is no sign-in data associated with the user.
Type: String
Required: Yes

 ** LastUsedDate **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when the access key was most recently used. This field is null in the following situations:
+ The user does not have an access key.
+ An access key exists but has not been used since IAM began tracking this information.
+ There is no sign-in data associated with the user.
Type: Timestamp
Required: No

## See Also
<a name="API_AccessKeyLastUsed_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/AccessKeyLastUsed)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/AccessKeyLastUsed)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/AccessKeyLastUsed)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
