---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPointForObjectLambda.html
---

# CreateAccessPointForObjectLambda
<a name="API_control_CreateAccessPointForObjectLambda"></a>

**Note**
This operation is not supported by directory buckets.

Creates an Object Lambda Access Point. For more information, see [Transforming objects with Object Lambda Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transforming-objects.html) in the *Amazon S3 User Guide*.

The following actions are related to `CreateAccessPointForObjectLambda`:
+  [DeleteAccessPointForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointForObjectLambda.html)
+  [GetAccessPointForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointForObjectLambda.html)
+  [ListAccessPointsForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForObjectLambda.html)

## Request Syntax
<a name="API_control_CreateAccessPointForObjectLambda_RequestSyntax"></a>

```
PUT /v20180820/accesspointforobjectlambda/{{name}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
<?xml version="1.0" encoding="UTF-8"?>
<CreateAccessPointForObjectLambdaRequest xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <Configuration>
      <AllowedFeatures>
         <AllowedFeature>{{string}}</AllowedFeature>
      </AllowedFeatures>
      <CloudWatchMetricsEnabled>{{boolean}}</CloudWatchMetricsEnabled>
      <SupportingAccessPoint>{{string}}</SupportingAccessPoint>
      <TransformationConfigurations>
         <TransformationConfiguration>
            <Actions>
               <Action>{{string}}</Action>
            </Actions>
            <ContentTransformation>
               <AwsLambda>
                  <FunctionArn>{{string}}</FunctionArn>
                  <FunctionPayload>{{string}}</FunctionPayload>
               </AwsLambda>
            </ContentTransformation>
         </TransformationConfiguration>
      </TransformationConfigurations>
   </Configuration>
</CreateAccessPointForObjectLambdaRequest>
```

## URI Request Parameters
<a name="API_control_CreateAccessPointForObjectLambda_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_CreateAccessPointForObjectLambda_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessPointForObjectLambda-request-uri-uri-Name"></a>
The name you want to assign to this Object Lambda Access Point.
Length Constraints: Minimum length of 3. Maximum length of 45.
Pattern: `^[a-z0-9]([a-z0-9\-]*[a-z0-9])?$`
Required: Yes

 ** [x-amz-account-id](#API_control_CreateAccessPointForObjectLambda_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessPointForObjectLambda-request-header-AccountId"></a>
The AWS account ID for owner of the specified Object Lambda Access Point.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_CreateAccessPointForObjectLambda_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateAccessPointForObjectLambdaRequest](#API_control_CreateAccessPointForObjectLambda_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessPointForObjectLambda-request-CreateAccessPointForObjectLambdaRequest"></a>
Root level tag for the CreateAccessPointForObjectLambdaRequest parameters.
Required: Yes

 ** [Configuration](#API_control_CreateAccessPointForObjectLambda_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessPointForObjectLambda-request-Configuration"></a>
Object Lambda Access Point configuration as a JSON document.
Type: [ObjectLambdaConfiguration](API_control_ObjectLambdaConfiguration.md) data type
Required: Yes

## Response Syntax
<a name="API_control_CreateAccessPointForObjectLambda_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<CreateAccessPointForObjectLambdaResult>
   <ObjectLambdaAccessPointArn>string</ObjectLambdaAccessPointArn>
   <Alias>
      <Status>string</Status>
      <Value>string</Value>
   </Alias>
</CreateAccessPointForObjectLambdaResult>
```

## Response Elements
<a name="API_control_CreateAccessPointForObjectLambda_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [CreateAccessPointForObjectLambdaResult](#API_control_CreateAccessPointForObjectLambda_ResponseSyntax) **   <a name="AmazonS3-control_CreateAccessPointForObjectLambda-response-CreateAccessPointForObjectLambdaResult"></a>
Root level tag for the CreateAccessPointForObjectLambdaResult parameters.
Required: Yes

 ** [Alias](#API_control_CreateAccessPointForObjectLambda_ResponseSyntax) **   <a name="AmazonS3-control_CreateAccessPointForObjectLambda-response-Alias"></a>
The alias of the Object Lambda Access Point.
Type: [ObjectLambdaAccessPointAlias](API_control_ObjectLambdaAccessPointAlias.md) data type

 ** [ObjectLambdaAccessPointArn](#API_control_CreateAccessPointForObjectLambda_ResponseSyntax) **   <a name="AmazonS3-control_CreateAccessPointForObjectLambda-response-ObjectLambdaAccessPointArn"></a>
Specifies the ARN for the Object Lambda Access Point.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[^:]+:s3-object-lambda:[^:]*:\d{12}:accesspoint/.*`

## See Also
<a name="API_control_CreateAccessPointForObjectLambda_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateAccessPointForObjectLambda)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/CreateAccessPointForObjectLambda)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateAccessPointForObjectLambda)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateAccessPointForObjectLambda)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateAccessPointForObjectLambda)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateAccessPointForObjectLambda)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateAccessPointForObjectLambda)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateAccessPointForObjectLambda)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateAccessPointForObjectLambda)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateAccessPointForObjectLambda)
