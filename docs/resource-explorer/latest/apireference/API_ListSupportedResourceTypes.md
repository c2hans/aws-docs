---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListSupportedResourceTypes.html
---

# ListSupportedResourceTypes
<a name="API_ListSupportedResourceTypes"></a>

Retrieves a list of all resource types currently supported by AWS Resource Explorer.

 **Minimum permissions**

To call this operation, you must have the following permissions:
+  **Action**: `resource-explorer-2:ListSupportedResourceTypes`

   **Resource**: No specific resource (\*).

## Request Syntax
<a name="API_ListSupportedResourceTypes_RequestSyntax"></a>

```
POST /ListSupportedResourceTypes HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListSupportedResourceTypes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListSupportedResourceTypes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListSupportedResourceTypes_RequestSyntax) **   <a name="resourceexplorer-ListSupportedResourceTypes-request-MaxResults"></a>
The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the `NextToken` response element is present and has a value (is not null). Include that value as the `NextToken` request parameter in the next call to the operation to get the next part of the results.
An API operation can return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListSupportedResourceTypes_RequestSyntax) **   <a name="resourceexplorer-ListSupportedResourceTypes-request-NextToken"></a>
The parameter for receiving additional results if you receive a `NextToken` response in a previous request. A `NextToken` response indicates that more output is available. Set this parameter to the value of the previous call's `NextToken` response to indicate where the output should continue from. The pagination tokens expire after 24 hours.
Type: String
Required: No

## Response Syntax
<a name="API_ListSupportedResourceTypes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ResourceTypes": [
      {
         "ResourceType": "string",
         "Service": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSupportedResourceTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListSupportedResourceTypes_ResponseSyntax) **   <a name="resourceexplorer-ListSupportedResourceTypes-response-NextToken"></a>
If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. The pagination tokens expire after 24 hours.
Type: String

 ** [ResourceTypes](#API_ListSupportedResourceTypes_ResponseSyntax) **   <a name="resourceexplorer-ListSupportedResourceTypes-response-ResourceTypes"></a>
The list of resource types supported by Resource Explorer.
Type: Array of [SupportedResourceType](API_SupportedResourceType.md) objects

## Errors
<a name="API_ListSupportedResourceTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The credentials that you used to call this operation don't have the minimum required permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request failed because of internal service error. Try your request again later.
HTTP Status Code: 500

 ** ThrottlingException **
The request failed because you exceeded a rate limit for this operation. For more information, see [Quotas for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html).
HTTP Status Code: 429

 ** ValidationException **
You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.
 ** FieldList **
An array of the request fields that had validation errors.
HTTP Status Code: 400

## Examples
<a name="API_ListSupportedResourceTypes_Examples"></a>

### Example
<a name="API_ListSupportedResourceTypes_Example_1"></a>

The following example shows how to list all of the resource type identifiers that you can use in a Resource Explorer search. The example response includes a `NextToken` value, which indicates that there is more output available to retrieve with additional calls.

#### Sample Request
<a name="API_ListSupportedResourceTypes_Example_1_Request"></a>

```
POST /ListSupportedResourceTypes HTTP/1.1
Host: resource-explorer-2.us-east-1.amazonaws.com
X-Amz-Date: 20221101T200059Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>

{}
```

#### Sample Response
<a name="API_ListSupportedResourceTypes_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "NextToken": "AG9VOEF1KLEXAMPLEOhJHVwo5chEXAMPLER5XiEpNrgsEXAMPLE...b0CmOFOryHEXAMPLE",
    "ResourceTypes": [
        {
            "ResourceType": "cloudfront:cache-policy",
            "Service": "cloudfront"
        },
        {
            "ResourceType": "cloudfront:distribution",
            "Service": "cloudfront"
        },
        {
            "ResourceType": "cloudfront:function",
            "Service": "cloudfront"
        },
...TRUNCATED FOR BREVITY...
    ]
}
```

## See Also
<a name="API_ListSupportedResourceTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/ListSupportedResourceTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/ListSupportedResourceTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/ListSupportedResourceTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/ListSupportedResourceTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/ListSupportedResourceTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/ListSupportedResourceTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/ListSupportedResourceTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/ListSupportedResourceTypes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/ListSupportedResourceTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/ListSupportedResourceTypes)
