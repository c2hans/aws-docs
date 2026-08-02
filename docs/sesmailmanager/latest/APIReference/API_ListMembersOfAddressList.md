---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ListMembersOfAddressList.html
---

# ListMembersOfAddressList
<a name="API_ListMembersOfAddressList"></a>

Lists members of an address list.

## Request Syntax
<a name="API_ListMembersOfAddressList_RequestSyntax"></a>

```
{
   "AddressListId": "{{string}}",
   "Filter": {
      "AddressPrefix": "{{string}}"
   },
   "NextToken": "{{string}}",
   "PageSize": {{number}}
}
```

## Request Parameters
<a name="API_ListMembersOfAddressList_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AddressListId](#API_ListMembersOfAddressList_RequestSyntax) **   <a name="sesmailmanager-ListMembersOfAddressList-request-AddressListId"></a>
The unique identifier of the address list to list the addresses from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [Filter](#API_ListMembersOfAddressList_RequestSyntax) **   <a name="sesmailmanager-ListMembersOfAddressList-request-Filter"></a>
Filter to be used to limit the results.
Type: [AddressFilter](API_AddressFilter.md) object
Required: No

 ** [NextToken](#API_ListMembersOfAddressList_RequestSyntax) **   <a name="sesmailmanager-ListMembersOfAddressList-request-NextToken"></a>
If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [PageSize](#API_ListMembersOfAddressList_RequestSyntax) **   <a name="sesmailmanager-ListMembersOfAddressList-request-PageSize"></a>
The maximum number of address list members that are returned per call. You can use NextToken to retrieve the next page of members.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

## Response Syntax
<a name="API_ListMembersOfAddressList_ResponseSyntax"></a>

```
{
   "Addresses": [
      {
         "Address": "string",
         "CreatedTimestamp": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMembersOfAddressList_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Addresses](#API_ListMembersOfAddressList_ResponseSyntax) **   <a name="sesmailmanager-ListMembersOfAddressList-response-Addresses"></a>
The list of addresses.
Type: Array of [SavedAddress](API_SavedAddress.md) objects

 ** [NextToken](#API_ListMembersOfAddressList_ResponseSyntax) **   <a name="sesmailmanager-ListMembersOfAddressList-response-NextToken"></a>
If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListMembersOfAddressList_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Occurs when a user is denied access to a specific resource or action.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Occurs when a requested resource is not found.
HTTP Status Code: 400

 ** ThrottlingException **
Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_ListMembersOfAddressList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/ListMembersOfAddressList)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/ListMembersOfAddressList)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/ListMembersOfAddressList)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/ListMembersOfAddressList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/ListMembersOfAddressList)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/ListMembersOfAddressList)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/ListMembersOfAddressList)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/ListMembersOfAddressList)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/ListMembersOfAddressList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/ListMembersOfAddressList)
