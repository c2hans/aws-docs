---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchGetObjectInformationResponse.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchGetObjectInformationResponse
<a name="API_BatchGetObjectInformationResponse"></a>

Represents the output of a [GetObjectInformation](API_GetObjectInformation.md) response operation.

## Contents
<a name="API_BatchGetObjectInformationResponse_Contents"></a>

 ** ObjectIdentifier **   <a name="amazoncds-Type-BatchGetObjectInformationResponse-ObjectIdentifier"></a>
The `ObjectIdentifier` of the specified object.
Type: String
Required: No

 ** SchemaFacets **   <a name="amazoncds-Type-BatchGetObjectInformationResponse-SchemaFacets"></a>
The facets attached to the specified object.
Type: Array of [SchemaFacet](API_SchemaFacet.md) objects
Required: No

## See Also
<a name="API_BatchGetObjectInformationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchGetObjectInformationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchGetObjectInformationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchGetObjectInformationResponse)
