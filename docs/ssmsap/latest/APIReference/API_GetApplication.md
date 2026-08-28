---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_GetApplication.html
---

# GetApplication
<a name="API_GetApplication"></a>

Gets an application registered with AWS Systems Manager for SAP. It also returns the components of the application.

## Request Syntax
<a name="API_GetApplication_RequestSyntax"></a>

```
POST /get-application HTTP/1.1
Content-type: application/json

{
   "ApplicationArn": "{{string}}",
   "ApplicationId": "{{string}}",
   "AppRegistryArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetApplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationArn](#API_GetApplication_RequestSyntax) **   <a name="ssmsap-GetApplication-request-ApplicationArn"></a>
The Amazon Resource Name (ARN) of the application.
Type: String
Pattern: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`
Required: No

 ** [ApplicationId](#API_GetApplication_RequestSyntax) **   <a name="ssmsap-GetApplication-request-ApplicationId"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w\d\.-]+`
Required: No

 ** [AppRegistryArn](#API_GetApplication_RequestSyntax) **   <a name="ssmsap-GetApplication-request-AppRegistryArn"></a>
The Amazon Resource Name (ARN) of the application registry.
Type: String
Pattern: `arn:aws:servicecatalog:[a-z0-9:\/-]+`
Required: No

## Response Syntax
<a name="API_GetApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Application": {
      "AppRegistryArn": "string",
      "Arn": "string",
      "AssociatedApplicationArns": [ "string" ],
      "Components": [ "string" ],
      "DiscoveryStatus": "string",
      "Id": "string",
      "LastUpdated": number,
      "Status": "string",
      "StatusMessage": "string",
      "Type": "string"
   },
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Application](#API_GetApplication_ResponseSyntax) **   <a name="ssmsap-GetApplication-response-Application"></a>
Returns all of the metadata of an application registered with AWS Systems Manager for SAP.
Type: [Application](API_Application.md) object

 ** [Tags](#API_GetApplication_ResponseSyntax) **   <a name="ssmsap-GetApplication-response-Tags"></a>
The tags of a registered application.
Type: String to string map
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_GetApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-sap-2018-05-10/GetApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-sap-2018-05-10/GetApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/GetApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-sap-2018-05-10/GetApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/GetApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-sap-2018-05-10/GetApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-sap-2018-05-10/GetApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-sap-2018-05-10/GetApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-sap-2018-05-10/GetApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/GetApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
