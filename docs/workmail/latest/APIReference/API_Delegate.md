---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_Delegate.html
---

# Delegate
<a name="API_Delegate"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

The name of the attribute, which is one of the values defined in the UserAttribute enumeration.

## Contents
<a name="API_Delegate_Contents"></a>

 ** Id **   <a name="workmail-Type-Delegate-Id"></a>
The identifier for the user or group associated as the resource's delegate.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** Type **   <a name="workmail-Type-Delegate-Type"></a>
The type of the delegate: user or group.
Type: String
Valid Values: `GROUP | USER`
Required: Yes

## See Also
<a name="API_Delegate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/Delegate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/Delegate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/Delegate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
