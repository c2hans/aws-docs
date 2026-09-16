---
source_url: https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_ListLinuxSubscriptionInstances.html
---

# ListLinuxSubscriptionInstances
<a name="API_ListLinuxSubscriptionInstances"></a>

Lists the running Amazon EC2 instances that were discovered with commercial Linux subscriptions.

## Request Syntax
<a name="API_ListLinuxSubscriptionInstances_RequestSyntax"></a>

```
POST /subscription/ListLinuxSubscriptionInstances HTTP/1.1
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
<a name="API_ListLinuxSubscriptionInstances_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListLinuxSubscriptionInstances_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_ListLinuxSubscriptionInstances_RequestSyntax) **   <a name="licensemanagerlinuxsubscriptions-ListLinuxSubscriptionInstances-request-Filters"></a>
An array of structures that you can use to filter the results by your specified criteria. For example, you can specify `Region` in the `Name`, with the `contains` operator to list all subscriptions that match a partial string in the `Value`, such as `us-west`.
For each filter, you can specify one of the following values for the `Name` key to streamline results:
+  `AccountID`
+  `AmiID`
+  `DualSubscription`
+  `InstanceID`
+  `InstanceType`
+  `ProductCode`
+  `Region`
+  `Status`
+  `UsageOperation`
For each filter, you can use one of the following `Operator` values to define the behavior of the filter:
+  `contains`
+  `equals`
+  `Notequal`
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [MaxResults](#API_ListLinuxSubscriptionInstances_RequestSyntax) **   <a name="licensemanagerlinuxsubscriptions-ListLinuxSubscriptionInstances-request-MaxResults"></a>
The maximum items to return in a request.
Type: Integer
Required: No

 ** [NextToken](#API_ListLinuxSubscriptionInstances_RequestSyntax) **   <a name="licensemanagerlinuxsubscriptions-ListLinuxSubscriptionInstances-request-NextToken"></a>
A token to specify where to start paginating. This is the nextToken from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: No

## Response Syntax
<a name="API_ListLinuxSubscriptionInstances_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Instances": [
      {
         "AccountID": "string",
         "AmiId": "string",
         "DualSubscription": "string",
         "InstanceID": "string",
         "InstanceType": "string",
         "LastUpdatedTime": "string",
         "OsVersion": "string",
         "ProductCode": [ "string" ],
         "Region": "string",
         "RegisteredWithSubscriptionProvider": "string",
         "Status": "string",
         "SubscriptionName": "string",
         "SubscriptionProviderCreateTime": "string",
         "SubscriptionProviderUpdateTime": "string",
         "UsageOperation": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListLinuxSubscriptionInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Instances](#API_ListLinuxSubscriptionInstances_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-ListLinuxSubscriptionInstances-response-Instances"></a>
An array that contains instance objects.
Type: Array of [Instance](API_Instance.md) objects

 ** [NextToken](#API_ListLinuxSubscriptionInstances_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-ListLinuxSubscriptionInstances-response-NextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String

## Errors
<a name="API_ListLinuxSubscriptionInstances_Errors"></a>

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
<a name="API_ListLinuxSubscriptionInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptionInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptionInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptionInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptionInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptionInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptionInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptionInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptionInstances)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptionInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptionInstances)
