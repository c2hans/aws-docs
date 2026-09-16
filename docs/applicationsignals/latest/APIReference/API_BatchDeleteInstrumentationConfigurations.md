---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchDeleteInstrumentationConfigurations.html
---

# BatchDeleteInstrumentationConfigurations
<a name="API_BatchDeleteInstrumentationConfigurations"></a>

Deletes multiple instrumentation configurations in a single request. Supports two mutually exclusive selection methods:
+ By scope: delete all configurations matching a service, environment, and instrumentation type.
+ By ARN list: delete specific configurations by providing a list of resource ARNs.

## Request Syntax
<a name="API_BatchDeleteInstrumentationConfigurations_RequestSyntax"></a>

```
POST /batch-delete-instrumentation-configurations HTTP/1.1
Content-type: application/json

{
   "DeletionTarget": { ... }
}
```

## URI Request Parameters
<a name="API_BatchDeleteInstrumentationConfigurations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchDeleteInstrumentationConfigurations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DeletionTarget](#API_BatchDeleteInstrumentationConfigurations_RequestSyntax) **   <a name="applicationsignals-BatchDeleteInstrumentationConfigurations-request-DeletionTarget"></a>
The deletion target - either bulk by scope or targeted by ARN list.
Type: [BatchDeleteDeletionTarget](API_BatchDeleteDeletionTarget.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_BatchDeleteInstrumentationConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DeletedCount": number,
   "Errors": [
      {
         "Code": "string",
         "Message": "string",
         "ResourceArn": "string"
      }
   ],
   "SuccessfulDeletions": [
      {
         "LocationHash": "string",
         "ResourceArn": "string",
         "SignalType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDeleteInstrumentationConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeletedCount](#API_BatchDeleteInstrumentationConfigurations_ResponseSyntax) **   <a name="applicationsignals-BatchDeleteInstrumentationConfigurations-response-DeletedCount"></a>
The number of configurations successfully deleted. When deleting by scope, this is the total count of deleted items. When deleting by ARN list, this equals the length of `SuccessfulDeletions`.
Type: Integer

 ** [Errors](#API_BatchDeleteInstrumentationConfigurations_ResponseSyntax) **   <a name="applicationsignals-BatchDeleteInstrumentationConfigurations-response-Errors"></a>
The list of configurations that failed to delete.
Type: Array of [BatchDeleteError](API_BatchDeleteError.md) objects

 ** [SuccessfulDeletions](#API_BatchDeleteInstrumentationConfigurations_ResponseSyntax) **   <a name="applicationsignals-BatchDeleteInstrumentationConfigurations-response-SuccessfulDeletions"></a>
The list of successfully deleted configurations. Deleting by scope populates `SignalType` and `LocationHash` per item; deleting by ARN list populates `ResourceArn` per item.
Type: Array of [BatchDeleteSuccessfulDeletion](API_BatchDeleteSuccessfulDeletion.md) objects

## Errors
<a name="API_BatchDeleteInstrumentationConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_BatchDeleteInstrumentationConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/BatchDeleteInstrumentationConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/BatchDeleteInstrumentationConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/BatchDeleteInstrumentationConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/BatchDeleteInstrumentationConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/BatchDeleteInstrumentationConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/BatchDeleteInstrumentationConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/BatchDeleteInstrumentationConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/BatchDeleteInstrumentationConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/BatchDeleteInstrumentationConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/BatchDeleteInstrumentationConfigurations)
