---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ProvisionPermissionSet.html
---

# ProvisionPermissionSet
<a name="API_ProvisionPermissionSet"></a>

The process by which a specified permission set is provisioned to the specified target.

## Request Syntax
<a name="API_ProvisionPermissionSet_RequestSyntax"></a>

```
{
   "InstanceArn": "{{string}}",
   "PermissionSetArn": "{{string}}",
   "TargetId": "{{string}}",
   "TargetType": "{{string}}"
}
```

## Request Parameters
<a name="API_ProvisionPermissionSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceArn](#API_ProvisionPermissionSet_RequestSyntax) **   <a name="singlesignon-ProvisionPermissionSet-request-InstanceArn"></a>
The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

 ** [PermissionSetArn](#API_ProvisionPermissionSet_RequestSyntax) **   <a name="singlesignon-ProvisionPermissionSet-request-PermissionSetArn"></a>
The ARN of the permission set.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::permissionSet/(sso)?ins-[a-zA-Z0-9-.]{16}/ps-[a-zA-Z0-9-./]{16}`
Required: Yes

 ** [TargetId](#API_ProvisionPermissionSet_RequestSyntax) **   <a name="singlesignon-ProvisionPermissionSet-request-TargetId"></a>
TargetID is an AWS account identifier, (For example, 123456789012).
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** [TargetType](#API_ProvisionPermissionSet_RequestSyntax) **   <a name="singlesignon-ProvisionPermissionSet-request-TargetType"></a>
The entity type for which the assignment will be created.
Type: String
Valid Values: `AWS_ACCOUNT | ALL_PROVISIONED_ACCOUNTS`
Required: Yes

## Response Syntax
<a name="API_ProvisionPermissionSet_ResponseSyntax"></a>

```
{
   "PermissionSetProvisioningStatus": {
      "AccountId": "string",
      "CreatedDate": number,
      "FailureReason": "string",
      "PermissionSetArn": "string",
      "RequestId": "string",
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_ProvisionPermissionSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PermissionSetProvisioningStatus](#API_ProvisionPermissionSet_ResponseSyntax) **   <a name="singlesignon-ProvisionPermissionSet-response-PermissionSetProvisioningStatus"></a>
The status object for the permission set provisioning operation.
Type: [PermissionSetProvisioningStatus](API_PermissionSetProvisioningStatus.md) object

## Errors
<a name="API_ProvisionPermissionSet_Errors"></a>

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
<a name="API_ProvisionPermissionSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/ProvisionPermissionSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/ProvisionPermissionSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/ProvisionPermissionSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/ProvisionPermissionSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/ProvisionPermissionSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/ProvisionPermissionSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/ProvisionPermissionSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/ProvisionPermissionSet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/ProvisionPermissionSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/ProvisionPermissionSet)
