---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_StartServiceSoftwareUpdate.html
---

# StartServiceSoftwareUpdate
<a name="API_StartServiceSoftwareUpdate"></a>

Schedules a service software update for an Amazon OpenSearch Service domain. For more information, see [Service software updates in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html).

## Request Syntax
<a name="API_StartServiceSoftwareUpdate_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/serviceSoftwareUpdate/start HTTP/1.1
Content-type: application/json

{
   "DesiredStartTime": {{number}},
   "DomainName": "{{string}}",
   "ScheduleAt": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartServiceSoftwareUpdate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartServiceSoftwareUpdate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DesiredStartTime](#API_StartServiceSoftwareUpdate_RequestSyntax) **   <a name="opensearchservice-StartServiceSoftwareUpdate-request-DesiredStartTime"></a>
The Epoch timestamp when you want the service software update to start. You only need to specify this parameter if you set `ScheduleAt` to `TIMESTAMP`.
Type: Long
Required: No

 ** [DomainName](#API_StartServiceSoftwareUpdate_RequestSyntax) **   <a name="opensearchservice-StartServiceSoftwareUpdate-request-DomainName"></a>
The name of the domain that you want to update to the latest service software.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** [ScheduleAt](#API_StartServiceSoftwareUpdate_RequestSyntax) **   <a name="opensearchservice-StartServiceSoftwareUpdate-request-ScheduleAt"></a>
When to start the service software update.
+  `NOW` - Immediately schedules the update to happen in the current hour if there's capacity available.
+  `TIMESTAMP` - Lets you specify a custom date and time to apply the update. If you specify this value, you must also provide a value for `DesiredStartTime`.
+  `OFF_PEAK_WINDOW` - Marks the update to be picked up during an upcoming off-peak window. There's no guarantee that the update will happen during the next immediate window. Depending on capacity, it might happen in subsequent days.
Default: `NOW` if you don't specify a value for `DesiredStartTime`, and `TIMESTAMP` if you do.
Type: String
Valid Values: `NOW | TIMESTAMP | OFF_PEAK_WINDOW`
Required: No

## Response Syntax
<a name="API_StartServiceSoftwareUpdate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ServiceSoftwareOptions": {
      "AutomatedUpdateDate": number,
      "Cancellable": boolean,
      "CurrentVersion": "string",
      "Description": "string",
      "NewVersion": "string",
      "OptionalDeployment": boolean,
      "UpdateAvailable": boolean,
      "UpdateStatus": "string"
   }
}
```

## Response Elements
<a name="API_StartServiceSoftwareUpdate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ServiceSoftwareOptions](#API_StartServiceSoftwareUpdate_ResponseSyntax) **   <a name="opensearchservice-StartServiceSoftwareUpdate-response-ServiceSoftwareOptions"></a>
The current status of the OpenSearch Service software update.
Type: [ServiceSoftwareOptions](API_ServiceSoftwareOptions.md) object

## Errors
<a name="API_StartServiceSoftwareUpdate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_StartServiceSoftwareUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/StartServiceSoftwareUpdate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/StartServiceSoftwareUpdate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/StartServiceSoftwareUpdate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/StartServiceSoftwareUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/StartServiceSoftwareUpdate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/StartServiceSoftwareUpdate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/StartServiceSoftwareUpdate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/StartServiceSoftwareUpdate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/StartServiceSoftwareUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/StartServiceSoftwareUpdate)
