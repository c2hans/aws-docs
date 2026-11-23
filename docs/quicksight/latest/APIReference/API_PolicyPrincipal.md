---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PolicyPrincipal.html
---

# PolicyPrincipal

A principal that a governance policy is assigned to.

## Contents
<a name="API_PolicyPrincipal_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** PrincipalArn **   <a name="QS-Type-PolicyPrincipal-PrincipalArn"></a>
The ARN of the user, group, or account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** PrincipalType **   <a name="QS-Type-PolicyPrincipal-PrincipalType"></a>
The type of the principal.
Type: String
Valid Values: `USER | GROUP | ACCOUNT`
Required: No

 ** Revision **   <a name="QS-Type-PolicyPrincipal-Revision"></a>
The current revision of the assignment.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** UpdatedAt **   <a name="QS-Type-PolicyPrincipal-UpdatedAt"></a>
The date and time that the assignment was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_PolicyPrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PolicyPrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PolicyPrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PolicyPrincipal)
