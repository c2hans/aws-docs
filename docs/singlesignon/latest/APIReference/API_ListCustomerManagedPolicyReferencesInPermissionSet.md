---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListCustomerManagedPolicyReferencesInPermissionSet.html
---

# ListCustomerManagedPolicyReferencesInPermissionSet
<a name="API_ListCustomerManagedPolicyReferencesInPermissionSet"></a>

Lists all customer managed policies attached to a specified [PermissionSet](API_PermissionSet.md).

## Request Syntax
<a name="API_ListCustomerManagedPolicyReferencesInPermissionSet_RequestSyntax"></a>

```
{
   "InstanceArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PermissionSetArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCustomerManagedPolicyReferencesInPermissionSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceArn](#API_ListCustomerManagedPolicyReferencesInPermissionSet_RequestSyntax) **   <a name="singlesignon-ListCustomerManagedPolicyReferencesInPermissionSet-request-InstanceArn"></a>
The ARN of the IAM Identity Center instance under which the operation will be executed.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

 ** [MaxResults](#API_ListCustomerManagedPolicyReferencesInPermissionSet_RequestSyntax) **   <a name="singlesignon-ListCustomerManagedPolicyReferencesInPermissionSet-request-MaxResults"></a>
The maximum number of results to display for the list call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListCustomerManagedPolicyReferencesInPermissionSet_RequestSyntax) **   <a name="singlesignon-ListCustomerManagedPolicyReferencesInPermissionSet-request-NextToken"></a>
The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/_]*`
Required: No

 ** [PermissionSetArn](#API_ListCustomerManagedPolicyReferencesInPermissionSet_RequestSyntax) **   <a name="singlesignon-ListCustomerManagedPolicyReferencesInPermissionSet-request-PermissionSetArn"></a>
The ARN of the `PermissionSet`.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::permissionSet/(sso)?ins-[a-zA-Z0-9-.]{16}/ps-[a-zA-Z0-9-./]{16}`
Required: Yes

## Response Syntax
<a name="API_ListCustomerManagedPolicyReferencesInPermissionSet_ResponseSyntax"></a>

```
{
   "CustomerManagedPolicyReferences": [
      {
         "Name": "string",
         "Path": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCustomerManagedPolicyReferencesInPermissionSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CustomerManagedPolicyReferences](#API_ListCustomerManagedPolicyReferencesInPermissionSet_ResponseSyntax) **   <a name="singlesignon-ListCustomerManagedPolicyReferencesInPermissionSet-response-CustomerManagedPolicyReferences"></a>
Specifies the names and paths of the customer managed policies that you have attached to your permission set.
Type: Array of [CustomerManagedPolicyReference](API_CustomerManagedPolicyReference.md) objects

 ** [NextToken](#API_ListCustomerManagedPolicyReferencesInPermissionSet_ResponseSyntax) **   <a name="singlesignon-ListCustomerManagedPolicyReferencesInPermissionSet-response-NextToken"></a>
The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/_]*`

## Errors
<a name="API_ListCustomerManagedPolicyReferencesInPermissionSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** Reason **
The reason for the access denied exception.
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
<a name="API_ListCustomerManagedPolicyReferencesInPermissionSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/ListCustomerManagedPolicyReferencesInPermissionSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/ListCustomerManagedPolicyReferencesInPermissionSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/ListCustomerManagedPolicyReferencesInPermissionSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/ListCustomerManagedPolicyReferencesInPermissionSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/ListCustomerManagedPolicyReferencesInPermissionSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/ListCustomerManagedPolicyReferencesInPermissionSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/ListCustomerManagedPolicyReferencesInPermissionSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/ListCustomerManagedPolicyReferencesInPermissionSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/ListCustomerManagedPolicyReferencesInPermissionSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/ListCustomerManagedPolicyReferencesInPermissionSet)
