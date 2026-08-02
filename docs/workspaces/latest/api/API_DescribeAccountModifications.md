---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeAccountModifications.html
---

# DescribeAccountModifications
<a name="API_DescribeAccountModifications"></a>

Retrieves a list that describes modifications to the configuration of Bring Your Own License (BYOL) for the specified account.

## Request Syntax
<a name="API_DescribeAccountModifications_RequestSyntax"></a>

```
{
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAccountModifications_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [NextToken](#API_DescribeAccountModifications_RequestSyntax) **   <a name="WorkSpaces-DescribeAccountModifications-request-NextToken"></a>
If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_DescribeAccountModifications_ResponseSyntax"></a>

```
{
   "AccountModifications": [
      {
         "DedicatedTenancyManagementCidrRange": "string",
         "DedicatedTenancySupport": "string",
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "ModificationState": "string",
         "StartTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeAccountModifications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountModifications](#API_DescribeAccountModifications_ResponseSyntax) **   <a name="WorkSpaces-DescribeAccountModifications-response-AccountModifications"></a>
The list of modifications to the configuration of BYOL.
Type: Array of [AccountModification](API_AccountModification.md) objects

 ** [NextToken](#API_DescribeAccountModifications_ResponseSyntax) **   <a name="WorkSpaces-DescribeAccountModifications-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_DescribeAccountModifications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAccountModifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeAccountModifications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeAccountModifications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeAccountModifications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeAccountModifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeAccountModifications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeAccountModifications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeAccountModifications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeAccountModifications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeAccountModifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeAccountModifications)
