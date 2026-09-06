---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListCuratedEnvironmentImages.html
---

# ListCuratedEnvironmentImages
<a name="API_ListCuratedEnvironmentImages"></a>

Gets information about Docker images that are managed by AWS CodeBuild.

## Response Syntax
<a name="API_ListCuratedEnvironmentImages_ResponseSyntax"></a>

```
{
   "platforms": [
      {
         "languages": [
            {
               "images": [
                  {
                     "description": "string",
                     "name": "string",
                     "versions": [ "string" ]
                  }
               ],
               "language": "string"
            }
         ],
         "platform": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListCuratedEnvironmentImages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [platforms](#API_ListCuratedEnvironmentImages_ResponseSyntax) **   <a name="CodeBuild-ListCuratedEnvironmentImages-response-platforms"></a>
Information about supported platforms for Docker images that are managed by AWS CodeBuild.
Type: Array of [EnvironmentPlatform](API_EnvironmentPlatform.md) objects

## Errors
<a name="API_ListCuratedEnvironmentImages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListCuratedEnvironmentImages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/ListCuratedEnvironmentImages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/ListCuratedEnvironmentImages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ListCuratedEnvironmentImages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/ListCuratedEnvironmentImages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ListCuratedEnvironmentImages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/ListCuratedEnvironmentImages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/ListCuratedEnvironmentImages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/ListCuratedEnvironmentImages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/ListCuratedEnvironmentImages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ListCuratedEnvironmentImages)
