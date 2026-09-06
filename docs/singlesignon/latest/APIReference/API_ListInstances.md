---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html
---

# ListInstances
<a name="API_ListInstances"></a>

Lists the details of the organization and account instances of IAM Identity Center that were created in or visible to the account calling this API.

## Request Syntax
<a name="API_ListInstances_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListInstances_RequestSyntax) **   <a name="singlesignon-ListInstances-request-MaxResults"></a>
The maximum number of results to display for the instance.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListInstances_RequestSyntax) **   <a name="singlesignon-ListInstances-request-NextToken"></a>
The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/_]*`
Required: No

## Response Syntax
<a name="API_ListInstances_ResponseSyntax"></a>

```
{
   "Instances": [
      {
         "CreatedDate": number,
         "IdentityStoreId": "string",
         "InstanceArn": "string",
         "Name": "string",
         "OwnerAccountId": "string",
         "PrimaryRegion": "string",
         "Regions": [
            {
               "AddedDate": number,
               "IsPrimaryRegion": boolean,
               "RegionName": "string",
               "Status": "string"
            }
         ],
         "Status": "string",
         "StatusReason": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Instances](#API_ListInstances_ResponseSyntax) **   <a name="singlesignon-ListInstances-response-Instances"></a>
Lists the IAM Identity Center instances that the caller has access to.
Type: Array of [InstanceMetadata](API_InstanceMetadata.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [NextToken](#API_ListInstances_ResponseSyntax) **   <a name="singlesignon-ListInstances-response-NextToken"></a>
The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/_]*`

## Errors
<a name="API_ListInstances_Errors"></a>

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
<a name="API_ListInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/ListInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/ListInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/ListInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/ListInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/ListInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/ListInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/ListInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/ListInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/ListInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/ListInstances)
