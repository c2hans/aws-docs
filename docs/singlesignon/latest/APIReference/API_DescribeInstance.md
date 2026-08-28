---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeInstance.html
---

# DescribeInstance
<a name="API_DescribeInstance"></a>

Returns the details of an instance of IAM Identity Center. The status can be one of the following:
+  `CREATE_IN_PROGRESS` - The instance is in the process of being created. When the instance is ready for use, DescribeInstance returns the status of `ACTIVE`. While the instance is in the `CREATE_IN_PROGRESS` state, you can call only DescribeInstance and DeleteInstance operations.
+  `DELETE_IN_PROGRESS` - The instance is being deleted. Returns `AccessDeniedException` after the delete operation completes.
+  `ACTIVE` - The instance is active.

## Request Syntax
<a name="API_DescribeInstance_RequestSyntax"></a>

```
{
   "InstanceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceArn](#API_DescribeInstance_RequestSyntax) **   <a name="singlesignon-DescribeInstance-request-InstanceArn"></a>
The ARN of the instance of IAM Identity Center under which the operation will run.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

## Response Syntax
<a name="API_DescribeInstance_ResponseSyntax"></a>

```
{
   "CreatedDate": number,
   "EncryptionConfigurationDetails": {
      "EncryptionStatus": "string",
      "EncryptionStatusReason": "string",
      "KeyType": "string",
      "KmsKeyArn": "string"
   },
   "IdentityStoreId": "string",
   "InstanceArn": "string",
   "Name": "string",
   "OwnerAccountId": "string",
   "PermissionSetsEnabled": boolean,
   "Status": "string",
   "StatusReason": "string"
}
```

## Response Elements
<a name="API_DescribeInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedDate](#API_DescribeInstance_ResponseSyntax) **   <a name="singlesignon-DescribeInstance-response-CreatedDate"></a>
The date the instance was created.
Type: Timestamp

 ** [EncryptionConfigurationDetails](#API_DescribeInstance_ResponseSyntax) **   <a name="singlesignon-DescribeInstance-response-EncryptionConfigurationDetails"></a>
Contains the encryption configuration for your IAM Identity Center instance, including the encryption status, KMS key type, and KMS key ARN.
Type: [EncryptionConfigurationDetails](API_EncryptionConfigurationDetails.md) object

 ** [IdentityStoreId](#API_DescribeInstance_ResponseSyntax) **   <a name="singlesignon-DescribeInstance-response-IdentityStoreId"></a>
The identifier of the identity store that is connected to the instance of IAM Identity Center.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]*`

 ** [InstanceArn](#API_DescribeInstance_ResponseSyntax) **   <a name="singlesignon-DescribeInstance-response-InstanceArn"></a>
The ARN of the instance of IAM Identity Center under which the operation will run. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`

 ** [Name](#API_DescribeInstance_ResponseSyntax) **   <a name="singlesignon-DescribeInstance-response-Name"></a>
Specifies the instance name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\w+=,.@-]+`

 ** [OwnerAccountId](#API_DescribeInstance_ResponseSyntax) **   <a name="singlesignon-DescribeInstance-response-OwnerAccountId"></a>
The identifier of the AWS account for which the instance was created.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

 ** [PermissionSetsEnabled](#API_DescribeInstance_ResponseSyntax) **   <a name="singlesignon-DescribeInstance-response-PermissionSetsEnabled"></a>
Indicates whether permission sets are enabled for this Identity Center instance.
Type: Boolean

 ** [Status](#API_DescribeInstance_ResponseSyntax) **   <a name="singlesignon-DescribeInstance-response-Status"></a>
The status of the instance.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | DELETE_IN_PROGRESS | ACTIVE`

 ** [StatusReason](#API_DescribeInstance_ResponseSyntax) **   <a name="singlesignon-DescribeInstance-response-StatusReason"></a>
Provides additional context about the current status of the IAM Identity Center instance. This field is particularly useful when an instance is in a non-ACTIVE state, such as CREATE\_FAILED. When an instance fails to create or update, this field contains information about the cause, which may include issues with KMS key configuration, permission problems with the specified KMS key, or service-related errors.
Type: String
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`

## Errors
<a name="API_DescribeInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** Reason **
The reason for the access denied exception.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure with an internal server.
HTTP Status Code: 500

 ** ThrottlingException **
Indicates that the principal has crossed the throttling limits of the API operations.
 ** Reason **
The reason for the throttling exception.
HTTP Status Code: 400

 ** ValidationException **
The request failed because it contains a syntax error.
 ** Reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/DescribeInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/DescribeInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/DescribeInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/DescribeInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/DescribeInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/DescribeInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/DescribeInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/DescribeInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/DescribeInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/DescribeInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
