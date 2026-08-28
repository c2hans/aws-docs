---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetCollaborationMLInputChannel.html
---

# GetCollaborationMLInputChannel
<a name="API_GetCollaborationMLInputChannel"></a>

Returns information about a specific ML input channel in a collaboration.

## Request Syntax
<a name="API_GetCollaborationMLInputChannel_RequestSyntax"></a>

```
GET /collaborations/{{collaborationIdentifier}}/ml-input-channels/{{mlInputChannelArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCollaborationMLInputChannel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [collaborationIdentifier](#API_GetCollaborationMLInputChannel_RequestSyntax) **   <a name="API-GetCollaborationMLInputChannel-request-uri-collaborationIdentifier"></a>
The collaboration ID of the collaboration that contains the ML input channel that you want to get.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [mlInputChannelArn](#API_GetCollaborationMLInputChannel_RequestSyntax) **   <a name="API-GetCollaborationMLInputChannel-request-uri-mlInputChannelArn"></a>
The Amazon Resource Name (ARN) of the ML input channel that you want to get.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/ml-input-channel/[-a-zA-Z0-9_/.]+`
Required: Yes

## Request Body
<a name="API_GetCollaborationMLInputChannel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCollaborationMLInputChannel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "collaborationIdentifier": "string",
   "configuredModelAlgorithmAssociations": [ "string" ],
   "createTime": "string",
   "creatorAccountId": "string",
   "description": "string",
   "membershipIdentifier": "string",
   "mlInputChannelArn": "string",
   "name": "string",
   "numberOfRecords": number,
   "payerConfiguration": {
      "computePayerAccountId": "string",
      "syntheticDataPayerAccountId": "string"
   },
   "privacyBudgets": { ... },
   "retentionInDays": number,
   "status": "string",
   "statusDetails": {
      "message": "string",
      "statusCode": "string"
   },
   "syntheticDataConfiguration": {
      "syntheticDataEvaluationScores": {
         "dataPrivacyScores": {
            "membershipInferenceAttackScores": [
               {
                  "attackVersion": "string",
                  "score": number
               }
            ]
         }
      },
      "syntheticDataParameters": {
         "columnClassification": {
            "columnMapping": [
               {
                  "columnName": "string",
                  "columnType": "string",
                  "isPredictiveValue": boolean
               }
            ]
         },
         "epsilon": number,
         "maxMembershipInferenceAttackScore": number
      }
   },
   "updateTime": "string"
}
```

## Response Elements
<a name="API_GetCollaborationMLInputChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collaborationIdentifier](#API_GetCollaborationMLInputChannel_ResponseSyntax) **   <a name="API-GetCollaborationMLInputChannel-response-collaborationIdentifier"></a>
The collaboration ID of the collaboration that contains the ML input channel.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [configuredModelAlgorithmAssociations](#API_GetCollaborationMLInputChannel_ResponseSyntax) **   <a name="API-GetCollaborationMLInputChannel-response-configuredModelAlgorithmAssociations"></a>
The configured model algorithm associations that were used to create the ML input channel.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/configured-model-algorithm-association/[-a-zA-Z0-9_/.]+`

 ** [createTime](#API_GetCollaborationMLInputChannel_ResponseSyntax) **   <a name="API-GetCollaborationMLInputChannel-response-createTime"></a>
The time at which the ML input channel was created.
Type: Timestamp

 ** [creatorAccountId](#API_GetCollaborationMLInputChannel_ResponseSyntax) **   <a name="API-GetCollaborationMLInputChannel-response-creatorAccountId"></a>
The account ID of the member who created the ML input channel.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [description](#API_GetCollaborationMLInputChannel_ResponseSyntax) **   <a name="API-GetCollaborationMLInputChannel-response-description"></a>
The description of the ML input channel.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`

 ** [membershipIdentifier](#API_GetCollaborationMLInputChannel_ResponseSyntax) **   <a name="API-GetCollaborationMLInputChannel-response-membershipIdentifier"></a>
The membership ID of the membership that contains the ML input channel.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [mlInputChannelArn](#API_GetCollaborationMLInputChannel_ResponseSyntax) **   <a name="API-GetCollaborationMLInputChannel-response-mlInputChannelArn"></a>
The Amazon Resource Name (ARN) of the ML input channel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/ml-input-channel/[-a-zA-Z0-9_/.]+`

 ** [name](#API_GetCollaborationMLInputChannel_ResponseSyntax) **   <a name="API-GetCollaborationMLInputChannel-response-name"></a>
The name of the ML input channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`

 ** [numberOfRecords](#API_GetCollaborationMLInputChannel_ResponseSyntax) **   <a name="API-GetCollaborationMLInputChannel-response-numberOfRecords"></a>
The number of records in the ML input channel.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 100000000000.

 ** [payerConfiguration](#API_GetCollaborationMLInputChannel_ResponseSyntax) **   <a name="API-GetCollaborationMLInputChannel-response-payerConfiguration"></a>
The payer configuration for the ML input channel.
Type: [PayerConfiguration](API_PayerConfiguration.md) object

 ** [privacyBudgets](#API_GetCollaborationMLInputChannel_ResponseSyntax) **   <a name="API-GetCollaborationMLInputChannel-response-privacyBudgets"></a>
Returns the privacy budgets that control access to this Clean Rooms ML input channel. Use these budgets to monitor and limit resource consumption over specified time periods.
Type: [PrivacyBudgets](API_PrivacyBudgets.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [retentionInDays](#API_GetCollaborationMLInputChannel_ResponseSyntax) **   <a name="API-GetCollaborationMLInputChannel-response-retentionInDays"></a>
The number of days to retain the data for the ML input channel.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 30.

 ** [status](#API_GetCollaborationMLInputChannel_ResponseSyntax) **   <a name="API-GetCollaborationMLInputChannel-response-status"></a>
The status of the ML input channel.
Type: String
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | DELETE_PENDING | DELETE_IN_PROGRESS | DELETE_FAILED | INACTIVE`

 ** [statusDetails](#API_GetCollaborationMLInputChannel_ResponseSyntax) **   <a name="API-GetCollaborationMLInputChannel-response-statusDetails"></a>
Details about the status of a resource.
Type: [StatusDetails](API_StatusDetails.md) object

 ** [syntheticDataConfiguration](#API_GetCollaborationMLInputChannel_ResponseSyntax) **   <a name="API-GetCollaborationMLInputChannel-response-syntheticDataConfiguration"></a>
The synthetic data configuration for this ML input channel, including parameters for generating privacy-preserving synthetic data and evaluation scores for measuring the privacy of the generated data.
Type: [SyntheticDataConfiguration](API_SyntheticDataConfiguration.md) object

 ** [updateTime](#API_GetCollaborationMLInputChannel_ResponseSyntax) **   <a name="API-GetCollaborationMLInputChannel-response-updateTime"></a>
The most recent time at which the ML input channel was updated.
Type: Timestamp

## Errors
<a name="API_GetCollaborationMLInputChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The resource you are requesting does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_GetCollaborationMLInputChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/GetCollaborationMLInputChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/GetCollaborationMLInputChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/GetCollaborationMLInputChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/GetCollaborationMLInputChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/GetCollaborationMLInputChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/GetCollaborationMLInputChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/GetCollaborationMLInputChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/GetCollaborationMLInputChannel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/GetCollaborationMLInputChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/GetCollaborationMLInputChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
