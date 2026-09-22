---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListLifecyclePolicies.html
---

# ListLifecyclePolicies
<a name="API_ListLifecyclePolicies"></a>

Retrieves a list of lifecycle policies in your AWS account.

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
Use the following filters to streamline results: `name`, `resourceType`, and `status`. Filter names are matched exactly as shown.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [maxResults](#API_ListLifecyclePolicies_RequestSyntax) **   <a name="imagebuilder-ListLifecyclePolicies-request-maxResults"></a>
The maximum number of items to return in a single request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListLifecyclePolicies_RequestSyntax) **   <a name="imagebuilder-ListLifecyclePolicies-request-nextToken"></a>
A token to specify where to start paginating. Use the `nextToken` value from a previously truncated response.
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
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidPaginationTokenException **
You have provided an invalid pagination token in your request.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_ListLifecyclePolicies_Examples"></a>

### List enabled lifecycle policies
<a name="API_ListLifecyclePolicies_Example_1"></a>

The following example lists the lifecycle policies in your account that have ENABLED status.

#### Sample Request
<a name="API_ListLifecyclePolicies_Example_1_Request"></a>

```
POST /ListLifecyclePolicies HTTP/1.1
Content-type: application/json

{
    "filters": [
        {
            "name": "status",
            "values": [
                "ENABLED"
            ]
        }
    ]
}
```

#### Sample Response
<a name="API_ListLifecyclePolicies_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "lifecyclePolicySummaryList": [
        {
            "arn": "arn:aws:imagebuilder:us-west-2:111122223333:lifecycle-policy/my-example-ami-policy",
            "name": "my-example-ami-policy",
            "description": "Deletes AMI image builds after they reach 6 months old",
            "status": "ENABLED",
            "executionRole": "arn:aws:iam::111122223333:role/my-example-lifecycle-role",
            "resourceType": "AMI_IMAGE",
            "dateCreated": 1788982577.612,
            "tags": {}
        },
        {
            "arn": "arn:aws:imagebuilder:us-west-2:111122223333:lifecycle-policy/my-example-container-policy",
            "name": "my-example-container-policy",
            "description": "Deletes container image builds after they reach 6 months old",
            "status": "ENABLED",
            "executionRole": "arn:aws:iam::111122223333:role/my-example-lifecycle-role",
            "resourceType": "CONTAINER_IMAGE",
            "dateCreated": 1788982579.339,
            "tags": {}
        }
    ]
}
```

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
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListLifecyclePolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListLifecyclePolicies)
