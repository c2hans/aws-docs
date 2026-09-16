---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateCloudConnector.html
---

# UpdateCloudConnector
<a name="API_UpdateCloudConnector"></a>

Updates an existing cloud connector with new configuration details.

## Request Syntax
<a name="API_UpdateCloudConnector_RequestSyntax"></a>

```
{
   "CloudConnectorId": "{{string}}",
   "Configuration": { ... },
   "Description": "{{string}}",
   "DisplayName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateCloudConnector_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CloudConnectorId](#API_UpdateCloudConnector_RequestSyntax) **   <a name="systemsmanager-UpdateCloudConnector-request-CloudConnectorId"></a>
The ID of the cloud connector to update.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** [Configuration](#API_UpdateCloudConnector_RequestSyntax) **   <a name="systemsmanager-UpdateCloudConnector-request-Configuration"></a>
The updated configuration details for connecting to the third-party cloud environment.
Type: [CloudConnectorConfiguration](API_CloudConnectorConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [Description](#API_UpdateCloudConnector_RequestSyntax) **   <a name="systemsmanager-UpdateCloudConnector-request-Description"></a>
A new description for the cloud connector.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}\p{P}\p{M}]*)$`
Required: No

 ** [DisplayName](#API_UpdateCloudConnector_RequestSyntax) **   <a name="systemsmanager-UpdateCloudConnector-request-DisplayName"></a>
A new friendly name for the cloud connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}\p{P}\p{M}]*)$`
Required: No

## Response Syntax
<a name="API_UpdateCloudConnector_ResponseSyntax"></a>

```
{
   "CloudConnectorId": "string"
}
```

## Response Elements
<a name="API_UpdateCloudConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CloudConnectorId](#API_UpdateCloudConnector_ResponseSyntax) **   <a name="systemsmanager-UpdateCloudConnector-response-CloudConnectorId"></a>
The ID of the cloud connector that was updated.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

## Errors
<a name="API_UpdateCloudConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
An error occurred because of a conflict with a concurrent request or the current state of the resource. Retry your request.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified parameter to be shared could not be found.
HTTP Status Code: 400

## Examples
<a name="API_UpdateCloudConnector_Examples"></a>

### Example
<a name="API_UpdateCloudConnector_Example_1"></a>

This example illustrates one usage of UpdateCloudConnector.

#### Sample Request
<a name="API_UpdateCloudConnector_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.UpdateCloudConnector
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240220T232503Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240220/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 430

{
    "CloudConnectorId": "8077bdca-72e6-4cda-8fd9-09bae51454f6",
    "DisplayName": "MyAzureConnector-Updated",
    "Description": "Updated Azure connector",
    "Configuration": {
        "AzureConfiguration": {
            "TenantId": "263dd747-5cc8-4e18-abf2-a25d8e374f66",
            "ApplicationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "Targets": {
                "Subscriptions": [
                    {
                        "Id": "14724fea-7bad-4c32-8af0-ebde38f42a46",
                        "DisplayName": "ProductionSubscription"
                    },
                    {
                        "Id": "25835gfb-8cae-5d43-9bg1-fcef49g53b57",
                        "DisplayName": "StagingSubscription"
                    }
                ]
            }
        }
    }
}
```

#### Sample Response
<a name="API_UpdateCloudConnector_Example_1_Response"></a>

```
{
    "CloudConnectorId": "8077bdca-72e6-4cda-8fd9-09bae51454f6"
}
```

## See Also
<a name="API_UpdateCloudConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/UpdateCloudConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/UpdateCloudConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/UpdateCloudConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/UpdateCloudConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/UpdateCloudConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/UpdateCloudConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/UpdateCloudConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/UpdateCloudConnector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/UpdateCloudConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/UpdateCloudConnector)
