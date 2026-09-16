---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchGetStandardsControlAssociations.html
---

# BatchGetStandardsControlAssociations
<a name="API_BatchGetStandardsControlAssociations"></a>

 For a batch of security controls and standards, identifies whether each control is currently enabled or disabled in a standard.

 Calls to this operation return a `RESOURCE_NOT_FOUND_EXCEPTION` error when the standard subscription for the association has a `NOT_READY_FOR_UPDATES` value for `StandardsControlsUpdatable`.

## Request Syntax
<a name="API_BatchGetStandardsControlAssociations_RequestSyntax"></a>

```
POST /associations/batchGet HTTP/1.1
Content-type: application/json

{
   "StandardsControlAssociationIds": [
      {
         "SecurityControlId": "{{string}}",
         "StandardsArn": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchGetStandardsControlAssociations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetStandardsControlAssociations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [StandardsControlAssociationIds](#API_BatchGetStandardsControlAssociations_RequestSyntax) **   <a name="securityhub-BatchGetStandardsControlAssociations-request-StandardsControlAssociationIds"></a>
 An array with one or more objects that includes a security control (identified with `SecurityControlId`, `SecurityControlArn`, or a mix of both parameters) and the Amazon Resource Name (ARN) of a standard. This field is used to query the enablement status of a control in a specified standard. The security control ID or ARN is the same across standards.
Type: Array of [StandardsControlAssociationId](API_StandardsControlAssociationId.md) objects
Required: Yes

## Response Syntax
<a name="API_BatchGetStandardsControlAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "StandardsControlAssociationDetails": [
      {
         "AssociationStatus": "string",
         "RelatedRequirements": [ "string" ],
         "SecurityControlArn": "string",
         "SecurityControlId": "string",
         "StandardsArn": "string",
         "StandardsControlArns": [ "string" ],
         "StandardsControlDescription": "string",
         "StandardsControlTitle": "string",
         "UpdatedAt": "string",
         "UpdatedReason": "string"
      }
   ],
   "UnprocessedAssociations": [
      {
         "ErrorCode": "string",
         "ErrorReason": "string",
         "StandardsControlAssociationId": {
            "SecurityControlId": "string",
            "StandardsArn": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetStandardsControlAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StandardsControlAssociationDetails](#API_BatchGetStandardsControlAssociations_ResponseSyntax) **   <a name="securityhub-BatchGetStandardsControlAssociations-response-StandardsControlAssociationDetails"></a>
Provides the enablement status of a security control in a specified standard and other details for the control in relation to the specified standard.
Type: Array of [StandardsControlAssociationDetail](API_StandardsControlAssociationDetail.md) objects

 ** [UnprocessedAssociations](#API_BatchGetStandardsControlAssociations_ResponseSyntax) **   <a name="securityhub-BatchGetStandardsControlAssociations-response-UnprocessedAssociations"></a>
 A security control (identified with `SecurityControlId`, `SecurityControlArn`, or a mix of both parameters) whose enablement status in a specified standard cannot be returned.
Type: Array of [UnprocessedStandardsControlAssociation](API_UnprocessedStandardsControlAssociation.md) objects

## Errors
<a name="API_BatchGetStandardsControlAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_BatchGetStandardsControlAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/BatchGetStandardsControlAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/BatchGetStandardsControlAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/BatchGetStandardsControlAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/BatchGetStandardsControlAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/BatchGetStandardsControlAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/BatchGetStandardsControlAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/BatchGetStandardsControlAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/BatchGetStandardsControlAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/BatchGetStandardsControlAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/BatchGetStandardsControlAssociations)
