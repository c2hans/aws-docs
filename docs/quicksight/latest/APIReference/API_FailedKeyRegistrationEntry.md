---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FailedKeyRegistrationEntry.html
---

# FailedKeyRegistrationEntry
<a name="API_FailedKeyRegistrationEntry"></a>

An entry that appears when a `KeyRegistration` update to Quick Sight fails.

## Contents
<a name="API_FailedKeyRegistrationEntry_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Message **   <a name="QS-Type-FailedKeyRegistrationEntry-Message"></a>
A message that provides information about why a `FailedKeyRegistrationEntry` error occurred.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** SenderFault **   <a name="QS-Type-FailedKeyRegistrationEntry-SenderFault"></a>
A boolean that indicates whether a `FailedKeyRegistrationEntry` resulted from user error. If the value of this property is `True`, the error was caused by user error. If the value of this property is `False`, the error occurred on the backend. If your job continues fail and with a `False` `SenderFault` value, contact Support.
Type: Boolean
Required: Yes

 ** StatusCode **   <a name="QS-Type-FailedKeyRegistrationEntry-StatusCode"></a>
The HTTP status of a `FailedKeyRegistrationEntry` error.
Type: Integer
Required: Yes

 ** KeyArn **   <a name="QS-Type-FailedKeyRegistrationEntry-KeyArn"></a>
The ARN of the AWS KMS key that failed to update.
Type: String
Required: No

## See Also
<a name="API_FailedKeyRegistrationEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FailedKeyRegistrationEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FailedKeyRegistrationEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FailedKeyRegistrationEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
