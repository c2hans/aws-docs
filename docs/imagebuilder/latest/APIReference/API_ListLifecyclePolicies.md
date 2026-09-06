---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListLifecyclePolicies.html
---

# ListLifecyclePolicies
<a name="API_ListLifecyclePolicies"></a>

Get a list of lifecycle policies in your AWS account.

## Request Syntax
<a name="API_ListLifecyclePolicies_RequestSyntax"></a>

```
POST /ListLifecyclePolicies HTTP/1.1
Content-type: application/json

{
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListLifecyclePolicies_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListLifecyclePolicies_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListLifecyclePolicies_RequestSyntax) **   <a name="imagebuilder-ListLifecyclePolicies-request-filters"></a>
Streamline results based on one of the following values: `Name`, `Status`.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [maxResults](#API_ListLifecyclePolicies_RequestSyntax) **   <a name="imagebuilder-ListLifecyclePolicies-request-maxResults"></a>
Specify the maximum number of items to return in a request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListLifecyclePolicies_RequestSyntax) **   <a name="imagebuilder-ListLifecyclePolicies-request-nextToken"></a>
A token to specify where to start paginating. This is the nextToken from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

## Response Syntax
<a name="API_ListLifecyclePolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "lifecyclePolicySummaryList": [
      {
         "arn": "string",
         "dateCreated": number,
         "dateLastRun": number,
         "dateUpdated": number,
         "description": "string",
         "executionRole": "string",
         "name": "string",
         "resourceType": "string",
         "status": "string",
         "tags": {
            "string" : "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListLifecyclePolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lifecyclePolicySummaryList](#API_ListLifecyclePolicies_ResponseSyntax) **   <a name="imagebuilder-ListLifecyclePolicies-response-lifecyclePolicySummaryList"></a>
A list of lifecycle policies in your AWS account that meet the criteria specified in the request.
Type: Array of [LifecyclePolicySummary](API_LifecyclePolicySummary.md) objects

 ** [nextToken](#API_ListLifecyclePolicies_ResponseSyntax) **   <a name="imagebuilder-ListLifecyclePolicies-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

## Errors
<a name="API_ListLifecyclePolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the specific operation.
HTTP Status Code: 429

 ** ClientException **
These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidPaginationTokenException **
You have provided an invalid pagination token in your request.
HTTP Status Code: 400

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_ListLifecyclePolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListLifecyclePolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListLifecyclePolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListLifecyclePolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListLifecyclePolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListLifecyclePolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListLifecyclePolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListLifecyclePolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListLifecyclePolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListLifecyclePolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListLifecyclePolicies)
