---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetModelManifest.html
---

# GetModelManifest
<a name="API_GetModelManifest"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

 Retrieves information about a vehicle model (model manifest).

## Request Syntax
<a name="API_GetModelManifest_RequestSyntax"></a>

```
{
   "name": "{{string}}"
}
```

## Request Parameters
<a name="API_GetModelManifest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [name](#API_GetModelManifest_RequestSyntax) **   <a name="iotfleetwise-GetModelManifest-request-name"></a>
 The name of the vehicle model to retrieve information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

## Response Syntax
<a name="API_GetModelManifest_ResponseSyntax"></a>

```
{
   "arn": "string",
   "creationTime": number,
   "description": "string",
   "lastModificationTime": number,
   "name": "string",
   "signalCatalogArn": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_GetModelManifest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetModelManifest_ResponseSyntax) **   <a name="iotfleetwise-GetModelManifest-response-arn"></a>
 The Amazon Resource Name (ARN) of the vehicle model.
Type: String

 ** [creationTime](#API_GetModelManifest_ResponseSyntax) **   <a name="iotfleetwise-GetModelManifest-response-creationTime"></a>
The time the vehicle model was created, in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp

 ** [description](#API_GetModelManifest_ResponseSyntax) **   <a name="iotfleetwise-GetModelManifest-response-description"></a>
 A brief description of the vehicle model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [lastModificationTime](#API_GetModelManifest_ResponseSyntax) **   <a name="iotfleetwise-GetModelManifest-response-lastModificationTime"></a>
The last time the vehicle model was modified.
Type: Timestamp

 ** [name](#API_GetModelManifest_ResponseSyntax) **   <a name="iotfleetwise-GetModelManifest-response-name"></a>
 The name of the vehicle model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`

 ** [signalCatalogArn](#API_GetModelManifest_ResponseSyntax) **   <a name="iotfleetwise-GetModelManifest-response-signalCatalogArn"></a>
 The ARN of the signal catalog associated with the vehicle model.
Type: String

 ** [status](#API_GetModelManifest_ResponseSyntax) **   <a name="iotfleetwise-GetModelManifest-response-status"></a>
 The state of the vehicle model. If the status is `ACTIVE`, the vehicle model can't be edited. You can edit the vehicle model if the status is marked `DRAFT`.
Type: String
Valid Values: `ACTIVE | DRAFT | INVALID | VALIDATING`

## Errors
<a name="API_GetModelManifest_Errors"></a>

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
<a name="API_GetModelManifest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/GetModelManifest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/GetModelManifest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/GetModelManifest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/GetModelManifest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/GetModelManifest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/GetModelManifest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/GetModelManifest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/GetModelManifest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/GetModelManifest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/GetModelManifest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
