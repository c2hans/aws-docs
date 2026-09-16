---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeContext.html
---

# DescribeContext
<a name="API_DescribeContext"></a>

Describes a context.

## Request Syntax
<a name="API_DescribeContext_RequestSyntax"></a>

```
{
   "ContextName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeContext_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContextName](#API_DescribeContext_RequestSyntax) **   <a name="sagemaker-DescribeContext-request-ContextName"></a>
The name of the context to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:context\/)?([a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,119})`
Required: Yes

## Response Syntax
<a name="API_DescribeContext_ResponseSyntax"></a>

```
{
   "ContextArn": "string",
   "ContextName": "string",
   "ContextType": "string",
   "CreatedBy": {
      "DomainId": "string",
      "IamIdentity": {
         "Arn": "string",
         "PrincipalId": "string",
         "SourceIdentity": "string"
      },
      "UserProfileArn": "string",
      "UserProfileName": "string"
   },
   "Description": "string",
   "LastModifiedBy": {
      "DomainId": "string",
      "IamIdentity": {
         "Arn": "string",
         "PrincipalId": "string",
         "SourceIdentity": "string"
      },
      "UserProfileArn": "string",
      "UserProfileName": "string"
   },
   "LineageGroupArn": "string",
   "Properties": {
      "string" : "string"
   },
   "Source": {
      "SourceId": "string",
      "SourceType": "string",
      "SourceUri": "string"
   }
}
```

## Response Elements
<a name="API_DescribeContext_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContextArn](#API_DescribeContext_ResponseSyntax) **   <a name="sagemaker-DescribeContext-response-ContextArn"></a>
The Amazon Resource Name (ARN) of the context.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:context/.*`

 ** [ContextName](#API_DescribeContext_ResponseSyntax) **   <a name="sagemaker-DescribeContext-response-ContextName"></a>
The name of the context.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,119}`

 ** [ContextType](#API_DescribeContext_ResponseSyntax) **   <a name="sagemaker-DescribeContext-response-ContextType"></a>
The type of the context.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [CreatedBy](#API_DescribeContext_ResponseSyntax) **   <a name="sagemaker-DescribeContext-response-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [Description](#API_DescribeContext_ResponseSyntax) **   <a name="sagemaker-DescribeContext-response-Description"></a>
The description of the context.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`

 ** [LastModifiedBy](#API_DescribeContext_ResponseSyntax) **   <a name="sagemaker-DescribeContext-response-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [LineageGroupArn](#API_DescribeContext_ResponseSyntax) **   <a name="sagemaker-DescribeContext-response-LineageGroupArn"></a>
The Amazon Resource Name (ARN) of the lineage group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:lineage-group/.*`

 ** [Properties](#API_DescribeContext_ResponseSyntax) **   <a name="sagemaker-DescribeContext-response-Properties"></a>
A list of the context's properties.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 30 items.
Key Length Constraints: Minimum length of 0. Maximum length of 2500.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 2500.
Value Pattern: `.*`

 ** [Source](#API_DescribeContext_ResponseSyntax) **   <a name="sagemaker-DescribeContext-response-Source"></a>
The source of the context.
Type: [ContextSource](API_ContextSource.md) object

## Errors
<a name="API_DescribeContext_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeContext)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeContext)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeContext)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeContext)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeContext)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeContext)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeContext)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeContext)
