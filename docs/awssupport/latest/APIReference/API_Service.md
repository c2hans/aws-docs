---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_Service.html
---

# Service
<a name="API_Service"></a>

Information about an AWS service returned by the [DescribeServices](API_DescribeServices.md) operation.

## Contents
<a name="API_Service_Contents"></a>

 ** categories **   <a name="AWSSupport-Type-Service-categories"></a>
A list of categories that describe the type of support issue a case describes. Categories consist of a category name and a category code. Category names and codes are passed to AWS Support when you call [CreateCase](API_CreateCase.md).
Type: Array of [Category](API_Category.md) objects

 ** code **   <a name="AWSSupport-Type-Service-code"></a>
The code for an AWS service returned by the [DescribeServices](API_DescribeServices.md) response. The `name` element contains the corresponding friendly name.
Type: String

 ** name **   <a name="AWSSupport-Type-Service-name"></a>
The friendly name for an AWS service. The `code` element contains the corresponding code.
Type: String

## See Also
<a name="API_Service_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/Service)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/Service)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/Service)
