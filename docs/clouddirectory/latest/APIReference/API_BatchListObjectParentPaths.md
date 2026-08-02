---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchListObjectParentPaths.html
---

Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchListObjectParentPaths
<a name="API_BatchListObjectParentPaths"></a>

Retrieves all available parent paths for any object type such as node, leaf node, policy node, and index node objects inside a [BatchRead](API_BatchRead.md) operation. For more information, see [ListObjectParentPaths](API_ListObjectParentPaths.md) and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations).

## Contents
<a name="API_BatchListObjectParentPaths_Contents"></a>

 ** ObjectReference **   <a name="amazoncds-Type-BatchListObjectParentPaths-ObjectReference"></a>
The reference that identifies the object whose attributes will be listed.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

 ** MaxResults **   <a name="amazoncds-Type-BatchListObjectParentPaths-MaxResults"></a>
The maximum number of results to retrieve.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** NextToken **   <a name="amazoncds-Type-BatchListObjectParentPaths-NextToken"></a>
The pagination token.
Type: String
Required: No

## See Also
<a name="API_BatchListObjectParentPaths_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchListObjectParentPaths)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchListObjectParentPaths)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchListObjectParentPaths)
