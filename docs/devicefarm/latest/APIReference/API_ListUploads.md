---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListUploads.html
---

# ListUploads
<a name="API_ListUploads"></a>

Gets information about uploads, given an AWS Device Farm project ARN.

## Request Syntax
<a name="API_ListUploads_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "nextToken": "{{string}}",
   "type": "{{string}}"
}
```

## Request Parameters
<a name="API_ListUploads_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_ListUploads_RequestSyntax) **   <a name="devicefarm-ListUploads-request-arn"></a>
The Amazon Resource Name (ARN) of the project for which you want to list uploads.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [nextToken](#API_ListUploads_RequestSyntax) **   <a name="devicefarm-ListUploads-request-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

 ** [type](#API_ListUploads_RequestSyntax) **   <a name="devicefarm-ListUploads-request-type"></a>
The type of upload.
Must be one of the following values:
+ ANDROID\_APP
+ IOS\_APP
+ WEB\_APP
+ EXTERNAL\_DATA
+ APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE
+ APPIUM\_JAVA\_TESTNG\_TEST\_PACKAGE
+ APPIUM\_PYTHON\_TEST\_PACKAGE
+ APPIUM\_NODE\_TEST\_PACKAGE
+ APPIUM\_RUBY\_TEST\_PACKAGE
+ APPIUM\_WEB\_JAVA\_JUNIT\_TEST\_PACKAGE
+ APPIUM\_WEB\_JAVA\_TESTNG\_TEST\_PACKAGE
+ APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE
+ APPIUM\_WEB\_NODE\_TEST\_PACKAGE
+ APPIUM\_WEB\_RUBY\_TEST\_PACKAGE
+ INSTRUMENTATION\_TEST\_PACKAGE
+ XCTEST\_TEST\_PACKAGE
+ XCTEST\_UI\_TEST\_PACKAGE
+ APPIUM\_JAVA\_JUNIT\_TEST\_SPEC
+ APPIUM\_JAVA\_TESTNG\_TEST\_SPEC
+ APPIUM\_PYTHON\_TEST\_SPEC
+ APPIUM\_NODE\_TEST\_SPEC
+  APPIUM\_RUBY\_TEST\_SPEC
+ APPIUM\_WEB\_JAVA\_JUNIT\_TEST\_SPEC
+ APPIUM\_WEB\_JAVA\_TESTNG\_TEST\_SPEC
+ APPIUM\_WEB\_PYTHON\_TEST\_SPEC
+ APPIUM\_WEB\_NODE\_TEST\_SPEC
+ APPIUM\_WEB\_RUBY\_TEST\_SPEC
+ INSTRUMENTATION\_TEST\_SPEC
+ XCTEST\_UI\_TEST\_SPEC
Type: String
Valid Values: `ANDROID_APP | IOS_APP | WEB_APP | EXTERNAL_DATA | APPIUM_JAVA_JUNIT_TEST_PACKAGE | APPIUM_JAVA_TESTNG_TEST_PACKAGE | APPIUM_PYTHON_TEST_PACKAGE | APPIUM_NODE_TEST_PACKAGE | APPIUM_RUBY_TEST_PACKAGE | APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE | APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE | APPIUM_WEB_PYTHON_TEST_PACKAGE | APPIUM_WEB_NODE_TEST_PACKAGE | APPIUM_WEB_RUBY_TEST_PACKAGE | CALABASH_TEST_PACKAGE | INSTRUMENTATION_TEST_PACKAGE | UIAUTOMATION_TEST_PACKAGE | UIAUTOMATOR_TEST_PACKAGE | XCTEST_TEST_PACKAGE | XCTEST_UI_TEST_PACKAGE | APPIUM_JAVA_JUNIT_TEST_SPEC | APPIUM_JAVA_TESTNG_TEST_SPEC | APPIUM_PYTHON_TEST_SPEC | APPIUM_NODE_TEST_SPEC | APPIUM_RUBY_TEST_SPEC | APPIUM_WEB_JAVA_JUNIT_TEST_SPEC | APPIUM_WEB_JAVA_TESTNG_TEST_SPEC | APPIUM_WEB_PYTHON_TEST_SPEC | APPIUM_WEB_NODE_TEST_SPEC | APPIUM_WEB_RUBY_TEST_SPEC | INSTRUMENTATION_TEST_SPEC | XCTEST_UI_TEST_SPEC`
Required: No

## Response Syntax
<a name="API_ListUploads_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "uploads": [
      {
         "arn": "string",
         "category": "string",
         "contentType": "string",
         "created": number,
         "message": "string",
         "metadata": "string",
         "name": "string",
         "status": "string",
         "type": "string",
         "url": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListUploads_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListUploads_ResponseSyntax) **   <a name="devicefarm-ListUploads-response-nextToken"></a>
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

 ** [uploads](#API_ListUploads_ResponseSyntax) **   <a name="devicefarm-ListUploads-response-uploads"></a>
Information about the uploads.
Type: Array of [Upload](API_Upload.md) objects

## Errors
<a name="API_ListUploads_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit was exceeded.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** NotFoundException **
The specified entity was not found.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** ServiceAccountException **
There was a problem with the service account.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListUploads_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListUploads)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListUploads)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListUploads)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListUploads)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListUploads)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListUploads)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListUploads)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListUploads)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListUploads)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListUploads)
