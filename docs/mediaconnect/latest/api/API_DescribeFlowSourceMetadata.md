---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_DescribeFlowSourceMetadata.html
---

# DescribeFlowSourceMetadata
<a name="API_DescribeFlowSourceMetadata"></a>

 The `DescribeFlowSourceMetadata` API is used to view information about the flow's source transport stream and programs. This API displays status messages about the flow's source as well as details about the program's video, audio, and other data.

## Request Syntax
<a name="API_DescribeFlowSourceMetadata_RequestSyntax"></a>

```
GET /v1/flows/{{flowArn}}/source-metadata HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeFlowSourceMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowArn](#API_DescribeFlowSourceMetadata_RequestSyntax) **   <a name="mediaconnect-DescribeFlowSourceMetadata-request-uri-flowArn"></a>
 The Amazon Resource Name (ARN) of the flow.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:flow:[a-zA-Z0-9-]+:[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_DescribeFlowSourceMetadata_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeFlowSourceMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "flowArn": "string",
   "messages": [
      {
         "code": "string",
         "message": "string",
         "resourceName": "string"
      }
   ],
   "ndiInfo": {
      "activeSource": {
         "sourceName": "string"
      },
      "discoveredSources": [
         {
            "sourceName": "string"
         }
      ],
      "mediaInfo": {
         "streams": [
            {
               "channels": number,
               "codec": "string",
               "frameRate": "string",
               "frameResolution": {
                  "frameHeight": number,
                  "frameWidth": number
               },
               "sampleRate": number,
               "scanMode": "string",
               "streamId": number,
               "streamType": "string"
            }
         ]
      },
      "messages": [
         {
            "code": "string",
            "message": "string",
            "resourceName": "string"
         }
      ]
   },
   "timestamp": "string",
   "transportMediaInfo": {
      "programs": [
         {
            "pcrPid": number,
            "programName": "string",
            "programNumber": number,
            "programPid": number,
            "streams": [
               {
                  "channels": number,
                  "codec": "string",
                  "frameRate": "string",
                  "frameResolution": {
                     "frameHeight": number,
                     "frameWidth": number
                  },
                  "pid": number,
                  "sampleRate": number,
                  "sampleSize": number,
                  "streamType": "string"
               }
            ]
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeFlowSourceMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [flowArn](#API_DescribeFlowSourceMetadata_ResponseSyntax) **   <a name="mediaconnect-DescribeFlowSourceMetadata-response-flowArn"></a>
 The ARN of the flow that DescribeFlowSourceMetadata was performed on.
Type: String

 ** [messages](#API_DescribeFlowSourceMetadata_ResponseSyntax) **   <a name="mediaconnect-DescribeFlowSourceMetadata-response-messages"></a>
 Provides a status code and message regarding issues found with the flow source metadata.
Type: Array of [MessageDetail](API_MessageDetail.md) objects

 ** [ndiInfo](#API_DescribeFlowSourceMetadata_ResponseSyntax) **   <a name="mediaconnect-DescribeFlowSourceMetadata-response-ndiInfo"></a>
 The NDI® specific information about the flow's source. This includes the current active NDI sender, a list of all discovered NDI senders, the associated media streams for the active NDI sender, and any relevant status messages.
Type: [NdiSourceMetadataInfo](API_NdiSourceMetadataInfo.md) object

 ** [timestamp](#API_DescribeFlowSourceMetadata_ResponseSyntax) **   <a name="mediaconnect-DescribeFlowSourceMetadata-response-timestamp"></a>
 The timestamp of the most recent change in metadata for this flow’s source.
Type: Timestamp

 ** [transportMediaInfo](#API_DescribeFlowSourceMetadata_ResponseSyntax) **   <a name="mediaconnect-DescribeFlowSourceMetadata-response-transportMediaInfo"></a>
 Information about the flow's transport media.
Type: [TransportMediaInfo](API_TransportMediaInfo.md) object

## Errors
<a name="API_DescribeFlowSourceMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ForbiddenException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_DescribeFlowSourceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/DescribeFlowSourceMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/DescribeFlowSourceMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/DescribeFlowSourceMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/DescribeFlowSourceMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/DescribeFlowSourceMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/DescribeFlowSourceMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/DescribeFlowSourceMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/DescribeFlowSourceMetadata)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/DescribeFlowSourceMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/DescribeFlowSourceMetadata)
