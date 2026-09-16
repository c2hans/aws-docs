---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DisassociateHoursOfOperations.html
---

# DisassociateHoursOfOperations
<a name="API_DisassociateHoursOfOperations"></a>

Disassociates a set of hours of operations with another hours of operation. For more information about inheriting overrides from parent hours of operation, see [Hours of operation overrides](https://docs.aws.amazon.com/connect/latest/adminguide/hours-of-operation-overrides.html) in the Administrator Guide.

## Request Syntax
<a name="API_DisassociateHoursOfOperations_RequestSyntax"></a>

```
POST /hours-of-operations/{{InstanceId}}/{{HoursOfOperationId}}/disassociate-hours HTTP/1.1
Content-type: application/json

{
   "ParentHoursOfOperationIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DisassociateHoursOfOperations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HoursOfOperationId](#API_DisassociateHoursOfOperations_RequestSyntax) **   <a name="connect-DisassociateHoursOfOperations-request-uri-HoursOfOperationId"></a>
The identifier of the child hours of operation.
Required: Yes

 ** [InstanceId](#API_DisassociateHoursOfOperations_RequestSyntax) **   <a name="connect-DisassociateHoursOfOperations-request-uri-InstanceId"></a>
The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DisassociateHoursOfOperations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ParentHoursOfOperationIds](#API_DisassociateHoursOfOperations_RequestSyntax) **   <a name="connect-DisassociateHoursOfOperations-request-ParentHoursOfOperationIds"></a>
The Amazon Resource Names (ARNs) of the parent hours of operation resources to disassociate with the child hours of operation resource.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: Yes

## Response Syntax
<a name="API_DisassociateHoursOfOperations_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisassociateHoursOfOperations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateHoursOfOperations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConditionalOperationFailedException **
Request processing failed because dependent condition failed.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DisassociateHoursOfOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DisassociateHoursOfOperations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DisassociateHoursOfOperations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DisassociateHoursOfOperations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DisassociateHoursOfOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DisassociateHoursOfOperations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DisassociateHoursOfOperations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DisassociateHoursOfOperations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DisassociateHoursOfOperations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DisassociateHoursOfOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DisassociateHoursOfOperations)
