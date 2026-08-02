---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-voice-id_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_connect-voice-id_ListTagsForResource"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Lists all tags associated with a specified Voice ID resource.

## Request Syntax
<a name="API_connect-voice-id_ListTagsForResource_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_connect-voice-id_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_connect-voice-id_ListTagsForResource_RequestSyntax) **   <a name="connect-connect-voice-id_ListTagsForResource-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the Voice ID resource for which you want to list the tags.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[^:]+)?:voiceid.+:[0-9]{12}:domain/[a-zA-Z0-9]{22}`
Required: Yes

## Response Syntax
<a name="API_connect-voice-id_ListTagsForResource_ResponseSyntax"></a>

```
{
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_connect-voice-id_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Tags](#API_connect-voice-id_ListTagsForResource_ResponseSyntax) **   <a name="connect-connect-voice-id_ListTagsForResource-response-Tags"></a>
The list of tags associated with the specified resource.
Type: Array of [Tag](API_connect-voice-id_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_connect-voice-id_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action. Check the error message and try again.
HTTP Status Code: 400

 ** InternalServerException **
The request failed due to an unknown error on the server side.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found. Check the `ResourceType` and error message for more details.
 ** ResourceType **
The type of resource which cannot not be found. Possible types are `BATCH_JOB`, `COMPLIANCE_CONSENT`, `DOMAIN`, `FRAUDSTER`, `SESSION` and `SPEAKER`.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling. Please slow down your request rate. Refer to [ Connect Customer Voice ID Service API throttling quotas ](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas) and try your request again.
HTTP Status Code: 400

 ** ValidationException **
The request failed one or more validations; check the error message for more details.
HTTP Status Code: 400

## See Also
<a name="API_connect-voice-id_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/voice-id-2021-09-27/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/voice-id-2021-09-27/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/voice-id-2021-09-27/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/voice-id-2021-09-27/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/voice-id-2021-09-27/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/voice-id-2021-09-27/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/voice-id-2021-09-27/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/ListTagsForResource)
