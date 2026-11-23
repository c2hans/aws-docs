---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_EmailApprover.html
---

# EmailApprover

An approver who is identified by an email address.

## Contents
<a name="API_marketplace-agreements_EmailApprover_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** emailAddress **   <a name="AWSMarketplaceService-Type-marketplace-agreements_EmailApprover-emailAddress"></a>
The email address of the approver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}`
Required: Yes

 ** name **   <a name="AWSMarketplaceService-Type-marketplace-agreements_EmailApprover-name"></a>
The name of the approver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_marketplace-agreements_EmailApprover_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/EmailApprover)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/EmailApprover)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/EmailApprover)
