---
source_url: https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_ListLinuxSubscriptions.html
---

# ListLinuxSubscriptions
<a name="API_ListLinuxSubscriptions"></a>

Lists the Linux subscriptions that have been discovered. If you have linked your organization, the returned results will include data aggregated across your accounts in AWS Organizations.

## Request Syntax
<a name="API_ListLinuxSubscriptions_RequestSyntax"></a>

```
POST /subscription/ListLinuxSubscriptions HTTP/1.1
Content-type: application/json

{
   "Filters": [
      {
         "Name": "{{string}}",
         "Operator": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListLinuxSubscriptions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListLinuxSubscriptions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_ListLinuxSubscriptions_RequestSyntax) **   <a name="licensemanagerlinuxsubscriptions-ListLinuxSubscriptions-request-Filters"></a>
An array of structures that you can use to filter the results to those that match one or more sets of key-value pairs that you specify. For example, you can filter by the name of `Subscription` with an optional operator to see subscriptions that match, partially match, or don't match a certain subscription's name.
The valid names for this filter are:
+  `Subscription`
The valid Operators for this filter are:
+  `contains`
+  `equals`
+  `Notequal`
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [MaxResults](#API_ListLinuxSubscriptions_RequestSyntax) **   <a name="licensemanagerlinuxsubscriptions-ListLinuxSubscriptions-request-MaxResults"></a>
The maximum items to return in a request.
Type: Integer
Required: No

 ** [NextToken](#API_ListLinuxSubscriptions_RequestSyntax) **   <a name="licensemanagerlinuxsubscriptions-ListLinuxSubscriptions-request-NextToken"></a>
A token to specify where to start paginating. This is the nextToken from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: No

## Response Syntax
<a name="API_ListLinuxSubscriptions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Subscriptions": [
      {
         "InstanceCount": number,
         "Name": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListLinuxSubscriptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListLinuxSubscriptions_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-ListLinuxSubscriptions-response-NextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String

 ** [Subscriptions](#API_ListLinuxSubscriptions_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-ListLinuxSubscriptions-response-Subscriptions"></a>
An array that contains subscription objects.
Type: Array of [Subscription](API_Subscription.md) objects

## Errors
<a name="API_ListLinuxSubscriptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An exception occurred with the service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_ListLinuxSubscriptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptions)
