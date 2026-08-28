---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_SvmActiveDirectoryConfiguration.html
---

# SvmActiveDirectoryConfiguration
<a name="API_SvmActiveDirectoryConfiguration"></a>

Describes the Microsoft Active Directory (AD) directory configuration to which the FSx for ONTAP storage virtual machine (SVM) is joined. Note that account credentials are not returned in the response payload.

## Contents
<a name="API_SvmActiveDirectoryConfiguration_Contents"></a>

 ** NetBiosName **   <a name="FSx-Type-SvmActiveDirectoryConfiguration-NetBiosName"></a>
The NetBIOS name of the AD computer object to which the SVM is joined.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`
Required: No

 ** SelfManagedActiveDirectoryConfiguration **   <a name="FSx-Type-SvmActiveDirectoryConfiguration-SelfManagedActiveDirectoryConfiguration"></a>
The configuration of the self-managed Microsoft Active Directory (AD) directory to which the Windows File Server or ONTAP storage virtual machine (SVM) instance is joined.
Type: [SelfManagedActiveDirectoryAttributes](API_SelfManagedActiveDirectoryAttributes.md) object
Required: No

## See Also
<a name="API_SvmActiveDirectoryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/SvmActiveDirectoryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/SvmActiveDirectoryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/SvmActiveDirectoryConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
