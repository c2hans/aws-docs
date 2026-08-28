---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListComponents.html
---

# ListComponents
<a name="API_ListComponents"></a>

Returns the list of components that can be filtered by name, or by using the listed `filters` to streamline results. Newly created components can take up to two minutes to appear in the ListComponents API Results.

**Note**
The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.
 **Filtering:** With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.

## Request Syntax
<a name="API_ListComponents_RequestSyntax"></a>

```
POST /ListComponents HTTP/1.1
Content-type: application/json

{
   "byName": {{boolean}},
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "owner": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListComponents_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListComponents_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [byName](#API_ListComponents_RequestSyntax) **   <a name="imagebuilder-ListComponents-request-byName"></a>
Returns the list of components for the specified name.
Type: Boolean
Required: No

 ** [filters](#API_ListComponents_RequestSyntax) **   <a name="imagebuilder-ListComponents-request-filters"></a>
Use the following filters to streamline results:
+  `description`
+  `name`
+  `platform`
+  `supportedOsVersion`
+  `type`
+  `version`
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [maxResults](#API_ListComponents_RequestSyntax) **   <a name="imagebuilder-ListComponents-request-maxResults"></a>
Specify the maximum number of items to return in a request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListComponents_RequestSyntax) **   <a name="imagebuilder-ListComponents-request-nextToken"></a>
A token to specify where to start paginating. This is the nextToken from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

 ** [owner](#API_ListComponents_RequestSyntax) **   <a name="imagebuilder-ListComponents-request-owner"></a>
Filters results based on the type of owner for the component. By default, this request returns a list of components that your account owns. To see results for other types of owners, you can specify components that Amazon manages, third party components, or components that other accounts have shared with you.
Type: String
Valid Values: `Self | Shared | Amazon | ThirdParty | AWSMarketplace`
Required: No

## Response Syntax
<a name="API_ListComponents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "componentVersionList": [
      {
         "arn": "string",
         "dateCreated": "string",
         "description": "string",
         "name": "string",
         "owner": "string",
         "platform": "string",
         "productCodes": [
            {
               "productCodeId": "string",
               "productCodeType": "string"
            }
         ],
         "status": "string",
         "supportedOsVersions": [ "string" ],
         "type": "string",
         "version": "string"
      }
   ],
   "nextToken": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_ListComponents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [componentVersionList](#API_ListComponents_ResponseSyntax) **   <a name="imagebuilder-ListComponents-response-componentVersionList"></a>
The list of component semantic versions.
The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.
Type: Array of [ComponentVersion](API_ComponentVersion.md) objects

 ** [nextToken](#API_ListComponents_ResponseSyntax) **   <a name="imagebuilder-ListComponents-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [requestId](#API_ListComponents_ResponseSyntax) **   <a name="imagebuilder-ListComponents-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListComponents_Errors"></a>

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
<a name="API_ListComponents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListComponents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListComponents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListComponents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListComponents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListComponents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListComponents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListComponents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListComponents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListComponents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListComponents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
