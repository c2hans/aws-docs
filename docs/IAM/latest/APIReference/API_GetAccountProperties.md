---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountProperties.html
---

# GetAccountProperties
<a name="API_GetAccountProperties"></a>

Retrieves the account-level properties for the caller's AWS account. Account properties are configuration settings that control account-wide IAM features such as Role Manager.

The service returns properties as key-value pairs in `Namespace/PropertyName` format. Each namespace groups related configuration settings. Use [PutAccountProperties](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutAccountProperties.html) to modify these properties.

## Response Elements
<a name="API_GetAccountProperties_ResponseElements"></a>

The following element is returned by the service.

 **Properties** Properties.entry.N.key (key)Properties.entry.N.value (value)
A map of account property key-value pairs. Keys are in the format `Namespace/PropertyName`.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Key Pattern: `^[A-Za-z][A-Za-z0-9/_-]*$`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_GetAccountProperties_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_GetAccountProperties_Examples"></a>

### Retrieve account properties
<a name="API_GetAccountProperties_Example_1"></a>

This example retrieves all account-level properties for the calling account.

#### Sample Request
<a name="API_GetAccountProperties_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=GetAccountProperties
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetAccountProperties_Example_1_Response"></a>

```
<GetAccountPropertiesResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <GetAccountPropertiesResult>
    <Properties>
      <entry>
        <key>RoleManager/Enabled</key>
        <value>true</value>
      </entry>
    </Properties>
  </GetAccountPropertiesResult>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</GetAccountPropertiesResponse>
```

## See Also
<a name="API_GetAccountProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/GetAccountProperties)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/GetAccountProperties)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GetAccountProperties)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/GetAccountProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GetAccountProperties)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/GetAccountProperties)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/GetAccountProperties)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/GetAccountProperties)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/GetAccountProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GetAccountProperties)
