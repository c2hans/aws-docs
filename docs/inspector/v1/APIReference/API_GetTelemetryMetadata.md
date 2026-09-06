---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_GetTelemetryMetadata.html
---

# GetTelemetryMetadata
<a name="API_GetTelemetryMetadata"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Information about the data that is collected for the specified assessment run.

## Request Syntax
<a name="API_GetTelemetryMetadata_RequestSyntax"></a>

```
{
   "assessmentRunArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTelemetryMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [assessmentRunArn](#API_GetTelemetryMetadata_RequestSyntax) **   <a name="Inspector-GetTelemetryMetadata-request-assessmentRunArn"></a>
The ARN that specifies the assessment run that has the telemetry data that you want to obtain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Response Syntax
<a name="API_GetTelemetryMetadata_ResponseSyntax"></a>

```
{
   "telemetryMetadata": [
      {
         "count": number,
         "dataSize": number,
         "messageType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetTelemetryMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [telemetryMetadata](#API_GetTelemetryMetadata_ResponseSyntax) **   <a name="Inspector-GetTelemetryMetadata-response-telemetryMetadata"></a>
Telemetry details.
Type: Array of [TelemetryMetadata](API_TelemetryMetadata.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5000 items.

## Errors
<a name="API_GetTelemetryMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
 ** canRetry **
You can immediately retry your request.
 ** message **
Details of the exception error.
HTTP Status Code: 500

 ** InvalidInputException **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

 ** NoSuchEntityException **
The request was rejected because it referenced an entity that does not exist. The error code describes the entity.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

## Examples
<a name="API_GetTelemetryMetadata_Examples"></a>

### Example
<a name="API_GetTelemetryMetadata_Example_1"></a>

This example illustrates one usage of GetTelemetryMetadata.

#### Sample Request
<a name="API_GetTelemetryMetadata_Example_1_Request"></a>

```

                  POST / HTTP/1.1
                  Host: inspector.us-west-2.amazonaws.com
                  Accept-Encoding: identity
                  Content-Length: 117
                  X-Amz-Target: InspectorService.GetTelemetryMetadata
                  X-Amz-Date: 20160329T223852Z
                  User-Agent: aws-cli/1.10.12 Python/2.7.9 Windows/7 botocore/1.4.3
                  Content-Type: application/x-amz-json-1.1
                  Authorization: AUTHPARAMS
                  {
                    "assessmentRunArn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE"
                  }
```

#### Sample Response
<a name="API_GetTelemetryMetadata_Example_1_Response"></a>

```

                  HTTP/1.1 200 OK
                  x-amzn-RequestId: 03ffa82f-f5ff-11e5-9cf9-9fd5e2aef2f6
                  Content-Type: application/x-amz-json-1.1
                  Content-Length: 1990
                  Date: Tue, 29 Mar 2016 22:38:53 GMT
                  {
                    "telemetryMetadata": [
                      {
                        "count": 2,
                        "dataSize": 345,
                        "messageType": "InspectorDuplicateProcess"
                      },
                      {
                        "count": 3,
                        "dataSize": 255,
                        "messageType": "InspectorTimeEventMsg"
                      },
                      {
                        "count": 4,
                        "dataSize": 1082,
                        "messageType": "InspectorNetworkInterface"
                      },
                      {
                        "count": 2,
                        "dataSize": 349,
                        "messageType": "InspectorDnsEntry"
                      },
                      {
                        "count": 11,
                        "dataSize": 2514,
                        "messageType": "InspectorDirectoryInfoMsg"
                      },
                      {
                        "count": 1,
                        "dataSize": 179,
                        "messageType": "InspectorTcpV6ListeningPort"
                      },
                      {
                        "count": 101,
                        "dataSize": 10949,
                        "messageType": "InspectorTerminal"
                      },
                      {
                        "count": 26,
                        "dataSize": 5916,
                        "messageType": "InspectorUser"
                      },
                      {
                        "count": 282,
                        "dataSize": 32148,
                        "messageType": "InspectorDynamicallyLoadedCodeModule"
                      },
                      {
                        "count": 18,
                        "dataSize": 10172,
                        "messageType": "InspectorCreateProcess"
                      },
                      {
                        "count": 3,
                        "dataSize": 8001,
                        "messageType": "InspectorProcessPerformance"
                      },
                      {
                        "count": 1,
                        "dataSize": 360,
                        "messageType": "InspectorOperatingSystem"
                      },
                      {
                        "count": 6,
                        "dataSize": 546,
                        "messageType": "InspectorStopProcess"
                      },
                      {
                        "count": 1,
                        "dataSize": 1553,
                        "messageType": "InspectorInstanceMetaData"
                      },
                      {
                        "count": 2,
                        "dataSize": 434,
                        "messageType": "InspectorTcpV4Connection"
                      },
                      {
                        "count": 474,
                        "dataSize": 2960322,
                        "messageType": "InspectorPackageInfo"
                      },
                      {
                        "count": 3,
                        "dataSize": 2235,
                        "messageType": "InspectorSystemPerformance"
                      },
                      {
                        "count": 105,
                        "dataSize": 46048,
                        "messageType": "InspectorCodeModule"
                      },
                      {
                        "count": 1,
                        "dataSize": 182,
                        "messageType": "InspectorUdpV6ListeningPort"
                      },
                      {
                        "count": 2,
                        "dataSize": 371,
                        "messageType": "InspectorUdpV4ListeningPort"
                      },
                      {
                        "count": 18,
                        "dataSize": 8362,
                        "messageType": "InspectorKernelModule"
                      },
                      {
                        "count": 29,
                        "dataSize": 48788,
                        "messageType": "InspectorConfigurationInfo"
                      },
                      {
                        "count": 1,
                        "dataSize": 79,
                        "messageType": "InspectorMonitoringStart"
                      },
                      {
                        "count": 5,
                        "dataSize": 0,
                        "messageType": "InspectorSplitMsgBegin"
                      },
                      {
                        "count": 51,
                        "dataSize": 4593,
                        "messageType": "InspectorGroup"
                      },
                      {
                        "count": 1,
                        "dataSize": 184,
                        "messageType": "InspectorTcpV4ListeningPort"
                      },
                      {
                        "count": 1159,
                        "dataSize": 3146579,
                        "messageType": "Total"
                      },
                      {
                        "count": 5,
                        "dataSize": 0,
                        "messageType": "InspectorSplitMsgEnd"
                      },
                      {
                        "count": 1,
                        "dataSize": 612,
                        "messageType": "InspectorLoadImageInProcess"
                      }
                    ]
                  }
```

## See Also
<a name="API_GetTelemetryMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/GetTelemetryMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/GetTelemetryMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/GetTelemetryMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/GetTelemetryMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/GetTelemetryMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/GetTelemetryMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/GetTelemetryMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/GetTelemetryMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/GetTelemetryMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/GetTelemetryMetadata)
