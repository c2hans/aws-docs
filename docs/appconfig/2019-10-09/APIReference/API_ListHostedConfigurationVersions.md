---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListHostedConfigurationVersions.html
---

# ListHostedConfigurationVersions
<a name="API_ListHostedConfigurationVersions"></a>

Lists configurations stored in the AWS AppConfig hosted configuration store by version.

## Request Syntax
<a name="API_ListHostedConfigurationVersions_RequestSyntax"></a>

```
GET /applications/{{ApplicationId}}/configurationprofiles/{{ConfigurationProfileId}}/hostedconfigurationversions?max_results={{MaxResults}}&next_token={{NextToken}}&version_label={{VersionLabel}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListHostedConfigurationVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationId](#API_ListHostedConfigurationVersions_RequestSyntax) **   <a name="appconfig-ListHostedConfigurationVersions-request-uri-ApplicationId"></a>
The ID or name of the application.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [ConfigurationProfileId](#API_ListHostedConfigurationVersions_RequestSyntax) **   <a name="appconfig-ListHostedConfigurationVersions-request-uri-ConfigurationProfileId"></a>
The ID or name of the configuration profile.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [MaxResults](#API_ListHostedConfigurationVersions_RequestSyntax) **   <a name="appconfig-ListHostedConfigurationVersions-request-uri-MaxResults"></a>
The maximum number of items to return for this call. If `MaxResults` is not provided in the call, AWS AppConfig returns the maximum of 50. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListHostedConfigurationVersions_RequestSyntax) **   <a name="appconfig-ListHostedConfigurationVersions-request-uri-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [VersionLabel](#API_ListHostedConfigurationVersions_RequestSyntax) **   <a name="appconfig-ListHostedConfigurationVersions-request-uri-VersionLabel"></a>
An optional filter that can be used to specify the version label of an AWS AppConfig hosted configuration version. This parameter supports filtering by prefix using a wildcard, for example "v2\*". If you don't specify an asterisk at the end of the value, only an exact match is returned.
Length Constraints: Minimum length of 1. Maximum length of 64.

## Request Body
<a name="API_ListHostedConfigurationVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListHostedConfigurationVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "ApplicationId": "string",
         "ConfigurationProfileId": "string",
         "ContentType": "string",
         "Description": "string",
         "KmsKeyArn": "string",
         "VersionLabel": "string",
         "VersionNumber": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListHostedConfigurationVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListHostedConfigurationVersions_ResponseSyntax) **   <a name="appconfig-ListHostedConfigurationVersions-response-Items"></a>
The elements from this collection.
Type: Array of [HostedConfigurationVersionSummary](API_HostedConfigurationVersionSummary.md) objects

 ** [NextToken](#API_ListHostedConfigurationVersions_ResponseSyntax) **   <a name="appconfig-ListHostedConfigurationVersions-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListHostedConfigurationVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
HTTP Status Code: 404

## Examples
<a name="API_ListHostedConfigurationVersions_Examples"></a>

### Example
<a name="API_ListHostedConfigurationVersions_Example_1"></a>

This example illustrates one usage of ListHostedConfigurationVersions.

#### Sample Request
<a name="API_ListHostedConfigurationVersions_Example_1_Request"></a>

```
GET /applications/abc1234/configurationprofiles/ur8hx2f/hostedconfigurationversions HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.134-73.228.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/appconfig.list-hosted-configuration-versions
X-Amz-Date: 20210920T183555Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210920/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
```

#### Sample Response
<a name="API_ListHostedConfigurationVersions_Example_1_Response"></a>

```
{
    "Items": [
        {
            "ApplicationId": "abc1234",
            "ConfigurationProfileId": "ur8hx2f",
            "VersionNumber": 1,
            "ContentType": "application/json"
        }
    ]
}
```

## See Also
<a name="API_ListHostedConfigurationVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/ListHostedConfigurationVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/ListHostedConfigurationVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/ListHostedConfigurationVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/ListHostedConfigurationVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/ListHostedConfigurationVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/ListHostedConfigurationVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/ListHostedConfigurationVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/ListHostedConfigurationVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/ListHostedConfigurationVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/ListHostedConfigurationVersions)
