---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateSlotType.html
---

# CreateSlotType
<a name="API_CreateSlotType"></a>

Creates a custom slot type

 To create a custom slot type, specify a name for the slot type and a set of enumeration values, the values that a slot of this type can assume.

## Request Syntax
<a name="API_CreateSlotType_RequestSyntax"></a>

```
PUT /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/slottypes/ HTTP/1.1
Content-type: application/json

{
   "compositeSlotTypeSetting": {
      "subSlots": [
         {
            "name": "{{string}}",
            "slotTypeId": "{{string}}"
         }
      ]
   },
   "description": "{{string}}",
   "externalSourceSetting": {
      "grammarSlotTypeSetting": {
         "source": {
            "kmsKeyArn": "{{string}}",
            "s3BucketName": "{{string}}",
            "s3ObjectKey": "{{string}}"
         }
      }
   },
   "parentSlotTypeSignature": "{{string}}",
   "slotTypeName": "{{string}}",
   "slotTypeValues": [
      {
         "sampleValue": {
            "value": "{{string}}"
         },
         "synonyms": [
            {
               "value": "{{string}}"
            }
         ]
      }
   ],
   "valueSelectionSetting": {
      "advancedRecognitionSetting": {
         "audioRecognitionStrategy": "{{string}}"
      },
      "regexFilter": {
         "pattern": "{{string}}"
      },
      "resolutionStrategy": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateSlotType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_CreateSlotType_RequestSyntax) **   <a name="lexv2-CreateSlotType-request-uri-botId"></a>
The identifier of the bot associated with this slot type.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_CreateSlotType_RequestSyntax) **   <a name="lexv2-CreateSlotType-request-uri-botVersion"></a>
The identifier of the bot version associated with this slot type.
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`
Required: Yes

 ** [localeId](#API_CreateSlotType_RequestSyntax) **   <a name="lexv2-CreateSlotType-request-uri-localeId"></a>
The identifier of the language and locale that the slot type will be used in. The string must match one of the supported locales. All of the bots, intents, and slots used by the slot type must have the same locale. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
Required: Yes

## Request Body
<a name="API_CreateSlotType_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [compositeSlotTypeSetting](#API_CreateSlotType_RequestSyntax) **   <a name="lexv2-CreateSlotType-request-compositeSlotTypeSetting"></a>
Specifications for a composite slot type.
Type: [CompositeSlotTypeSetting](API_CompositeSlotTypeSetting.md) object
Required: No

 ** [description](#API_CreateSlotType_RequestSyntax) **   <a name="lexv2-CreateSlotType-request-description"></a>
A description of the slot type. Use the description to help identify the slot type in lists.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** [externalSourceSetting](#API_CreateSlotType_RequestSyntax) **   <a name="lexv2-CreateSlotType-request-externalSourceSetting"></a>
Sets the type of external information used to create the slot type.
Type: [ExternalSourceSetting](API_ExternalSourceSetting.md) object
Required: No

 ** [parentSlotTypeSignature](#API_CreateSlotType_RequestSyntax) **   <a name="lexv2-CreateSlotType-request-parentSlotTypeSignature"></a>
The built-in slot type used as a parent of this slot type. When you define a parent slot type, the new slot type has the configuration of the parent slot type.
Only `AMAZON.AlphaNumeric` is supported.
Type: String
Required: No

 ** [slotTypeName](#API_CreateSlotType_RequestSyntax) **   <a name="lexv2-CreateSlotType-request-slotTypeName"></a>
The name for the slot. A slot type name must be unique within the intent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

 ** [slotTypeValues](#API_CreateSlotType_RequestSyntax) **   <a name="lexv2-CreateSlotType-request-slotTypeValues"></a>
A list of `SlotTypeValue` objects that defines the values that the slot type can take. Each value can have a list of synonyms, additional values that help train the machine learning model about the values that it resolves for a slot.
Type: Array of [SlotTypeValue](API_SlotTypeValue.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10000 items.
Required: No

 ** [valueSelectionSetting](#API_CreateSlotType_RequestSyntax) **   <a name="lexv2-CreateSlotType-request-valueSelectionSetting"></a>
Determines the strategy that Amazon Lex uses to select a value from the list of possible values. The field can be set to one of the following values:
+  `ORIGINAL_VALUE` - Returns the value entered by the user, if the user value is similar to the slot value.
+  `TOP_RESOLUTION` - If there is a resolution list for the slot, return the first value in the resolution list. If there is no resolution list, return null.
If you don't specify the `valueSelectionSetting` parameter, the default is `ORIGINAL_VALUE`.
Type: [SlotValueSelectionSetting](API_SlotValueSelectionSetting.md) object
Required: No

## Response Syntax
<a name="API_CreateSlotType_ResponseSyntax"></a>

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
<a name="API_CreateSlotType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_CreateSlotType_ResponseSyntax) **   <a name="lexv2-CreateSlotType-response-botId"></a>
The identifier for the bot associated with the slot type.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_CreateSlotType_ResponseSyntax) **   <a name="lexv2-CreateSlotType-response-botVersion"></a>
The version of the bot associated with the slot type.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [compositeSlotTypeSetting](#API_CreateSlotType_ResponseSyntax) **   <a name="lexv2-CreateSlotType-response-compositeSlotTypeSetting"></a>
Specifications for a composite slot type.
Type: [CompositeSlotTypeSetting](API_CompositeSlotTypeSetting.md) object

 ** [creationDateTime](#API_CreateSlotType_ResponseSyntax) **   <a name="lexv2-CreateSlotType-response-creationDateTime"></a>
A timestamp of the date and time that the slot type was created.
Type: Timestamp

 ** [description](#API_CreateSlotType_ResponseSyntax) **   <a name="lexv2-CreateSlotType-response-description"></a>
The description specified for the slot type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [externalSourceSetting](#API_CreateSlotType_ResponseSyntax) **   <a name="lexv2-CreateSlotType-response-externalSourceSetting"></a>
The type of external information used to create the slot type.
Type: [ExternalSourceSetting](API_ExternalSourceSetting.md) object

 ** [localeId](#API_CreateSlotType_ResponseSyntax) **   <a name="lexv2-CreateSlotType-response-localeId"></a>
The specified language and local specified for the slot type.
Type: String

 ** [parentSlotTypeSignature](#API_CreateSlotType_ResponseSyntax) **   <a name="lexv2-CreateSlotType-response-parentSlotTypeSignature"></a>
The signature of the base slot type specified for the slot type.
Type: String

 ** [slotTypeId](#API_CreateSlotType_ResponseSyntax) **   <a name="lexv2-CreateSlotType-response-slotTypeId"></a>
The unique identifier assigned to the slot type. Use this to identify the slot type in the `UpdateSlotType` and `DeleteSlotType` operations.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [slotTypeName](#API_CreateSlotType_ResponseSyntax) **   <a name="lexv2-CreateSlotType-response-slotTypeName"></a>
The name specified for the slot type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`

 ** [slotTypeValues](#API_CreateSlotType_ResponseSyntax) **   <a name="lexv2-CreateSlotType-response-slotTypeValues"></a>
The list of values that the slot type can assume.
Type: Array of [SlotTypeValue](API_SlotTypeValue.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10000 items.

 ** [valueSelectionSetting](#API_CreateSlotType_ResponseSyntax) **   <a name="lexv2-CreateSlotType-response-valueSelectionSetting"></a>
The strategy that Amazon Lex uses to select a value from the list of possible values.
Type: [SlotValueSelectionSetting](API_SlotValueSelectionSetting.md) object

## Errors
<a name="API_CreateSlotType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again.
HTTP Status Code: 409

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** PreconditionFailedException **
Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.
HTTP Status Code: 412

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
<a name="API_CreateSlotType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/CreateSlotType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/CreateSlotType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/CreateSlotType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/CreateSlotType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/CreateSlotType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/CreateSlotType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/CreateSlotType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/CreateSlotType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/CreateSlotType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/CreateSlotType)
