---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListInfrastructureConfigurations.html
---

# ListInfrastructureConfigurations
<a name="API_ListInfrastructureConfigurations"></a>

Returns a list of infrastructure configurations.

## Request Syntax
<a name="API_ListInfrastructureConfigurations_RequestSyntax"></a>

```
POST /ListInfrastructureConfigurations HTTP/1.1
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
<a name="API_ListInfrastructureConfigurations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListInfrastructureConfigurations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListInfrastructureConfigurations_RequestSyntax) **   <a name="imagebuilder-ListInfrastructureConfigurations-request-filters"></a>
You can filter on `name` to streamline results.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [maxResults](#API_ListInfrastructureConfigurations_RequestSyntax) **   <a name="imagebuilder-ListInfrastructureConfigurations-request-maxResults"></a>
The maximum number of items to return in a single request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListInfrastructureConfigurations_RequestSyntax) **   <a name="imagebuilder-ListInfrastructureConfigurations-request-nextToken"></a>
A token to specify where to start paginating. Use the `nextToken` value from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

## Response Syntax
<a name="API_ListInfrastructureConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "infrastructureConfigurationSummaryList": [
      {
         "arn": "string",
         "dateCreated": "string",
         "dateUpdated": "string",
         "description": "string",
         "instanceProfileName": "string",
         "instanceTypes": [ "string" ],
         "name": "string",
         "placement": {
            "availabilityZone": "string",
            "hostId": "string",
            "hostResourceGroupArn": "string",
            "tenancy": "string"
         },
         "resourceTags": {
            "string" : "string"
         },
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
<a name="API_ListInfrastructureConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [infrastructureConfigurationSummaryList](#API_ListInfrastructureConfigurations_ResponseSyntax) **   <a name="imagebuilder-ListInfrastructureConfigurations-response-infrastructureConfigurationSummaryList"></a>
The list of infrastructure configurations.
Type: Array of [InfrastructureConfigurationSummary](API_InfrastructureConfigurationSummary.md) objects

 ** [nextToken](#API_ListInfrastructureConfigurations_ResponseSyntax) **   <a name="imagebuilder-ListInfrastructureConfigurations-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [requestId](#API_ListInfrastructureConfigurations_ResponseSyntax) **   <a name="imagebuilder-ListInfrastructureConfigurations-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListInfrastructureConfigurations_Errors"></a>

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
<a name="API_ListInfrastructureConfigurations_Examples"></a>

### List infrastructure configurations by name
<a name="API_ListInfrastructureConfigurations_Example_1"></a>

The following example lists your infrastructure configurations, filtered to a specific resource name.

#### Sample Request
<a name="API_ListInfrastructureConfigurations_Example_1_Request"></a>

```
POST /ListInfrastructureConfigurations HTTP/1.1
Content-type: application/json

{
    "filters": [
        {
            "name": "name",
            "values": [
                "my-example-infrastructure-configuration"
            ]
        }
    ]
}
```

#### Sample Response
<a name="API_ListInfrastructureConfigurations_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "dbadaf86-3a9d-48fc-8e34-6062ef0a70f2",
    "infrastructureConfigurationSummaryList": [
        {
            "arn": "arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure-configuration",
            "name": "my-example-infrastructure-configuration",
            "description": "An example infrastructure configuration for Amazon Linux builds",
            "dateCreated": "2026-09-09T19:37:17.350Z",
            "tags": {
                "Environment": "test"
            },
            "instanceTypes": [
                "m5.large",
                "m5.xlarge"
            ],
            "instanceProfileName": "EC2InstanceProfileForImageBuilder"
        }
    ]
}
```

## See Also
<a name="API_ListInfrastructureConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListInfrastructureConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListInfrastructureConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListInfrastructureConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListInfrastructureConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListInfrastructureConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListInfrastructureConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListInfrastructureConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListInfrastructureConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListInfrastructureConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListInfrastructureConfigurations)
