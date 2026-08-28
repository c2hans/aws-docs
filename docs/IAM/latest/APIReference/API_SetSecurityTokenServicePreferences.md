---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_SetSecurityTokenServicePreferences.html
---

# SetSecurityTokenServicePreferences
<a name="API_SetSecurityTokenServicePreferences"></a>

Sets the specified version of the global endpoint token as the token version used for the AWS account.

By default, AWS Security Token Service (AWS STS) is available as a global service, and all AWS STS requests go to a single endpoint at `https://sts.amazonaws.com`. AWS recommends using Regional AWS STS endpoints to reduce latency, build in redundancy, and increase session token availability. For information about Regional endpoints for AWS STS, see [AWS Security Token Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sts.html) in the * AWS General Reference*.

If you make an AWS STS call to the global endpoint, the resulting session tokens might be valid in some Regions but not others. It depends on the version that is set in this operation. Version 1 tokens are valid only in AWS Regions that are available by default. These tokens do not work in manually enabled Regions, such as Asia Pacific (Hong Kong). Version 2 tokens are valid in all Regions. However, version 2 tokens are longer and might affect systems where you temporarily store tokens. For information, see [Activating and deactivating AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html) in the *IAM User Guide*.

To view the current session token version, see the `GlobalEndpointTokenVersion` entry in the response of the [GetAccountSummary](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountSummary.html) operation.

## Request Parameters
<a name="API_SetSecurityTokenServicePreferences_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** GlobalEndpointTokenVersion **
The version of the global endpoint token. Version 1 tokens are valid only in AWS Regions that are available by default. These tokens do not work in manually enabled Regions, such as Asia Pacific (Hong Kong). Version 2 tokens are valid in all Regions. However, version 2 tokens are longer and might affect systems where you temporarily store tokens.
For information, see [Activating and deactivating AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html) in the *IAM User Guide*.
Type: String
Valid Values: `v1Token | v2Token`
Required: Yes

## Errors
<a name="API_SetSecurityTokenServicePreferences_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_SetSecurityTokenServicePreferences_Examples"></a>

### Example
<a name="API_SetSecurityTokenServicePreferences_Example_1"></a>

This example illustrates one usage of SetSecurityTokenServicePreferences.

#### Sample Request
<a name="API_SetSecurityTokenServicePreferences_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=SetSecurityTokenServicePreferences
&GlobalEndpointTokenVersion=v2Token
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_SetSecurityTokenServicePreferences_Example_1_Response"></a>

```
<SetSecurityTokenServicePreferences xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>31a241af-1ebc-12b4-9d0d-8f876EXAMPLE</RequestId>
  </ResponseMetadata>
</SetSecurityTokenServicePreferences>
```

## See Also
<a name="API_SetSecurityTokenServicePreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/SetSecurityTokenServicePreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/SetSecurityTokenServicePreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/SetSecurityTokenServicePreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/SetSecurityTokenServicePreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/SetSecurityTokenServicePreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/SetSecurityTokenServicePreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/SetSecurityTokenServicePreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/SetSecurityTokenServicePreferences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/SetSecurityTokenServicePreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/SetSecurityTokenServicePreferences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
