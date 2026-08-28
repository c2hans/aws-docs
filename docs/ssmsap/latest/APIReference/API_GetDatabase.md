---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_GetDatabase.html
---

# GetDatabase
<a name="API_GetDatabase"></a>

Gets the SAP HANA database of an application registered with AWS Systems Manager for SAP.

## Request Syntax
<a name="API_GetDatabase_RequestSyntax"></a>

```
POST /get-database HTTP/1.1
Content-type: application/json

{
   "ApplicationId": "{{string}}",
   "ComponentId": "{{string}}",
   "DatabaseArn": "{{string}}",
   "DatabaseId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetDatabase_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetDatabase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationId](#API_GetDatabase_RequestSyntax) **   <a name="ssmsap-GetDatabase-request-ApplicationId"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w\d\.-]+`
Required: No

 ** [ComponentId](#API_GetDatabase_RequestSyntax) **   <a name="ssmsap-GetDatabase-request-ComponentId"></a>
The ID of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\d-]+`
Required: No

 ** [DatabaseArn](#API_GetDatabase_RequestSyntax) **   <a name="ssmsap-GetDatabase-request-DatabaseArn"></a>
The Amazon Resource Name (ARN) of the database.
Type: String
Pattern: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`
Required: No

 ** [DatabaseId](#API_GetDatabase_RequestSyntax) **   <a name="ssmsap-GetDatabase-request-DatabaseId"></a>
The ID of the database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `.*[\w\d]+`
Required: No

## Response Syntax
<a name="API_GetDatabase_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Database": {
      "ApplicationId": "string",
      "Arn": "string",
      "ComponentId": "string",
      "ConnectedComponentArns": [ "string" ],
      "Credentials": [
         {
            "CredentialType": "string",
            "DatabaseName": "string",
            "SecretId": "string"
         }
      ],
      "DatabaseId": "string",
      "DatabaseName": "string",
      "DatabaseType": "string",
      "LastUpdated": number,
      "PrimaryHost": "string",
      "SQLPort": number,
      "Status": "string"
   },
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetDatabase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Database](#API_GetDatabase_ResponseSyntax) **   <a name="ssmsap-GetDatabase-response-Database"></a>
The SAP HANA database of an application registered with AWS Systems Manager for SAP.
Type: [Database](API_Database.md) object

 ** [Tags](#API_GetDatabase_ResponseSyntax) **   <a name="ssmsap-GetDatabase-response-Tags"></a>
The tags of a database.
Type: String to string map
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_GetDatabase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-sap-2018-05-10/GetDatabase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-sap-2018-05-10/GetDatabase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/GetDatabase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-sap-2018-05-10/GetDatabase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/GetDatabase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-sap-2018-05-10/GetDatabase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-sap-2018-05-10/GetDatabase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-sap-2018-05-10/GetDatabase)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-sap-2018-05-10/GetDatabase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/GetDatabase)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
