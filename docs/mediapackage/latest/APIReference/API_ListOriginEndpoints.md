---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListOriginEndpoints.html
---

# ListOriginEndpoints
<a name="API_ListOriginEndpoints"></a>

Retrieves all origin endpoints in a specific channel that are configured in AWS Elemental MediaPackage.

## Request Syntax
<a name="API_ListOriginEndpoints_RequestSyntax"></a>

```
GET /channelGroup/{{ChannelGroupName}}/channel/{{ChannelName}}/originEndpoint?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListOriginEndpoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelGroupName](#API_ListOriginEndpoints_RequestSyntax) **   <a name="mediapackage-ListOriginEndpoints-request-uri-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [ChannelName](#API_ListOriginEndpoints_RequestSyntax) **   <a name="mediapackage-ListOriginEndpoints-request-uri-ChannelName"></a>
The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [MaxResults](#API_ListOriginEndpoints_RequestSyntax) **   <a name="mediapackage-ListOriginEndpoints-request-uri-MaxResults"></a>
The maximum number of results to return in the response.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListOriginEndpoints_RequestSyntax) **   <a name="mediapackage-ListOriginEndpoints-request-uri-NextToken"></a>
The pagination token from the GET list request. Use the token to fetch the next page of results.

## Request Body
<a name="API_ListOriginEndpoints_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListOriginEndpoints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "Arn": "string",
         "ChannelGroupName": "string",
         "ChannelName": "string",
         "ContainerType": "string",
         "CreatedAt": number,
         "DashManifests": [
            {
               "ManifestName": "string",
               "Url": "string"
            }
         ],
         "Description": "string",
         "ForceEndpointErrorConfiguration": {
            "EndpointErrorConditions": [ "string" ]
         },
         "HlsManifests": [
            {
               "ChildManifestName": "string",
               "ManifestName": "string",
               "Url": "string"
            }
         ],
         "LowLatencyHlsManifests": [
            {
               "ChildManifestName": "string",
               "ManifestName": "string",
               "Url": "string"
            }
         ],
         "ModifiedAt": number,
         "MssManifests": [
            {
               "ManifestName": "string",
               "Url": "string"
            }
         ],
         "OriginEndpointName": "string",
         "UriSeparator": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListOriginEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListOriginEndpoints_ResponseSyntax) **   <a name="mediapackage-ListOriginEndpoints-response-Items"></a>
The objects being returned.
Type: Array of [OriginEndpointListConfiguration](API_OriginEndpointListConfiguration.md) objects

 ** [NextToken](#API_ListOriginEndpoints_ResponseSyntax) **   <a name="mediapackage-ListOriginEndpoints-response-NextToken"></a>
The pagination token from the GET list request. Use the token to fetch the next page of results.
Type: String

## Errors
<a name="API_ListOriginEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.
HTTP Status Code: 403

 ** InternalServerException **
Indicates that an error from the service occurred while trying to process a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource doesn't exist.
 ** ResourceTypeNotFound **
The specified resource type wasn't found.
HTTP Status Code: 404

 ** ThrottlingException **
The request throughput limit was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** ValidationExceptionType **
The type of ValidationException.
HTTP Status Code: 400

## See Also
<a name="API_ListOriginEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediapackagev2-2022-12-25/ListOriginEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediapackagev2-2022-12-25/ListOriginEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/ListOriginEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediapackagev2-2022-12-25/ListOriginEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/ListOriginEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediapackagev2-2022-12-25/ListOriginEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediapackagev2-2022-12-25/ListOriginEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediapackagev2-2022-12-25/ListOriginEndpoints)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediapackagev2-2022-12-25/ListOriginEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/ListOriginEndpoints)
