---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateCloudConnector.html
---

# CreateCloudConnector
<a name="API_CreateCloudConnector"></a>

Creates a cloud connector that establishes a connection between Systems Manager and a third-party cloud environment.

## Request Syntax
<a name="API_CreateCloudConnector_RequestSyntax"></a>

```
{
   "ConfigConnectorArn": "{{string}}",
   "Configuration": { ... },
   "Description": "{{string}}",
   "DisplayName": "{{string}}",
   "RoleArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateCloudConnector_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigConnectorArn](#API_CreateCloudConnector_RequestSyntax) **   <a name="systemsmanager-CreateCloudConnector-request-ConfigConnectorArn"></a>
The ARN of the AWS Config connector associated with this cloud connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:aws(-cn|-us-gov)?:config:([^:]+):\d{12}:connector/.+$`
Required: Yes

 ** [Configuration](#API_CreateCloudConnector_RequestSyntax) **   <a name="systemsmanager-CreateCloudConnector-request-Configuration"></a>
The configuration details for connecting to the third-party cloud environment.
Type: [CloudConnectorConfiguration](API_CloudConnectorConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Description](#API_CreateCloudConnector_RequestSyntax) **   <a name="systemsmanager-CreateCloudConnector-request-Description"></a>
A description for the cloud connector.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}\p{P}\p{M}]*)$`
Required: No

 ** [DisplayName](#API_CreateCloudConnector_RequestSyntax) **   <a name="systemsmanager-CreateCloudConnector-request-DisplayName"></a>
A friendly name for the cloud connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}\p{P}\p{M}]*)$`
Required: Yes

 ** [RoleArn](#API_CreateCloudConnector_RequestSyntax) **   <a name="systemsmanager-CreateCloudConnector-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that the cloud connector uses to communicate with the third-party cloud environment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z0-9-]*:iam::\d{12}:role\/[\w-\/.@+=,]{1,1017}$`
Required: Yes

 ** [Tags](#API_CreateCloudConnector_RequestSyntax) **   <a name="systemsmanager-CreateCloudConnector-request-Tags"></a>
Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 1000 items.
Required: No

## Response Syntax
<a name="API_CreateCloudConnector_ResponseSyntax"></a>

```
{
   "CloudConnectorId": "string"
}
```

## Response Elements
<a name="API_CreateCloudConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CloudConnectorId](#API_CreateCloudConnector_ResponseSyntax) **   <a name="systemsmanager-CreateCloudConnector-response-CloudConnectorId"></a>
The ID of the cloud connector that was created.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

## Errors
<a name="API_CreateCloudConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
An error occurred because of a conflict with a concurrent request or the current state of the resource. Retry your request.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request exceeds the service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
 ** QuotaCode **
The quota code recognized by the AWS Service Quotas service.
 ** ResourceId **
The unique ID of the resource referenced in the failed request.
 ** ResourceType **
The resource type of the resource referenced in the failed request.
 ** ServiceCode **
The code for the AWS service that owns the quota.
HTTP Status Code: 400

## Examples
<a name="API_CreateCloudConnector_Examples"></a>

### Example
<a name="API_CreateCloudConnector_Example_1"></a>

This example illustrates one usage of CreateCloudConnector.

#### Sample Request
<a name="API_CreateCloudConnector_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.CreateCloudConnector
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240220T232503Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240220/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 560

{
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
    }
}
```

#### Sample Response
<a name="API_CreateCloudConnector_Example_1_Response"></a>

```
{
    "CloudConnectorId": "8077bdca-72e6-4cda-8fd9-09bae51454f6"
}
```

## See Also
<a name="API_CreateCloudConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/CreateCloudConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/CreateCloudConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/CreateCloudConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/CreateCloudConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/CreateCloudConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/CreateCloudConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/CreateCloudConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/CreateCloudConnector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/CreateCloudConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/CreateCloudConnector)
