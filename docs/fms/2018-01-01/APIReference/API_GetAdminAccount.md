---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetAdminAccount.html
---

# GetAdminAccount
<a name="API_GetAdminAccount"></a>

Returns the AWS Organizations account that is associated with AWS Firewall Manager as the AWS Firewall Manager default administrator.

## Response Syntax
<a name="API_GetAdminAccount_ResponseSyntax"></a>

```
{
   "AdminAccount": "string",
   "RoleStatus": "string"
}
```

## Response Elements
<a name="API_GetAdminAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdminAccount](#API_GetAdminAccount_ResponseSyntax) **   <a name="fms-GetAdminAccount-response-AdminAccount"></a>
The account that is set as the AWS Firewall Manager default administrator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`

 ** [RoleStatus](#API_GetAdminAccount_ResponseSyntax) **   <a name="fms-GetAdminAccount-response-RoleStatus"></a>
The status of the account that you set as the AWS Firewall Manager default administrator.
Type: String
Valid Values: `READY | CREATING | PENDING_DELETION | DELETING | DELETED`

## Errors
<a name="API_GetAdminAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 400

 ** InvalidOperationException **
The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an `AssociateAdminAccount` request for an account ID that was already set as the AWS Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for AWS Organizations before you can access it.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_GetAdminAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/GetAdminAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/GetAdminAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/GetAdminAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/GetAdminAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/GetAdminAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/GetAdminAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/GetAdminAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/GetAdminAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/GetAdminAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/GetAdminAccount)
