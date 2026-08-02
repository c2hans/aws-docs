---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_RoleLastUsed.html
---

# RoleLastUsed
<a name="API_RoleLastUsed"></a>

Contains information about the last time that an IAM role was used. This includes the date and time and the Region in which the role was last used. Activity is only reported for the trailing 400 days. This period can be shorter if your Region began supporting these features within the last year. The role might have been used more than 400 days ago. For more information, see [Regions where data is tracked](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period) in the *IAM user Guide*.

This data type is returned as a response element in the [GetRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetRole.html) and [GetAccountAuthorizationDetails](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountAuthorizationDetails.html) operations.

## Contents
<a name="API_RoleLastUsed_Contents"></a>

 ** LastUsedDate **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601) that the role was last used.
This field is null if the role has not been used within the IAM tracking period. For more information about the tracking period, see [Regions where data is tracked](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period) in the *IAM User Guide*.
Type: Timestamp
Required: No

 ** Region **
The name of the AWS Region in which the role was last used.
Type: String
Required: No

## See Also
<a name="API_RoleLastUsed_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/RoleLastUsed)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/RoleLastUsed)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/RoleLastUsed)
