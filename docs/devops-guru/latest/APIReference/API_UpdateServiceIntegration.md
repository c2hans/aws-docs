---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_UpdateServiceIntegration.html
---

# UpdateServiceIntegration
<a name="API_UpdateServiceIntegration"></a>

**Note**
End of support notice: On September 30, 2027, AWS will end support for Amazon DevOps Guru. After September 30, 2027, you will no longer be able to access the Amazon DevOps Guru console or Amazon DevOps Guru resources. For more information, see [Amazon DevOps Guru end of support](https://docs.aws.amazon.com/devops-guru/latest/userguide/devops-guru-end-of-support.html).

 Enables or disables integration with a service that can be integrated with DevOps Guru.

## Request Syntax
<a name="API_UpdateServiceIntegration_RequestSyntax"></a>

```
PUT /service-integrations HTTP/1.1
Content-type: application/json

{
   "ServiceIntegration": {
      "KMSServerSideEncryption": {
         "KMSKeyId": "{{string}}",
         "OptInStatus": "{{string}}",
         "Type": "{{string}}"
      },
      "LogsAnomalyDetection": {
         "OptInStatus": "{{string}}"
      },
      "OpsCenter": {
         "OptInStatus": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateServiceIntegration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateServiceIntegration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ServiceIntegration](#API_UpdateServiceIntegration_RequestSyntax) **   <a name="DevOpsGuru-UpdateServiceIntegration-request-ServiceIntegration"></a>
 An `IntegratedServiceConfig` object used to specify the integrated service you want to update, and whether you want to update it to enabled or disabled.
Type: [UpdateServiceIntegrationConfig](API_UpdateServiceIntegrationConfig.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateServiceIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateServiceIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateServiceIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.
HTTP Status Code: 403

 ** ConflictException **
 An exception that is thrown when a conflict occurs.
 ** ResourceId **
 The ID of the AWS resource in which a conflict occurred.
 ** ResourceType **
 The type of the AWS resource in which a conflict occurred.
HTTP Status Code: 409

 ** InternalServerException **
An internal failure in an Amazon service occurred.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the internal server exception can be retried.
HTTP Status Code: 500

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
<a name="API_UpdateServiceIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-guru-2020-12-01/UpdateServiceIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-guru-2020-12-01/UpdateServiceIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/UpdateServiceIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-guru-2020-12-01/UpdateServiceIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/UpdateServiceIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-guru-2020-12-01/UpdateServiceIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-guru-2020-12-01/UpdateServiceIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-guru-2020-12-01/UpdateServiceIntegration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-guru-2020-12-01/UpdateServiceIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/UpdateServiceIntegration)
