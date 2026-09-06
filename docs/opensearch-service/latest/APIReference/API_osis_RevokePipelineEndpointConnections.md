---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_RevokePipelineEndpointConnections.html
---

# RevokePipelineEndpointConnections
<a name="API_osis_RevokePipelineEndpointConnections"></a>

Revokes pipeline endpoints from specified endpoint IDs.

## Request Syntax
<a name="API_osis_RevokePipelineEndpointConnections_RequestSyntax"></a>

```
POST /2022-01-01/osis/revokePipelineEndpointConnections HTTP/1.1
Content-type: application/json

{
   "EndpointIds": [ "{{string}}" ],
   "PipelineArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_osis_RevokePipelineEndpointConnections_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_osis_RevokePipelineEndpointConnections_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EndpointIds](#API_osis_RevokePipelineEndpointConnections_RequestSyntax) **   <a name="opensearchservice-osis_RevokePipelineEndpointConnections-request-EndpointIds"></a>
A list of endpoint IDs for which to revoke access to the pipeline.
Type: Array of strings
Length Constraints: Minimum length of 3. Maximum length of 512.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]+$`
Required: Yes

 ** [PipelineArn](#API_osis_RevokePipelineEndpointConnections_RequestSyntax) **   <a name="opensearchservice-osis_RevokePipelineEndpointConnections-request-PipelineArn"></a>
The Amazon Resource Name (ARN) of the pipeline from which to revoke endpoint connections.
Type: String
Length Constraints: Minimum length of 46. Maximum length of 76.
Pattern: `^arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b):osis:.+:pipeline\/.+$`
Required: Yes

## Response Syntax
<a name="API_osis_RevokePipelineEndpointConnections_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PipelineArn": "string"
}
```

## Response Elements
<a name="API_osis_RevokePipelineEndpointConnections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PipelineArn](#API_osis_RevokePipelineEndpointConnections_ResponseSyntax) **   <a name="opensearchservice-osis_RevokePipelineEndpointConnections-response-PipelineArn"></a>
The Amazon Resource Name (ARN) of the pipeline from which endpoint connections were revoked.
Type: String
Length Constraints: Minimum length of 46. Maximum length of 76.
Pattern: `^arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b):osis:.+:pipeline\/.+$`

## Errors
<a name="API_osis_RevokePipelineEndpointConnections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to access the resource.
HTTP Status Code: 403

 ** DisabledOperationException **
Exception is thrown when an operation has been disabled.
HTTP Status Code: 409

 ** InternalException **
The request failed because of an unknown error, exception, or failure (the failure is internal to the service).
HTTP Status Code: 500

 ** LimitExceededException **
You attempted to create more than the allowed number of tags.
HTTP Status Code: 409

 ** ValidationException **
An exception for missing or invalid input fields.
HTTP Status Code: 400

## See Also
<a name="API_osis_RevokePipelineEndpointConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/osis-2022-01-01/RevokePipelineEndpointConnections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/osis-2022-01-01/RevokePipelineEndpointConnections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/RevokePipelineEndpointConnections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/osis-2022-01-01/RevokePipelineEndpointConnections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/RevokePipelineEndpointConnections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/osis-2022-01-01/RevokePipelineEndpointConnections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/osis-2022-01-01/RevokePipelineEndpointConnections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/osis-2022-01-01/RevokePipelineEndpointConnections)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/osis-2022-01-01/RevokePipelineEndpointConnections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/RevokePipelineEndpointConnections)
