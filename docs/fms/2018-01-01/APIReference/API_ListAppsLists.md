---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListAppsLists.html
---

# ListAppsLists
<a name="API_ListAppsLists"></a>

Returns an array of `AppsListDataSummary` objects.

## Request Syntax
<a name="API_ListAppsLists_RequestSyntax"></a>

```
{
   "DefaultLists": {{boolean}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAppsLists_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DefaultLists](#API_ListAppsLists_RequestSyntax) **   <a name="fms-ListAppsLists-request-DefaultLists"></a>
Specifies whether the lists to retrieve are default lists owned by AWS Firewall Manager.
Type: Boolean
Required: No

 ** [MaxResults](#API_ListAppsLists_RequestSyntax) **   <a name="fms-ListAppsLists-request-MaxResults"></a>
The maximum number of objects that you want AWS Firewall Manager to return for this request. If more objects are available, in the response, AWS Firewall Manager provides a `NextToken` value that you can use in a subsequent call to get the next batch of objects.
If you don't specify this, AWS Firewall Manager returns all available objects.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: Yes

 ** [NextToken](#API_ListAppsLists_RequestSyntax) **   <a name="fms-ListAppsLists-request-NextToken"></a>
If you specify a value for `MaxResults` in your list request, and you have more objects than the maximum, AWS Firewall Manager returns this token in the response. For all but the first request, you provide the token returned by the prior request in the request parameters, to retrieve the next batch of objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_ListAppsLists_ResponseSyntax"></a>

```
{
   "AppsLists": [
      {
         "AppsList": [
            {
               "AppName": "string",
               "Port": number,
               "Protocol": "string"
            }
         ],
         "ListArn": "string",
         "ListId": "string",
         "ListName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAppsLists_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppsLists](#API_ListAppsLists_ResponseSyntax) **   <a name="fms-ListAppsLists-response-AppsLists"></a>
An array of `AppsListDataSummary` objects.
Type: Array of [AppsListDataSummary](API_AppsListDataSummary.md) objects

 ** [NextToken](#API_ListAppsLists_ResponseSyntax) **   <a name="fms-ListAppsLists-response-NextToken"></a>
If you specify a value for `MaxResults` in your list request, and you have more objects than the maximum, AWS Firewall Manager returns this token in the response. You can use this token in subsequent requests to retrieve the next batch of objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors
<a name="API_ListAppsLists_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 400

 ** InvalidOperationException **
The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an `AssociateAdminAccount` request for an account ID that was already set as the AWS Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for AWS Organizations before you can access it.
HTTP Status Code: 400

 ** LimitExceededException **
The operation exceeds a resource limit, for example, the maximum number of `policy` objects that you can create for an AWS account. For more information, see [Firewall Manager Limits](https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html) in the * AWS WAF Developer Guide*.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_ListAppsLists_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/ListAppsLists)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/ListAppsLists)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ListAppsLists)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/ListAppsLists)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ListAppsLists)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/ListAppsLists)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/ListAppsLists)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/ListAppsLists)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/ListAppsLists)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ListAppsLists)
