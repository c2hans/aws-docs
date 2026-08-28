---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdateInstance.html
---

# UpdateInstance
<a name="API_UpdateInstance"></a>

Update the details for the instance of IAM Identity Center that is owned by the AWS account.

In a single `UpdateInstance` request, you can perform only one of the following operations:
+ Update the encryption configuration of the instance by specifying `EncryptionConfiguration`.
+ Enable permission sets for the instance by specifying `PermissionSetsEnabled`.

A request that specifies both `EncryptionConfiguration` and `PermissionSetsEnabled` returns a `ValidationException`. To perform both operations, call `UpdateInstance` separately for each. The two calls can be made in parallel.

## Request Syntax
<a name="API_UpdateInstance_RequestSyntax"></a>

```
{
   "EncryptionConfiguration": {
      "KeyType": "{{string}}",
      "KmsKeyArn": "{{string}}"
   },
   "InstanceArn": "{{string}}",
   "Name": "{{string}}",
   "PermissionSetsEnabled": {{boolean}}
}
```

## Request Parameters
<a name="API_UpdateInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EncryptionConfiguration](#API_UpdateInstance_RequestSyntax) **   <a name="singlesignon-UpdateInstance-request-EncryptionConfiguration"></a>
Specifies the encryption configuration for your IAM Identity Center instance. You can use this to configure customer managed KMS keys or AWS owned KMS keys for encrypting your instance data.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** [InstanceArn](#API_UpdateInstance_RequestSyntax) **   <a name="singlesignon-UpdateInstance-request-InstanceArn"></a>
The ARN of the instance of IAM Identity Center under which the operation will run. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

 ** [Name](#API_UpdateInstance_RequestSyntax) **   <a name="singlesignon-UpdateInstance-request-Name"></a>
Updates the instance name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\w+=,.@-]+`
Required: No

 ** [PermissionSetsEnabled](#API_UpdateInstance_RequestSyntax) **   <a name="singlesignon-UpdateInstance-request-PermissionSetsEnabled"></a>
Enables permission sets for this Identity Center instance. The only accepted value is `true `. After permission sets are enabled, they cannot be disabled.
You can't set `EncryptionConfiguration` and `PermissionSetsEnabled` in the same request. To configure both, make two separate `UpdateInstance` calls. These calls can be made in parallel.
Type: Boolean
Required: No

## Response Elements
<a name="API_UpdateInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** Reason **
The reason for the access denied exception.
HTTP Status Code: 400

 ** ConflictException **
Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure with an internal server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Indicates that a requested resource is not found.
 ** Reason **
The reason for the resource not found exception.
HTTP Status Code: 400

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
<a name="API_UpdateInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/UpdateInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/UpdateInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/UpdateInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/UpdateInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/UpdateInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/UpdateInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/UpdateInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/UpdateInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/UpdateInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/UpdateInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
