---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DeleteTieringConfiguration.html
---

# DeleteTieringConfiguration
<a name="API_DeleteTieringConfiguration"></a>

Deletes the tiering configuration specified by a tiering configuration name.

## Request Syntax
<a name="API_DeleteTieringConfiguration_RequestSyntax"></a>

```
DELETE /tiering-configurations/{{tieringConfigurationName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteTieringConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tieringConfigurationName](#API_DeleteTieringConfiguration_RequestSyntax) **   <a name="Backup-DeleteTieringConfiguration-request-uri-TieringConfigurationName"></a>
The unique name of a tiering configuration.
Pattern: `^[a-zA-Z0-9_]{1,200}$`
Required: Yes

## Request Body
<a name="API_DeleteTieringConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteTieringConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteTieringConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteTieringConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** MissingParameterValueException **
Indicates that a required parameter is missing.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource that is required for the action doesn't exist.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_DeleteTieringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/DeleteTieringConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/DeleteTieringConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/DeleteTieringConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/DeleteTieringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/DeleteTieringConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/DeleteTieringConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/DeleteTieringConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/DeleteTieringConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/DeleteTieringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/DeleteTieringConfiguration)
