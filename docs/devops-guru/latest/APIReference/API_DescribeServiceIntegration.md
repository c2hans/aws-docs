---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeServiceIntegration.html
---

# DescribeServiceIntegration
<a name="API_DescribeServiceIntegration"></a>

 Returns the integration status of services that are integrated with DevOps Guru.

## Request Syntax
<a name="API_DescribeServiceIntegration_RequestSyntax"></a>

```
GET /service-integrations HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeServiceIntegration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeServiceIntegration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeServiceIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ServiceIntegration": {
      "KMSServerSideEncryption": {
         "KMSKeyId": "string",
         "OptInStatus": "string",
         "Type": "string"
      },
      "LogsAnomalyDetection": {
         "OptInStatus": "string"
      },
      "OpsCenter": {
         "OptInStatus": "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeServiceIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ServiceIntegration](#API_DescribeServiceIntegration_ResponseSyntax) **   <a name="DevOpsGuru-DescribeServiceIntegration-response-ServiceIntegration"></a>
 Information about the integration of DevOps Guru with another AWS service, such as AWS Systems Manager.
Type: [ServiceIntegrationConfig](API_ServiceIntegrationConfig.md) object

## Errors
<a name="API_DescribeServiceIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.
HTTP Status Code: 403

 ** InternalServerException **
An internal failure in an Amazon service occurred.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the internal server exception can be retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A requested resource could not be found
 ** ResourceId **
 The ID of the AWS resource that could not be found.
 ** ResourceType **
 The type of the AWS resource that could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to a request throttling.
 ** QuotaCode **
 The code of the quota that was exceeded, causing the throttling exception.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the throttling exception can be retried.
 ** ServiceCode **
 The code of the service that caused the throttling exception.
HTTP Status Code: 429

 ** ValidationException **
 Contains information about data passed in to a field during a request that is not valid.
 ** Fields **
 An array of fields that are associated with the validation exception.
 ** Message **
 A message that describes the validation exception.
 ** Reason **
 The reason the validation exception was thrown.
HTTP Status Code: 400

## See Also
<a name="API_DescribeServiceIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-guru-2020-12-01/DescribeServiceIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-guru-2020-12-01/DescribeServiceIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/DescribeServiceIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-guru-2020-12-01/DescribeServiceIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/DescribeServiceIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-guru-2020-12-01/DescribeServiceIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-guru-2020-12-01/DescribeServiceIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-guru-2020-12-01/DescribeServiceIntegration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-guru-2020-12-01/DescribeServiceIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/DescribeServiceIntegration)
