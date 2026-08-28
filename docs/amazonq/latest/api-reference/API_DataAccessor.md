---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DataAccessor.html
---

# DataAccessor
<a name="API_DataAccessor"></a>

Provides summary information about a data accessor.

## Contents
<a name="API_DataAccessor_Contents"></a>

 ** authenticationDetail **   <a name="qbusiness-Type-DataAccessor-authenticationDetail"></a>
The authentication configuration details for the data accessor. This specifies how the ISV authenticates when accessing data through this data accessor.
Type: [DataAccessorAuthenticationDetail](API_DataAccessorAuthenticationDetail.md) object
Required: No

 ** createdAt **   <a name="qbusiness-Type-DataAccessor-createdAt"></a>
The timestamp when the data accessor was created.
Type: Timestamp
Required: No

 ** dataAccessorArn **   <a name="qbusiness-Type-DataAccessor-dataAccessorArn"></a>
The Amazon Resource Name (ARN) of the data accessor.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** dataAccessorId **   <a name="qbusiness-Type-DataAccessor-dataAccessorId"></a>
The unique identifier of the data accessor.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** displayName **   <a name="qbusiness-Type-DataAccessor-displayName"></a>
The friendly name of the data accessor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** idcApplicationArn **   <a name="qbusiness-Type-DataAccessor-idcApplicationArn"></a>
The Amazon Resource Name (ARN) of the associated IAM Identity Center application.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: No

 ** principal **   <a name="qbusiness-Type-DataAccessor-principal"></a>
The Amazon Resource Name (ARN) of the IAM role for the ISV associated with this data accessor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1284.
Pattern: `arn:aws:iam::[0-9]{12}:role/[a-zA-Z0-9_/+=,.@-]+`
Required: No

 ** updatedAt **   <a name="qbusiness-Type-DataAccessor-updatedAt"></a>
The timestamp when the data accessor was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_DataAccessor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DataAccessor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DataAccessor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DataAccessor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
