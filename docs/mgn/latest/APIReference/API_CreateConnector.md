---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_CreateConnector.html
---

# CreateConnector
<a name="API_CreateConnector"></a>

Create Connector.

## Request Syntax
<a name="API_CreateConnector_RequestSyntax"></a>

```
POST /CreateConnector HTTP/1.1
Content-type: application/json

{
   "name": "{{string}}",
   "ssmCommandConfig": {
      "cloudWatchLogGroupName": "{{string}}",
      "cloudWatchOutputEnabled": {{boolean}},
      "outputS3BucketName": "{{string}}",
      "s3OutputEnabled": {{boolean}}
   },
   "ssmInstanceID": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateConnector_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_CreateConnector_RequestSyntax) **   <a name="mgn-CreateConnector-request-name"></a>
Create Connector request name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** [ssmCommandConfig](#API_CreateConnector_RequestSyntax) **   <a name="mgn-CreateConnector-request-ssmCommandConfig"></a>
Create Connector request SSM command config.
Type: [ConnectorSsmCommandConfig](API_ConnectorSsmCommandConfig.md) object
Required: No

 ** [ssmInstanceID](#API_CreateConnector_RequestSyntax) **   <a name="mgn-CreateConnector-request-ssmInstanceID"></a>
Create Connector request SSM instance ID.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 20.
Pattern: `.*(^i-[0-9a-zA-Z]{17}$)|(^mi-[0-9a-zA-Z]{17}$).*`
Required: Yes

 ** [tags](#API_CreateConnector_RequestSyntax) **   <a name="mgn-CreateConnector-request-tags"></a>
Create Connector request tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateConnector_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "connectorID": "string",
   "name": "string",
   "ssmCommandConfig": {
      "cloudWatchLogGroupName": "string",
      "cloudWatchOutputEnabled": boolean,
      "outputS3BucketName": "string",
      "s3OutputEnabled": boolean
   },
   "ssmInstanceID": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_CreateConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateConnector_ResponseSyntax) **   <a name="mgn-CreateConnector-response-arn"></a>
Connector arn.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [connectorID](#API_CreateConnector_ResponseSyntax) **   <a name="mgn-CreateConnector-response-connectorID"></a>
Connector ID.
Type: String
Length Constraints: Fixed length of 27.
Pattern: `connector-[0-9a-zA-Z]{17}`

 ** [name](#API_CreateConnector_ResponseSyntax) **   <a name="mgn-CreateConnector-response-name"></a>
Connector name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_-]+`

 ** [ssmCommandConfig](#API_CreateConnector_ResponseSyntax) **   <a name="mgn-CreateConnector-response-ssmCommandConfig"></a>
Connector SSM command config.
Type: [ConnectorSsmCommandConfig](API_ConnectorSsmCommandConfig.md) object

 ** [ssmInstanceID](#API_CreateConnector_ResponseSyntax) **   <a name="mgn-CreateConnector-response-ssmInstanceID"></a>
Connector SSM instance ID.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 20.
Pattern: `.*(^i-[0-9a-zA-Z]{17}$)|(^mi-[0-9a-zA-Z]{17}$).*`

 ** [tags](#API_CreateConnector_ResponseSyntax) **   <a name="mgn-CreateConnector-response-tags"></a>
Connector tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_CreateConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_CreateConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/CreateConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/CreateConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/CreateConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/CreateConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/CreateConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/CreateConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/CreateConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/CreateConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/CreateConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/CreateConnector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
