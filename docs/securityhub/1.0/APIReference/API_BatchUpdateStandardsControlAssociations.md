---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html
---

# BatchUpdateStandardsControlAssociations
<a name="API_BatchUpdateStandardsControlAssociations"></a>

 For a batch of security controls and standards, this operation updates the enablement status of a control in a standard.

## Request Syntax
<a name="API_BatchUpdateStandardsControlAssociations_RequestSyntax"></a>

```
PATCH /associations HTTP/1.1
Content-type: application/json

{
   "StandardsControlAssociationUpdates": [
      {
         "AssociationStatus": "{{string}}",
         "SecurityControlId": "{{string}}",
         "StandardsArn": "{{string}}",
         "UpdatedReason": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchUpdateStandardsControlAssociations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchUpdateStandardsControlAssociations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [StandardsControlAssociationUpdates](#API_BatchUpdateStandardsControlAssociations_RequestSyntax) **   <a name="securityhub-BatchUpdateStandardsControlAssociations-request-StandardsControlAssociationUpdates"></a>
 Updates the enablement status of a security control in a specified standard.
 Calls to this operation return a `RESOURCE_NOT_FOUND_EXCEPTION` error when the standard subscription for the control has `StandardsControlsUpdatable` value `NOT_READY_FOR_UPDATES`.
Type: Array of [StandardsControlAssociationUpdate](API_StandardsControlAssociationUpdate.md) objects
Required: Yes

## Response Syntax
<a name="API_BatchUpdateStandardsControlAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "UnprocessedAssociationUpdates": [
      {
         "ErrorCode": "string",
         "ErrorReason": "string",
         "StandardsControlAssociationUpdate": {
            "AssociationStatus": "string",
            "SecurityControlId": "string",
            "StandardsArn": "string",
            "UpdatedReason": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_BatchUpdateStandardsControlAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UnprocessedAssociationUpdates](#API_BatchUpdateStandardsControlAssociations_ResponseSyntax) **   <a name="securityhub-BatchUpdateStandardsControlAssociations-response-UnprocessedAssociationUpdates"></a>
 A security control (identified with `SecurityControlId`, `SecurityControlArn`, or a mix of both parameters) whose enablement status in a specified standard couldn't be updated.
Type: Array of [UnprocessedStandardsControlAssociationUpdate](API_UnprocessedStandardsControlAssociationUpdate.md) objects

## Errors
<a name="API_BatchUpdateStandardsControlAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

## See Also
<a name="API_BatchUpdateStandardsControlAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/BatchUpdateStandardsControlAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/BatchUpdateStandardsControlAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/BatchUpdateStandardsControlAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/BatchUpdateStandardsControlAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/BatchUpdateStandardsControlAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/BatchUpdateStandardsControlAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/BatchUpdateStandardsControlAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/BatchUpdateStandardsControlAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/BatchUpdateStandardsControlAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/BatchUpdateStandardsControlAssociations)
