---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_OrganizationSummary.html
---

# OrganizationSummary
<a name="API_OrganizationSummary"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

The representation of an organization.

## Contents
<a name="API_OrganizationSummary_Contents"></a>

 ** Alias **   <a name="workmail-Type-OrganizationSummary-Alias"></a>
The alias associated with the organization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 62.
Pattern: `^(?!d-)([\da-zA-Z]+)([-][\da-zA-Z]+)*`
Required: No

 ** DefaultMailDomain **   <a name="workmail-Type-OrganizationSummary-DefaultMailDomain"></a>
The default email domain associated with the organization.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9.-]+`
Required: No

 ** ErrorMessage **   <a name="workmail-Type-OrganizationSummary-ErrorMessage"></a>
The error message associated with the organization. It is only present if unexpected behavior has occurred with regards to the organization. It provides insight or solutions regarding unexpected behavior.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** OrganizationId **   <a name="workmail-Type-OrganizationSummary-OrganizationId"></a>
The identifier associated with the organization.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: No

 ** State **   <a name="workmail-Type-OrganizationSummary-State"></a>
The state associated with the organization.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_OrganizationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/OrganizationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/OrganizationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/OrganizationSummary)
