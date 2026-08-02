---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_GetLineageGroupPolicy.html
---

# GetLineageGroupPolicy
<a name="API_GetLineageGroupPolicy"></a>

The resource policy for the lineage group.

## Request Syntax
<a name="API_GetLineageGroupPolicy_RequestSyntax"></a>

```
{
   "LineageGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetLineageGroupPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LineageGroupName](#API_GetLineageGroupPolicy_RequestSyntax) **   <a name="sagemaker-GetLineageGroupPolicy-request-LineageGroupName"></a>
The name or Amazon Resource Name (ARN) of the lineage group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:lineage-group\/)?([a-zA-Z0-9](-*[a-zA-Z0-9]){0,119})`
Required: Yes

## Response Syntax
<a name="API_GetLineageGroupPolicy_ResponseSyntax"></a>

```
{
   "LineageGroupArn": "string",
   "ResourcePolicy": "string"
}
```

## Response Elements
<a name="API_GetLineageGroupPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LineageGroupArn](#API_GetLineageGroupPolicy_ResponseSyntax) **   <a name="sagemaker-GetLineageGroupPolicy-response-LineageGroupArn"></a>
The Amazon Resource Name (ARN) of the lineage group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:lineage-group/.*`

 ** [ResourcePolicy](#API_GetLineageGroupPolicy_ResponseSyntax) **   <a name="sagemaker-GetLineageGroupPolicy-response-ResourcePolicy"></a>
The resource policy that gives access to the lineage group in another account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20480.
Pattern: `.*(?:[ \r\n\t].*)*`

## Errors
<a name="API_GetLineageGroupPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_GetLineageGroupPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/GetLineageGroupPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/GetLineageGroupPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/GetLineageGroupPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/GetLineageGroupPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/GetLineageGroupPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/GetLineageGroupPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/GetLineageGroupPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/GetLineageGroupPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/GetLineageGroupPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/GetLineageGroupPolicy)
