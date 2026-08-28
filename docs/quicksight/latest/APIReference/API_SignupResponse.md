---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SignupResponse.html
---

# SignupResponse
<a name="API_SignupResponse"></a>

A `SignupResponse` object that contains a summary of a newly created account.

## Contents
<a name="API_SignupResponse_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** accountName **   <a name="QS-Type-SignupResponse-accountName"></a>
The name of your Quick Sight account.
Type: String
Required: No

 ** directoryType **   <a name="QS-Type-SignupResponse-directoryType"></a>
The type of Active Directory that is being used to authenticate the Amazon Quick Sight account. Valid values are `SIMPLE_AD`, `AD_CONNECTOR`, and `MICROSOFT_AD`.
Type: String
Required: No

 ** IAMUser **   <a name="QS-Type-SignupResponse-IAMUser"></a>
A Boolean that is `TRUE` if the Amazon Quick Sight uses IAM as an authentication method.
Type: Boolean
Required: No

 ** userLoginName **   <a name="QS-Type-SignupResponse-userLoginName"></a>
The user login name for your Amazon Quick Sight account.
Type: String
Required: No

## See Also
<a name="API_SignupResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SignupResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SignupResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SignupResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
