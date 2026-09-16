---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_ListResourcePolicies.html
---

# ListResourcePolicies
<a name="API_ListResourcePolicies"></a>

Returns the list of resource policies in the target AWS account.

## Request Syntax
<a name="API_ListResourcePolicies_RequestSyntax"></a>

```
POST /ListResourcePolicies HTTP/1.1
Content-type: application/json

{
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListResourcePolicies_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListResourcePolicies_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [NextToken](#API_ListResourcePolicies_RequestSyntax) **   <a name="xray-ListResourcePolicies-request-NextToken"></a>
Not currently supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Syntax
<a name="API_ListResourcePolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ResourcePolicies": [
      {
         "LastUpdatedTime": number,
         "PolicyDocument": "string",
         "PolicyName": "string",
         "PolicyRevisionId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListResourcePolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListResourcePolicies_ResponseSyntax) **   <a name="xray-ListResourcePolicies-response-NextToken"></a>
Pagination token. Not currently supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [ResourcePolicies](#API_ListResourcePolicies_ResponseSyntax) **   <a name="xray-ListResourcePolicies-response-ResourcePolicies"></a>
The list of resource policies in the target AWS account.
Type: Array of [ResourcePolicy](API_ResourcePolicy.md) objects

## Errors
<a name="API_ListResourcePolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_ListResourcePolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/ListResourcePolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/ListResourcePolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/ListResourcePolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/ListResourcePolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/ListResourcePolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/ListResourcePolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/ListResourcePolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/ListResourcePolicies)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/ListResourcePolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/ListResourcePolicies)
