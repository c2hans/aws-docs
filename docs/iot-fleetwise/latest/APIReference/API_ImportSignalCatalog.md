---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ImportSignalCatalog.html
---

# ImportSignalCatalog
<a name="API_ImportSignalCatalog"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

 Creates a signal catalog using your existing VSS formatted content from your local device.

## Request Syntax
<a name="API_ImportSignalCatalog_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "name": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "vss": { ... }
}
```

## Request Parameters
<a name="API_ImportSignalCatalog_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_ImportSignalCatalog_RequestSyntax) **   <a name="iotfleetwise-ImportSignalCatalog-request-description"></a>
 A brief description of the signal catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [name](#API_ImportSignalCatalog_RequestSyntax) **   <a name="iotfleetwise-ImportSignalCatalog-request-name"></a>
The name of the signal catalog to import.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

 ** [tags](#API_ImportSignalCatalog_RequestSyntax) **   <a name="iotfleetwise-ImportSignalCatalog-request-tags"></a>
Metadata that can be used to manage the signal catalog.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [vss](#API_ImportSignalCatalog_RequestSyntax) **   <a name="iotfleetwise-ImportSignalCatalog-request-vss"></a>
The contents of the Vehicle Signal Specification (VSS) configuration. VSS is a precise language used to describe and model signals in vehicle networks.
Type: [FormattedVss](API_FormattedVss.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_ImportSignalCatalog_ResponseSyntax"></a>

```
{
   "arn": "string",
   "name": "string"
}
```

## Response Elements
<a name="API_ImportSignalCatalog_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_ImportSignalCatalog_ResponseSyntax) **   <a name="iotfleetwise-ImportSignalCatalog-response-arn"></a>
 The Amazon Resource Name (ARN) of the imported signal catalog.
Type: String

 ** [name](#API_ImportSignalCatalog_ResponseSyntax) **   <a name="iotfleetwise-ImportSignalCatalog-response-name"></a>
 The name of the imported signal catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`

## Errors
<a name="API_ImportSignalCatalog_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resource **
The resource on which there are conflicting operations.
 ** resourceType **
The type of resource on which there are conflicting operations..
HTTP Status Code: 400

 ** InternalServerException **
The request couldn't be completed because the server temporarily failed.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
HTTP Status Code: 500

 ** InvalidSignalsException **
The request couldn't be completed because it contains signals that aren't valid.
 ** invalidSignals **
The signals which caused the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A service quota was exceeded.
 ** resourceId **
The identifier of the resource that was exceeded.
 ** resourceType **
The type of resource that was exceeded.
HTTP Status Code: 400

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
<a name="API_ImportSignalCatalog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/ImportSignalCatalog)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/ImportSignalCatalog)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/ImportSignalCatalog)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/ImportSignalCatalog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/ImportSignalCatalog)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/ImportSignalCatalog)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/ImportSignalCatalog)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/ImportSignalCatalog)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/ImportSignalCatalog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/ImportSignalCatalog)
