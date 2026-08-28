---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateSvmActiveDirectoryConfiguration.html
---

# UpdateSvmActiveDirectoryConfiguration
<a name="API_UpdateSvmActiveDirectoryConfiguration"></a>

Specifies updates to an FSx for ONTAP storage virtual machine's (SVM) Microsoft Active Directory (AD) configuration. Note that account credentials are not returned in the response payload.

## Contents
<a name="API_UpdateSvmActiveDirectoryConfiguration_Contents"></a>

 ** NetBiosName **   <a name="FSx-Type-UpdateSvmActiveDirectoryConfiguration-NetBiosName"></a>
Specifies an updated NetBIOS name of the AD computer object `NetBiosName` to which an SVM is joined.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`
Required: No

 ** SelfManagedActiveDirectoryConfiguration **   <a name="FSx-Type-UpdateSvmActiveDirectoryConfiguration-SelfManagedActiveDirectoryConfiguration"></a>
Specifies changes you are making to the self-managed Microsoft Active Directory configuration to which an FSx for Windows File Server file system or an FSx for ONTAP SVM is joined.
Type: [SelfManagedActiveDirectoryConfigurationUpdates](API_SelfManagedActiveDirectoryConfigurationUpdates.md) object
Required: No

## See Also
<a name="API_UpdateSvmActiveDirectoryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateSvmActiveDirectoryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateSvmActiveDirectoryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateSvmActiveDirectoryConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
