---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAccessControlApplicationSecret.html
---

# UpdateAccessControlApplicationSecret

Updates the AWS Secrets Manager secret ARNs of an IdP-provided client secret. You can add, replace, or remove the ARN for a Region, but you can't remove the last remaining Region. To remove it, delete the client secret.

## Request Syntax
<a name="API_UpdateAccessControlApplicationSecret_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/access-control-applications/{{ApplicationId}}/client-secrets/{{ClientSecretId}} HTTP/1.1
Content-type: application/json

{
   "RemoveRegionalSecretManagerArns": [ "{{string}}" ],
   "UpdateRegionalSecretManagerArns": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateAccessControlApplicationSecret_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationId](#API_UpdateAccessControlApplicationSecret_RequestSyntax) **   <a name="QS-UpdateAccessControlApplicationSecret-request-uri-ApplicationId"></a>
The ID of the access control application.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** [AwsAccountId](#API_UpdateAccessControlApplicationSecret_RequestSyntax) **   <a name="QS-UpdateAccessControlApplicationSecret-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the Quick Sight account.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [ClientSecretId](#API_UpdateAccessControlApplicationSecret_RequestSyntax) **   <a name="QS-UpdateAccessControlApplicationSecret-request-uri-ClientSecretId"></a>
The ID of the client secret.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

## Request Body
<a name="API_UpdateAccessControlApplicationSecret_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RemoveRegionalSecretManagerArns](#API_UpdateAccessControlApplicationSecret_RequestSyntax) **   <a name="QS-UpdateAccessControlApplicationSecret-request-RemoveRegionalSecretManagerArns"></a>
The Regions whose ARNs to remove. You can't remove the last remaining Region. To remove it, delete the client secret instead.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 5. Maximum length of 30.
Pattern: `[a-z]{2}(-[a-z]+)+-[0-9]+`
Required: No

 ** [UpdateRegionalSecretManagerArns](#API_UpdateAccessControlApplicationSecret_RequestSyntax) **   <a name="QS-UpdateAccessControlApplicationSecret-request-UpdateRegionalSecretManagerArns"></a>
The Region ARNs to add or replace. The Region in each ARN must match its key.
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 5. Maximum length of 30.
Key Pattern: `[a-z]{2}(-[a-z]+)+-[0-9]+`
Value Length Constraints: Minimum length of 20. Maximum length of 2048.
Value Pattern: `arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:.+`
Required: No

## Response Syntax
<a name="API_UpdateAccessControlApplicationSecret_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "ClientSecretId": "string",
   "RegionalSecretManagerArns": {
      "string" : "string"
   },
   "RequestId": "string",
   "UpdatedAt": number
}
```

## Response Elements
<a name="API_UpdateAccessControlApplicationSecret_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateAccessControlApplicationSecret_ResponseSyntax) **   <a name="QS-UpdateAccessControlApplicationSecret-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [ClientSecretId](#API_UpdateAccessControlApplicationSecret_ResponseSyntax) **   <a name="QS-UpdateAccessControlApplicationSecret-response-ClientSecretId"></a>
The ID of the client secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`

 ** [RegionalSecretManagerArns](#API_UpdateAccessControlApplicationSecret_ResponseSyntax) **   <a name="QS-UpdateAccessControlApplicationSecret-response-RegionalSecretManagerArns"></a>
The Region ARNs of the client secret after the update.
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 5. Maximum length of 30.
Key Pattern: `[a-z]{2}(-[a-z]+)+-[0-9]+`
Value Length Constraints: Minimum length of 20. Maximum length of 2048.
Value Pattern: `arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:.+`

 ** [RequestId](#API_UpdateAccessControlApplicationSecret_ResponseSyntax) **   <a name="QS-UpdateAccessControlApplicationSecret-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [UpdatedAt](#API_UpdateAccessControlApplicationSecret_ResponseSyntax) **   <a name="QS-UpdateAccessControlApplicationSecret-response-UpdatedAt"></a>
The time when the client secret was updated.
Type: Timestamp

## Errors
<a name="API_UpdateAccessControlApplicationSecret_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateAccessControlApplicationSecret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateAccessControlApplicationSecret)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateAccessControlApplicationSecret)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateAccessControlApplicationSecret)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateAccessControlApplicationSecret)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateAccessControlApplicationSecret)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateAccessControlApplicationSecret)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateAccessControlApplicationSecret)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateAccessControlApplicationSecret)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateAccessControlApplicationSecret)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateAccessControlApplicationSecret)
