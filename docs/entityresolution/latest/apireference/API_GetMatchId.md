---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetMatchId.html
---

# GetMatchId
<a name="API_GetMatchId"></a>

Returns the corresponding Match ID of a customer record if the record has been processed in a rule-based matching workflow.

You can call this API as a dry run of an incremental load on the rule-based matching workflow.

## Request Syntax
<a name="API_GetMatchId_RequestSyntax"></a>

```
POST /matchingworkflows/{{workflowName}}/matches HTTP/1.1
Content-type: application/json

{
   "applyNormalization": {{boolean}},
   "record": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_GetMatchId_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workflowName](#API_GetMatchId_RequestSyntax) **   <a name="API-GetMatchId-request-uri-workflowName"></a>
The name of the workflow.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

## Request Body
<a name="API_GetMatchId_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applyNormalization](#API_GetMatchId_RequestSyntax) **   <a name="API-GetMatchId-request-applyNormalization"></a>
Normalizes the attributes defined in the schema in the input data. For example, if an attribute has an `AttributeType` of `PHONE_NUMBER`, and the data in the input table is in a format of 1234567890, AWS Entity Resolution will normalize this field in the output to (123)-456-7890.
Type: Boolean
Required: No

 ** [record](#API_GetMatchId_RequestSyntax) **   <a name="API-GetMatchId-request-record"></a>
The record to fetch the Match ID for.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 255.
Key Pattern: `[a-zA-Z_0-9- \t]*`
Value Length Constraints: Minimum length of 0. Maximum length of 255.
Value Pattern: `[a-zA-Z_0-9-./@ ()+\t]*`
Required: Yes

## Response Syntax
<a name="API_GetMatchId_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "matchId": "string",
   "matchRule": "string"
}
```

## Response Elements
<a name="API_GetMatchId_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [matchId](#API_GetMatchId_ResponseSyntax) **   <a name="API-GetMatchId-response-matchId"></a>
The unique identifiers for this group of match records.
Type: String

 ** [matchRule](#API_GetMatchId_ResponseSyntax) **   <a name="API-GetMatchId-response-matchRule"></a>
The rule the record matched on.
Type: String

## Errors
<a name="API_GetMatchId_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Entity Resolution service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by AWS Entity Resolution.
HTTP Status Code: 400

## Examples
<a name="API_GetMatchId_Examples"></a>

### Example
<a name="API_GetMatchId_Example_1"></a>

The following example uses the `GetMatchID` API to find matches for the given record using the specified matching workflow, while applying normalization to the input data. The request sets the `applyNormalization` field to `true`, indicating that the service should apply normalization to the input record before matching. The request body contains a `record` object containing the data to be matched. In this case, it includes `name`, `email`, and `phone`. The response from the API includes the `matchId`, which is the unique identifier for the matching entity record, and the `matchRule`, which is the rule the record matched on.

#### Sample Request
<a name="API_GetMatchId_Example_1_Request"></a>

```
POST /matchingworkflows/customerMatchingWorkflow/matches HTTP/1.1
Host: entity-resolution.us-west-2.amazonaws.com
Content-Type: application/json
X-Amz-Date: 20241114T101530Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20241114/us-west-2/entity-resolution/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=<signature>

{
  "applyNormalization": true,
  "record": {
    "name": "John Smith",
    "email": "john.smith@example.com",
    "phone": "+1-555-123-4567"
  }
}
```

#### Sample Response
<a name="API_GetMatchId_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
X-Amzn-RequestId: 9876zyxw-98zy-76xw-54vu-9876543210zy
Date: Thu, 14 Nov 2024 10:30:45 GMT

{
  "matchId": "491089aec7a1481cab8b492a1edf7953",
  "matchRule": "nameAndEmailMatch"
}
```

## See Also
<a name="API_GetMatchId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/GetMatchId)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/GetMatchId)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/GetMatchId)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/GetMatchId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/GetMatchId)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/GetMatchId)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/GetMatchId)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/GetMatchId)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/GetMatchId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/GetMatchId)
