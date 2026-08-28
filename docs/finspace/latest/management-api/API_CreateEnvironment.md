---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateEnvironment.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# CreateEnvironment
<a name="API_CreateEnvironment"></a>

Create a new FinSpace environment.

## Request Syntax
<a name="API_CreateEnvironment_RequestSyntax"></a>

```
POST /environment HTTP/1.1
Content-type: application/json

{
   "dataBundles": [ "{{string}}" ],
   "description": "{{string}}",
   "federationMode": "{{string}}",
   "federationParameters": {
      "applicationCallBackURL": "{{string}}",
      "attributeMap": {
         "{{string}}" : "{{string}}"
      },
      "federationProviderName": "{{string}}",
      "federationURN": "{{string}}",
      "samlMetadataDocument": "{{string}}",
      "samlMetadataURL": "{{string}}"
   },
   "kmsKeyId": "{{string}}",
   "name": "{{string}}",
   "superuserParameters": {
      "emailAddress": "{{string}}",
      "firstName": "{{string}}",
      "lastName": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateEnvironment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_CreateEnvironment_RequestSyntax) **   <a name="finspace-CreateEnvironment-request-name"></a>
The name of the FinSpace environment to be created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]$`
Required: Yes

 ** [dataBundles](#API_CreateEnvironment_RequestSyntax) **   <a name="finspace-CreateEnvironment-request-dataBundles"></a>
The list of Amazon Resource Names (ARN) of the data bundles to install. Currently supported data bundle ARNs:
+  `arn:aws:finspace:${Region}::data-bundle/capital-markets-sample` - Contains sample Capital Markets datasets, categories and controlled vocabularies.
+  `arn:aws:finspace:${Region}::data-bundle/taq` (default) - Contains trades and quotes data in addition to sample Capital Markets data.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws:finspace:[A-Za-z0-9_/.-]{0,63}:\d*:data-bundle/[0-9A-Za-z_-]{1,128}$`
Required: No

 ** [description](#API_CreateEnvironment_RequestSyntax) **   <a name="finspace-CreateEnvironment-request-description"></a>
The description of the FinSpace environment to be created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`
Required: No

 ** [federationMode](#API_CreateEnvironment_RequestSyntax) **   <a name="finspace-CreateEnvironment-request-federationMode"></a>
Authentication mode for the environment.
+  `FEDERATED` - Users access FinSpace through Single Sign On (SSO) via your Identity provider.
+  `LOCAL` - Users access FinSpace via email and password managed within the FinSpace environment.
Type: String
Valid Values: `FEDERATED | LOCAL`
Required: No

 ** [federationParameters](#API_CreateEnvironment_RequestSyntax) **   <a name="finspace-CreateEnvironment-request-federationParameters"></a>
Configuration information when authentication mode is FEDERATED.
Type: [FederationParameters](API_FederationParameters.md) object
Required: No

 ** [kmsKeyId](#API_CreateEnvironment_RequestSyntax) **   <a name="finspace-CreateEnvironment-request-kmsKeyId"></a>
The KMS key id to encrypt your data in the FinSpace environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z-0-9-:\/]*$`
Required: No

 ** [superuserParameters](#API_CreateEnvironment_RequestSyntax) **   <a name="finspace-CreateEnvironment-request-superuserParameters"></a>
Configuration information for the superuser.
Type: [SuperuserParameters](API_SuperuserParameters.md) object
Required: No

 ** [tags](#API_CreateEnvironment_RequestSyntax) **   <a name="finspace-CreateEnvironment-request-tags"></a>
Add tags to your FinSpace environment.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `^[a-zA-Z0-9+-=._:@ ]+$`
Required: No

## Response Syntax
<a name="API_CreateEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "environmentArn": "string",
   "environmentId": "string",
   "environmentUrl": "string"
}
```

## Response Elements
<a name="API_CreateEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentArn](#API_CreateEnvironment_ResponseSyntax) **   <a name="finspace-CreateEnvironment-response-environmentArn"></a>
The Amazon Resource Name (ARN) of the FinSpace environment that you created.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws:finspace:[A-Za-z0-9_/.-]{0,63}:\d+:environment/[0-9A-Za-z_-]{1,128}$`

 ** [environmentId](#API_CreateEnvironment_ResponseSyntax) **   <a name="finspace-CreateEnvironment-response-environmentId"></a>
The unique identifier for FinSpace environment that you created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`

 ** [environmentUrl](#API_CreateEnvironment_ResponseSyntax) **   <a name="finspace-CreateEnvironment-response-environmentUrl"></a>
The sign-in URL for the web application of the FinSpace environment you created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^https?://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`

## Errors
<a name="API_CreateEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** LimitExceededException **
A service limit or quota is exceeded.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
 You have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/CreateEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/CreateEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/CreateEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/CreateEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/CreateEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/CreateEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/CreateEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/CreateEnvironment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/CreateEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/CreateEnvironment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
