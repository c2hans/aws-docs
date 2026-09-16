---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_GetAWSOrganizationsAccessStatus.html
---

# GetAWSOrganizationsAccessStatus
<a name="API_GetAWSOrganizationsAccessStatus"></a>

Get the Access Status for AWS Organizations portfolio share feature. This API can only be called by the management account in the organization or by a delegated admin.

## Response Syntax
<a name="API_GetAWSOrganizationsAccessStatus_ResponseSyntax"></a>

```
{
   "AccessStatus": "string"
}
```

## Response Elements
<a name="API_GetAWSOrganizationsAccessStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccessStatus](#API_GetAWSOrganizationsAccessStatus_ResponseSyntax) **   <a name="servicecatalog-GetAWSOrganizationsAccessStatus-response-AccessStatus"></a>
The status of the portfolio share feature.
Type: String
Valid Values: `ENABLED | UNDER_CHANGE | DISABLED`

## Errors
<a name="API_GetAWSOrganizationsAccessStatus_Errors"></a>

 ** OperationNotSupportedException **
The operation is not supported.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_GetAWSOrganizationsAccessStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus)
