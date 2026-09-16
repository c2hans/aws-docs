---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ListEnvironmentAccountConnections.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ListEnvironmentAccountConnections
<a name="API_ListEnvironmentAccountConnections"></a>

View a list of environment account connections.

For more information, see [Environment account connections](https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html) in the * AWS Proton User guide*.

## Request Syntax
<a name="API_ListEnvironmentAccountConnections_RequestSyntax"></a>

```
{
   "environmentName": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "requestedBy": "{{string}}",
   "statuses": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListEnvironmentAccountConnections_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [environmentName](#API_ListEnvironmentAccountConnections_RequestSyntax) **   <a name="proton-ListEnvironmentAccountConnections-request-environmentName"></a>
The environment name that's associated with each listed environment account connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** [maxResults](#API_ListEnvironmentAccountConnections_RequestSyntax) **   <a name="proton-ListEnvironmentAccountConnections-request-maxResults"></a>
The maximum number of environment account connections to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListEnvironmentAccountConnections_RequestSyntax) **   <a name="proton-ListEnvironmentAccountConnections-request-nextToken"></a>
A token that indicates the location of the next environment account connection in the array of environment account connections, after the list of environment account connections that was previously requested.
Type: String
Pattern: `[A-Za-z0-9+=/]+`
Required: No

 ** [requestedBy](#API_ListEnvironmentAccountConnections_RequestSyntax) **   <a name="proton-ListEnvironmentAccountConnections-request-requestedBy"></a>
The type of account making the `ListEnvironmentAccountConnections` request.
Type: String
Valid Values: `MANAGEMENT_ACCOUNT | ENVIRONMENT_ACCOUNT`
Required: Yes

 ** [statuses](#API_ListEnvironmentAccountConnections_RequestSyntax) **   <a name="proton-ListEnvironmentAccountConnections-request-statuses"></a>
The status details for each listed environment account connection.
Type: Array of strings
Valid Values: `PENDING | CONNECTED | REJECTED`
Required: No

## Response Syntax
<a name="API_ListEnvironmentAccountConnections_ResponseSyntax"></a>

```
{
   "environmentAccountConnections": [
      {
         "arn": "string",
         "componentRoleArn": "string",
         "environmentAccountId": "string",
         "environmentName": "string",
         "id": "string",
         "lastModifiedAt": number,
         "managementAccountId": "string",
         "requestedAt": number,
         "roleArn": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEnvironmentAccountConnections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentAccountConnections](#API_ListEnvironmentAccountConnections_ResponseSyntax) **   <a name="proton-ListEnvironmentAccountConnections-response-environmentAccountConnections"></a>
An array of environment account connections with details that's returned by AWS Proton.
Type: Array of [EnvironmentAccountConnectionSummary](API_EnvironmentAccountConnectionSummary.md) objects

 ** [nextToken](#API_ListEnvironmentAccountConnections_ResponseSyntax) **   <a name="proton-ListEnvironmentAccountConnections-response-nextToken"></a>
A token that indicates the location of the next environment account connection in the array of environment account connections, after the current requested list of environment account connections.
Type: String
Pattern: `[A-Za-z0-9+=/]+`

## Errors
<a name="API_ListEnvironmentAccountConnections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
HTTP Status Code: 400

 ** InternalServerException **
The request failed to register with the service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_ListEnvironmentAccountConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/ListEnvironmentAccountConnections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/ListEnvironmentAccountConnections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ListEnvironmentAccountConnections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/ListEnvironmentAccountConnections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ListEnvironmentAccountConnections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/ListEnvironmentAccountConnections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/ListEnvironmentAccountConnections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/ListEnvironmentAccountConnections)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/ListEnvironmentAccountConnections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ListEnvironmentAccountConnections)
