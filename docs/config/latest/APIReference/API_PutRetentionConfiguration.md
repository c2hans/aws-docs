---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_PutRetentionConfiguration.html
---

# PutRetentionConfiguration
<a name="API_PutRetentionConfiguration"></a>

Creates and updates the retention configuration with details about retention period (number of days) that AWS Config stores your historical information. The API creates the `RetentionConfiguration` object and names the object as **default**. When you have a `RetentionConfiguration` object named **default**, calling the API modifies the default object.

**Note**
Currently, AWS Config supports only one retention configuration per region in your account.

## Request Syntax
<a name="API_PutRetentionConfiguration_RequestSyntax"></a>

```
{
   "RetentionPeriodInDays": {{number}}
}
```

## Request Parameters
<a name="API_PutRetentionConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RetentionPeriodInDays](#API_PutRetentionConfiguration_RequestSyntax) **   <a name="config-PutRetentionConfiguration-request-RetentionPeriodInDays"></a>
Number of days AWS Config stores your historical information.
Currently, only applicable to the configuration item history.
Type: Integer
Valid Range: Minimum value of 30. Maximum value of 2557.
Required: Yes

## Response Syntax
<a name="API_PutRetentionConfiguration_ResponseSyntax"></a>

```
{
   "RetentionConfiguration": {
      "Name": "string",
      "RetentionPeriodInDays": number
   }
}
```

## Response Elements
<a name="API_PutRetentionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RetentionConfiguration](#API_PutRetentionConfiguration_ResponseSyntax) **   <a name="config-PutRetentionConfiguration-response-RetentionConfiguration"></a>
Returns a retention configuration object.
Type: [RetentionConfiguration](API_RetentionConfiguration.md) object

## Errors
<a name="API_PutRetentionConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

 ** MaxNumberOfRetentionConfigurationsExceededException **
Failed to add the retention configuration because a retention configuration with that name already exists.
HTTP Status Code: 400

## See Also
<a name="API_PutRetentionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/PutRetentionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/PutRetentionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/PutRetentionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/PutRetentionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/PutRetentionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/PutRetentionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/PutRetentionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/PutRetentionConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/PutRetentionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/PutRetentionConfiguration)
