---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ValidateCloudConnector.html
---

# ValidateCloudConnector
<a name="API_ValidateCloudConnector"></a>

Validates the configuration and connectivity of a cloud connector.

## Request Syntax
<a name="API_ValidateCloudConnector_RequestSyntax"></a>

```
{
   "CloudConnectorId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ValidateCloudConnector_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CloudConnectorId](#API_ValidateCloudConnector_RequestSyntax) **   <a name="systemsmanager-ValidateCloudConnector-request-CloudConnectorId"></a>
The ID of the cloud connector to validate.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** [MaxResults](#API_ValidateCloudConnector_RequestSyntax) **   <a name="systemsmanager-ValidateCloudConnector-request-MaxResults"></a>
The maximum number of validation findings to return.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 75.
Required: No

 ** [NextToken](#API_ValidateCloudConnector_RequestSyntax) **   <a name="systemsmanager-ValidateCloudConnector-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_ValidateCloudConnector_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ValidationFindings": [
      {
         "Code": "string",
         "Message": "string",
         "ProviderMessage": "string",
         "Scope": {
            "Id": "string",
            "Type": "string"
         },
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ValidateCloudConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ValidateCloudConnector_ResponseSyntax) **   <a name="systemsmanager-ValidateCloudConnector-response-NextToken"></a>
The token to use when requesting the next set of items.
Type: String

 ** [ValidationFindings](#API_ValidateCloudConnector_ResponseSyntax) **   <a name="systemsmanager-ValidateCloudConnector-response-ValidationFindings"></a>
A list of validation findings for the cloud connector.
Type: Array of [ValidationFinding](API_ValidationFinding.md) objects

## Errors
<a name="API_ValidateCloudConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified parameter to be shared could not be found.
HTTP Status Code: 400

## Examples
<a name="API_ValidateCloudConnector_Examples"></a>

### Example
<a name="API_ValidateCloudConnector_Example_1"></a>

This example illustrates one usage of ValidateCloudConnector.

#### Sample Request
<a name="API_ValidateCloudConnector_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ValidateCloudConnector
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
<a name="API_ValidateCloudConnector_Example_1_Response"></a>

```
{
    "ValidationFindings": [
        {
            "Type": "ERROR",
            "Code": "TargetInaccessible",
            "Message": "Target not found or not accessible with the provided credentials",
            "Scope": {
                "Type": "azure:subscription",
                "Id": "14724fea-7bad-4c32-8af0-ebde38f42a46"
            }
        }
    ]
}
```

## See Also
<a name="API_ValidateCloudConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ValidateCloudConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ValidateCloudConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ValidateCloudConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ValidateCloudConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ValidateCloudConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ValidateCloudConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ValidateCloudConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ValidateCloudConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ValidateCloudConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ValidateCloudConnector)
