---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeAccount.html
---

# DescribeAccount
<a name="API_DescribeAccount"></a>

Retrieves a list that describes the configuration of Bring Your Own License (BYOL) for the specified account.

## Response Syntax
<a name="API_DescribeAccount_ResponseSyntax"></a>

```
{
   "DedicatedTenancyAccountType": "string",
   "DedicatedTenancyManagementCidrRange": "string",
   "DedicatedTenancySupport": "string",
   "Message": "string"
}
```

## Response Elements
<a name="API_DescribeAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DedicatedTenancyAccountType](#API_DescribeAccount_ResponseSyntax) **   <a name="WorkSpaces-DescribeAccount-response-DedicatedTenancyAccountType"></a>
The type of linked account.
Type: String
Valid Values: `SOURCE_ACCOUNT | TARGET_ACCOUNT`

 ** [DedicatedTenancyManagementCidrRange](#API_DescribeAccount_ResponseSyntax) **   <a name="WorkSpaces-DescribeAccount-response-DedicatedTenancyManagementCidrRange"></a>
The IP address range, specified as an IPv4 CIDR block, used for the management network interface.
The management network interface is connected to a secure Amazon WorkSpaces management network. It is used for interactive streaming of the WorkSpace desktop to Amazon WorkSpaces clients, and to allow Amazon WorkSpaces to manage the WorkSpace.
Type: String
Pattern: `(^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.0\.0)(\/(16$))$`

 ** [DedicatedTenancySupport](#API_DescribeAccount_ResponseSyntax) **   <a name="WorkSpaces-DescribeAccount-response-DedicatedTenancySupport"></a>
The status of BYOL (whether BYOL is enabled or disabled).
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [Message](#API_DescribeAccount_ResponseSyntax) **   <a name="WorkSpaces-DescribeAccount-response-Message"></a>
The text message to describe the status of BYOL.
Type: String

## Errors
<a name="API_DescribeAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeAccount)
