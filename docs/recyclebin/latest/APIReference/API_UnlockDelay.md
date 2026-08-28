---
source_url: https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_UnlockDelay.html
---

# UnlockDelay
<a name="API_UnlockDelay"></a>

Information about the retention rule unlock delay. The unlock delay is the period after which a retention rule can be modified or edited after it has been unlocked by a user with the required permissions. The retention rule can't be modified or deleted during the unlock delay.

## Contents
<a name="API_UnlockDelay_Contents"></a>

 ** UnlockDelayUnit **   <a name="recyclebin-Type-UnlockDelay-UnlockDelayUnit"></a>
The unit of time in which to measure the unlock delay. Currently, the unlock delay can be measured only in days.
Type: String
Valid Values: `DAYS`
Required: Yes

 ** UnlockDelayValue **   <a name="recyclebin-Type-UnlockDelay-UnlockDelayValue"></a>
The unlock delay period, measured in the unit specified for ** UnlockDelayUnit**.
Type: Integer
Valid Range: Minimum value of 7. Maximum value of 30.
Required: Yes

## See Also
<a name="API_UnlockDelay_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rbin-2021-06-15/UnlockDelay)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rbin-2021-06-15/UnlockDelay)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rbin-2021-06-15/UnlockDelay)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Recycle Bin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recyclebin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
