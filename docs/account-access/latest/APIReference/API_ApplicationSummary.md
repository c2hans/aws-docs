---
source_url: https://docs.aws.amazon.com/account-access/latest/APIReference/API_ApplicationSummary.html
---

# ApplicationSummary
<a name="API_ApplicationSummary"></a>

Contains summary information about an account access manager application.

## Contents
<a name="API_ApplicationSummary_Contents"></a>

 ** applicationArn **   <a name="accountaccess-Type-ApplicationSummary-applicationArn"></a>
The ARN of the IAM Identity Center application created for this account access manager application. This property is not required or supported as input. It can be read after creation.
Type: String
Length Constraints: Minimum length of 49. Maximum length of 2048.
Pattern: `arn:[a-z0-9-]+:account-access:[a-z0-9]+(-[a-z0-9]+)*:[0-9]{12}:application/[a-zA-Z0-9-]+`
Required: Yes

 ** createdAt **   <a name="accountaccess-Type-ApplicationSummary-createdAt"></a>
The date and time when the application was created.
Type: Timestamp
Required: Yes

 ** updatedAt **   <a name="accountaccess-Type-ApplicationSummary-updatedAt"></a>
The date and time when the application was last updated.
Type: Timestamp
Required: Yes

 ** tenantId **   <a name="accountaccess-Type-ApplicationSummary-tenantId"></a>
The tenant identifier associated with the application.
Type: String
Required: No

## See Also
<a name="API_ApplicationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-2018-05-10/ApplicationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-2018-05-10/ApplicationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-2018-05-10/ApplicationSummary)
