---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_BookingOptions.html
---

# BookingOptions
<a name="API_BookingOptions"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

At least one delegate must be associated to the resource to disable automatic replies from the resource.

## Contents
<a name="API_BookingOptions_Contents"></a>

 ** AutoAcceptRequests **   <a name="workmail-Type-BookingOptions-AutoAcceptRequests"></a>
The resource's ability to automatically reply to requests. If disabled, delegates must be associated to the resource.
Type: Boolean
Required: No

 ** AutoDeclineConflictingRequests **   <a name="workmail-Type-BookingOptions-AutoDeclineConflictingRequests"></a>
The resource's ability to automatically decline any conflicting requests.
Type: Boolean
Required: No

 ** AutoDeclineRecurringRequests **   <a name="workmail-Type-BookingOptions-AutoDeclineRecurringRequests"></a>
The resource's ability to automatically decline any recurring requests.
Type: Boolean
Required: No

## See Also
<a name="API_BookingOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/BookingOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/BookingOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/BookingOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
