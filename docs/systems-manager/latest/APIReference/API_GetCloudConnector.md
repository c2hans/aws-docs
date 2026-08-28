---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetCloudConnector.html
---

# GetCloudConnector
<a name="API_GetCloudConnector"></a>

Returns detailed information about a cloud connector.

## Request Syntax
<a name="API_GetCloudConnector_RequestSyntax"></a>

```
{
   "CloudConnectorId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCloudConnector_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CloudConnectorId](#API_GetCloudConnector_RequestSyntax) **   <a name="systemsmanager-GetCloudConnector-request-CloudConnectorId"></a>
The ID of the cloud connector to retrieve information about.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## Response Syntax
<a name="API_GetCloudConnector_ResponseSyntax"></a>

```
{
   "CloudConnectorArn": "string",
   "ConfigConnectorArn": "string",
   "Configuration": { ... },
   "CreatedAt": number,
   "Description": "string",
   "DisplayName": "string",
   "RoleArn": "string",
   "UpdatedAt": number
}
```

## Response Elements
<a name="API_GetCloudConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CloudConnectorArn](#API_GetCloudConnector_ResponseSyntax) **   <a name="systemsmanager-GetCloudConnector-response-CloudConnectorArn"></a>
The ARN of the cloud connector.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws(-cn|-us-gov)?:ssm:([^:]+):\d{12}:cloud-connector/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [ConfigConnectorArn](#API_GetCloudConnector_ResponseSyntax) **   <a name="systemsmanager-GetCloudConnector-response-ConfigConnectorArn"></a>
The ARN of the AWS Config connector associated with this cloud connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:aws(-cn|-us-gov)?:config:([^:]+):\d{12}:connector/.+$`

 ** [Configuration](#API_GetCloudConnector_ResponseSyntax) **   <a name="systemsmanager-GetCloudConnector-response-Configuration"></a>
The configuration details for the third-party cloud environment connection.
Type: [CloudConnectorConfiguration](API_CloudConnectorConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [CreatedAt](#API_GetCloudConnector_ResponseSyntax) **   <a name="systemsmanager-GetCloudConnector-response-CreatedAt"></a>
The date and time the cloud connector was created.
Type: Timestamp

 ** [Description](#API_GetCloudConnector_ResponseSyntax) **   <a name="systemsmanager-GetCloudConnector-response-Description"></a>
The description of the cloud connector.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}\p{P}\p{M}]*)$`

 ** [DisplayName](#API_GetCloudConnector_ResponseSyntax) **   <a name="systemsmanager-GetCloudConnector-response-DisplayName"></a>
The friendly name of the cloud connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}\p{P}\p{M}]*)$`

 ** [RoleArn](#API_GetCloudConnector_ResponseSyntax) **   <a name="systemsmanager-GetCloudConnector-response-RoleArn"></a>
The ARN of the IAM role used by the cloud connector.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z0-9-]*:iam::\d{12}:role\/[\w-\/.@+=,]{1,1017}$`

 ** [UpdatedAt](#API_GetCloudConnector_ResponseSyntax) **   <a name="systemsmanager-GetCloudConnector-response-UpdatedAt"></a>
The date and time the cloud connector was last updated.
Type: Timestamp

## Errors
<a name="API_GetCloudConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified parameter to be shared could not be found.
HTTP Status Code: 400

## Examples
<a name="API_GetCloudConnector_Examples"></a>

### Example
<a name="API_GetCloudConnector_Example_1"></a>

This example illustrates one usage of GetCloudConnector.

#### Sample Request
<a name="API_GetCloudConnector_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.GetCloudConnector
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240220T232503Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240220/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 62

{
    "CloudConnectorId": "8077bdca-72e6-4cda-8fd9-09bae51454f6"
}
```

#### Sample Response
<a name="API_GetCloudConnector_Example_1_Response"></a>

```
{
    "CloudConnectorArn": "arn:aws:ssm:us-east-2:123456789012:cloud-connector/8077bdca-72e6-4cda-8fd9-09bae51454f6",
    "DisplayName": "MyAzureConnector",
    "Description": "Azure connector for production workloads",
    "RoleArn": "arn:aws:iam::123456789012:role/SSMAzureConnectorRole",
    "ConfigConnectorArn": "arn:aws:config:us-east-2:123456789012:connector/azure/263dd747-5cc8-4e18-abf2-a25d8e374f66/061a61b6-5954-4b72-b6a2-458c62d046d9",
    "Configuration": {
        "AzureConfiguration": {
            "TenantId": "263dd747-5cc8-4e18-abf2-a25d8e374f66",
            "TenantDisplayName": "MyAzureTenant",
            "ApplicationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "ApplicationDisplayName": "SSMAdminApp",
            "Targets": {
                "Subscriptions": [
                    {
                        "Id": "14724fea-7bad-4c32-8af0-ebde38f42a46",
                        "DisplayName": "ProductionSubscription"
                    }
                ]
            }
        }
    },
    "CreatedAt": "2024-02-20T23:25:03.000Z",
    "UpdatedAt": "2024-02-20T23:25:03.000Z"
}
```

## See Also
<a name="API_GetCloudConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetCloudConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetCloudConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetCloudConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetCloudConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetCloudConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetCloudConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetCloudConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetCloudConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetCloudConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetCloudConnector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
