---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateOrganizationsAccess.html
---

# ActivateOrganizationsAccess
<a name="API_ActivateOrganizationsAccess"></a>

Activate trusted access with AWS Organizations. With trusted access between StackSets and Organizations activated, the management account has permissions to create and manage StackSets for your organization.

## Errors
<a name="API_ActivateOrganizationsAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidOperation **
The specified operation isn't valid.
HTTP Status Code: 400

 ** OperationNotFound **
The specified ID refers to an operation that doesn't exist.
HTTP Status Code: 404

## Examples
<a name="API_ActivateOrganizationsAccess_Examples"></a>

### ActivateOrganizationsAccess
<a name="API_ActivateOrganizationsAccess_Example_1"></a>

This example illustrates one usage of ActivateOrganizationsAccess.

#### Sample Request
<a name="API_ActivateOrganizationsAccess_Example_1_Request"></a>

```
https://cloudformation.us-east-1.amazonaws.com/
    ?Action=ActivateOrganizationsAccess
```

#### Sample Response
<a name="API_ActivateOrganizationsAccess_Example_1_Response"></a>

```
<ActivateOrganizationsAccessResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <ActivateOrganizationsAccessResult/>
  <ResponseMetadata>
    <RequestId>f2038c6a-2ef6-45d0-a045-f2b4d15647ba</RequestId>
  </ResponseMetadata>
</ActivateOrganizationsAccessResponse>
```

## See Also
<a name="API_ActivateOrganizationsAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ActivateOrganizationsAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/ActivateOrganizationsAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ActivateOrganizationsAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ActivateOrganizationsAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ActivateOrganizationsAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ActivateOrganizationsAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ActivateOrganizationsAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ActivateOrganizationsAccess)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ActivateOrganizationsAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ActivateOrganizationsAccess)
