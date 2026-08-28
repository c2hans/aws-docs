---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ListAddressLists.html
---

# ListAddressLists
<a name="API_ListAddressLists"></a>

Lists address lists for this account.

## Request Syntax
<a name="API_ListAddressLists_RequestSyntax"></a>

```
{
   "NextToken": "{{string}}",
   "PageSize": {{number}}
}
```

## Request Parameters
<a name="API_ListAddressLists_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NextToken](#API_ListAddressLists_RequestSyntax) **   <a name="sesmailmanager-ListAddressLists-request-NextToken"></a>
If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [PageSize](#API_ListAddressLists_RequestSyntax) **   <a name="sesmailmanager-ListAddressLists-request-PageSize"></a>
The maximum number of address list resources that are returned per call. You can use NextToken to retrieve the next page of address lists.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

## Response Syntax
<a name="API_ListAddressLists_ResponseSyntax"></a>

```
{
   "AddressLists": [
      {
         "AddressListArn": "string",
         "AddressListId": "string",
         "AddressListName": "string",
         "CreatedTimestamp": number,
         "LastUpdatedTimestamp": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAddressLists_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AddressLists](#API_ListAddressLists_ResponseSyntax) **   <a name="sesmailmanager-ListAddressLists-response-AddressLists"></a>
The list of address lists.
Type: Array of [AddressList](API_AddressList.md) objects

 ** [NextToken](#API_ListAddressLists_ResponseSyntax) **   <a name="sesmailmanager-ListAddressLists-response-NextToken"></a>
If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListAddressLists_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Occurs when a user is denied access to a specific resource or action.
HTTP Status Code: 400

 ** ThrottlingException **
Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_ListAddressLists_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/ListAddressLists)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/ListAddressLists)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/ListAddressLists)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/ListAddressLists)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/ListAddressLists)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/ListAddressLists)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/ListAddressLists)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/ListAddressLists)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/ListAddressLists)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/ListAddressLists)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
