---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutAccountProperties.html
---

# PutAccountProperties
<a name="API_PutAccountProperties"></a>

Sets account-level properties for the caller's AWS account. Account properties are configuration settings that control account-wide IAM features such as Role Manager.

Specify properties as key-value pairs in `Namespace/PropertyName` format. All properties in a single request must belong to the same namespace. Use [GetAccountProperties](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountProperties.html) to view the current properties.

## Request Parameters
<a name="API_PutAccountProperties_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Properties** Properties.entry.N.key (key)Properties.entry.N.value (value)
A map of property key-value pairs to set. All keys must belong to the same namespace.
Each key uses the format `Namespace/PropertyName`. The key must contain exactly one `/` separating the namespace from the property name, and cannot start or end with `/`.
The service validates each value based on the property key's expected type. For example, boolean properties expect `true` or `false`.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Key Pattern: `^[A-Za-z][A-Za-z0-9/_-]*$`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## Errors
<a name="API_PutAccountProperties_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModification **
The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
HTTP Status Code: 409

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_PutAccountProperties_Examples"></a>

### Enable Role Manager
<a name="API_PutAccountProperties_Example_1"></a>

This example enables the Role Manager feature for the calling account.

#### Sample Request
<a name="API_PutAccountProperties_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=PutAccountProperties
&Properties.entry.1.key=RoleManager/Enabled
&Properties.entry.1.value=true
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_PutAccountProperties_Example_1_Response"></a>

```
<PutAccountPropertiesResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>3a4c2b1d-5e6f-7890-abcd-1234EXAMPLE</RequestId>
  </ResponseMetadata>
</PutAccountPropertiesResponse>
```

### Disable Role Manager
<a name="API_PutAccountProperties_Example_2"></a>

This example illustrates one usage of PutAccountProperties.

#### Sample Request
<a name="API_PutAccountProperties_Example_2_Request"></a>

```
https://iam.amazonaws.com/?Action=PutAccountProperties
&Properties.entry.1.key=RoleManager/Enabled
&Properties.entry.1.value=false
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_PutAccountProperties_Example_2_Response"></a>

```
<PutAccountPropertiesResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</PutAccountPropertiesResponse>
```

## See Also
<a name="API_PutAccountProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/PutAccountProperties)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/PutAccountProperties)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/PutAccountProperties)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/PutAccountProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/PutAccountProperties)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/PutAccountProperties)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/PutAccountProperties)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/PutAccountProperties)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/PutAccountProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/PutAccountProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
