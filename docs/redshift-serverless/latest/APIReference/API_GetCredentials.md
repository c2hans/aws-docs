---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetCredentials.html
---

# GetCredentials
<a name="API_GetCredentials"></a>

Returns a database user name and temporary password with temporary authorization to log in to Amazon Redshift Serverless.

By default, the temporary credentials expire in 900 seconds. You can optionally specify a duration between 900 seconds (15 minutes) and 3600 seconds (60 minutes).

The AWS Identity and Access Management (IAM) user or role that runs GetCredentials must have an IAM policy attached that allows access to all necessary actions and resources.

If the `DbName` parameter is specified, the IAM policy must allow access to the resource dbname for the specified database name.

## Request Syntax
<a name="API_GetCredentials_RequestSyntax"></a>

```
{
   "customDomainName": "{{string}}",
   "dbName": "{{string}}",
   "durationSeconds": {{number}},
   "workgroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCredentials_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [customDomainName](#API_GetCredentials_RequestSyntax) **   <a name="redshiftserverless-GetCredentials-request-customDomainName"></a>
The custom domain name associated with the workgroup. The custom domain name or the workgroup name must be included in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`
Required: No

 ** [dbName](#API_GetCredentials_RequestSyntax) **   <a name="redshiftserverless-GetCredentials-request-dbName"></a>
The name of the database to get temporary authorization to log on to.
Constraints:
+ Must be 1 to 64 alphanumeric characters or hyphens.
+ Must contain only uppercase or lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.
+ The first character must be a letter.
+ Must not contain a colon ( : ) or slash ( / ).
+ Cannot be a reserved word. A list of reserved words can be found in [Reserved Words ](https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide
Type: String
Required: No

 ** [durationSeconds](#API_GetCredentials_RequestSyntax) **   <a name="redshiftserverless-GetCredentials-request-durationSeconds"></a>
The number of seconds until the returned temporary password expires. The minimum is 900 seconds, and the maximum is 3600 seconds.
Type: Integer
Required: No

 ** [workgroupName](#API_GetCredentials_RequestSyntax) **   <a name="redshiftserverless-GetCredentials-request-workgroupName"></a>
The name of the workgroup associated with the database.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: No

## Response Syntax
<a name="API_GetCredentials_ResponseSyntax"></a>

```
{
   "dbPassword": "string",
   "dbUser": "string",
   "expiration": number,
   "nextRefreshTime": number
}
```

## Response Elements
<a name="API_GetCredentials_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dbPassword](#API_GetCredentials_ResponseSyntax) **   <a name="redshiftserverless-GetCredentials-response-dbPassword"></a>
A temporary password that authorizes the user name returned by `DbUser` to log on to the database `DbName`.
Type: String

 ** [dbUser](#API_GetCredentials_ResponseSyntax) **   <a name="redshiftserverless-GetCredentials-response-dbUser"></a>
A database user name that is authorized to log on to the database `DbName` using the password `DbPassword`. If the specified `DbUser` exists in the database, the new user name has the same database privileges as the the user named in `DbUser`. By default, the user is added to PUBLIC.
Type: String

 ** [expiration](#API_GetCredentials_ResponseSyntax) **   <a name="redshiftserverless-GetCredentials-response-expiration"></a>
The date and time the password in `DbPassword` expires.
Type: Timestamp

 ** [nextRefreshTime](#API_GetCredentials_ResponseSyntax) **   <a name="redshiftserverless-GetCredentials-response-nextRefreshTime"></a>
The date and time of when the `DbUser` and `DbPassword` authorization refreshes.
Type: Timestamp

## Errors
<a name="API_GetCredentials_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/GetCredentials)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/GetCredentials)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/GetCredentials)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/GetCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/GetCredentials)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/GetCredentials)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/GetCredentials)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/GetCredentials)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/GetCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/GetCredentials)
