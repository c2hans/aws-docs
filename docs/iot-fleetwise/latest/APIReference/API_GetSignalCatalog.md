---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetSignalCatalog.html
---

# GetSignalCatalog
<a name="API_GetSignalCatalog"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

 Retrieves information about a signal catalog.

## Request Syntax
<a name="API_GetSignalCatalog_RequestSyntax"></a>

```
{
   "name": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSignalCatalog_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [name](#API_GetSignalCatalog_RequestSyntax) **   <a name="iotfleetwise-GetSignalCatalog-request-name"></a>
 The name of the signal catalog to retrieve information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

## Response Syntax
<a name="API_GetSignalCatalog_ResponseSyntax"></a>

```
{
   "arn": "string",
   "creationTime": number,
   "description": "string",
   "lastModificationTime": number,
   "name": "string",
   "nodeCounts": {
      "totalActuators": number,
      "totalAttributes": number,
      "totalBranches": number,
      "totalNodes": number,
      "totalProperties": number,
      "totalSensors": number,
      "totalStructs": number
   }
}
```

## Response Elements
<a name="API_GetSignalCatalog_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetSignalCatalog_ResponseSyntax) **   <a name="iotfleetwise-GetSignalCatalog-response-arn"></a>
 The Amazon Resource Name (ARN) of the signal catalog.
Type: String

 ** [creationTime](#API_GetSignalCatalog_ResponseSyntax) **   <a name="iotfleetwise-GetSignalCatalog-response-creationTime"></a>
 The time the signal catalog was created in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp

 ** [description](#API_GetSignalCatalog_ResponseSyntax) **   <a name="iotfleetwise-GetSignalCatalog-response-description"></a>
 A brief description of the signal catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [lastModificationTime](#API_GetSignalCatalog_ResponseSyntax) **   <a name="iotfleetwise-GetSignalCatalog-response-lastModificationTime"></a>
The last time the signal catalog was modified.
Type: Timestamp

 ** [name](#API_GetSignalCatalog_ResponseSyntax) **   <a name="iotfleetwise-GetSignalCatalog-response-name"></a>
 The name of the signal catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`

 ** [nodeCounts](#API_GetSignalCatalog_ResponseSyntax) **   <a name="iotfleetwise-GetSignalCatalog-response-nodeCounts"></a>
 The total number of network nodes specified in a signal catalog.
Type: [NodeCounts](API_NodeCounts.md) object

## Errors
<a name="API_GetSignalCatalog_Errors"></a>

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
<a name="API_GetSignalCatalog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/GetSignalCatalog)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/GetSignalCatalog)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/GetSignalCatalog)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/GetSignalCatalog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/GetSignalCatalog)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/GetSignalCatalog)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/GetSignalCatalog)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/GetSignalCatalog)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/GetSignalCatalog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/GetSignalCatalog)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
