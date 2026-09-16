---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_UpdateApplicationComponentConfig.html
---

# UpdateApplicationComponentConfig
<a name="API_UpdateApplicationComponentConfig"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

 Updates the configuration of an application component.

## Request Syntax
<a name="API_UpdateApplicationComponentConfig_RequestSyntax"></a>

```
POST /update-applicationcomponent-config/ HTTP/1.1
Content-type: application/json

{
   "applicationComponentId": "{{string}}",
   "appType": "{{string}}",
   "configureOnly": {{boolean}},
   "inclusionStatus": "{{string}}",
   "secretsManagerKey": "{{string}}",
   "sourceCodeList": [
      {
         "location": "{{string}}",
         "projectName": "{{string}}",
         "sourceVersion": "{{string}}",
         "versionControl": "{{string}}"
      }
   ],
   "strategyOption": {
      "isPreferred": {{boolean}},
      "strategy": "{{string}}",
      "targetDestination": "{{string}}",
      "toolName": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateApplicationComponentConfig_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateApplicationComponentConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applicationComponentId](#API_UpdateApplicationComponentConfig_RequestSyntax) **   <a name="migrationhubstrategy-UpdateApplicationComponentConfig-request-applicationComponentId"></a>
 The ID of the application component. The ID is unique within an AWS account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 44.
Pattern: `.*[0-9a-zA-Z-]+.*`
Required: Yes

 ** [appType](#API_UpdateApplicationComponentConfig_RequestSyntax) **   <a name="migrationhubstrategy-UpdateApplicationComponentConfig-request-appType"></a>
The type of known component.
Type: String
Valid Values: `DotNetFramework | Java | SQLServer | IIS | Oracle | Other | Tomcat | JBoss | Spring | Mongo DB | DB2 | Maria DB | MySQL | Sybase | PostgreSQLServer | Cassandra | IBM WebSphere | Oracle WebLogic | Visual Basic | Unknown | DotnetCore | Dotnet`
Required: No

 ** [configureOnly](#API_UpdateApplicationComponentConfig_RequestSyntax) **   <a name="migrationhubstrategy-UpdateApplicationComponentConfig-request-configureOnly"></a>
Update the configuration request of an application component. If it is set to true, the source code and/or database credentials are updated. If it is set to false, the source code and/or database credentials are updated and an analysis is initiated.
Type: Boolean
Required: No

 ** [inclusionStatus](#API_UpdateApplicationComponentConfig_RequestSyntax) **   <a name="migrationhubstrategy-UpdateApplicationComponentConfig-request-inclusionStatus"></a>
 Indicates whether the application component has been included for server recommendation or not.
Type: String
Valid Values: `excludeFromAssessment | includeInAssessment`
Required: No

 ** [secretsManagerKey](#API_UpdateApplicationComponentConfig_RequestSyntax) **   <a name="migrationhubstrategy-UpdateApplicationComponentConfig-request-secretsManagerKey"></a>
 Database credentials.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*`
Required: No

 ** [sourceCodeList](#API_UpdateApplicationComponentConfig_RequestSyntax) **   <a name="migrationhubstrategy-UpdateApplicationComponentConfig-request-sourceCodeList"></a>
 The list of source code configurations to update for the application component.
Type: Array of [SourceCode](API_SourceCode.md) objects
Required: No

 ** [strategyOption](#API_UpdateApplicationComponentConfig_RequestSyntax) **   <a name="migrationhubstrategy-UpdateApplicationComponentConfig-request-strategyOption"></a>
 The preferred strategy options for the application component. Use values from the [GetApplicationComponentStrategies](API_GetApplicationComponentStrategies.md) response.
Type: [StrategyOption](API_StrategyOption.md) object
Required: No

## Response Syntax
<a name="API_UpdateApplicationComponentConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateApplicationComponentConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateApplicationComponentConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
 The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The specified ID in the request is not found.
HTTP Status Code: 404

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
 The request body isn't valid.
HTTP Status Code: 400

## See Also
<a name="API_UpdateApplicationComponentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhubstrategy-2020-02-19/UpdateApplicationComponentConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhubstrategy-2020-02-19/UpdateApplicationComponentConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/UpdateApplicationComponentConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhubstrategy-2020-02-19/UpdateApplicationComponentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/UpdateApplicationComponentConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhubstrategy-2020-02-19/UpdateApplicationComponentConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhubstrategy-2020-02-19/UpdateApplicationComponentConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhubstrategy-2020-02-19/UpdateApplicationComponentConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/migrationhubstrategy-2020-02-19/UpdateApplicationComponentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/UpdateApplicationComponentConfig)
