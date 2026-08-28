---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_SuperuserParameters.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# SuperuserParameters
<a name="API_SuperuserParameters"></a>

Configuration information for the superuser.

## Contents
<a name="API_SuperuserParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** emailAddress **   <a name="finspace-Type-SuperuserParameters-emailAddress"></a>
The email address of the superuser.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+[.]+[A-Za-z]+`
Required: Yes

 ** firstName **   <a name="finspace-Type-SuperuserParameters-firstName"></a>
The first name of the superuser.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^[a-zA-Z0-9]{1,50}$`
Required: Yes

 ** lastName **   <a name="finspace-Type-SuperuserParameters-lastName"></a>
The last name of the superuser.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^[a-zA-Z0-9]{1,50}$`
Required: Yes

## See Also
<a name="API_SuperuserParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/SuperuserParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/SuperuserParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/SuperuserParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
