---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_Contact.html
---

# Contact
<a name="API_invoicing_Contact"></a>

Represents contact information for a person or role associated with the procurement portal preference.

## Contents
<a name="API_invoicing_Contact_Contents"></a>

 ** Email **   <a name="awscostmanagement-Type-invoicing_Contact-Email"></a>
The email address of the contact person or role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
Required: No

 ** Name **   <a name="awscostmanagement-Type-invoicing_Contact-Name"></a>
The name of the contact person or role.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_invoicing_Contact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/Contact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/Contact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/Contact)
