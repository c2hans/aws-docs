---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_ListPhoneNumbersOptedOut.html
---

# ListPhoneNumbersOptedOut
<a name="API_ListPhoneNumbersOptedOut"></a>

Returns a list of phone numbers that are opted out, meaning you cannot send SMS messages to them.

The results for `ListPhoneNumbersOptedOut` are paginated, and each page returns up to 100 phone numbers. If additional phone numbers are available after the first page of results, then a `NextToken` string will be returned. To receive the next page, you call `ListPhoneNumbersOptedOut` again using the `NextToken` string received from the previous call. When there are no more records to return, `NextToken` will be null.

## Request Parameters
<a name="API_ListPhoneNumbersOptedOut_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** nextToken **
A `NextToken` string is used when you call the `ListPhoneNumbersOptedOut` action to retrieve additional records that are available after the first page of results.
Type: String
Required: No

## Response Elements
<a name="API_ListPhoneNumbersOptedOut_ResponseElements"></a>

The following elements are returned by the service.

 ** nextToken **
A `NextToken` string is returned when you call the `ListPhoneNumbersOptedOut` action if additional records are available after the first page of results.
Type: String

 **phoneNumbers.member.N**
A list of phone numbers that are opted out of receiving SMS messages. The list is paginated, and each page can contain up to 100 phone numbers.
Type: Array of strings

## Errors
<a name="API_ListPhoneNumbersOptedOut_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
HTTP Status Code: 403

 ** InternalError **
Indicates an internal service error.
HTTP Status Code: 500

 ** InvalidParameter **
Indicates that a request parameter does not comply with the associated constraints.
HTTP Status Code: 400

 ** Throttled **
Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.
 ** message **
Throttled request.
HTTP Status Code: 429

## See Also
<a name="API_ListPhoneNumbersOptedOut_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/ListPhoneNumbersOptedOut)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/ListPhoneNumbersOptedOut)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/ListPhoneNumbersOptedOut)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/ListPhoneNumbersOptedOut)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/ListPhoneNumbersOptedOut)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/ListPhoneNumbersOptedOut)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/ListPhoneNumbersOptedOut)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/ListPhoneNumbersOptedOut)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/ListPhoneNumbersOptedOut)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/ListPhoneNumbersOptedOut)
