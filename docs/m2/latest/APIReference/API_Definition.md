---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_Definition.html
---

# Definition
<a name="API_Definition"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

The application definition for a particular application.

## Contents
<a name="API_Definition_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** content **   <a name="m2-Type-Definition-content"></a>
The content of the application definition. This is a JSON object that contains the resource configuration/definitions that identify an application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65000.
Required: No

 ** s3Location **   <a name="m2-Type-Definition-s3Location"></a>
The S3 bucket that contains the application definition.
Type: String
Pattern: `\S{1,2000}`
Required: No

## See Also
<a name="API_Definition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/Definition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/Definition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/Definition)
