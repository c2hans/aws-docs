---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeSlotType.html
---

# DescribeSlotType
<a name="API_DescribeSlotType"></a>

Gets metadata information about a slot type.

## Request Syntax
<a name="API_DescribeSlotType_RequestSyntax"></a>

```
GET /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/slottypes/{{slotTypeId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeSlotType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_DescribeSlotType_RequestSyntax) **   <a name="lexv2-DescribeSlotType-request-uri-botId"></a>
The identifier of the bot associated with the slot type.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_DescribeSlotType_RequestSyntax) **   <a name="lexv2-DescribeSlotType-request-uri-botVersion"></a>
The version of the bot associated with the slot type.
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: Yes

 ** [localeId](#API_DescribeSlotType_RequestSyntax) **   <a name="lexv2-DescribeSlotType-request-uri-localeId"></a>
The identifier of the language and locale of the slot type to describe. The string must match one of the supported locales. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
Required: Yes

 ** [slotTypeId](#API_DescribeSlotType_RequestSyntax) **   <a name="lexv2-DescribeSlotType-request-uri-slotTypeId"></a>
The identifier of the slot type.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_DescribeSlotType_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeSlotType_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botId": "string",
   "botVersion": "string",
   "compositeSlotTypeSetting": {
      "subSlots": [
         {
            "name": "string",
            "slotTypeId": "string"
         }
      ]
   },
   "creationDateTime": number,
   "description": "string",
   "externalSourceSetting": {
      "grammarSlotTypeSetting": {
         "source": {
            "kmsKeyArn": "string",
            "s3BucketName": "string",
            "s3ObjectKey": "string"
         }
      }
   },
   "lastUpdatedDateTime": number,
   "localeId": "string",
   "parentSlotTypeSignature": "string",
   "slotTypeId": "string",
   "slotTypeName": "string",
   "slotTypeValues": [
      {
         "sampleValue": {
            "value": "string"
         },
         "synonyms": [
            {
               "value": "string"
            }
         ]
      }
   ],
   "valueSelectionSetting": {
      "advancedRecognitionSetting": {
         "audioRecognitionStrategy": "string"
      },
      "regexFilter": {
         "pattern": "string"
      },
      "resolutionStrategy": "string"
   }
}
```

## Response Elements
<a name="API_DescribeSlotType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_DescribeSlotType_ResponseSyntax) **   <a name="lexv2-DescribeSlotType-response-botId"></a>
The identifier of the bot associated with the slot type.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_DescribeSlotType_ResponseSyntax) **   <a name="lexv2-DescribeSlotType-response-botVersion"></a>
The version of the bot associated with the slot type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`

 ** [compositeSlotTypeSetting](#API_DescribeSlotType_ResponseSyntax) **   <a name="lexv2-DescribeSlotType-response-compositeSlotTypeSetting"></a>
Specifications for a composite slot type.
Type: [CompositeSlotTypeSetting](API_CompositeSlotTypeSetting.md) object

 ** [creationDateTime](#API_DescribeSlotType_ResponseSyntax) **   <a name="lexv2-DescribeSlotType-response-creationDateTime"></a>
A timestamp of the date and time that the slot type was created.
Type: Timestamp

 ** [description](#API_DescribeSlotType_ResponseSyntax) **   <a name="lexv2-DescribeSlotType-response-description"></a>
The description specified for the slot type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [externalSourceSetting](#API_DescribeSlotType_ResponseSyntax) **   <a name="lexv2-DescribeSlotType-response-externalSourceSetting"></a>
Provides information about the external source of the slot type's definition.
Type: [ExternalSourceSetting](API_ExternalSourceSetting.md) object

 ** [lastUpdatedDateTime](#API_DescribeSlotType_ResponseSyntax) **   <a name="lexv2-DescribeSlotType-response-lastUpdatedDateTime"></a>
A timestamp of the date and time that the slot type was last updated.
Type: Timestamp

 ** [localeId](#API_DescribeSlotType_ResponseSyntax) **   <a name="lexv2-DescribeSlotType-response-localeId"></a>
The language and locale specified for the slot type.
Type: String

 ** [parentSlotTypeSignature](#API_DescribeSlotType_ResponseSyntax) **   <a name="lexv2-DescribeSlotType-response-parentSlotTypeSignature"></a>
The built in slot type used as a parent to this slot type.
Type: String

 ** [slotTypeId](#API_DescribeSlotType_ResponseSyntax) **   <a name="lexv2-DescribeSlotType-response-slotTypeId"></a>
The unique identifier for the slot type.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [slotTypeName](#API_DescribeSlotType_ResponseSyntax) **   <a name="lexv2-DescribeSlotType-response-slotTypeName"></a>
The name specified for the slot type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`

 ** [slotTypeValues](#API_DescribeSlotType_ResponseSyntax) **   <a name="lexv2-DescribeSlotType-response-slotTypeValues"></a>
The values that the slot type can take. Includes any synonyms for the slot type values.
Type: Array of [SlotTypeValue](API_SlotTypeValue.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10000 items.

 ** [valueSelectionSetting](#API_DescribeSlotType_ResponseSyntax) **   <a name="lexv2-DescribeSlotType-response-valueSelectionSetting"></a>
The strategy that Amazon Lex uses to choose a value from a list of possible values.
Type: [SlotValueSelectionSetting](API_SlotValueSelectionSetting.md) object

## Errors
<a name="API_DescribeSlotType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have reached a quota for your bot.
HTTP Status Code: 402

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_DescribeSlotType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DescribeSlotType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DescribeSlotType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DescribeSlotType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DescribeSlotType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DescribeSlotType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DescribeSlotType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DescribeSlotType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DescribeSlotType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DescribeSlotType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DescribeSlotType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
