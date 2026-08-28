---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListDecoderManifestSignals.html
---

# ListDecoderManifestSignals
<a name="API_ListDecoderManifestSignals"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

 A list of information about signal decoders specified in a decoder manifest.

**Note**
This API operation uses pagination. Specify the `nextToken` parameter in the request to return more results.

## Request Syntax
<a name="API_ListDecoderManifestSignals_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "name": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDecoderManifestSignals_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListDecoderManifestSignals_RequestSyntax) **   <a name="iotfleetwise-ListDecoderManifestSignals-request-maxResults"></a>
The maximum number of items to return, between 1 and 100, inclusive.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [name](#API_ListDecoderManifestSignals_RequestSyntax) **   <a name="iotfleetwise-ListDecoderManifestSignals-request-name"></a>
 The name of the decoder manifest to list information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

 ** [nextToken](#API_ListDecoderManifestSignals_RequestSyntax) **   <a name="iotfleetwise-ListDecoderManifestSignals-request-nextToken"></a>
A pagination token for the next set of results.
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## Response Syntax
<a name="API_ListDecoderManifestSignals_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "signalDecoders": [
      {
         "canSignal": {
            "factor": number,
            "isBigEndian": boolean,
            "isSigned": boolean,
            "length": number,
            "messageId": number,
            "name": "string",
            "offset": number,
            "signalValueType": "string",
            "startBit": number
         },
         "customDecodingSignal": {
            "id": "string"
         },
         "fullyQualifiedName": "string",
         "interfaceId": "string",
         "messageSignal": {
            "structuredMessage": { ... },
            "topicName": "string"
         },
         "obdSignal": {
            "bitMaskLength": number,
            "bitRightShift": number,
            "byteLength": number,
            "isSigned": boolean,
            "offset": number,
            "pid": number,
            "pidResponseLength": number,
            "scaling": number,
            "serviceMode": number,
            "signalValueType": "string",
            "startByte": number
         },
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListDecoderManifestSignals_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListDecoderManifestSignals_ResponseSyntax) **   <a name="iotfleetwise-ListDecoderManifestSignals-response-nextToken"></a>
 The token to retrieve the next set of results, or `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [signalDecoders](#API_ListDecoderManifestSignals_ResponseSyntax) **   <a name="iotfleetwise-ListDecoderManifestSignals-response-signalDecoders"></a>
 Information about a list of signals to decode.
Type: Array of [SignalDecoder](API_SignalDecoder.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.

## Errors
<a name="API_ListDecoderManifestSignals_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request couldn't be completed because the server temporarily failed.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource wasn't found.
 ** resourceId **
The identifier of the resource that wasn't found.
 ** resourceType **
The type of resource that wasn't found.
HTTP Status Code: 400

 ** ThrottlingException **
The request couldn't be completed due to throttling.
 ** quotaCode **
The quota identifier of the applied throttling rules for this request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
 ** serviceCode **
The code for the service that couldn't be completed due to throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The list of fields that fail to satisfy the constraints specified by an AWS service.
 ** reason **
The reason the input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListDecoderManifestSignals_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/ListDecoderManifestSignals)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/ListDecoderManifestSignals)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/ListDecoderManifestSignals)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/ListDecoderManifestSignals)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/ListDecoderManifestSignals)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/ListDecoderManifestSignals)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/ListDecoderManifestSignals)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/ListDecoderManifestSignals)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/ListDecoderManifestSignals)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/ListDecoderManifestSignals)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
