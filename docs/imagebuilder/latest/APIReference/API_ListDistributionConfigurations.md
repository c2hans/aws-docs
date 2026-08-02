---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListDistributionConfigurations.html
---

# ListDistributionConfigurations
<a name="API_ListDistributionConfigurations"></a>

Returns a list of distribution configurations.

## Request Syntax
<a name="API_ListDistributionConfigurations_RequestSyntax"></a>

```
POST /ListDistributionConfigurations HTTP/1.1
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
<a name="API_ListDistributionConfigurations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListDistributionConfigurations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListDistributionConfigurations_RequestSyntax) **   <a name="imagebuilder-ListDistributionConfigurations-request-filters"></a>
You can filter on `name` to streamline results.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [maxResults](#API_ListDistributionConfigurations_RequestSyntax) **   <a name="imagebuilder-ListDistributionConfigurations-request-maxResults"></a>
Specify the maximum number of items to return in a request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListDistributionConfigurations_RequestSyntax) **   <a name="imagebuilder-ListDistributionConfigurations-request-nextToken"></a>
A token to specify where to start paginating. This is the nextToken from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

## Response Syntax
<a name="API_ListDistributionConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "distributionConfigurationSummaryList": [
      {
         "arn": "string",
         "dateCreated": "string",
         "dateUpdated": "string",
         "description": "string",
         "name": "string",
         "regions": [ "string" ],
         "tags": {
            "string" : "string"
         }
      }
   ],
   "nextToken": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_ListDistributionConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [distributionConfigurationSummaryList](#API_ListDistributionConfigurations_ResponseSyntax) **   <a name="imagebuilder-ListDistributionConfigurations-response-distributionConfigurationSummaryList"></a>
The list of distributions.
Type: Array of [DistributionConfigurationSummary](API_DistributionConfigurationSummary.md) objects

 ** [nextToken](#API_ListDistributionConfigurations_ResponseSyntax) **   <a name="imagebuilder-ListDistributionConfigurations-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [requestId](#API_ListDistributionConfigurations_ResponseSyntax) **   <a name="imagebuilder-ListDistributionConfigurations-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListDistributionConfigurations_Errors"></a>

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
<a name="API_ListDistributionConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListDistributionConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListDistributionConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListDistributionConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListDistributionConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListDistributionConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListDistributionConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListDistributionConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListDistributionConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListDistributionConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListDistributionConfigurations)
