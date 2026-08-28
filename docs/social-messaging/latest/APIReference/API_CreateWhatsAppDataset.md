---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_CreateWhatsAppDataset.html
---

# CreateWhatsAppDataset
<a name="API_CreateWhatsAppDataset"></a>

Creates a Meta Conversions API dataset for a WhatsApp Business Account.

## Request Syntax
<a name="API_CreateWhatsAppDataset_RequestSyntax"></a>

```
POST /v1/whatsapp/waba/dataset HTTP/1.1
Content-type: application/json

{
   "id": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateWhatsAppDataset_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWhatsAppDataset_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [id](#API_CreateWhatsAppDataset_RequestSyntax) **   <a name="Social-CreateWhatsAppDataset-request-id"></a>
The ID of the WhatsApp Business Account to create a dataset for, formatted as `waba-01234567890123456789012345678901`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

## Response Syntax
<a name="API_CreateWhatsAppDataset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datasetId": "string"
}
```

## Response Elements
<a name="API_CreateWhatsAppDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datasetId](#API_CreateWhatsAppDataset_ResponseSyntax) **   <a name="Social-CreateWhatsAppDataset-response-datasetId"></a>
The Meta-generated dataset ID, a numeric string of 10 to 20 digits.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 20.
Pattern: `[0-9]+`

## Errors
<a name="API_CreateWhatsAppDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedByMetaException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** DependencyException **
Thrown when performing an action because a dependency would be broken.
HTTP Status Code: 502

 ** InternalServiceException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** InvalidParametersException **
One or more parameters provided to the action are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource was not found.
HTTP Status Code: 404

 ** ThrottledRequestException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request contains an invalid parameter value.
HTTP Status Code: 400

## See Also
<a name="API_CreateWhatsAppDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/CreateWhatsAppDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/CreateWhatsAppDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/CreateWhatsAppDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/CreateWhatsAppDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/CreateWhatsAppDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/CreateWhatsAppDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/CreateWhatsAppDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/CreateWhatsAppDataset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/CreateWhatsAppDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/CreateWhatsAppDataset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
