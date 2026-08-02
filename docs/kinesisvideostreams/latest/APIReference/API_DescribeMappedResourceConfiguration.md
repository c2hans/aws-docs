---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_DescribeMappedResourceConfiguration.html
---

# DescribeMappedResourceConfiguration
<a name="API_DescribeMappedResourceConfiguration"></a>

Returns the most current information about the stream. The `streamName` or `streamARN` should be provided in the input.

## Request Syntax
<a name="API_DescribeMappedResourceConfiguration_RequestSyntax"></a>

```
POST /describeMappedResourceConfiguration HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StreamARN": "{{string}}",
   "StreamName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeMappedResourceConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeMappedResourceConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeMappedResourceConfiguration_RequestSyntax) **   <a name="KinesisVideo-DescribeMappedResourceConfiguration-request-MaxResults"></a>
The maximum number of results to return in the response.
Type: Integer
Valid Range: Fixed value of 1.
Required: No

 ** [NextToken](#API_DescribeMappedResourceConfiguration_RequestSyntax) **   <a name="KinesisVideo-DescribeMappedResourceConfiguration-request-NextToken"></a>
The token to provide in your next request, to get another batch of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=]*`
Required: No

 ** [StreamARN](#API_DescribeMappedResourceConfiguration_RequestSyntax) **   <a name="KinesisVideo-DescribeMappedResourceConfiguration-request-StreamARN"></a>
The Amazon Resource Name (ARN) of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`
Required: No

 ** [StreamName](#API_DescribeMappedResourceConfiguration_RequestSyntax) **   <a name="KinesisVideo-DescribeMappedResourceConfiguration-request-StreamName"></a>
The name of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Syntax
<a name="API_DescribeMappedResourceConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MappedResourceConfigurationList": [
      {
         "ARN": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeMappedResourceConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MappedResourceConfigurationList](#API_DescribeMappedResourceConfiguration_ResponseSyntax) **   <a name="KinesisVideo-DescribeMappedResourceConfiguration-response-MappedResourceConfigurationList"></a>
A structure that encapsulates, or contains, the media storage configuration properties.
Type: Array of [MappedResourceConfigurationListItem](API_MappedResourceConfigurationListItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [NextToken](#API_DescribeMappedResourceConfiguration_ResponseSyntax) **   <a name="KinesisVideo-DescribeMappedResourceConfiguration-response-NextToken"></a>
The token that was used in the `NextToken`request to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=]*`

## Errors
<a name="API_DescribeMappedResourceConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have required permissions to perform this operation.
HTTP Status Code: 401

 ** ClientLimitExceededException **
Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.
HTTP Status Code: 400

 ** InvalidArgumentException **
The value for this input parameter is invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Amazon Kinesis Video Streams can't find the stream that you specified.
HTTP Status Code: 404

## See Also
<a name="API_DescribeMappedResourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration)
